# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Muse.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Muse.proto',
  package='',
  serialized_pb='\n\nMuse.proto\"3\n\x12MuseDataCollection\x12\x1d\n\ncollection\x18\x01 \x03(\x0b\x32\t.MuseData\"\xd0\x01\n\x08MuseData\x12\x11\n\ttimestamp\x18\x01 \x02(\x01\x12$\n\x08\x64\x61tatype\x18\x02 \x02(\x0e\x32\x12.MuseData.Datatype\"|\n\x08\x44\x61tatype\x12\x07\n\x03\x45\x45G\x10\x00\x12\t\n\x05QUANT\x10\x01\x12\t\n\x05\x41\x43\x43\x45L\x10\x02\x12\x0b\n\x07\x42\x41TTERY\x10\x03\x12\x0b\n\x07VERSION\x10\x04\x12\n\n\x06\x43ONFIG\x10\x05\x12\x0e\n\nANNOTATION\x10\x06\x12\r\n\tHISTOGRAM\x10\x07\x12\x0c\n\x08\x41LGVALUE\x10\x08*\x05\x08\x08\x10\xe8\x07*\x06\x08\xe8\x07\x10\x80\x10\"\xc3\x01\n\x07MuseEEG\x12\x10\n\x08left_aux\x18\x01 \x01(\x11\x12\x10\n\x08left_ear\x18\x02 \x01(\x11\x12\x15\n\rleft_forehead\x18\x03 \x01(\x11\x12\x16\n\x0eright_forehead\x18\x04 \x01(\x11\x12\x11\n\tright_ear\x18\x05 \x01(\x11\x12\x11\n\tright_aux\x18\x06 \x01(\x11\x12\x0b\n\x03ref\x18\x07 \x01(\x11\x12\x0b\n\x03\x64rl\x18\x08 \x01(\x11\x32%\n\x08museData\x12\t.MuseData\x18\x08 \x02(\x0b\x32\x08.MuseEEG\"\xbb\x01\n\x10MuseQuantization\x12\x10\n\x08left_aux\x18\x01 \x01(\r\x12\x10\n\x08left_ear\x18\x02 \x01(\r\x12\x15\n\rleft_forehead\x18\x03 \x01(\r\x12\x16\n\x0eright_forehead\x18\x04 \x01(\r\x12\x11\n\tright_ear\x18\x05 \x01(\r\x12\x11\n\tright_aux\x18\x06 \x01(\r2.\n\x08museData\x12\t.MuseData\x18\t \x02(\x0b\x32\x11.MuseQuantization\"n\n\x11MuseAccelerometer\x12\x0c\n\x04\x61\x63\x63\x31\x18\x01 \x01(\x11\x12\x0c\n\x04\x61\x63\x63\x32\x18\x02 \x01(\x11\x12\x0c\n\x04\x61\x63\x63\x33\x18\x03 \x01(\x11\x32/\n\x08museData\x12\t.MuseData\x18\n \x02(\x0b\x32\x12.MuseAccelerometer\"\xf2\x01\n\x0eMuseAnnotation\x12\x12\n\nevent_data\x18\x01 \x01(\t\x12?\n\x11\x65vent_data_format\x18\x02 \x01(\x0e\x32\x16.MuseAnnotation.Format:\x0cPLAIN_STRING\x12\x12\n\nevent_type\x18\x03 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x04 \x01(\t\x12\x11\n\tparent_id\x18\x05 \x01(\t\"$\n\x06\x46ormat\x12\x10\n\x0cPLAIN_STRING\x10\x00\x12\x08\n\x04JSON\x10\x01\x32,\n\x08museData\x12\t.MuseData\x18\x64 \x02(\x0b\x32\x0f.MuseAnnotation\"\xb7\x01\n\x0bMuseBattery\x12\x19\n\x11percent_remaining\x18\x01 \x01(\r\x12%\n\x1d\x62\x61ttery_fuel_gauge_millivolts\x18\x02 \x01(\r\x12\x1e\n\x16\x62\x61ttery_adc_millivolts\x18\x03 \x01(\r\x12\x1b\n\x13temperature_celsius\x18\x04 \x01(\x11\x32)\n\x08museData\x12\t.MuseData\x18\x65 \x02(\x0b\x32\x0c.MuseBattery\"\xe0\x01\n\x0bMuseVersion\x12\x18\n\x10hardware_version\x18\x01 \x01(\t\x12 \n\x18\x66irmware_headset_version\x18\x02 \x01(\t\x12\x15\n\rfirmware_type\x18\x03 \x01(\t\x12#\n\x1b\x66irmware_bootloader_version\x18\x04 \x01(\t\x12\x14\n\x0c\x62uild_number\x18\x05 \x01(\t\x12\x18\n\x10protocol_version\x18\x06 \x01(\t2)\n\x08museData\x12\t.MuseData\x18\x66 \x02(\x0b\x32\x0c.MuseVersion\"\x9b\x04\n\nMuseConfig\x12\x0e\n\x06preset\x18\x01 \x01(\t\x12\x17\n\x0f\x66ilters_enabled\x18\x02 \x01(\x08\x12\x1a\n\x12notch_frequency_hz\x18\x03 \x01(\r\x12\"\n\x1a\x61\x63\x63\x65lerometer_data_enabled\x18\x04 \x01(\x08\x12\x1c\n\x14\x62\x61ttery_data_enabled\x18\x05 \x01(\x08\x12\x1a\n\x12\x65rror_data_enabled\x18\x06 \x01(\x08\x12\x1b\n\x13\x63ompression_enabled\x18\x07 \x01(\x08\x12\x1f\n\x17\x65\x65g_sample_frequency_hz\x18\x08 \x01(\r\x12\x1f\n\x17\x65\x65g_output_frequency_hz\x18\t \x01(\r\x12\x1c\n\x14\x65\x65g_samples_bitwidth\x18\n \x01(\r\x12\x19\n\x11\x65\x65g_channel_count\x18\x0b \x01(\r\x12\x1a\n\x12\x65\x65g_channel_layout\x18\x0c \x01(\t\x12\x14\n\x0c\x64ownsampling\x18\r \x01(\r\x12\x13\n\x0boutput_mode\x18\x0e \x01(\t\x12!\n\x19\x62\x61ttery_percent_remaining\x18\x0f \x01(\r\x12\x1a\n\x12\x62\x61ttery_millivolts\x18\x10 \x01(\r\x12\x10\n\x08\x61\x66\x65_gain\x18\x11 \x01(\x02\x12\x10\n\x08mac_addr\x18\x12 \x01(\t2(\n\x08museData\x12\t.MuseData\x18g \x02(\x0b\x32\x0b.MuseConfigB#\n\x11\x63om.ix.basis.museB\x0eMuseSerializer')



