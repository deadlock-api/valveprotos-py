import networkbasetypes_pb2 as _networkbasetypes_pb2
import citadel_gcmessages_common_pb2 as _citadel_gcmessages_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CITADEL_CM_AbilityPing: ECitadelClientMessages
CITADEL_CM_ChatMsg: ECitadelClientMessages
CITADEL_CM_CheaterVote: ECitadelClientMessages
CITADEL_CM_ExecuteMapUnitAbility: ECitadelClientMessages
CITADEL_CM_GetDamageStats: ECitadelClientMessages
CITADEL_CM_MapLine: ECitadelClientMessages
CITADEL_CM_MapPing: ECitadelClientMessages
CITADEL_CM_MutePlayers: ECitadelClientMessages
CITADEL_CM_Pause: ECitadelClientMessages
CITADEL_CM_PerfReport: ECitadelClientMessages
CITADEL_CM_PerformanceStats: ECitadelClientMessages
CITADEL_CM_PingWheel: ECitadelClientMessages
CITADEL_CM_QuickResponse: ECitadelClientMessages
DESCRIPTOR: _descriptor.FileDescriptor

class CCitadelClientCachedPlayerStats(_message.Message):
    __slots__ = ["stats", "version"]
    class Stat(_message.Message):
        __slots__ = ["all_time_life_max", "all_time_match_max", "all_time_total", "stat_name"]
        ALL_TIME_LIFE_MAX_FIELD_NUMBER: _ClassVar[int]
        ALL_TIME_MATCH_MAX_FIELD_NUMBER: _ClassVar[int]
        ALL_TIME_TOTAL_FIELD_NUMBER: _ClassVar[int]
        STAT_NAME_FIELD_NUMBER: _ClassVar[int]
        all_time_life_max: int
        all_time_match_max: int
        all_time_total: int
        stat_name: str
        def __init__(self, stat_name: _Optional[str] = ..., all_time_total: _Optional[int] = ..., all_time_match_max: _Optional[int] = ..., all_time_life_max: _Optional[int] = ...) -> None: ...
    STATS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[CCitadelClientCachedPlayerStats.Stat]
    version: int
    def __init__(self, version: _Optional[int] = ..., stats: _Optional[_Iterable[_Union[CCitadelClientCachedPlayerStats.Stat, _Mapping]]] = ...) -> None: ...

class CCitadelClientMsg_AbilityPing(_message.Message):
    __slots__ = ["entity_index", "pinged_ability_id", "pinged_player_slot"]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    PINGED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    PINGED_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    entity_index: int
    pinged_ability_id: int
    pinged_player_slot: int
    def __init__(self, entity_index: _Optional[int] = ..., pinged_ability_id: _Optional[int] = ..., pinged_player_slot: _Optional[int] = ...) -> None: ...

class CCitadelClientMsg_ChatMsg(_message.Message):
    __slots__ = ["all_chat", "chat_text", "lane_color"]
    ALL_CHAT_FIELD_NUMBER: _ClassVar[int]
    CHAT_TEXT_FIELD_NUMBER: _ClassVar[int]
    LANE_COLOR_FIELD_NUMBER: _ClassVar[int]
    all_chat: bool
    chat_text: str
    lane_color: _citadel_gcmessages_common_pb2.CMsgLaneColor
    def __init__(self, chat_text: _Optional[str] = ..., all_chat: bool = ..., lane_color: _Optional[_Union[_citadel_gcmessages_common_pb2.CMsgLaneColor, str]] = ...) -> None: ...

class CCitadelClientMsg_CheaterVote(_message.Message):
    __slots__ = ["end_game_immediately"]
    END_GAME_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    end_game_immediately: bool
    def __init__(self, end_game_immediately: bool = ...) -> None: ...

class CCitadelClientMsg_ExecuteMapUnitAbility(_message.Message):
    __slots__ = ["ability_entity_index", "target_entity_index"]
    ABILITY_ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    ability_entity_index: int
    target_entity_index: int
    def __init__(self, ability_entity_index: _Optional[int] = ..., target_entity_index: _Optional[int] = ...) -> None: ...

class CCitadelClientMsg_GetDamageStats(_message.Message):
    __slots__ = ["ability_name", "lobby_player_slot"]
    ABILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOBBY_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    ability_name: str
    lobby_player_slot: int
    def __init__(self, lobby_player_slot: _Optional[int] = ..., ability_name: _Optional[str] = ...) -> None: ...

class CCitadelClientMsg_MapLine(_message.Message):
    __slots__ = ["mapline"]
    MAPLINE_FIELD_NUMBER: _ClassVar[int]
    mapline: _citadel_gcmessages_common_pb2.CMsgMapLine
    def __init__(self, mapline: _Optional[_Union[_citadel_gcmessages_common_pb2.CMsgMapLine, _Mapping]] = ...) -> None: ...

