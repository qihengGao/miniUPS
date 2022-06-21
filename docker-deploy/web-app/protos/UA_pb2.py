# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UA.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UA.proto',
  package='UPS',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x08UA.proto\x12\x03UPS\" \n\x0cUSendWorldId\x12\x10\n\x08world_id\x18\x01 \x02(\x03\"[\n\nAPacPickup\x12\x0c\n\x04whid\x18\x01 \x02(\x05\x12\x13\n\x0bshipment_id\x18\x02 \x02(\x03\x12\x14\n\x0cups_username\x18\x03 \x01(\t\x12\t\n\x01x\x18\x04 \x02(\x05\x12\t\n\x01y\x18\x05 \x02(\x05\"^\n\rUPacPickupRes\x12\x13\n\x0btracking_id\x18\x01 \x02(\x03\x12\x11\n\tis_binded\x18\x02 \x01(\x08\x12\x13\n\x0bshipment_id\x18\x03 \x02(\x03\x12\x10\n\x08truck_id\x18\x04 \x02(\x05\"5\n\x0bUsendArrive\x12\x10\n\x08truck_id\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\"B\n\x08\x41Product\x12\x12\n\nproduct_id\x18\x01 \x02(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x02(\t\x12\r\n\x05\x63ount\x18\x03 \x02(\x05\"S\n\x08\x41Package\x12\t\n\x01x\x18\x01 \x02(\x05\x12\t\n\x01y\x18\x02 \x02(\x05\x12\x13\n\x0bshipment_id\x18\x03 \x02(\x03\x12\x1c\n\x05items\x18\x04 \x03(\x0b\x32\r.UPS.AProduct\"C\n\x0e\x41SendAllLoaded\x12\x1f\n\x08packages\x18\x01 \x03(\x0b\x32\r.UPS.APackage\x12\x10\n\x08truck_id\x18\x02 \x02(\x05\"$\n\rUPacDelivered\x12\x13\n\x0bshipment_id\x18\x01 \x02(\x03\"9\n\x0c\x41\x42indUpsUser\x12\x13\n\x0bshipment_id\x18\x01 \x02(\x03\x12\x14\n\x0cups_username\x18\x02 \x02(\t\"2\n\x08UBindRes\x12\x13\n\x0bshipment_id\x18\x01 \x02(\x03\x12\x11\n\tis_binded\x18\x02 \x02(\x08\"%\n\x0eUResendPackage\x12\x13\n\x0bshipment_id\x18\x01 \x02(\x03\"\xf8\x01\n\tUAmessage\x12#\n\x08world_id\x18\x01 \x01(\x0b\x32\x11.UPS.USendWorldId\x12&\n\npickup_res\x18\x02 \x01(\x0b\x32\x12.UPS.UPacPickupRes\x12%\n\x0bsend_arrive\x18\x03 \x01(\x0b\x32\x10.UPS.UsendArrive\x12)\n\rpac_delivered\x18\x04 \x01(\x0b\x32\x12.UPS.UPacDelivered\x12\x1f\n\x08\x62ind_res\x18\x05 \x01(\x0b\x32\r.UPS.UBindRes\x12+\n\x0eresend_package\x18\x06 \x01(\x0b\x32\x13.UPS.UResendPackage\"~\n\tAUmessage\x12\x1f\n\x06pickup\x18\x01 \x01(\x0b\x32\x0f.UPS.APacPickup\x12\'\n\nall_loaded\x18\x02 \x01(\x0b\x32\x13.UPS.ASendAllLoaded\x12\'\n\x0c\x62ind_upsuser\x18\x03 \x01(\x0b\x32\x11.UPS.ABindUpsUser')
)




_USENDWORLDID = _descriptor.Descriptor(
  name='USendWorldId',
  full_name='UPS.USendWorldId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world_id', full_name='UPS.USendWorldId.world_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=17,
  serialized_end=49,
)


_APACPICKUP = _descriptor.Descriptor(
  name='APacPickup',
  full_name='UPS.APacPickup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='whid', full_name='UPS.APacPickup.whid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipment_id', full_name='UPS.APacPickup.shipment_id', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ups_username', full_name='UPS.APacPickup.ups_username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='UPS.APacPickup.x', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='UPS.APacPickup.y', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=51,
  serialized_end=142,
)


