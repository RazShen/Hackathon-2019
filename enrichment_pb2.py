# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enrichment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import abp_pb2 as abp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='enrichment.proto',
  package='Config.Enrichment',
  syntax='proto2',
  serialized_options=_b('\n\027com.incapsula.visit.genB\026EnrichmentConfigProtos'),
  serialized_pb=_b('\n\x10\x65nrichment.proto\x12\x11\x43onfig.Enrichment\x1a\tabp.proto\"%\n\x04Site\x12\x1d\n\x03\x61\x62p\x18\x01 \x01(\x0b\x32\x10.Config.Abp.SiteB1\n\x17\x63om.incapsula.visit.genB\x16\x45nrichmentConfigProtos')
  ,
  dependencies=[abp__pb2.DESCRIPTOR,])




_SITE = _descriptor.Descriptor(
  name='Site',
  full_name='Config.Enrichment.Site',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='abp', full_name='Config.Enrichment.Site.abp', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=50,
  serialized_end=87,
)

_SITE.fields_by_name['abp'].message_type = abp__pb2._SITE
DESCRIPTOR.message_types_by_name['Site'] = _SITE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Site = _reflection.GeneratedProtocolMessageType('Site', (_message.Message,), dict(
  DESCRIPTOR = _SITE,
  __module__ = 'enrichment_pb2'
  # @@protoc_insertion_point(class_scope:Config.Enrichment.Site)
  ))
_sym_db.RegisterMessage(Site)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
