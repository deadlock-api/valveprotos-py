# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: usercmd.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rusercmd.proto\x1a\x16networkbasetypes.proto\"T\n\x10\x43InButtonStatePB\x12\x14\n\x0c\x62uttonstate1\x18\x01 \x01(\x04\x12\x14\n\x0c\x62uttonstate2\x18\x02 \x01(\x04\x12\x14\n\x0c\x62uttonstate3\x18\x03 \x01(\x04\"z\n\x10\x43SubtickMoveStep\x12\x0e\n\x06\x62utton\x18\x01 \x01(\x04\x12\x0f\n\x07pressed\x18\x02 \x01(\x08\x12\x0c\n\x04when\x18\x03 \x01(\x02\x12\x1c\n\x14\x61nalog_forward_delta\x18\x04 \x01(\x02\x12\x19\n\x11\x61nalog_left_delta\x18\x05 \x01(\x02\"\xbd\x03\n\x0e\x43\x42\x61seUserCmdPB\x12\x1d\n\x15legacy_command_number\x18\x01 \x01(\x05\x12\x13\n\x0b\x63lient_tick\x18\x02 \x01(\x05\x12%\n\nbuttons_pb\x18\x03 \x01(\x0b\x32\x11.CInButtonStatePB\x12\x1f\n\nviewangles\x18\x04 \x01(\x0b\x32\x0b.CMsgQAngle\x12\x13\n\x0b\x66orwardmove\x18\x05 \x01(\x02\x12\x10\n\x08leftmove\x18\x06 \x01(\x02\x12\x0e\n\x06upmove\x18\x07 \x01(\x02\x12\x0f\n\x07impulse\x18\x08 \x01(\x05\x12\x14\n\x0cweaponselect\x18\t \x01(\x05\x12\x13\n\x0brandom_seed\x18\n \x01(\x05\x12\x0f\n\x07mousedx\x18\x0b \x01(\x05\x12\x0f\n\x07mousedy\x18\x0c \x01(\x05\x12$\n\x12pawn_entity_handle\x18\x0e \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12(\n\rsubtick_moves\x18\x12 \x03(\x0b\x32\x11.CSubtickMoveStep\x12\x10\n\x08move_crc\x18\x13 \x01(\x0c\x12%\n\x1d\x63onsumed_server_angle_changes\x18\x14 \x01(\r\x12\x11\n\tcmd_flags\x18\x15 \x01(\x05\"/\n\x0e\x43UserCmdBasePB\x12\x1d\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x0f.CBaseUserCmdPB')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'usercmd_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CINBUTTONSTATEPB._serialized_start=41
  _CINBUTTONSTATEPB._serialized_end=125
  _CSUBTICKMOVESTEP._serialized_start=127
  _CSUBTICKMOVESTEP._serialized_end=249
  _CBASEUSERCMDPB._serialized_start=252
  _CBASEUSERCMDPB._serialized_end=697
  _CUSERCMDBASEPB._serialized_start=699
  _CUSERCMDBASEPB._serialized_end=746
# @@protoc_insertion_point(module_scope)