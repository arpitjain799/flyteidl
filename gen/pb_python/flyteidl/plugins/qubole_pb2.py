# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/qubole.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66lyteidl/plugins/qubole.proto\x12\x10\x66lyteidl.plugins\"b\n\tHiveQuery\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12\x1f\n\x0btimeout_sec\x18\x02 \x01(\rR\ntimeoutSec\x12\x1e\n\nretryCount\x18\x03 \x01(\rR\nretryCount\"L\n\x13HiveQueryCollection\x12\x35\n\x07queries\x18\x02 \x03(\x0b\x32\x1b.flyteidl.plugins.HiveQueryR\x07queries\"\xd1\x01\n\rQuboleHiveJob\x12#\n\rcluster_label\x18\x01 \x01(\tR\x0c\x63lusterLabel\x12T\n\x10query_collection\x18\x02 \x01(\x0b\x32%.flyteidl.plugins.HiveQueryCollectionB\x02\x18\x01R\x0fqueryCollection\x12\x12\n\x04tags\x18\x03 \x03(\tR\x04tags\x12\x31\n\x05query\x18\x04 \x01(\x0b\x32\x1b.flyteidl.plugins.HiveQueryR\x05queryB\xbd\x01\n\x14\x63om.flyteidl.pluginsB\x0bQuboleProtoP\x01Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/plugins\xa2\x02\x03\x46PX\xaa\x02\x10\x46lyteidl.Plugins\xca\x02\x10\x46lyteidl\\Plugins\xe2\x02\x1c\x46lyteidl\\Plugins\\GPBMetadata\xea\x02\x11\x46lyteidl::Pluginsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.plugins.qubole_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.flyteidl.pluginsB\013QuboleProtoP\001Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/plugins\242\002\003FPX\252\002\020Flyteidl.Plugins\312\002\020Flyteidl\\Plugins\342\002\034Flyteidl\\Plugins\\GPBMetadata\352\002\021Flyteidl::Plugins'
  _QUBOLEHIVEJOB.fields_by_name['query_collection']._options = None
  _QUBOLEHIVEJOB.fields_by_name['query_collection']._serialized_options = b'\030\001'
  _globals['_HIVEQUERY']._serialized_start=51
  _globals['_HIVEQUERY']._serialized_end=149
  _globals['_HIVEQUERYCOLLECTION']._serialized_start=151
  _globals['_HIVEQUERYCOLLECTION']._serialized_end=227
  _globals['_QUBOLEHIVEJOB']._serialized_start=230
  _globals['_QUBOLEHIVEJOB']._serialized_end=439
# @@protoc_insertion_point(module_scope)
