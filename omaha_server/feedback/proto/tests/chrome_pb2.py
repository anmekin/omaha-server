# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chrome.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chrome.proto',
  package='userfeedback',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x0c\x63hrome.proto\x12\x0cuserfeedback\"\x80\x02\n\nChromeData\x12K\n\x0f\x63hrome_platform\x18\x01 \x01(\x0e\x32\'.userfeedback.ChromeData.ChromePlatform:\tCHROME_OS\x12\x32\n\x0e\x63hrome_os_data\x18\x02 \x01(\x0b\x32\x1a.userfeedback.ChromeOsData\x12<\n\x13\x63hrome_browser_data\x18\x03 \x01(\x0b\x32\x1f.userfeedback.ChromeBrowserData\"3\n\x0e\x43hromePlatform\x12\r\n\tCHROME_OS\x10\x01\x12\x12\n\x0e\x43HROME_BROWSER\x10\x02\"\x8a\x02\n\x0c\x43hromeOsData\x12\x44\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32+.userfeedback.ChromeOsData.ChromeOsCategory:\x05OTHER\"\xb3\x01\n\x10\x43hromeOsCategory\x12\x10\n\x0c\x43ONNECTIVITY\x10\x01\x12\x08\n\x04SYNC\x10\x02\x12\t\n\x05\x43RASH\x10\x03\x12\x1d\n\x19PAGE_FORMATTING_OR_LAYOUT\x10\x04\x12\x16\n\x12\x45XTENSIONS_OR_APPS\x10\x05\x12\x15\n\x11STANDBY_OR_RESUME\x10\x06\x12\x11\n\rPHISHING_PAGE\x10\x07\x12\t\n\x05OTHER\x10\x08\x12\x0c\n\x08\x41UTOFILL\x10\t\"\xbc\x02\n\x11\x43hromeBrowserData\x12N\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x35.userfeedback.ChromeBrowserData.ChromeBrowserCategory:\x05OTHER\"\xd6\x01\n\x15\x43hromeBrowserCategory\x12\x1d\n\x19PAGE_FORMATTING_OR_LAYOUT\x10\x01\x12\x15\n\x11PAGES_NOT_LOADING\x10\x02\x12\x0b\n\x07PLUGINS\x10\x03\x12\x13\n\x0fTABS_OR_WINDOWS\x10\x04\x12\x16\n\x12SYNCED_PREFERENCES\x10\x05\x12\t\n\x05\x43RASH\x10\x06\x12\x16\n\x12\x45XTENSIONS_OR_APPS\x10\x07\x12\x11\n\rPHISHING_PAGE\x10\x08\x12\t\n\x05OTHER\x10\t\x12\x0c\n\x08\x41UTOFILL\x10\nB\x02H\x03')
)



_CHROMEDATA_CHROMEPLATFORM = _descriptor.EnumDescriptor(
  name='ChromePlatform',
  full_name='userfeedback.ChromeData.ChromePlatform',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHROME_OS', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHROME_BROWSER', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=236,
  serialized_end=287,
)
_sym_db.RegisterEnumDescriptor(_CHROMEDATA_CHROMEPLATFORM)

_CHROMEOSDATA_CHROMEOSCATEGORY = _descriptor.EnumDescriptor(
  name='ChromeOsCategory',
  full_name='userfeedback.ChromeOsData.ChromeOsCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONNECTIVITY', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRASH', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAGE_FORMATTING_OR_LAYOUT', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENSIONS_OR_APPS', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDBY_OR_RESUME', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHISHING_PAGE', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOFILL', index=8, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=377,
  serialized_end=556,
)
_sym_db.RegisterEnumDescriptor(_CHROMEOSDATA_CHROMEOSCATEGORY)