_UPACPICKUPRES = _descriptor.Descriptor(
  name='UPacPickupRes',
  full_name='UPS.UPacPickupRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracking_id', full_name='UPS.UPacPickupRes.tracking_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_binded', full_name='UPS.UPacPickupRes.is_binded', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipment_id', full_name='UPS.UPacPickupRes.shipment_id', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='UPS.UPacPickupRes.truck_id', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=144,
  serialized_end=238,
)


_USENDARRIVE = _descriptor.Descriptor(
  name='UsendArrive',
  full_name='UPS.UsendArrive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='UPS.UsendArrive.truck_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='UPS.UsendArrive.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='UPS.UsendArrive.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=240,
  serialized_end=293,
)


_APRODUCT = _descriptor.Descriptor(
  name='AProduct',
  full_name='UPS.AProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='UPS.AProduct.product_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='UPS.AProduct.description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='UPS.AProduct.count', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=295,
  serialized_end=361,
)


_APACKAGE = _descriptor.Descriptor(
  name='APackage',
  full_name='UPS.APackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='UPS.APackage.x', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='UPS.APackage.y', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipment_id', full_name='UPS.APackage.shipment_id', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='UPS.APackage.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=363,
  serialized_end=446,
)


_ASENDALLLOADED = _descriptor.Descriptor(
  name='ASendAllLoaded',
  full_name='UPS.ASendAllLoaded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packages', full_name='UPS.ASendAllLoaded.packages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='UPS.ASendAllLoaded.truck_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=448,
  serialized_end=515,
)


_UPACDELIVERED = _descriptor.Descriptor(
  name='UPacDelivered',
  full_name='UPS.UPacDelivered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipment_id', full_name='UPS.UPacDelivered.shipment_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=517,
  serialized_end=553,
)


_ABINDUPSUSER = _descriptor.Descriptor(
  name='ABindUpsUser',
  full_name='UPS.ABindUpsUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipment_id', full_name='UPS.ABindUpsUser.shipment_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ups_username', full_name='UPS.ABindUpsUser.ups_username', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=612,
)


_UBINDRES = _descriptor.Descriptor(
  name='UBindRes',
  full_name='UPS.UBindRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipment_id', full_name='UPS.UBindRes.shipment_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_binded', full_name='UPS.UBindRes.is_binded', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=614,
  serialized_end=664,
)


_URESENDPACKAGE = _descriptor.Descriptor(
  name='UResendPackage',
  full_name='UPS.UResendPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipment_id', full_name='UPS.UResendPackage.shipment_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=666,
  serialized_end=703,
)


_UAMESSAGE = _descriptor.Descriptor(
  name='UAmessage',
  full_name='UPS.UAmessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world_id', full_name='UPS.UAmessage.world_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pickup_res', full_name='UPS.UAmessage.pickup_res', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_arrive', full_name='UPS.UAmessage.send_arrive', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pac_delivered', full_name='UPS.UAmessage.pac_delivered', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bind_res', full_name='UPS.UAmessage.bind_res', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resend_package', full_name='UPS.UAmessage.resend_package', index=5,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=706,
  serialized_end=954,
)


_AUMESSAGE = _descriptor.Descriptor(
  name='AUmessage',
  full_name='UPS.AUmessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pickup', full_name='UPS.AUmessage.pickup', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_loaded', full_name='UPS.AUmessage.all_loaded', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bind_upsuser', full_name='UPS.AUmessage.bind_upsuser', index=2,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=956,
  serialized_end=1082,
)

_APACKAGE.fields_by_name['items'].message_type = _APRODUCT
_ASENDALLLOADED.fields_by_name['packages'].message_type = _APACKAGE
_UAMESSAGE.fields_by_name['world_id'].message_type = _USENDWORLDID
_UAMESSAGE.fields_by_name['pickup_res'].message_type = _UPACPICKUPRES
_UAMESSAGE.fields_by_name['send_arrive'].message_type = _USENDARRIVE
_UAMESSAGE.fields_by_name['pac_delivered'].message_type = _UPACDELIVERED
_UAMESSAGE.fields_by_name['bind_res'].message_type = _UBINDRES
_UAMESSAGE.fields_by_name['resend_package'].message_type = _URESENDPACKAGE
_AUMESSAGE.fields_by_name['pickup'].message_type = _APACPICKUP
_AUMESSAGE.fields_by_name['all_loaded'].message_type = _ASENDALLLOADED
_AUMESSAGE.fields_by_name['bind_upsuser'].message_type = _ABINDUPSUSER
DESCRIPTOR.message_types_by_name['USendWorldId'] = _USENDWORLDID
DESCRIPTOR.message_types_by_name['APacPickup'] = _APACPICKUP
DESCRIPTOR.message_types_by_name['UPacPickupRes'] = _UPACPICKUPRES
DESCRIPTOR.message_types_by_name['UsendArrive'] = _USENDARRIVE
DESCRIPTOR.message_types_by_name['AProduct'] = _APRODUCT
DESCRIPTOR.message_types_by_name['APackage'] = _APACKAGE
DESCRIPTOR.message_types_by_name['ASendAllLoaded'] = _ASENDALLLOADED
DESCRIPTOR.message_types_by_name['UPacDelivered'] = _UPACDELIVERED
DESCRIPTOR.message_types_by_name['ABindUpsUser'] = _ABINDUPSUSER
DESCRIPTOR.message_types_by_name['UBindRes'] = _UBINDRES
DESCRIPTOR.message_types_by_name['UResendPackage'] = _URESENDPACKAGE
DESCRIPTOR.message_types_by_name['UAmessage'] = _UAMESSAGE
DESCRIPTOR.message_types_by_name['AUmessage'] = _AUMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

