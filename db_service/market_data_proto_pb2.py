# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market_data_proto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17market_data_proto.proto\x12\x0bmarket_data\"c\n\x07request\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x03\x12\x10\n\x08\x64uration\x18\x05 \x01(\t\"=\n\nob_request\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x05 \x01(\x05\"C\n\x08response\x12\x12\n\nis_success\x18\x01 \x01(\x08\x12#\n\x07payload\x18\x02 \x03(\x0b\x32\x12.market_data.OHLCV\"\x84\x01\n\x0bob_response\x12%\n\x04\x62ids\x18\x01 \x03(\x0b\x32\x17.market_data.priceLevel\x12%\n\x04\x61sks\x18\x02 \x03(\x0b\x32\x17.market_data.priceLevel\x12\x14\n\x0clastUpdateId\x18\x03 \x01(\t\x12\x11\n\tisSuccess\x18\x04 \x01(\x08\"-\n\npriceLevel\x12\r\n\x05price\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\t\"c\n\x05OHLCV\x12\x0c\n\x04open\x18\x01 \x01(\t\x12\x0c\n\x04high\x18\x02 \x01(\t\x12\x0b\n\x03low\x18\x03 \x01(\t\x12\r\n\x05\x63lose\x18\x04 \x01(\t\x12\x12\n\nstart_time\x18\x05 \x01(\t\x12\x0e\n\x06volume\x18\x06 \x01(\t2\x9b\x01\n\x11MarketDataService\x12=\n\x0cGetKlineData\x12\x14.market_data.request\x1a\x15.market_data.response\"\x00\x12G\n\x10GetOrderBookData\x12\x17.market_data.ob_request\x1a\x18.market_data.ob_response\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['request']
_OB_REQUEST = DESCRIPTOR.message_types_by_name['ob_request']
_RESPONSE = DESCRIPTOR.message_types_by_name['response']
_OB_RESPONSE = DESCRIPTOR.message_types_by_name['ob_response']
_PRICELEVEL = DESCRIPTOR.message_types_by_name['priceLevel']
_OHLCV = DESCRIPTOR.message_types_by_name['OHLCV']
request = _reflection.GeneratedProtocolMessageType('request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'market_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:market_data.request)
  })
_sym_db.RegisterMessage(request)

ob_request = _reflection.GeneratedProtocolMessageType('ob_request', (_message.Message,), {
  'DESCRIPTOR' : _OB_REQUEST,
  '__module__' : 'market_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:market_data.ob_request)
  })
_sym_db.RegisterMessage(ob_request)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'market_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:market_data.response)
  })
_sym_db.RegisterMessage(response)

ob_response = _reflection.GeneratedProtocolMessageType('ob_response', (_message.Message,), {
  'DESCRIPTOR' : _OB_RESPONSE,
  '__module__' : 'market_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:market_data.ob_response)
  })
_sym_db.RegisterMessage(ob_response)

priceLevel = _reflection.GeneratedProtocolMessageType('priceLevel', (_message.Message,), {
  'DESCRIPTOR' : _PRICELEVEL,
  '__module__' : 'market_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:market_data.priceLevel)
  })
_sym_db.RegisterMessage(priceLevel)

OHLCV = _reflection.GeneratedProtocolMessageType('OHLCV', (_message.Message,), {
  'DESCRIPTOR' : _OHLCV,
  '__module__' : 'market_data_proto_pb2'
  # @@protoc_insertion_point(class_scope:market_data.OHLCV)
  })
_sym_db.RegisterMessage(OHLCV)

_MARKETDATASERVICE = DESCRIPTOR.services_by_name['MarketDataService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=40
  _REQUEST._serialized_end=139
  _OB_REQUEST._serialized_start=141
  _OB_REQUEST._serialized_end=202
  _RESPONSE._serialized_start=204
  _RESPONSE._serialized_end=271
  _OB_RESPONSE._serialized_start=274
  _OB_RESPONSE._serialized_end=406
  _PRICELEVEL._serialized_start=408
  _PRICELEVEL._serialized_end=453
  _OHLCV._serialized_start=455
  _OHLCV._serialized_end=554
  _MARKETDATASERVICE._serialized_start=557
  _MARKETDATASERVICE._serialized_end=712
# @@protoc_insertion_point(module_scope)
