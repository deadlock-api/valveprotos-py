# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_unified_base.steamworkssdk.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.steammessages_unified_base.steamworkssdk.proto\x1a google/protobuf/descriptor.proto*]\n\x13\x45ProtoExecutionSite\x12 \n\x1ck_EProtoExecutionSiteUnknown\x10\x00\x12$\n k_EProtoExecutionSiteSteamClient\x10\x03:4\n\x0b\x64\x65scription\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\t:>\n\x13service_description\x12\x1f.google.protobuf.ServiceOptions\x18\xd0\x86\x03 \x01(\t:u\n\x16service_execution_site\x12\x1f.google.protobuf.ServiceOptions\x18\xd8\x86\x03 \x01(\x0e\x32\x14.EProtoExecutionSite:\x1ck_EProtoExecutionSiteUnknown:<\n\x12method_description\x12\x1e.google.protobuf.MethodOptions\x18\xd0\x86\x03 \x01(\t:8\n\x10\x65num_description\x12\x1c.google.protobuf.EnumOptions\x18\xd0\x86\x03 \x01(\t:C\n\x16\x65num_value_description\x12!.google.protobuf.EnumValueOptions\x18\xd0\x86\x03 \x01(\tB\x05H\x01\x80\x01\x00')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_unified_base.steamworkssdk_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(description)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_description)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_execution_site)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method_description)
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_description)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value_description)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001\200\001\000'
  _EPROTOEXECUTIONSITE._serialized_start=84
  _EPROTOEXECUTIONSITE._serialized_end=177
# @@protoc_insertion_point(module_scope)
