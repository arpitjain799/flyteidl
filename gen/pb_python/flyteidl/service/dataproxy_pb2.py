# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/service/dataproxy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n flyteidl/service/dataproxy.proto\x12\x10\x66lyteidl.service\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1c\x66lyteidl/core/literals.proto\"\x97\x01\n\x1c\x43reateUploadLocationResponse\x12\x1d\n\nsigned_url\x18\x01 \x01(\tR\tsignedUrl\x12\x1d\n\nnative_url\x18\x02 \x01(\tR\tnativeUrl\x12\x39\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\"\xc6\x01\n\x1b\x43reateUploadLocationRequest\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x1a\n\x08\x66ilename\x18\x03 \x01(\tR\x08\x66ilename\x12\x38\n\nexpires_in\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\texpiresIn\x12\x1f\n\x0b\x63ontent_md5\x18\x05 \x01(\x0cR\ncontentMd5\"|\n\x1d\x43reateDownloadLocationRequest\x12\x1d\n\nnative_url\x18\x01 \x01(\tR\tnativeUrl\x12\x38\n\nexpires_in\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\texpiresIn:\x02\x18\x01\"~\n\x1e\x43reateDownloadLocationResponse\x12\x1d\n\nsigned_url\x18\x01 \x01(\tR\tsignedUrl\x12\x39\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt:\x02\x18\x01\"\xfa\x01\n\x19\x43reateDownloadLinkRequest\x12\x43\n\rartifact_type\x18\x01 \x01(\x0e\x32\x1e.flyteidl.service.ArtifactTypeR\x0c\x61rtifactType\x12\x38\n\nexpires_in\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\texpiresIn\x12T\n\x11node_execution_id\x18\x03 \x01(\x0b\x32&.flyteidl.core.NodeExecutionIdentifierH\x00R\x0fnodeExecutionIdB\x08\n\x06source\"v\n\x1a\x43reateDownloadLinkResponse\x12\x1d\n\nsigned_url\x18\x01 \x03(\tR\tsignedUrl\x12\x39\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\"-\n\x0eGetDataRequest\x12\x1b\n\tflyte_url\x18\x01 \x01(\tR\x08\x66lyteUrl\"\xc0\x01\n\x0fGetDataResponse\x12<\n\x0bliteral_map\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.LiteralMapH\x00R\nliteralMap\x12g\n\x18\x66lyte_deck_download_link\x18\x02 \x01(\x0b\x32,.flyteidl.service.CreateDownloadLinkResponseH\x00R\x15\x66lyteDeckDownloadLinkB\x06\n\x04\x64\x61ta*C\n\x0c\x41rtifactType\x12\x1b\n\x17\x41RTIFACT_TYPE_UNDEFINED\x10\x00\x12\x16\n\x12\x41RTIFACT_TYPE_DECK\x10\x01\x32\xe2\x04\n\x10\x44\x61taProxyService\x12\xa0\x01\n\x14\x43reateUploadLocation\x12-.flyteidl.service.CreateUploadLocationRequest\x1a..flyteidl.service.CreateUploadLocationResponse\")\x82\xd3\xe4\x93\x02#:\x01*\"\x1e/api/v1/dataproxy/artifact_urn\x12\xa6\x01\n\x16\x43reateDownloadLocation\x12/.flyteidl.service.CreateDownloadLocationRequest\x1a\x30.flyteidl.service.CreateDownloadLocationResponse\")\x88\x02\x01\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/dataproxy/artifact_urn\x12\x9b\x01\n\x12\x43reateDownloadLink\x12+.flyteidl.service.CreateDownloadLinkRequest\x1a,.flyteidl.service.CreateDownloadLinkResponse\"*\x82\xd3\xe4\x93\x02$:\x01*\"\x1f/api/v1/dataproxy/artifact_link\x12\x64\n\x07GetData\x12 .flyteidl.service.GetDataRequest\x1a!.flyteidl.service.GetDataResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/v1/dataB\xc0\x01\n\x14\x63om.flyteidl.serviceB\x0e\x44\x61taproxyProtoP\x01Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/service\xa2\x02\x03\x46SX\xaa\x02\x10\x46lyteidl.Service\xca\x02\x10\x46lyteidl\\Service\xe2\x02\x1c\x46lyteidl\\Service\\GPBMetadata\xea\x02\x11\x46lyteidl::Serviceb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.service.dataproxy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.flyteidl.serviceB\016DataproxyProtoP\001Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/service\242\002\003FSX\252\002\020Flyteidl.Service\312\002\020Flyteidl\\Service\342\002\034Flyteidl\\Service\\GPBMetadata\352\002\021Flyteidl::Service'
  _CREATEDOWNLOADLOCATIONREQUEST._options = None
  _CREATEDOWNLOADLOCATIONREQUEST._serialized_options = b'\030\001'
  _CREATEDOWNLOADLOCATIONRESPONSE._options = None
  _CREATEDOWNLOADLOCATIONRESPONSE._serialized_options = b'\030\001'
  _DATAPROXYSERVICE.methods_by_name['CreateUploadLocation']._options = None
  _DATAPROXYSERVICE.methods_by_name['CreateUploadLocation']._serialized_options = b'\202\323\344\223\002#:\001*\"\036/api/v1/dataproxy/artifact_urn'
  _DATAPROXYSERVICE.methods_by_name['CreateDownloadLocation']._options = None
  _DATAPROXYSERVICE.methods_by_name['CreateDownloadLocation']._serialized_options = b'\210\002\001\202\323\344\223\002 \022\036/api/v1/dataproxy/artifact_urn'
  _DATAPROXYSERVICE.methods_by_name['CreateDownloadLink']._options = None
  _DATAPROXYSERVICE.methods_by_name['CreateDownloadLink']._serialized_options = b'\202\323\344\223\002$:\001*\"\037/api/v1/dataproxy/artifact_link'
  _DATAPROXYSERVICE.methods_by_name['GetData']._options = None
  _DATAPROXYSERVICE.methods_by_name['GetData']._serialized_options = b'\202\323\344\223\002\016\022\014/api/v1/data'
  _ARTIFACTTYPE._serialized_start=1435
  _ARTIFACTTYPE._serialized_end=1502
  _CREATEUPLOADLOCATIONRESPONSE._serialized_start=212
  _CREATEUPLOADLOCATIONRESPONSE._serialized_end=363
  _CREATEUPLOADLOCATIONREQUEST._serialized_start=366
  _CREATEUPLOADLOCATIONREQUEST._serialized_end=564
  _CREATEDOWNLOADLOCATIONREQUEST._serialized_start=566
  _CREATEDOWNLOADLOCATIONREQUEST._serialized_end=690
  _CREATEDOWNLOADLOCATIONRESPONSE._serialized_start=692
  _CREATEDOWNLOADLOCATIONRESPONSE._serialized_end=818
  _CREATEDOWNLOADLINKREQUEST._serialized_start=821
  _CREATEDOWNLOADLINKREQUEST._serialized_end=1071
  _CREATEDOWNLOADLINKRESPONSE._serialized_start=1073
  _CREATEDOWNLOADLINKRESPONSE._serialized_end=1191
  _GETDATAREQUEST._serialized_start=1193
  _GETDATAREQUEST._serialized_end=1238
  _GETDATARESPONSE._serialized_start=1241
  _GETDATARESPONSE._serialized_end=1433
  _DATAPROXYSERVICE._serialized_start=1505
  _DATAPROXYSERVICE._serialized_end=2115
# @@protoc_insertion_point(module_scope)
