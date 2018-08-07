# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/launch_plan.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2
from flyteidl.core import interface_pb2 as flyteidl_dot_core_dot_interface__pb2
from flyteidl.admin import schedule_pb2 as flyteidl_dot_admin_dot_schedule__pb2
from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/launch_plan.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_pb=_b('\n flyteidl/admin/launch_plan.proto\x12\x0e\x66lyteidl.admin\x1a\x1c\x66lyteidl/core/literals.proto\x1a\x1d\x66lyteidl/core/interface.proto\x1a\x1d\x66lyteidl/admin/schedule.proto\x1a\x1b\x66lyteidl/admin/common.proto\"\x80\x01\n\x17LaunchPlanCreateRequest\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.flyteidl.admin.Identifier\x12\x0f\n\x07version\x18\x02 \x01(\t\x12,\n\x04spec\x18\x03 \x01(\x0b\x32\x1e.flyteidl.admin.LaunchPlanSpec\"\'\n\x18LaunchPlanCreateResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\"\xb2\x01\n\nLaunchPlan\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.flyteidl.admin.Identifier\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12,\n\x04spec\x18\x04 \x01(\x0b\x32\x1e.flyteidl.admin.LaunchPlanSpec\x12\x30\n\x06status\x18\x05 \x01(\x0b\x32 .flyteidl.admin.LaunchPlanStatus\"B\n\x0eLaunchPlanList\x12\x30\n\x0claunch_plans\x18\x01 \x03(\x0b\x32\x1a.flyteidl.admin.LaunchPlan\"\xc9\x01\n\x0eLaunchPlanSpec\x12\x14\n\x0cworkflow_urn\x18\x01 \x01(\t\x12;\n\x0f\x65ntity_metadata\x18\x02 \x01(\x0b\x32\".flyteidl.admin.LaunchPlanMetadata\x12\x33\n\x0e\x64\x65\x66\x61ult_inputs\x18\x03 \x01(\x0b\x32\x1b.flyteidl.core.ParameterMap\x12/\n\x0c\x66ixed_inputs\x18\x04 \x01(\x0b\x32\x19.flyteidl.core.LiteralMap\"\xae\x01\n\x10LaunchPlanStatus\x12.\n\x05phase\x18\x01 \x01(\x0e\x32\x1f.flyteidl.admin.LaunchPlanPhase\x12\x34\n\x0f\x65xpected_inputs\x18\x02 \x01(\x0b\x32\x1b.flyteidl.core.ParameterMap\x12\x34\n\x10\x65xpected_outputs\x18\x03 \x01(\x0b\x32\x1a.flyteidl.core.VariableMap\"u\n\x12LaunchPlanMetadata\x12*\n\x08schedule\x18\x01 \x01(\x0b\x32\x18.flyteidl.admin.Schedule\x12\x33\n\rnotifications\x18\x02 \x03(\x0b\x32\x1c.flyteidl.admin.Notification*+\n\x0fLaunchPlanPhase\x12\x0c\n\x08INACTIVE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x42\x33Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_core_dot_literals__pb2.DESCRIPTOR,flyteidl_dot_core_dot_interface__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_schedule__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_common__pb2.DESCRIPTOR,])

_LAUNCHPLANPHASE = _descriptor.EnumDescriptor(
  name='LaunchPlanPhase',
  full_name='flyteidl.admin.LaunchPlanPhase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1094,
  serialized_end=1137,
)
_sym_db.RegisterEnumDescriptor(_LAUNCHPLANPHASE)

LaunchPlanPhase = enum_type_wrapper.EnumTypeWrapper(_LAUNCHPLANPHASE)
INACTIVE = 0
ACTIVE = 1



_LAUNCHPLANCREATEREQUEST = _descriptor.Descriptor(
  name='LaunchPlanCreateRequest',
  full_name='flyteidl.admin.LaunchPlanCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.LaunchPlanCreateRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='flyteidl.admin.LaunchPlanCreateRequest.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='flyteidl.admin.LaunchPlanCreateRequest.spec', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=302,
)


_LAUNCHPLANCREATERESPONSE = _descriptor.Descriptor(
  name='LaunchPlanCreateResponse',
  full_name='flyteidl.admin.LaunchPlanCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urn', full_name='flyteidl.admin.LaunchPlanCreateResponse.urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=343,
)


_LAUNCHPLAN = _descriptor.Descriptor(
  name='LaunchPlan',
  full_name='flyteidl.admin.LaunchPlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.LaunchPlan.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='flyteidl.admin.LaunchPlan.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='flyteidl.admin.LaunchPlan.urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='flyteidl.admin.LaunchPlan.spec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='flyteidl.admin.LaunchPlan.status', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=524,
)


_LAUNCHPLANLIST = _descriptor.Descriptor(
  name='LaunchPlanList',
  full_name='flyteidl.admin.LaunchPlanList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='launch_plans', full_name='flyteidl.admin.LaunchPlanList.launch_plans', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=592,
)


_LAUNCHPLANSPEC = _descriptor.Descriptor(
  name='LaunchPlanSpec',
  full_name='flyteidl.admin.LaunchPlanSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow_urn', full_name='flyteidl.admin.LaunchPlanSpec.workflow_urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_metadata', full_name='flyteidl.admin.LaunchPlanSpec.entity_metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_inputs', full_name='flyteidl.admin.LaunchPlanSpec.default_inputs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_inputs', full_name='flyteidl.admin.LaunchPlanSpec.fixed_inputs', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=796,
)


_LAUNCHPLANSTATUS = _descriptor.Descriptor(
  name='LaunchPlanStatus',
  full_name='flyteidl.admin.LaunchPlanStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phase', full_name='flyteidl.admin.LaunchPlanStatus.phase', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_inputs', full_name='flyteidl.admin.LaunchPlanStatus.expected_inputs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_outputs', full_name='flyteidl.admin.LaunchPlanStatus.expected_outputs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=799,
  serialized_end=973,
)


_LAUNCHPLANMETADATA = _descriptor.Descriptor(
  name='LaunchPlanMetadata',
  full_name='flyteidl.admin.LaunchPlanMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedule', full_name='flyteidl.admin.LaunchPlanMetadata.schedule', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifications', full_name='flyteidl.admin.LaunchPlanMetadata.notifications', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=975,
  serialized_end=1092,
)

_LAUNCHPLANCREATEREQUEST.fields_by_name['id'].message_type = flyteidl_dot_admin_dot_common__pb2._IDENTIFIER
_LAUNCHPLANCREATEREQUEST.fields_by_name['spec'].message_type = _LAUNCHPLANSPEC
_LAUNCHPLAN.fields_by_name['id'].message_type = flyteidl_dot_admin_dot_common__pb2._IDENTIFIER
_LAUNCHPLAN.fields_by_name['spec'].message_type = _LAUNCHPLANSPEC
_LAUNCHPLAN.fields_by_name['status'].message_type = _LAUNCHPLANSTATUS
_LAUNCHPLANLIST.fields_by_name['launch_plans'].message_type = _LAUNCHPLAN
_LAUNCHPLANSPEC.fields_by_name['entity_metadata'].message_type = _LAUNCHPLANMETADATA
_LAUNCHPLANSPEC.fields_by_name['default_inputs'].message_type = flyteidl_dot_core_dot_interface__pb2._PARAMETERMAP
_LAUNCHPLANSPEC.fields_by_name['fixed_inputs'].message_type = flyteidl_dot_core_dot_literals__pb2._LITERALMAP
_LAUNCHPLANSTATUS.fields_by_name['phase'].enum_type = _LAUNCHPLANPHASE
_LAUNCHPLANSTATUS.fields_by_name['expected_inputs'].message_type = flyteidl_dot_core_dot_interface__pb2._PARAMETERMAP
_LAUNCHPLANSTATUS.fields_by_name['expected_outputs'].message_type = flyteidl_dot_core_dot_interface__pb2._VARIABLEMAP
_LAUNCHPLANMETADATA.fields_by_name['schedule'].message_type = flyteidl_dot_admin_dot_schedule__pb2._SCHEDULE
_LAUNCHPLANMETADATA.fields_by_name['notifications'].message_type = flyteidl_dot_admin_dot_common__pb2._NOTIFICATION
DESCRIPTOR.message_types_by_name['LaunchPlanCreateRequest'] = _LAUNCHPLANCREATEREQUEST
DESCRIPTOR.message_types_by_name['LaunchPlanCreateResponse'] = _LAUNCHPLANCREATERESPONSE
DESCRIPTOR.message_types_by_name['LaunchPlan'] = _LAUNCHPLAN
DESCRIPTOR.message_types_by_name['LaunchPlanList'] = _LAUNCHPLANLIST
DESCRIPTOR.message_types_by_name['LaunchPlanSpec'] = _LAUNCHPLANSPEC
DESCRIPTOR.message_types_by_name['LaunchPlanStatus'] = _LAUNCHPLANSTATUS
DESCRIPTOR.message_types_by_name['LaunchPlanMetadata'] = _LAUNCHPLANMETADATA
DESCRIPTOR.enum_types_by_name['LaunchPlanPhase'] = _LAUNCHPLANPHASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LaunchPlanCreateRequest = _reflection.GeneratedProtocolMessageType('LaunchPlanCreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHPLANCREATEREQUEST,
  __module__ = 'flyteidl.admin.launch_plan_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LaunchPlanCreateRequest)
  ))
