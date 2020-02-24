# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/PlayerPath.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import Origin_pb2 as pyatv_dot_mrp_dot_protobuf_dot_Origin__pb2
from pyatv.mrp.protobuf import NowPlayingClient_pb2 as pyatv_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2
from pyatv.mrp.protobuf import NowPlayingPlayer_pb2 as pyatv_dot_mrp_dot_protobuf_dot_NowPlayingPlayer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/PlayerPath.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n#pyatv/mrp/protobuf/PlayerPath.proto\x1a\x1fpyatv/mrp/protobuf/Origin.proto\x1a)pyatv/mrp/protobuf/NowPlayingClient.proto\x1a)pyatv/mrp/protobuf/NowPlayingPlayer.proto\"k\n\nPlayerPath\x12\x17\n\x06origin\x18\x01 \x01(\x0b\x32\x07.Origin\x12!\n\x06\x63lient\x18\x02 \x01(\x0b\x32\x11.NowPlayingClient\x12!\n\x06player\x18\x03 \x01(\x0b\x32\x11.NowPlayingPlayer'
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_Origin__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_NowPlayingPlayer__pb2.DESCRIPTOR,])




_PLAYERPATH = _descriptor.Descriptor(
  name='PlayerPath',
  full_name='PlayerPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='PlayerPath.origin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client', full_name='PlayerPath.client', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player', full_name='PlayerPath.player', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=265,
)

_PLAYERPATH.fields_by_name['origin'].message_type = pyatv_dot_mrp_dot_protobuf_dot_Origin__pb2._ORIGIN
_PLAYERPATH.fields_by_name['client'].message_type = pyatv_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2._NOWPLAYINGCLIENT
_PLAYERPATH.fields_by_name['player'].message_type = pyatv_dot_mrp_dot_protobuf_dot_NowPlayingPlayer__pb2._NOWPLAYINGPLAYER
DESCRIPTOR.message_types_by_name['PlayerPath'] = _PLAYERPATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerPath = _reflection.GeneratedProtocolMessageType('PlayerPath', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERPATH,
  '__module__' : 'pyatv.mrp.protobuf.PlayerPath_pb2'
  # @@protoc_insertion_point(class_scope:PlayerPath)
  })
_sym_db.RegisterMessage(PlayerPath)


# @@protoc_insertion_point(module_scope)