_CHROMEBROWSERDATA_CHROMEBROWSERCATEGORY = _descriptor.EnumDescriptor(
  name='ChromeBrowserCategory',
  full_name='userfeedback.ChromeBrowserData.ChromeBrowserCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAGE_FORMATTING_OR_LAYOUT', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAGES_NOT_LOADING', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLUGINS', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TABS_OR_WINDOWS', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNCED_PREFERENCES', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRASH', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENSIONS_OR_APPS', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHISHING_PAGE', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOFILL', index=9, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=661,
  serialized_end=875,
)
_sym_db.RegisterEnumDescriptor(_CHROMEBROWSERDATA_CHROMEBROWSERCATEGORY)


_CHROMEDATA = _descriptor.Descriptor(
  name='ChromeData',
  full_name='userfeedback.ChromeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chrome_platform', full_name='userfeedback.ChromeData.chrome_platform', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chrome_os_data', full_name='userfeedback.ChromeData.chrome_os_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chrome_browser_data', full_name='userfeedback.ChromeData.chrome_browser_data', index=2,
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
    _CHROMEDATA_CHROMEPLATFORM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=287,
)


_CHROMEOSDATA = _descriptor.Descriptor(
  name='ChromeOsData',
  full_name='userfeedback.ChromeOsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='userfeedback.ChromeOsData.category', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHROMEOSDATA_CHROMEOSCATEGORY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=556,
)


_CHROMEBROWSERDATA = _descriptor.Descriptor(
  name='ChromeBrowserData',
  full_name='userfeedback.ChromeBrowserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='userfeedback.ChromeBrowserData.category', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=9,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHROMEBROWSERDATA_CHROMEBROWSERCATEGORY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=875,
)

_CHROMEDATA.fields_by_name['chrome_platform'].enum_type = _CHROMEDATA_CHROMEPLATFORM
_CHROMEDATA.fields_by_name['chrome_os_data'].message_type = _CHROMEOSDATA
_CHROMEDATA.fields_by_name['chrome_browser_data'].message_type = _CHROMEBROWSERDATA
_CHROMEDATA_CHROMEPLATFORM.containing_type = _CHROMEDATA
_CHROMEOSDATA.fields_by_name['category'].enum_type = _CHROMEOSDATA_CHROMEOSCATEGORY
_CHROMEOSDATA_CHROMEOSCATEGORY.containing_type = _CHROMEOSDATA
_CHROMEBROWSERDATA.fields_by_name['category'].enum_type = _CHROMEBROWSERDATA_CHROMEBROWSERCATEGORY
_CHROMEBROWSERDATA_CHROMEBROWSERCATEGORY.containing_type = _CHROMEBROWSERDATA
DESCRIPTOR.message_types_by_name['ChromeData'] = _CHROMEDATA
DESCRIPTOR.message_types_by_name['ChromeOsData'] = _CHROMEOSDATA
DESCRIPTOR.message_types_by_name['ChromeBrowserData'] = _CHROMEBROWSERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChromeData = _reflection.GeneratedProtocolMessageType('ChromeData', (_message.Message,), dict(
  DESCRIPTOR = _CHROMEDATA,
  __module__ = 'chrome_pb2'
  # @@protoc_insertion_point(class_scope:userfeedback.ChromeData)
  ))
_sym_db.RegisterMessage(ChromeData)

ChromeOsData = _reflection.GeneratedProtocolMessageType('ChromeOsData', (_message.Message,), dict(
  DESCRIPTOR = _CHROMEOSDATA,
  __module__ = 'chrome_pb2'
  # @@protoc_insertion_point(class_scope:userfeedback.ChromeOsData)
  ))
_sym_db.RegisterMessage(ChromeOsData)

ChromeBrowserData = _reflection.GeneratedProtocolMessageType('ChromeBrowserData', (_message.Message,), dict(
  DESCRIPTOR = _CHROMEBROWSERDATA,
  __module__ = 'chrome_pb2'
  # @@protoc_insertion_point(class_scope:userfeedback.ChromeBrowserData)
  ))
_sym_db.RegisterMessage(ChromeBrowserData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