class CCitadelClientMsg_MapPing(_message.Message):
    __slots__ = ["entity_index", "event_type", "is_aggressive_ping", "is_blind_ping", "is_minimap_ping", "ping_location"]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_AGGRESSIVE_PING_FIELD_NUMBER: _ClassVar[int]
    IS_BLIND_PING_FIELD_NUMBER: _ClassVar[int]
    IS_MINIMAP_PING_FIELD_NUMBER: _ClassVar[int]
    PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    entity_index: int
    event_type: int
    is_aggressive_ping: bool
    is_blind_ping: bool
    is_minimap_ping: bool
    ping_location: _networkbasetypes_pb2.CMsgVector
    def __init__(self, ping_location: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., event_type: _Optional[int] = ..., entity_index: _Optional[int] = ..., is_aggressive_ping: bool = ..., is_minimap_ping: bool = ..., is_blind_ping: bool = ...) -> None: ...

class CCitadelClientMsg_MutePlayers(_message.Message):
    __slots__ = ["player_slots", "unmute"]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    UNMUTE_FIELD_NUMBER: _ClassVar[int]
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    unmute: bool
    def __init__(self, player_slots: _Optional[_Iterable[int]] = ..., unmute: bool = ...) -> None: ...

class CCitadelClientMsg_Pause(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CCitadelClientMsg_PerfReport(_message.Message):
    __slots__ = ["average_client_simulate_time", "average_client_tick_time", "average_compute_time", "average_frame_time", "average_frame_update_time", "average_idle_time", "average_input_processing_time", "average_output_time", "average_swap_time", "average_wait_for_rendering_to_complete_time", "max_client_simulate_time", "max_client_tick_time", "max_compute_time", "max_frame_time", "max_frame_update_time", "max_idle_time", "max_input_processing_time", "max_output_time", "max_swap_time", "max_wait_for_rendering_to_complete_time"]
    AVERAGE_CLIENT_SIMULATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CLIENT_TICK_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_COMPUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FRAME_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FRAME_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_IDLE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_INPUT_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_OUTPUT_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SWAP_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_WAIT_FOR_RENDERING_TO_COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIENT_SIMULATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIENT_TICK_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_COMPUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_FRAME_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_FRAME_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_IDLE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_INPUT_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTPUT_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_SWAP_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_WAIT_FOR_RENDERING_TO_COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    average_client_simulate_time: float
    average_client_tick_time: float
    average_compute_time: float
    average_frame_time: float
    average_frame_update_time: float
    average_idle_time: float
    average_input_processing_time: float
    average_output_time: float
    average_swap_time: float
    average_wait_for_rendering_to_complete_time: float
    max_client_simulate_time: float
    max_client_tick_time: float
    max_compute_time: float
    max_frame_time: float
    max_frame_update_time: float
    max_idle_time: float
    max_input_processing_time: float
    max_output_time: float
    max_swap_time: float
    max_wait_for_rendering_to_complete_time: float
    def __init__(self, average_frame_time: _Optional[float] = ..., max_frame_time: _Optional[float] = ..., average_compute_time: _Optional[float] = ..., max_compute_time: _Optional[float] = ..., average_client_tick_time: _Optional[float] = ..., max_client_tick_time: _Optional[float] = ..., average_client_simulate_time: _Optional[float] = ..., max_client_simulate_time: _Optional[float] = ..., average_output_time: _Optional[float] = ..., max_output_time: _Optional[float] = ..., average_wait_for_rendering_to_complete_time: _Optional[float] = ..., max_wait_for_rendering_to_complete_time: _Optional[float] = ..., average_swap_time: _Optional[float] = ..., max_swap_time: _Optional[float] = ..., average_frame_update_time: _Optional[float] = ..., max_frame_update_time: _Optional[float] = ..., average_idle_time: _Optional[float] = ..., max_idle_time: _Optional[float] = ..., average_input_processing_time: _Optional[float] = ..., max_input_processing_time: _Optional[float] = ...) -> None: ...

class CCitadelClientMsg_PerformanceStats(_message.Message):
    __slots__ = ["average_fps", "current_game_time", "max_fps", "min_fps"]
    AVERAGE_FPS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_FPS_FIELD_NUMBER: _ClassVar[int]
    MIN_FPS_FIELD_NUMBER: _ClassVar[int]
    average_fps: float
    current_game_time: float
    max_fps: float
    min_fps: float
    def __init__(self, current_game_time: _Optional[float] = ..., average_fps: _Optional[float] = ..., min_fps: _Optional[float] = ..., max_fps: _Optional[float] = ...) -> None: ...

class CCitadelClientMsg_PingWheel(_message.Message):
    __slots__ = ["entity_index", "ping_location", "ping_wheel_option_id", "subnav_message_id"]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PING_WHEEL_OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNAV_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    entity_index: int
    ping_location: _networkbasetypes_pb2.CMsgVector
    ping_wheel_option_id: int
    subnav_message_id: int
    def __init__(self, ping_wheel_option_id: _Optional[int] = ..., subnav_message_id: _Optional[int] = ..., ping_location: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ..., entity_index: _Optional[int] = ...) -> None: ...

class CCitadelClientMsg_QuickResponse(_message.Message):
    __slots__ = ["ping_wheel_message_id", "responding_to_ping_message_id", "responding_to_player_slot"]
    PING_WHEEL_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONDING_TO_PING_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONDING_TO_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    ping_wheel_message_id: int
    responding_to_ping_message_id: int
    responding_to_player_slot: int
    def __init__(self, ping_wheel_message_id: _Optional[int] = ..., responding_to_ping_message_id: _Optional[int] = ..., responding_to_player_slot: _Optional[int] = ...) -> None: ...

class ECitadelClientMessages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
