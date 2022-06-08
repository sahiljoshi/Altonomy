import json
import time

import requests
import grpc
import market_data_proto_pb2
import market_data_proto_pb2_grpc


class Binance:
    def getKlineData(self, symbol, interval, start_time, end_time):
        url = 'https://api.binance.com/api/v3/klines'
        limit = 500

        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': start_time,
            'endTime': end_time,
            # "limit": 500

        }
        print(f'sending request {params}')
        response = requests.get(url, params=params)
        print('response   received')
        print(type(response))
        obj = response.json()
        print(type(obj))
        l = []
        for r in obj:
            print(r)
            ohlcv = market_data_proto_pb2.OHLCV(
                open=r[1],
                high=r[2],
                low=r[3],
                close=r[4],
                start_time=str(r[0]),
                volume=r[5])

            print("appending data")
            l.append(ohlcv)

        response = market_data_proto_pb2.response(
            is_success=True,
            payload=l
        )
        print(response)
        return response

    def getOrderBook(self, symbol, limit):
        url = 'https://api.binance.com/api/v3/depth'
        if limit == 0:
            limit = 1
        params = {
            'symbol': symbol,
            "limit": limit
        }

        print(f'sending request {params}')
        response = requests.get(url, params=params)
        print('response   received')
        print(type(response))
        obj = response.json()
        print(type(obj))
        print(obj)
        bids = []
        asks = []
        print("reading bids ")
        for b in obj['bids']:
            p = market_data_proto_pb2.priceLevel(price=b[0], quantity=b[1])
            bids.append(p)
        print("reading asks ")
        for a in obj['asks']:
            p = market_data_proto_pb2.priceLevel(price=a[0], quantity=a[1])
            asks.append(p)
        response = market_data_proto_pb2.ob_response(isSuccess=True, bids=bids, asks=asks,
                                                     lastUpdateId=str(time.time()))
        return response


if __name__ == '__main__':
    b = Binance()
    now = int(time.time() * 1000)
    start = now - (15 * 500 * 60 * 1000)
    # b.getKlineData("BTCUSDT",  '15m', start, now )
