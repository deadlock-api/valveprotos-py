# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .networkbasetypes_p2p import CMsgQAngle
from .networkbasetypes_p2p import CMsgVector
from .usercmd_p2p import CBaseUserCmdPB
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class CCitadelUserCmdPB(BaseModel):
    base: CBaseUserCmdPB = Field()
    vec_camera_position: CMsgVector = Field()
    ang_camera_angles: CMsgQAngle = Field()
    execute_ability_indices: int = Field(default=0)
    in_shop: bool = Field(default=False)
    camera_roaming_speed: float = Field(default=0.0)
    using_free_cursor: bool = Field(default=False)
    enemy_hero_aimed_at: int = Field(default=0)
    view_delta_x: typing.List[int] = Field(default_factory=list)
    view_delta_y: typing.List[int] = Field(default_factory=list)