_MUSEDATA_DATATYPE = _descriptor.EnumDescriptor(
  name='Datatype',
  full_name='MuseData.Datatype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EEG', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUANT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERSION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIG', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANNOTATION', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HISTOGRAM', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALGVALUE', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=137,
  serialized_end=261,
)

_MUSEANNOTATION_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='MuseAnnotation.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAIN_STRING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=939,
  serialized_end=975,
)


_MUSEDATACOLLECTION = _descriptor.Descriptor(
  name='MuseDataCollection',
  full_name='MuseDataCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='MuseDataCollection.collection', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=14,
  serialized_end=65,
)


_MUSEDATA = _descriptor.Descriptor(
  name='MuseData',
  full_name='MuseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MuseData.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datatype', full_name='MuseData.datatype', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MUSEDATA_DATATYPE,
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(8, 1000), (1000, 2048), ],
  serialized_start=68,
  serialized_end=276,
)


_MUSEEEG = _descriptor.Descriptor(
  name='MuseEEG',
  full_name='MuseEEG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_aux', full_name='MuseEEG.left_aux', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_ear', full_name='MuseEEG.left_ear', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_forehead', full_name='MuseEEG.left_forehead', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_forehead', full_name='MuseEEG.right_forehead', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_ear', full_name='MuseEEG.right_ear', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_aux', full_name='MuseEEG.right_aux', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ref', full_name='MuseEEG.ref', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drl', full_name='MuseEEG.drl', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='museData', full_name='MuseEEG.museData', index=0,
      number=8, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=279,
  serialized_end=474,
)


