import json
import time

import requests


class FTXConnect:
    api_url = 'https://ftx.us/api'

    def getKlineData(self, symbol, interval, start_time, end_time):
        path = f'/markets/{symbol}/candles?resolution={interval}&start={start_time}&end_time={end_time}'
        url = self.api_url + path
        print(f'sending request')
        response = requests.get(url).json()
        print('response   received')
        print(type(response))
        print(response)

    def getOrderBook(self, symbol, depth):
        path = f'/markets/{symbol}/orderbook?depth={depth}'
        url = self.api_url + path
        print(f'sending request ')
        response = requests.get(url).json()
        print('response   received')
        print(type(response))
        print(response)


if __name__ == '__main__':
    b = FTXConnect()
    now = int(time.time())
    start = now - (15 * 10 * 60)
    b.getKlineData("BTC/USDT",  300, start, now )
    #b.getOrderBook("BTC/USD", 10)
