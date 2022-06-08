# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import enum
import sys
from concurrent import futures
import grpc
import time

sys.path.append("usr/app/grpc_compiled")

import market_data_proto_pb2
import market_data_proto_pb2_grpc

from BinanceConnector import Binance
from FTXConnector import FTXConnect


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Exchange(enum.Enum):
    BINANCE = 0
    FTX = 1


class Symbol(enum.Enum):
    BTCUSDT = 0
    ETHUSDT = 1
    SOLUSDT = 2


class MarketData(market_data_proto_pb2_grpc.MarketDataServiceServicer):
    _binanceConnector = Binance()
    _ftxConnector = FTXConnect()

    def GetKlineData(self, request, context):
        print('Received kline {request} !')
        print(request)
        exchange = request.exchange
        symbol = request.symbol
        start_time = request.start_time
        end_time = request.end_time
        interval = request.duration
        #l = []
        if exchange == Exchange.BINANCE.name:
            result = self._binanceConnector.getKlineData(symbol, interval, start_time, end_time)
            return result
        elif exchange == Exchange.FTX.name:
            response = market_data_proto_pb2.response(
                is_success=False
            )
            return response
        else:
            print("no valid exchage found ")
            response = market_data_proto_pb2.response(
                is_success=False
            )
            return response

    def GetOrderBookData(self, request, context):
        print("Received  OB request!")
        print(request.exchange)
        exchange = request.exchange
        symbol = request.symbol
        limit = request.depth

        if exchange == Exchange.BINANCE.name:

            result = self._binanceConnector.getOrderBook(symbol, limit)
            print("result received")
            return result
        elif exchange == Exchange.FTX.name:
            response = market_data_proto_pb2.ob_response(
                isSuccess=False
            )
            return response
        else:
            print("no valid exchange found ")
            response = market_data_proto_pb2.ob_response(
                isSuccess=False
            )
            return response


def start_server():
    print("starting server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    market_data_proto_pb2_grpc.add_MarketDataServiceServicer_to_server(MarketData(), server)

    server.add_insecure_port('[::]:13000')
    server.start()
    print("Server started. Awaiting jobs...")
    server.wait_for_termination()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm re ')
    #print(r)
    start_server()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
