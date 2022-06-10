import threading
import time

import sqlalchemy as db
import sys
# specify database configurations
from sqlalchemy import MetaData, Integer, String, Column, Table, Float, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import grpc

sys.path.append("usr/app")
import market_data_proto_pb2_grpc
import market_data_proto_pb2
import schedule, time

Base = declarative_base()


class OHLCV(Base):
    __tablename__ = 'ohlc_data'
    id = Column(Integer, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    start_time = Column(Integer)
    volume = Column(Float)
    symbol = Column(String)
    exchange = Column(String)


class BidAsk(Base):
    __tablename__ = 'bid_ask_data'
    id = Column(Integer, primary_key=True)
    bid = Column(Float)
    ask = Column(Float)
    bid_qty = Column(Float)
    ask_qty = Column(Float)
    last_update_time = Column(Integer)
    symbol = Column(String)
    exchange = Column(String)


def initDb():
    config = {
        'host': '0.0.0.0',
        'port': 3306,
        'user': 'root',
        'password': 'passwd',
        'database': 'marketData'
    }
    db_user = config.get('user')
    db_pwd = config.get('password')
    db_host = config.get('host')
    db_port = config.get('port')
    db_name = config.get('database')
    # specify connection string
    # connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
    connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@test_mysql_db/{db_name}'

    print(connection_str)
    # connect to database
    # engine1 = db.create_engine("mysql://root:passwd@localhost:3306/,market_data", echo=True)
    engine1 = db.create_engine(connection_str)
    connection = engine1.connect()

    metadata = db.MetaData(bind=engine1)

    meta = MetaData()

    market_data = Table(
        'ohlc_data', meta,
        Column('id', Integer, primary_key=True),
        Column('symbol', String(32)),
        Column('exchange', String(32)),
        Column('open', Float),
        Column('high', Float),
        Column('low', Float),
        Column('close', Float),
        Column('volume', Float),
        Column('start_time', Integer),
    )

    bid_ask_data = Table(
        'bid_ask_data', meta,
        Column('id', Integer, primary_key=True),
        Column('symbol', String(32)),
        Column('exchange', String(32)),
        Column('bid', Float),
        Column('ask', Float),
        Column('bid_qty', Float),
        Column('ask_qty', Float),
        Column('last_update_time', Integer),

    )

    meta.create_all(engine1)
    return engine1


def query_for_data(engine, exchange, symbol, duration):
    channel = grpc.insecure_channel('market_data_connector:13000')
    stub = market_data_proto_pb2_grpc.MarketDataServiceStub(channel)

    end_time = int(time.time() * 1000)
    start_time = end_time - 60 * 15 * 45 * 1000;

    request = market_data_proto_pb2.request()
    request.exchange = exchange
    request.symbol = symbol
    request.duration = duration
    request.start_time = start_time
    request.end_time = end_time
    print(stub)
    result = stub.GetKlineData(request)
    print(result)
    print(type(result.payload))
    Session = sessionmaker(bind=engine)
    session = Session()

    for r in result.payload:
        l1 = OHLCV(open=r.open, high=r.high, low=r.low, close=r.close, start_time=r.start_time, volume=r.volume,
                   symbol=symbol, exchange=exchange)
        session.add(l1)

    session.commit()


def query_for_ob_data(engine):
    channel = grpc.insecure_channel('market_data_connector:13000')
    stub = market_data_proto_pb2_grpc.MarketDataServiceStub(channel)
    exchange = "BINANCE"
    symbol = "BTCUSDT"
    request = market_data_proto_pb2.ob_request()
    request.exchange = exchange
    request.symbol = symbol
    request.depth = 2
    r = stub.GetOrderBookData(request)
    Session = sessionmaker(bind=engine)
    session = Session()
    l1 = BidAsk(bid=r.bids[0].price, ask=r.asks[0].price, last_update_time=int(r.lastUpdateId),
                bid_qty=r.bids[0].quantity, ask_qty=r.asks[0].quantity, symbol=symbol, exchange=exchange)
    session.add(l1)
    session.commit()
    print("commit complete ")


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.next_call += self.interval
            self._timer = threading.Timer(self.next_call - time.time(), self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm re ')
    engine = initDb()
    exchange = "BINANCE"
    symbol = "BTCUSDT"
    duration = "15m"
    rt = RepeatedTimer(1, query_for_ob_data, engine, exchange, symbol, duration)
    try:
        time.sleep(30000)
    finally:
        rt.stop()
