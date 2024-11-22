import networkbasetypes_pb2 as _networkbasetypes_pb2
import usercmd_pb2 as _usercmd_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CCitadelUserCmdPB(_message.Message):
    __slots__ = ["ang_camera_angles", "base", "camera_roaming_speed", "enemy_hero_aimed_at", "execute_ability_indices", "in_shop", "mouse_delta_x", "mouse_delta_y", "using_free_cursor", "vec_camera_position"]
    ANG_CAMERA_ANGLES_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ROAMING_SPEED_FIELD_NUMBER: _ClassVar[int]
    ENEMY_HERO_AIMED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_ABILITY_INDICES_FIELD_NUMBER: _ClassVar[int]
    IN_SHOP_FIELD_NUMBER: _ClassVar[int]
    MOUSE_DELTA_X_FIELD_NUMBER: _ClassVar[int]
    MOUSE_DELTA_Y_FIELD_NUMBER: _ClassVar[int]
    USING_FREE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    VEC_CAMERA_POSITION_FIELD_NUMBER: _ClassVar[int]
    ang_camera_angles: _networkbasetypes_pb2.CMsgQAngle
    base: _usercmd_pb2.CBaseUserCmdPB
    camera_roaming_speed: float
    enemy_hero_aimed_at: int
    execute_ability_indices: int
    in_shop: bool
    mouse_delta_x: _containers.RepeatedScalarFieldContainer[int]
    mouse_delta_y: _containers.RepeatedScalarFieldContainer[int]
    using_free_cursor: bool
    vec_camera_position: _networkbasetypes_pb2.CMsgVector
    def __init__(self, base: _Optional[_Union[_usercmd_pb2.CBaseUserCmdPB, _Mapping]] = ..., vec_camera_position: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., ang_camera_angles: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ..., execute_ability_indices: _Optional[int] = ..., in_shop: bool = ..., camera_roaming_speed: _Optional[float] = ..., using_free_cursor: bool = ..., enemy_hero_aimed_at: _Optional[int] = ..., mouse_delta_x: _Optional[_Iterable[int]] = ..., mouse_delta_y: _Optional[_Iterable[int]] = ...) -> None: ...
