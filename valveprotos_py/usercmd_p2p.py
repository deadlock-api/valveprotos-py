# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .networkbasetypes_p2p import CMsgQAngle
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class CInButtonStatePB(BaseModel):
    buttonstate1: int = Field(default=0)
    buttonstate2: int = Field(default=0)
    buttonstate3: int = Field(default=0)

class CSubtickMoveStep(BaseModel):
    button: int = Field(default=0)
    pressed: bool = Field(default=False)
    when: float = Field(default=0.0)
    analog_forward_delta: float = Field(default=0.0)
    analog_left_delta: float = Field(default=0.0)
    analog_pitch_delta: float = Field(default=0.0)
    analog_yaw_delta: float = Field(default=0.0)

class CBaseUserCmdPB(BaseModel):
    legacy_command_number: int = Field(default=0)
    client_tick: int = Field(default=0)
    buttons_pb: CInButtonStatePB = Field()
    viewangles: CMsgQAngle = Field()
    forwardmove: float = Field(default=0.0)
    leftmove: float = Field(default=0.0)
    upmove: float = Field(default=0.0)
    impulse: int = Field(default=0)
    weaponselect: int = Field(default=0)
    random_seed: int = Field(default=0)
    mousedx: int = Field(default=0)
    mousedy: int = Field(default=0)
    pawn_entity_handle: int = Field(default=0)
    subtick_moves: typing.List[CSubtickMoveStep] = Field(default_factory=list)
    move_crc: bytes = Field(default=b"")
    consumed_server_angle_changes: int = Field(default=0)
    cmd_flags: int = Field(default=0)

class CUserCmdBasePB(BaseModel):
    base: CBaseUserCmdPB = Field()
