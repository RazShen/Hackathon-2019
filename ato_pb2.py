# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ato.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import config_common_pb2 as config__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ato.proto',
  package='Config.Ato',
  syntax='proto2',
  serialized_options=_b('\n\027com.incapsula.visit.genB\017AtoConfigProtos'),
  serialized_pb=_b('\n\tato.proto\x12\nConfig.Ato\x1a\x13\x63onfig_common.proto\"\xc6\x01\n\x15LoginSuccessCondition\x12*\n\x04type\x18\x01 \x02(\x0e\x32\x1c.Config.Ato.LoginSuccessType\x12\x0e\n\x06status\x18\x02 \x01(\r\x12)\n\x06header\x18\x03 \x01(\x0b\x32\x19.Config.Common.HttpHeader\x12\x10\n\x08\x62odyWord\x18\x04 \x01(\x0c\x12\x1e\n\x10indicatesSuccess\x18\x05 \x01(\x08:\x04true\x12\x14\n\x0cheaderExists\x18\x06 \x01(\x0c\"\xbe\x01\n\x10LoginSuccessRule\x12\x0e\n\x06\x66ilter\x18\x01 \x02(\x0c\x12\x16\n\x0eloginParamName\x18\x02 \x02(\x0c\x12\x19\n\x11passwordParamName\x18\x03 \x02(\x0c\x12<\n\x11successConditions\x18\x04 \x03(\x0b\x32!.Config.Ato.LoginSuccessCondition\x12\x1d\n\x0e\x61llShouldMatch\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\n\n\x02id\x18\x06 \x02(\r\"P\n\x0cWorkerConfig\x12\x1f\n\x10\x65nableMonitoring\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10\x65nableMitigation\x18\x02 \x01(\x08:\x05\x66\x61lse\"o\n\x04Site\x12\x37\n\x11loginSuccessRules\x18\x01 \x03(\x0b\x32\x1c.Config.Ato.LoginSuccessRule\x12.\n\x0cworkerConfig\x18\x02 \x02(\x0b\x32\x18.Config.Ato.WorkerConfig*p\n\x10LoginSuccessType\x12\x0e\n\nATO_STATUS\x10\x01\x12\x0e\n\nATO_HEADER\x10\x02\x12\x11\n\rATO_BODY_WORD\x10\x03\x12\x15\n\x11\x41TO_HEADER_EXISTS\x10\x04\x12\x12\n\x0e\x41TO_EMPTY_BODY\x10\x05\x42*\n\x17\x63om.incapsula.visit.genB\x0f\x41toConfigProtos')
  ,
  dependencies=[config__common__pb2.DESCRIPTOR,])

_LOGINSUCCESSTYPE = _descriptor.EnumDescriptor(
  name='LoginSuccessType',
  full_name='Config.Ato.LoginSuccessType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ATO_STATUS', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATO_HEADER', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATO_BODY_WORD', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATO_HEADER_EXISTS', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATO_EMPTY_BODY', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=635,
  serialized_end=747,
)
_sym_db.RegisterEnumDescriptor(_LOGINSUCCESSTYPE)

LoginSuccessType = enum_type_wrapper.EnumTypeWrapper(_LOGINSUCCESSTYPE)
ATO_STATUS = 1
ATO_HEADER = 2
ATO_BODY_WORD = 3
ATO_HEADER_EXISTS = 4
ATO_EMPTY_BODY = 5



_LOGINSUCCESSCONDITION = _descriptor.Descriptor(
  name='LoginSuccessCondition',
  full_name='Config.Ato.LoginSuccessCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Config.Ato.LoginSuccessCondition.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Config.Ato.LoginSuccessCondition.status', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='Config.Ato.LoginSuccessCondition.header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bodyWord', full_name='Config.Ato.LoginSuccessCondition.bodyWord', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indicatesSuccess', full_name='Config.Ato.LoginSuccessCondition.indicatesSuccess', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headerExists', full_name='Config.Ato.LoginSuccessCondition.headerExists', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=47,
  serialized_end=245,
)


