import networkbasetypes_pb2 as _networkbasetypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CBaseUserCmdPB(_message.Message):
    __slots__ = ["buttons_pb", "client_tick", "cmd_flags", "consumed_server_angle_changes", "forwardmove", "impulse", "leftmove", "legacy_command_number", "mousedx", "mousedy", "move_crc", "pawn_entity_handle", "random_seed", "subtick_moves", "upmove", "viewangles", "weaponselect"]
    BUTTONS_PB_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TICK_FIELD_NUMBER: _ClassVar[int]
    CMD_FLAGS_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_SERVER_ANGLE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    FORWARDMOVE_FIELD_NUMBER: _ClassVar[int]
    IMPULSE_FIELD_NUMBER: _ClassVar[int]
    LEFTMOVE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_COMMAND_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MOUSEDX_FIELD_NUMBER: _ClassVar[int]
    MOUSEDY_FIELD_NUMBER: _ClassVar[int]
    MOVE_CRC_FIELD_NUMBER: _ClassVar[int]
    PAWN_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    RANDOM_SEED_FIELD_NUMBER: _ClassVar[int]
    SUBTICK_MOVES_FIELD_NUMBER: _ClassVar[int]
    UPMOVE_FIELD_NUMBER: _ClassVar[int]
    VIEWANGLES_FIELD_NUMBER: _ClassVar[int]
    WEAPONSELECT_FIELD_NUMBER: _ClassVar[int]
    buttons_pb: CInButtonStatePB
    client_tick: int
    cmd_flags: int
    consumed_server_angle_changes: int
    forwardmove: float
    impulse: int
    leftmove: float
    legacy_command_number: int
    mousedx: int
    mousedy: int
    move_crc: bytes
    pawn_entity_handle: int
    random_seed: int
    subtick_moves: _containers.RepeatedCompositeFieldContainer[CSubtickMoveStep]
    upmove: float
    viewangles: _networkbasetypes_pb2.CMsgQAngle
    weaponselect: int
    def __init__(self, legacy_command_number: _Optional[int] = ..., client_tick: _Optional[int] = ..., buttons_pb: _Optional[_Union[CInButtonStatePB, _Mapping]] = ..., viewangles: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ..., forwardmove: _Optional[float] = ..., leftmove: _Optional[float] = ..., upmove: _Optional[float] = ..., impulse: _Optional[int] = ..., weaponselect: _Optional[int] = ..., random_seed: _Optional[int] = ..., mousedx: _Optional[int] = ..., mousedy: _Optional[int] = ..., pawn_entity_handle: _Optional[int] = ..., subtick_moves: _Optional[_Iterable[_Union[CSubtickMoveStep, _Mapping]]] = ..., move_crc: _Optional[bytes] = ..., consumed_server_angle_changes: _Optional[int] = ..., cmd_flags: _Optional[int] = ...) -> None: ...

class CInButtonStatePB(_message.Message):
    __slots__ = ["buttonstate1", "buttonstate2", "buttonstate3"]
    BUTTONSTATE1_FIELD_NUMBER: _ClassVar[int]
    BUTTONSTATE2_FIELD_NUMBER: _ClassVar[int]
    BUTTONSTATE3_FIELD_NUMBER: _ClassVar[int]
    buttonstate1: int
    buttonstate2: int
    buttonstate3: int
    def __init__(self, buttonstate1: _Optional[int] = ..., buttonstate2: _Optional[int] = ..., buttonstate3: _Optional[int] = ...) -> None: ...

class CSubtickMoveStep(_message.Message):
    __slots__ = ["analog_forward_delta", "analog_left_delta", "analog_pitch_delta", "analog_yaw_delta", "button", "pressed", "when"]
    ANALOG_FORWARD_DELTA_FIELD_NUMBER: _ClassVar[int]
    ANALOG_LEFT_DELTA_FIELD_NUMBER: _ClassVar[int]
    ANALOG_PITCH_DELTA_FIELD_NUMBER: _ClassVar[int]
    ANALOG_YAW_DELTA_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    PRESSED_FIELD_NUMBER: _ClassVar[int]
    WHEN_FIELD_NUMBER: _ClassVar[int]
    analog_forward_delta: float
    analog_left_delta: float
    analog_pitch_delta: float
    analog_yaw_delta: float
    button: int
    pressed: bool
    when: float
    def __init__(self, button: _Optional[int] = ..., pressed: bool = ..., when: _Optional[float] = ..., analog_forward_delta: _Optional[float] = ..., analog_left_delta: _Optional[float] = ..., analog_pitch_delta: _Optional[float] = ..., analog_yaw_delta: _Optional[float] = ...) -> None: ...

class CUserCmdBasePB(_message.Message):
    __slots__ = ["base"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: CBaseUserCmdPB
    def __init__(self, base: _Optional[_Union[CBaseUserCmdPB, _Mapping]] = ...) -> None: ...