_sym_db.RegisterMessage(LaunchPlanCreateRequest)

LaunchPlanCreateResponse = _reflection.GeneratedProtocolMessageType('LaunchPlanCreateResponse', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHPLANCREATERESPONSE,
  __module__ = 'flyteidl.admin.launch_plan_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LaunchPlanCreateResponse)
  ))
_sym_db.RegisterMessage(LaunchPlanCreateResponse)

LaunchPlan = _reflection.GeneratedProtocolMessageType('LaunchPlan', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHPLAN,
  __module__ = 'flyteidl.admin.launch_plan_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LaunchPlan)
  ))
_sym_db.RegisterMessage(LaunchPlan)

LaunchPlanList = _reflection.GeneratedProtocolMessageType('LaunchPlanList', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHPLANLIST,
  __module__ = 'flyteidl.admin.launch_plan_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LaunchPlanList)
  ))
_sym_db.RegisterMessage(LaunchPlanList)

LaunchPlanSpec = _reflection.GeneratedProtocolMessageType('LaunchPlanSpec', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHPLANSPEC,
  __module__ = 'flyteidl.admin.launch_plan_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LaunchPlanSpec)
  ))
_sym_db.RegisterMessage(LaunchPlanSpec)

LaunchPlanStatus = _reflection.GeneratedProtocolMessageType('LaunchPlanStatus', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHPLANSTATUS,
  __module__ = 'flyteidl.admin.launch_plan_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LaunchPlanStatus)
  ))
_sym_db.RegisterMessage(LaunchPlanStatus)

LaunchPlanMetadata = _reflection.GeneratedProtocolMessageType('LaunchPlanMetadata', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHPLANMETADATA,
  __module__ = 'flyteidl.admin.launch_plan_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LaunchPlanMetadata)
  ))
_sym_db.RegisterMessage(LaunchPlanMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/admin'))
# @@protoc_insertion_point(module_scope)