_MUSEQUANTIZATION = _descriptor.Descriptor(
  name='MuseQuantization',
  full_name='MuseQuantization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_aux', full_name='MuseQuantization.left_aux', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_ear', full_name='MuseQuantization.left_ear', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_forehead', full_name='MuseQuantization.left_forehead', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_forehead', full_name='MuseQuantization.right_forehead', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_ear', full_name='MuseQuantization.right_ear', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_aux', full_name='MuseQuantization.right_aux', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='museData', full_name='MuseQuantization.museData', index=0,
      number=9, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=477,
  serialized_end=664,
)


_MUSEACCELEROMETER = _descriptor.Descriptor(
  name='MuseAccelerometer',
  full_name='MuseAccelerometer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acc1', full_name='MuseAccelerometer.acc1', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc2', full_name='MuseAccelerometer.acc2', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc3', full_name='MuseAccelerometer.acc3', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='museData', full_name='MuseAccelerometer.museData', index=0,
      number=10, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=666,
  serialized_end=776,
)


_MUSEANNOTATION = _descriptor.Descriptor(
  name='MuseAnnotation',
  full_name='MuseAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_data', full_name='MuseAnnotation.event_data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_data_format', full_name='MuseAnnotation.event_data_format', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='MuseAnnotation.event_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='MuseAnnotation.event_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='MuseAnnotation.parent_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='museData', full_name='MuseAnnotation.museData', index=0,
      number=100, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _MUSEANNOTATION_FORMAT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=779,
  serialized_end=1021,
)


_MUSEBATTERY = _descriptor.Descriptor(
  name='MuseBattery',
  full_name='MuseBattery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='percent_remaining', full_name='MuseBattery.percent_remaining', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_fuel_gauge_millivolts', full_name='MuseBattery.battery_fuel_gauge_millivolts', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_adc_millivolts', full_name='MuseBattery.battery_adc_millivolts', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_celsius', full_name='MuseBattery.temperature_celsius', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='museData', full_name='MuseBattery.museData', index=0,
      number=101, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1024,
  serialized_end=1207,
)


_MUSEVERSION = _descriptor.Descriptor(
  name='MuseVersion',
  full_name='MuseVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hardware_version', full_name='MuseVersion.hardware_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_headset_version', full_name='MuseVersion.firmware_headset_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_type', full_name='MuseVersion.firmware_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_bootloader_version', full_name='MuseVersion.firmware_bootloader_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_number', full_name='MuseVersion.build_number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='MuseVersion.protocol_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='museData', full_name='MuseVersion.museData', index=0,
      number=102, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1210,
  serialized_end=1434,
)


_MUSECONFIG = _descriptor.Descriptor(
  name='MuseConfig',
  full_name='MuseConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preset', full_name='MuseConfig.preset', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters_enabled', full_name='MuseConfig.filters_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notch_frequency_hz', full_name='MuseConfig.notch_frequency_hz', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accelerometer_data_enabled', full_name='MuseConfig.accelerometer_data_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_data_enabled', full_name='MuseConfig.battery_data_enabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_data_enabled', full_name='MuseConfig.error_data_enabled', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compression_enabled', full_name='MuseConfig.compression_enabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eeg_sample_frequency_hz', full_name='MuseConfig.eeg_sample_frequency_hz', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eeg_output_frequency_hz', full_name='MuseConfig.eeg_output_frequency_hz', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eeg_samples_bitwidth', full_name='MuseConfig.eeg_samples_bitwidth', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eeg_channel_count', full_name='MuseConfig.eeg_channel_count', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eeg_channel_layout', full_name='MuseConfig.eeg_channel_layout', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downsampling', full_name='MuseConfig.downsampling', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_mode', full_name='MuseConfig.output_mode', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_percent_remaining', full_name='MuseConfig.battery_percent_remaining', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_millivolts', full_name='MuseConfig.battery_millivolts', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='afe_gain', full_name='MuseConfig.afe_gain', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac_addr', full_name='MuseConfig.mac_addr', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='museData', full_name='MuseConfig.museData', index=0,
      number=103, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1437,
  serialized_end=1976,
)

