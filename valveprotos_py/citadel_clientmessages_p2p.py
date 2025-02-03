# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .citadel_gcmessages_common_p2p import CMsgLaneColor
from .citadel_gcmessages_common_p2p import CMsgMapLine
from .networkbasetypes_p2p import CMsgVector
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class ECitadelClientMessages(IntEnum):
    CITADEL_CM_MapPing = 1002
    CITADEL_CM_PerformanceStats = 1003
    CITADEL_CM_PingWheel = 1004
    CITADEL_CM_ChatMsg = 1005
    CITADEL_CM_PerfReport = 1006
    CITADEL_CM_QuickResponse = 1007
    CITADEL_CM_Pause = 1008
    CITADEL_CM_MapLine = 1009
    CITADEL_CM_AbilityPing = 1010
    CITADEL_CM_ExecuteMapUnitAbility = 1011
    CITADEL_CM_GetDamageStats = 1012
    CITADEL_CM_CheaterVote = 1013
    CITADEL_CM_MutePlayers = 1014

class CCitadelClientMsg_Pause(BaseModel):
    pass

class CCitadelClientMsg_MapPing(BaseModel):
    ping_location: CMsgVector = Field()
    event_type: int = Field(default=0)
    entity_index: int = Field(default=0)
    is_aggressive_ping: bool = Field(default=False)
    is_minimap_ping: bool = Field(default=False)
    is_blind_ping: bool = Field(default=False)

class CCitadelClientMsg_PingWheel(BaseModel):
    ping_wheel_option_id: int = Field(default=0)
    subnav_message_id: int = Field(default=0)
    ping_location: CMsgVector = Field()
    entity_index: int = Field(default=0)

class CCitadelClientMsg_AbilityPing(BaseModel):
    entity_index: int = Field(default=0)
    pinged_ability_id: int = Field(default=0)
    pinged_player_slot: int = Field(default=0)

class CCitadelClientMsg_MapLine(BaseModel):
    mapline: CMsgMapLine = Field()

class CCitadelClientMsg_QuickResponse(BaseModel):
    ping_wheel_message_id: int = Field(default=0)
    responding_to_ping_message_id: int = Field(default=0)
    responding_to_player_slot: int = Field(default=0)

class CCitadelClientMsg_PerformanceStats(BaseModel):
    current_game_time: float = Field(default=0.0)
    average_fps: float = Field(default=0.0)
    min_fps: float = Field(default=0.0)
    max_fps: float = Field(default=0.0)

class CCitadelClientMsg_ChatMsg(BaseModel):
    chat_text: str = Field(default="")
    all_chat: bool = Field(default=False)
    lane_color: CMsgLaneColor = Field(default=0)

class CCitadelClientMsg_PerfReport(BaseModel):
    average_frame_time: float = Field(default=0.0)
    max_frame_time: float = Field(default=0.0)
    average_compute_time: float = Field(default=0.0)
    max_compute_time: float = Field(default=0.0)
    average_client_tick_time: float = Field(default=0.0)
    max_client_tick_time: float = Field(default=0.0)
    average_client_simulate_time: float = Field(default=0.0)
    max_client_simulate_time: float = Field(default=0.0)
    average_output_time: float = Field(default=0.0)
    max_output_time: float = Field(default=0.0)
    average_wait_for_rendering_to_complete_time: float = Field(default=0.0)
    max_wait_for_rendering_to_complete_time: float = Field(default=0.0)
    average_swap_time: float = Field(default=0.0)
    max_swap_time: float = Field(default=0.0)
    average_frame_update_time: float = Field(default=0.0)
    max_frame_update_time: float = Field(default=0.0)
    average_idle_time: float = Field(default=0.0)
    max_idle_time: float = Field(default=0.0)
    average_input_processing_time: float = Field(default=0.0)
    max_input_processing_time: float = Field(default=0.0)

class CCitadelClientMsg_GetDamageStats(BaseModel):
    lobby_player_slot: int = Field(default=0)
    ability_name: str = Field(default="")

class CCitadelClientCachedPlayerStats(BaseModel):
    class Stat(BaseModel):
        stat_name: str = Field(default="")
        all_time_total: int = Field(default=0)
        all_time_match_max: int = Field(default=0)
        all_time_life_max: int = Field(default=0)

    version: int = Field(default=0)
    stats: typing.List["CCitadelClientCachedPlayerStats.Stat"] = Field(default_factory=list)

class CCitadelClientMsg_ExecuteMapUnitAbility(BaseModel):
    ability_entity_index: int = Field(default=0)
    target_entity_index: int = Field(default=0)

class CCitadelClientMsg_CheaterVote(BaseModel):
    end_game_immediately: bool = Field(default=False)

class CCitadelClientMsg_MutePlayers(BaseModel):
    player_slots: typing.List[int] = Field(default_factory=list)
    unmute: bool = Field(default=False)
