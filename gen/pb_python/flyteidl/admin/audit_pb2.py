# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/audit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/audit.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_options=_b('Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/admin'),
  serialized_pb=_b('\n\x1a\x66lyteidl/admin/audit.proto\x12\x0e\x66lyteidl.admin\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb4\x01\n\x08\x41uditLog\x12,\n\tprincipal\x18\x01 \x01(\x0b\x32\x19.flyteidl.admin.Principal\x12\x11\n\tclient_ip\x18\x02 \x01(\t\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12(\n\x07request\x18\x04 \x01(\x0b\x32\x17.flyteidl.admin.Request\x12*\n\x08response\x18\x05 \x01(\x0b\x32\x18.flyteidl.admin.Response\"Q\n\tPrincipal\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x33\n\x0ftoken_issued_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa0\x02\n\x07Request\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x11\n\thttp_verb\x18\x02 \x01(\t\x12;\n\nparameters\x18\x03 \x03(\x0b\x32\'.flyteidl.admin.Request.ParametersEntry\x12*\n\x04mode\x18\x04 \x01(\x0e\x32\x1c.flyteidl.admin.Request.Mode\x12/\n\x0breceived_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x04Mode\x12\r\n\tREAD_ONLY\x10\x00\x12\x0e\n\nREAD_WRITE\x10\x01\"N\n\x08Response\x12\x15\n\rresponse_code\x18\x01 \x01(\t\x12+\n\x07sent_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB3Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_REQUEST_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='flyteidl.admin.Request.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ_ONLY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_WRITE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=597,
  serialized_end=634,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_MODE)


_AUDITLOG = _descriptor.Descriptor(
  name='AuditLog',
  full_name='flyteidl.admin.AuditLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='principal', full_name='flyteidl.admin.AuditLog.principal', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_ip', full_name='flyteidl.admin.AuditLog.client_ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='flyteidl.admin.AuditLog.client_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='flyteidl.admin.AuditLog.request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='flyteidl.admin.AuditLog.response', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=80,
  serialized_end=260,
)


_PRINCIPAL = _descriptor.Descriptor(
  name='Principal',
  full_name='flyteidl.admin.Principal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject', full_name='flyteidl.admin.Principal.subject', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_issued_at', full_name='flyteidl.admin.Principal.token_issued_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=262,
  serialized_end=343,
)


_REQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='flyteidl.admin.Request.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.admin.Request.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.admin.Request.ParametersEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=595,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='flyteidl.admin.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='flyteidl.admin.Request.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_verb', full_name='flyteidl.admin.Request.http_verb', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='flyteidl.admin.Request.parameters', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='flyteidl.admin.Request.mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='received_at', full_name='flyteidl.admin.Request.received_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_PARAMETERSENTRY, ],
  enum_types=[
    _REQUEST_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=634,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='flyteidl.admin.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_code', full_name='flyteidl.admin.Response.response_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sent_at', full_name='flyteidl.admin.Response.sent_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=636,
  serialized_end=714,
)

_AUDITLOG.fields_by_name['principal'].message_type = _PRINCIPAL
_AUDITLOG.fields_by_name['request'].message_type = _REQUEST
_AUDITLOG.fields_by_name['response'].message_type = _RESPONSE
_PRINCIPAL.fields_by_name['token_issued_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REQUEST_PARAMETERSENTRY.containing_type = _REQUEST
_REQUEST.fields_by_name['parameters'].message_type = _REQUEST_PARAMETERSENTRY
_REQUEST.fields_by_name['mode'].enum_type = _REQUEST_MODE
_REQUEST.fields_by_name['received_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REQUEST_MODE.containing_type = _REQUEST
_RESPONSE.fields_by_name['sent_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['AuditLog'] = _AUDITLOG
DESCRIPTOR.message_types_by_name['Principal'] = _PRINCIPAL
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuditLog = _reflection.GeneratedProtocolMessageType('AuditLog', (_message.Message,), dict(
  DESCRIPTOR = _AUDITLOG,
  __module__ = 'flyteidl.admin.audit_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.AuditLog)
  ))
_sym_db.RegisterMessage(AuditLog)

Principal = _reflection.GeneratedProtocolMessageType('Principal', (_message.Message,), dict(
  DESCRIPTOR = _PRINCIPAL,
  __module__ = 'flyteidl.admin.audit_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Principal)
  ))
_sym_db.RegisterMessage(Principal)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST_PARAMETERSENTRY,
    __module__ = 'flyteidl.admin.audit_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.admin.Request.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _REQUEST,
  __module__ = 'flyteidl.admin.audit_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Request)
  ))
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.ParametersEntry)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'flyteidl.admin.audit_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR._options = None
_REQUEST_PARAMETERSENTRY._options = None
# @@protoc_insertion_point(module_scope)
