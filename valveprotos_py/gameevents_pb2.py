# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameevents.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10gameevents.proto\x1a\x16networkbasetypes.proto\"G\n\x1c\x43MsgVDebugGameSessionIDEvent\x12\x10\n\x08\x63lientid\x18\x01 \x01(\x05\x12\x15\n\rgamesessionid\x18\x02 \x01(\t\"\xce\x02\n\x13\x43MsgPlaceDecalEvent\x12\x1d\n\x08position\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06normal\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x05saxis\x18\x03 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x12\x64\x65\x63\x61lmaterialindex\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\x12\r\n\x05\x63olor\x18\x06 \x01(\x07\x12\r\n\x05width\x18\x07 \x01(\x02\x12\x0e\n\x06height\x18\x08 \x01(\x02\x12\r\n\x05\x64\x65pth\x18\t \x01(\x02\x12\x19\n\x11\x65ntityhandleindex\x18\n \x01(\r\x12\x1c\n\x14skeletoninstancehash\x18\x0b \x01(\x07\x12\x11\n\tboneindex\x18\x0c \x01(\x05\x12\x16\n\x0etranslucenthit\x18\r \x01(\x08\x12\x13\n\x0bis_adjacent\x18\x0e \x01(\x08\"1\n\x19\x43MsgClearWorldDecalsEvent\x12\x14\n\x0c\x66lagstoclear\x18\x01 \x01(\r\"2\n\x1a\x43MsgClearEntityDecalsEvent\x12\x14\n\x0c\x66lagstoclear\x18\x01 \x01(\r\"x\n\'CMsgClearDecalsForSkeletonInstanceEvent\x12\x14\n\x0c\x66lagstoclear\x18\x01 \x01(\r\x12\x19\n\x11\x65ntityhandleindex\x18\x02 \x01(\r\x12\x1c\n\x14skeletoninstancehash\x18\x03 \x01(\r\"\xec\x01\n\x1e\x43MsgSource1LegacyGameEventList\x12\x41\n\x0b\x64\x65scriptors\x18\x01 \x03(\x0b\x32,.CMsgSource1LegacyGameEventList.descriptor_t\x1a#\n\x05key_t\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\x62\n\x0c\x64\x65scriptor_t\x12\x0f\n\x07\x65ventid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x33\n\x04keys\x18\x03 \x03(\x0b\x32%.CMsgSource1LegacyGameEventList.key_t\"K\n\x1d\x43MsgSource1LegacyListenEvents\x12\x12\n\nplayerslot\x18\x01 \x01(\x05\x12\x16\n\x0e\x65ventarraybits\x18\x02 \x03(\r\"\xb8\x02\n\x1a\x43MsgSource1LegacyGameEvent\x12\x12\n\nevent_name\x18\x01 \x01(\t\x12\x0f\n\x07\x65ventid\x18\x02 \x01(\x05\x12/\n\x04keys\x18\x03 \x03(\x0b\x32!.CMsgSource1LegacyGameEvent.key_t\x12\x13\n\x0bserver_tick\x18\x04 \x01(\x05\x12\x13\n\x0bpassthrough\x18\x05 \x01(\x05\x1a\x99\x01\n\x05key_t\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x12\n\nval_string\x18\x02 \x01(\t\x12\x11\n\tval_float\x18\x03 \x01(\x02\x12\x10\n\x08val_long\x18\x04 \x01(\x05\x12\x11\n\tval_short\x18\x05 \x01(\x05\x12\x10\n\x08val_byte\x18\x06 \x01(\x05\x12\x10\n\x08val_bool\x18\x07 \x01(\x08\x12\x12\n\nval_uint64\x18\x08 \x01(\x04\"\xa4\x01\n\x16\x43MsgSosStartSoundEvent\x12\x17\n\x0fsoundevent_guid\x18\x01 \x01(\x05\x12\x17\n\x0fsoundevent_hash\x18\x02 \x01(\x07\x12\x1f\n\x13source_entity_index\x18\x03 \x01(\x05:\x02-1\x12\x0c\n\x04seed\x18\x04 \x01(\x05\x12\x15\n\rpacked_params\x18\x05 \x01(\x0c\x12\x12\n\nstart_time\x18\x06 \x01(\x02\"0\n\x15\x43MsgSosStopSoundEvent\x12\x17\n\x0fsoundevent_guid\x18\x01 \x01(\x05\"U\n\x19\x43MsgSosStopSoundEventHash\x12\x17\n\x0fsoundevent_hash\x18\x01 \x01(\x07\x12\x1f\n\x13source_entity_index\x18\x02 \x01(\x05:\x02-1\"L\n\x1a\x43MsgSosSetSoundEventParams\x12\x17\n\x0fsoundevent_guid\x18\x01 \x01(\x05\x12\x15\n\rpacked_params\x18\x05 \x01(\x0c\"I\n\x1c\x43MsgSosSetLibraryStackFields\x12\x12\n\nstack_hash\x18\x01 \x01(\x07\x12\x15\n\rpacked_fields\x18\x05 \x01(\x0c*\xb7\x03\n\x0f\x45\x42\x61seGameEvents\x12 \n\x1bGE_VDebugGameSessionIDEvent\x10\xc8\x01\x12\x17\n\x12GE_PlaceDecalEvent\x10\xc9\x01\x12\x1d\n\x18GE_ClearWorldDecalsEvent\x10\xca\x01\x12\x1e\n\x19GE_ClearEntityDecalsEvent\x10\xcb\x01\x12+\n&GE_ClearDecalsForSkeletonInstanceEvent\x10\xcc\x01\x12\"\n\x1dGE_Source1LegacyGameEventList\x10\xcd\x01\x12!\n\x1cGE_Source1LegacyListenEvents\x10\xce\x01\x12\x1e\n\x19GE_Source1LegacyGameEvent\x10\xcf\x01\x12\x1a\n\x15GE_SosStartSoundEvent\x10\xd0\x01\x12\x19\n\x14GE_SosStopSoundEvent\x10\xd1\x01\x12\x1e\n\x19GE_SosSetSoundEventParams\x10\xd2\x01\x12 \n\x1bGE_SosSetLibraryStackFields\x10\xd3\x01\x12\x1d\n\x18GE_SosStopSoundEventHash\x10\xd4\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gameevents_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EBASEGAMEEVENTS._serialized_start=1768
  _EBASEGAMEEVENTS._serialized_end=2207
  _CMSGVDEBUGGAMESESSIONIDEVENT._serialized_start=44
  _CMSGVDEBUGGAMESESSIONIDEVENT._serialized_end=115
  _CMSGPLACEDECALEVENT._serialized_start=118
  _CMSGPLACEDECALEVENT._serialized_end=452
  _CMSGCLEARWORLDDECALSEVENT._serialized_start=454
  _CMSGCLEARWORLDDECALSEVENT._serialized_end=503
  _CMSGCLEARENTITYDECALSEVENT._serialized_start=505
  _CMSGCLEARENTITYDECALSEVENT._serialized_end=555
  _CMSGCLEARDECALSFORSKELETONINSTANCEEVENT._serialized_start=557
  _CMSGCLEARDECALSFORSKELETONINSTANCEEVENT._serialized_end=677
  _CMSGSOURCE1LEGACYGAMEEVENTLIST._serialized_start=680
  _CMSGSOURCE1LEGACYGAMEEVENTLIST._serialized_end=916
  _CMSGSOURCE1LEGACYGAMEEVENTLIST_KEY_T._serialized_start=781
  _CMSGSOURCE1LEGACYGAMEEVENTLIST_KEY_T._serialized_end=816
  _CMSGSOURCE1LEGACYGAMEEVENTLIST_DESCRIPTOR_T._serialized_start=818
  _CMSGSOURCE1LEGACYGAMEEVENTLIST_DESCRIPTOR_T._serialized_end=916
  _CMSGSOURCE1LEGACYLISTENEVENTS._serialized_start=918
  _CMSGSOURCE1LEGACYLISTENEVENTS._serialized_end=993
  _CMSGSOURCE1LEGACYGAMEEVENT._serialized_start=996
  _CMSGSOURCE1LEGACYGAMEEVENT._serialized_end=1308
  _CMSGSOURCE1LEGACYGAMEEVENT_KEY_T._serialized_start=1155
  _CMSGSOURCE1LEGACYGAMEEVENT_KEY_T._serialized_end=1308
  _CMSGSOSSTARTSOUNDEVENT._serialized_start=1311
  _CMSGSOSSTARTSOUNDEVENT._serialized_end=1475
  _CMSGSOSSTOPSOUNDEVENT._serialized_start=1477
  _CMSGSOSSTOPSOUNDEVENT._serialized_end=1525
  _CMSGSOSSTOPSOUNDEVENTHASH._serialized_start=1527
  _CMSGSOSSTOPSOUNDEVENTHASH._serialized_end=1612
  _CMSGSOSSETSOUNDEVENTPARAMS._serialized_start=1614
  _CMSGSOSSETSOUNDEVENTPARAMS._serialized_end=1690
  _CMSGSOSSETLIBRARYSTACKFIELDS._serialized_start=1692
  _CMSGSOSSETLIBRARYSTACKFIELDS._serialized_end=1765
# @@protoc_insertion_point(module_scope)