USendWorldId = _reflection.GeneratedProtocolMessageType('USendWorldId', (_message.Message,), dict(
  DESCRIPTOR = _USENDWORLDID,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.USendWorldId)
  ))
_sym_db.RegisterMessage(USendWorldId)

APacPickup = _reflection.GeneratedProtocolMessageType('APacPickup', (_message.Message,), dict(
  DESCRIPTOR = _APACPICKUP,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.APacPickup)
  ))
_sym_db.RegisterMessage(APacPickup)

UPacPickupRes = _reflection.GeneratedProtocolMessageType('UPacPickupRes', (_message.Message,), dict(
  DESCRIPTOR = _UPACPICKUPRES,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.UPacPickupRes)
  ))
_sym_db.RegisterMessage(UPacPickupRes)

UsendArrive = _reflection.GeneratedProtocolMessageType('UsendArrive', (_message.Message,), dict(
  DESCRIPTOR = _USENDARRIVE,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.UsendArrive)
  ))
_sym_db.RegisterMessage(UsendArrive)

AProduct = _reflection.GeneratedProtocolMessageType('AProduct', (_message.Message,), dict(
  DESCRIPTOR = _APRODUCT,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.AProduct)
  ))
_sym_db.RegisterMessage(AProduct)

APackage = _reflection.GeneratedProtocolMessageType('APackage', (_message.Message,), dict(
  DESCRIPTOR = _APACKAGE,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.APackage)
  ))
_sym_db.RegisterMessage(APackage)

ASendAllLoaded = _reflection.GeneratedProtocolMessageType('ASendAllLoaded', (_message.Message,), dict(
  DESCRIPTOR = _ASENDALLLOADED,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.ASendAllLoaded)
  ))
_sym_db.RegisterMessage(ASendAllLoaded)

UPacDelivered = _reflection.GeneratedProtocolMessageType('UPacDelivered', (_message.Message,), dict(
  DESCRIPTOR = _UPACDELIVERED,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.UPacDelivered)
  ))
_sym_db.RegisterMessage(UPacDelivered)

ABindUpsUser = _reflection.GeneratedProtocolMessageType('ABindUpsUser', (_message.Message,), dict(
  DESCRIPTOR = _ABINDUPSUSER,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.ABindUpsUser)
  ))
_sym_db.RegisterMessage(ABindUpsUser)

UBindRes = _reflection.GeneratedProtocolMessageType('UBindRes', (_message.Message,), dict(
  DESCRIPTOR = _UBINDRES,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.UBindRes)
  ))
_sym_db.RegisterMessage(UBindRes)

UResendPackage = _reflection.GeneratedProtocolMessageType('UResendPackage', (_message.Message,), dict(
  DESCRIPTOR = _URESENDPACKAGE,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.UResendPackage)
  ))
_sym_db.RegisterMessage(UResendPackage)

UAmessage = _reflection.GeneratedProtocolMessageType('UAmessage', (_message.Message,), dict(
  DESCRIPTOR = _UAMESSAGE,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.UAmessage)
  ))
_sym_db.RegisterMessage(UAmessage)

AUmessage = _reflection.GeneratedProtocolMessageType('AUmessage', (_message.Message,), dict(
  DESCRIPTOR = _AUMESSAGE,
  __module__ = 'UA_pb2'
  # @@protoc_insertion_point(class_scope:UPS.AUmessage)
  ))
_sym_db.RegisterMessage(AUmessage)


# @@protoc_insertion_point(module_scope)