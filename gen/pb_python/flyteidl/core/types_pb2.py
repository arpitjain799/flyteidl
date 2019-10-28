# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/core/types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/core/types.proto',
  package='flyteidl.core',
  syntax='proto3',
  serialized_options=_b('Z0github.com/lyft/flyteidl/gen/pb-go/flyteidl/core'),
  serialized_pb=_b('\n\x19\x66lyteidl/core/types.proto\x12\rflyteidl.core\x1a\x1cgoogle/protobuf/struct.proto\"\x8c\x02\n\nSchemaType\x12\x37\n\x07\x63olumns\x18\x03 \x03(\x0b\x32&.flyteidl.core.SchemaType.SchemaColumn\x1a\xc4\x01\n\x0cSchemaColumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x04type\x18\x02 \x01(\x0e\x32\x37.flyteidl.core.SchemaType.SchemaColumn.SchemaColumnType\"_\n\x10SchemaColumnType\x12\x0b\n\x07INTEGER\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x0b\n\x07\x42OOLEAN\x10\x03\x12\x0c\n\x08\x44\x41TETIME\x10\x04\x12\x0c\n\x08\x44URATION\x10\x05\"\x8f\x01\n\x08\x42lobType\x12\x0e\n\x06\x66ormat\x18\x01 \x01(\t\x12\x42\n\x0e\x64imensionality\x18\x02 \x01(\x0e\x32*.flyteidl.core.BlobType.BlobDimensionality\"/\n\x12\x42lobDimensionality\x12\n\n\x06SINGLE\x10\x00\x12\r\n\tMULTIPART\x10\x01\"\xb0\x02\n\x0bLiteralType\x12+\n\x06simple\x18\x01 \x01(\x0e\x32\x19.flyteidl.core.SimpleTypeH\x00\x12+\n\x06schema\x18\x02 \x01(\x0b\x32\x19.flyteidl.core.SchemaTypeH\x00\x12\x35\n\x0f\x63ollection_type\x18\x03 \x01(\x0b\x32\x1a.flyteidl.core.LiteralTypeH\x00\x12\x34\n\x0emap_value_type\x18\x04 \x01(\x0b\x32\x1a.flyteidl.core.LiteralTypeH\x00\x12\'\n\x04\x62lob\x18\x05 \x01(\x0b\x32\x17.flyteidl.core.BlobTypeH\x00\x12)\n\x08metadata\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructB\x06\n\x04type\"/\n\x0fOutputReference\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\x0b\n\x03var\x18\x02 \x01(\t\"0\n\x05\x45rror\x12\x16\n\x0e\x66\x61iled_node_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t*\x86\x01\n\nSimpleType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07INTEGER\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\n\n\x06STRING\x10\x03\x12\x0b\n\x07\x42OOLEAN\x10\x04\x12\x0c\n\x08\x44\x41TETIME\x10\x05\x12\x0c\n\x08\x44URATION\x10\x06\x12\n\n\x06\x42INARY\x10\x07\x12\t\n\x05\x45RROR\x10\x08\x12\n\n\x06STRUCT\x10\tB2Z0github.com/lyft/flyteidl/gen/pb-go/flyteidl/coreb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])

_SIMPLETYPE = _descriptor.EnumDescriptor(
  name='SimpleType',
  full_name='flyteidl.core.SimpleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DURATION', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARY', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRUCT', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=898,
  serialized_end=1032,
)
_sym_db.RegisterEnumDescriptor(_SIMPLETYPE)

SimpleType = enum_type_wrapper.EnumTypeWrapper(_SIMPLETYPE)
NONE = 0
INTEGER = 1
FLOAT = 2
STRING = 3
BOOLEAN = 4
DATETIME = 5
DURATION = 6
BINARY = 7
ERROR = 8
STRUCT = 9


_SCHEMATYPE_SCHEMACOLUMN_SCHEMACOLUMNTYPE = _descriptor.EnumDescriptor(
  name='SchemaColumnType',
  full_name='flyteidl.core.SchemaType.SchemaColumn.SchemaColumnType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTEGER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DURATION', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=248,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_SCHEMATYPE_SCHEMACOLUMN_SCHEMACOLUMNTYPE)

_BLOBTYPE_BLOBDIMENSIONALITY = _descriptor.EnumDescriptor(
  name='BlobDimensionality',
  full_name='flyteidl.core.BlobType.BlobDimensionality',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SINGLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPART', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=442,
  serialized_end=489,
)
_sym_db.RegisterEnumDescriptor(_BLOBTYPE_BLOBDIMENSIONALITY)


_SCHEMATYPE_SCHEMACOLUMN = _descriptor.Descriptor(
  name='SchemaColumn',
  full_name='flyteidl.core.SchemaType.SchemaColumn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='flyteidl.core.SchemaType.SchemaColumn.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='flyteidl.core.SchemaType.SchemaColumn.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCHEMATYPE_SCHEMACOLUMN_SCHEMACOLUMNTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=343,
)

_SCHEMATYPE = _descriptor.Descriptor(
  name='SchemaType',
  full_name='flyteidl.core.SchemaType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='flyteidl.core.SchemaType.columns', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SCHEMATYPE_SCHEMACOLUMN, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=343,
)


_BLOBTYPE = _descriptor.Descriptor(
  name='BlobType',
  full_name='flyteidl.core.BlobType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='flyteidl.core.BlobType.format', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensionality', full_name='flyteidl.core.BlobType.dimensionality', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BLOBTYPE_BLOBDIMENSIONALITY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=489,
)


_LITERALTYPE = _descriptor.Descriptor(
  name='LiteralType',
  full_name='flyteidl.core.LiteralType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simple', full_name='flyteidl.core.LiteralType.simple', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema', full_name='flyteidl.core.LiteralType.schema', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_type', full_name='flyteidl.core.LiteralType.collection_type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_value_type', full_name='flyteidl.core.LiteralType.map_value_type', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob', full_name='flyteidl.core.LiteralType.blob', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='flyteidl.core.LiteralType.metadata', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='flyteidl.core.LiteralType.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=492,
  serialized_end=796,
)


_OUTPUTREFERENCE = _descriptor.Descriptor(
  name='OutputReference',
  full_name='flyteidl.core.OutputReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='flyteidl.core.OutputReference.node_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='var', full_name='flyteidl.core.OutputReference.var', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=798,
  serialized_end=845,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='flyteidl.core.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failed_node_id', full_name='flyteidl.core.Error.failed_node_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='flyteidl.core.Error.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=847,
  serialized_end=895,
)

_SCHEMATYPE_SCHEMACOLUMN.fields_by_name['type'].enum_type = _SCHEMATYPE_SCHEMACOLUMN_SCHEMACOLUMNTYPE
_SCHEMATYPE_SCHEMACOLUMN.containing_type = _SCHEMATYPE
_SCHEMATYPE_SCHEMACOLUMN_SCHEMACOLUMNTYPE.containing_type = _SCHEMATYPE_SCHEMACOLUMN
_SCHEMATYPE.fields_by_name['columns'].message_type = _SCHEMATYPE_SCHEMACOLUMN
_BLOBTYPE.fields_by_name['dimensionality'].enum_type = _BLOBTYPE_BLOBDIMENSIONALITY
_BLOBTYPE_BLOBDIMENSIONALITY.containing_type = _BLOBTYPE
_LITERALTYPE.fields_by_name['simple'].enum_type = _SIMPLETYPE
_LITERALTYPE.fields_by_name['schema'].message_type = _SCHEMATYPE
_LITERALTYPE.fields_by_name['collection_type'].message_type = _LITERALTYPE
_LITERALTYPE.fields_by_name['map_value_type'].message_type = _LITERALTYPE
_LITERALTYPE.fields_by_name['blob'].message_type = _BLOBTYPE
_LITERALTYPE.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LITERALTYPE.oneofs_by_name['type'].fields.append(
  _LITERALTYPE.fields_by_name['simple'])
_LITERALTYPE.fields_by_name['simple'].containing_oneof = _LITERALTYPE.oneofs_by_name['type']
_LITERALTYPE.oneofs_by_name['type'].fields.append(
  _LITERALTYPE.fields_by_name['schema'])
_LITERALTYPE.fields_by_name['schema'].containing_oneof = _LITERALTYPE.oneofs_by_name['type']
_LITERALTYPE.oneofs_by_name['type'].fields.append(
  _LITERALTYPE.fields_by_name['collection_type'])
_LITERALTYPE.fields_by_name['collection_type'].containing_oneof = _LITERALTYPE.oneofs_by_name['type']
_LITERALTYPE.oneofs_by_name['type'].fields.append(
  _LITERALTYPE.fields_by_name['map_value_type'])
_LITERALTYPE.fields_by_name['map_value_type'].containing_oneof = _LITERALTYPE.oneofs_by_name['type']
_LITERALTYPE.oneofs_by_name['type'].fields.append(
  _LITERALTYPE.fields_by_name['blob'])
_LITERALTYPE.fields_by_name['blob'].containing_oneof = _LITERALTYPE.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['SchemaType'] = _SCHEMATYPE
DESCRIPTOR.message_types_by_name['BlobType'] = _BLOBTYPE
DESCRIPTOR.message_types_by_name['LiteralType'] = _LITERALTYPE
DESCRIPTOR.message_types_by_name['OutputReference'] = _OUTPUTREFERENCE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.enum_types_by_name['SimpleType'] = _SIMPLETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SchemaType = _reflection.GeneratedProtocolMessageType('SchemaType', (_message.Message,), dict(

  SchemaColumn = _reflection.GeneratedProtocolMessageType('SchemaColumn', (_message.Message,), dict(
    DESCRIPTOR = _SCHEMATYPE_SCHEMACOLUMN,
    __module__ = 'flyteidl.core.types_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.core.SchemaType.SchemaColumn)
    ))
  ,
  DESCRIPTOR = _SCHEMATYPE,
  __module__ = 'flyteidl.core.types_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.SchemaType)
  ))
_sym_db.RegisterMessage(SchemaType)
_sym_db.RegisterMessage(SchemaType.SchemaColumn)

BlobType = _reflection.GeneratedProtocolMessageType('BlobType', (_message.Message,), dict(
  DESCRIPTOR = _BLOBTYPE,
  __module__ = 'flyteidl.core.types_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.BlobType)
  ))
_sym_db.RegisterMessage(BlobType)

LiteralType = _reflection.GeneratedProtocolMessageType('LiteralType', (_message.Message,), dict(
  DESCRIPTOR = _LITERALTYPE,
  __module__ = 'flyteidl.core.types_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.LiteralType)
  ))
_sym_db.RegisterMessage(LiteralType)

OutputReference = _reflection.GeneratedProtocolMessageType('OutputReference', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTREFERENCE,
  __module__ = 'flyteidl.core.types_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.OutputReference)
  ))
_sym_db.RegisterMessage(OutputReference)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'flyteidl.core.types_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.Error)
  ))
_sym_db.RegisterMessage(Error)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