_MUSEDATACOLLECTION.fields_by_name['collection'].message_type = _MUSEDATA
_MUSEDATA.fields_by_name['datatype'].enum_type = _MUSEDATA_DATATYPE
_MUSEDATA_DATATYPE.containing_type = _MUSEDATA;
_MUSEANNOTATION.fields_by_name['event_data_format'].enum_type = _MUSEANNOTATION_FORMAT
_MUSEANNOTATION_FORMAT.containing_type = _MUSEANNOTATION;
DESCRIPTOR.message_types_by_name['MuseDataCollection'] = _MUSEDATACOLLECTION
DESCRIPTOR.message_types_by_name['MuseData'] = _MUSEDATA
DESCRIPTOR.message_types_by_name['MuseEEG'] = _MUSEEEG
DESCRIPTOR.message_types_by_name['MuseQuantization'] = _MUSEQUANTIZATION
DESCRIPTOR.message_types_by_name['MuseAccelerometer'] = _MUSEACCELEROMETER
DESCRIPTOR.message_types_by_name['MuseAnnotation'] = _MUSEANNOTATION
DESCRIPTOR.message_types_by_name['MuseBattery'] = _MUSEBATTERY
DESCRIPTOR.message_types_by_name['MuseVersion'] = _MUSEVERSION
DESCRIPTOR.message_types_by_name['MuseConfig'] = _MUSECONFIG

class MuseDataCollection(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEDATACOLLECTION

  # @@protoc_insertion_point(class_scope:MuseDataCollection)

class MuseData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEDATA

  # @@protoc_insertion_point(class_scope:MuseData)

class MuseEEG(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEEEG

  # @@protoc_insertion_point(class_scope:MuseEEG)

class MuseQuantization(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEQUANTIZATION

  # @@protoc_insertion_point(class_scope:MuseQuantization)

class MuseAccelerometer(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEACCELEROMETER

  # @@protoc_insertion_point(class_scope:MuseAccelerometer)

class MuseAnnotation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEANNOTATION

  # @@protoc_insertion_point(class_scope:MuseAnnotation)

class MuseBattery(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEBATTERY

  # @@protoc_insertion_point(class_scope:MuseBattery)

class MuseVersion(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSEVERSION

  # @@protoc_insertion_point(class_scope:MuseVersion)

class MuseConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MUSECONFIG

  # @@protoc_insertion_point(class_scope:MuseConfig)

_MUSEEEG.extensions_by_name['museData'].message_type = _MUSEEEG
MuseData.RegisterExtension(_MUSEEEG.extensions_by_name['museData'])
_MUSEQUANTIZATION.extensions_by_name['museData'].message_type = _MUSEQUANTIZATION
MuseData.RegisterExtension(_MUSEQUANTIZATION.extensions_by_name['museData'])
_MUSEACCELEROMETER.extensions_by_name['museData'].message_type = _MUSEACCELEROMETER
MuseData.RegisterExtension(_MUSEACCELEROMETER.extensions_by_name['museData'])
_MUSEANNOTATION.extensions_by_name['museData'].message_type = _MUSEANNOTATION
MuseData.RegisterExtension(_MUSEANNOTATION.extensions_by_name['museData'])
_MUSEBATTERY.extensions_by_name['museData'].message_type = _MUSEBATTERY
MuseData.RegisterExtension(_MUSEBATTERY.extensions_by_name['museData'])
_MUSEVERSION.extensions_by_name['museData'].message_type = _MUSEVERSION
MuseData.RegisterExtension(_MUSEVERSION.extensions_by_name['museData'])
_MUSECONFIG.extensions_by_name['museData'].message_type = _MUSECONFIG
MuseData.RegisterExtension(_MUSECONFIG.extensions_by_name['museData'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\021com.ix.basis.museB\016MuseSerializer')
# @@protoc_insertion_point(module_scope)