_LOGINSUCCESSRULE = _descriptor.Descriptor(
  name='LoginSuccessRule',
  full_name='Config.Ato.LoginSuccessRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='Config.Ato.LoginSuccessRule.filter', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loginParamName', full_name='Config.Ato.LoginSuccessRule.loginParamName', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passwordParamName', full_name='Config.Ato.LoginSuccessRule.passwordParamName', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='successConditions', full_name='Config.Ato.LoginSuccessRule.successConditions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allShouldMatch', full_name='Config.Ato.LoginSuccessRule.allShouldMatch', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Config.Ato.LoginSuccessRule.id', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=248,
  serialized_end=438,
)


_WORKERCONFIG = _descriptor.Descriptor(
  name='WorkerConfig',
  full_name='Config.Ato.WorkerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enableMonitoring', full_name='Config.Ato.WorkerConfig.enableMonitoring', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enableMitigation', full_name='Config.Ato.WorkerConfig.enableMitigation', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=440,
  serialized_end=520,
)


_SITE = _descriptor.Descriptor(
  name='Site',
  full_name='Config.Ato.Site',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loginSuccessRules', full_name='Config.Ato.Site.loginSuccessRules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workerConfig', full_name='Config.Ato.Site.workerConfig', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=522,
  serialized_end=633,
)

_LOGINSUCCESSCONDITION.fields_by_name['type'].enum_type = _LOGINSUCCESSTYPE
_LOGINSUCCESSCONDITION.fields_by_name['header'].message_type = config__common__pb2._HTTPHEADER
_LOGINSUCCESSRULE.fields_by_name['successConditions'].message_type = _LOGINSUCCESSCONDITION
_SITE.fields_by_name['loginSuccessRules'].message_type = _LOGINSUCCESSRULE
_SITE.fields_by_name['workerConfig'].message_type = _WORKERCONFIG
DESCRIPTOR.message_types_by_name['LoginSuccessCondition'] = _LOGINSUCCESSCONDITION
DESCRIPTOR.message_types_by_name['LoginSuccessRule'] = _LOGINSUCCESSRULE
DESCRIPTOR.message_types_by_name['WorkerConfig'] = _WORKERCONFIG
DESCRIPTOR.message_types_by_name['Site'] = _SITE
DESCRIPTOR.enum_types_by_name['LoginSuccessType'] = _LOGINSUCCESSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginSuccessCondition = _reflection.GeneratedProtocolMessageType('LoginSuccessCondition', (_message.Message,), dict(
  DESCRIPTOR = _LOGINSUCCESSCONDITION,
  __module__ = 'ato_pb2'
  # @@protoc_insertion_point(class_scope:Config.Ato.LoginSuccessCondition)
  ))
_sym_db.RegisterMessage(LoginSuccessCondition)

LoginSuccessRule = _reflection.GeneratedProtocolMessageType('LoginSuccessRule', (_message.Message,), dict(
  DESCRIPTOR = _LOGINSUCCESSRULE,
  __module__ = 'ato_pb2'
  # @@protoc_insertion_point(class_scope:Config.Ato.LoginSuccessRule)
  ))
_sym_db.RegisterMessage(LoginSuccessRule)

WorkerConfig = _reflection.GeneratedProtocolMessageType('WorkerConfig', (_message.Message,), dict(
  DESCRIPTOR = _WORKERCONFIG,
  __module__ = 'ato_pb2'
  # @@protoc_insertion_point(class_scope:Config.Ato.WorkerConfig)
  ))
_sym_db.RegisterMessage(WorkerConfig)

Site = _reflection.GeneratedProtocolMessageType('Site', (_message.Message,), dict(
  DESCRIPTOR = _SITE,
  __module__ = 'ato_pb2'
  # @@protoc_insertion_point(class_scope:Config.Ato.Site)
  ))
_sym_db.RegisterMessage(Site)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)