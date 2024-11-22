import steammessages_pb2 as _steammessages_pb2
import gcsdk_gcmessages_pb2 as _gcsdk_gcmessages_pb2
import citadel_gcmessages_common_pb2 as _citadel_gcmessages_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
k_EMsgGCToServerAddSpectator: EGCCitadelServerMessages
k_EMsgGCToServerAddSpectatorResponse: EGCCitadelServerMessages
k_EMsgGCToServerAllocateForMatch: EGCCitadelServerMessages
k_EMsgGCToServerAllocateForMatchResponse: EGCCitadelServerMessages
k_EMsgGCToServerCancelAllocateForMatch: EGCCitadelServerMessages
k_EMsgGCToServerRequestPing: EGCCitadelServerMessages
k_EMsgGCToServerSetServerConVar: EGCCitadelServerMessages
k_EMsgGCToServerSetServerConVarResponse: EGCCitadelServerMessages
k_EMsgServerToGCAbandonMatch: EGCCitadelServerMessages
k_EMsgServerToGCAbandonMatchResponse: EGCCitadelServerMessages
k_EMsgServerToGCEnterMatchmaking: EGCCitadelServerMessages
k_EMsgServerToGCIdlePing: EGCCitadelServerMessages
k_EMsgServerToGCMatchSignout: EGCCitadelServerMessages
k_EMsgServerToGCMatchSignoutPermission: EGCCitadelServerMessages
k_EMsgServerToGCMatchSignoutPermissionResponse: EGCCitadelServerMessages
k_EMsgServerToGCMatchSignoutResponse: EGCCitadelServerMessages
k_EMsgServerToGCReportCheater: EGCCitadelServerMessages
k_EMsgServerToGCReportCheaterResponse: EGCCitadelServerMessages
k_EMsgServerToGCTestConnection: EGCCitadelServerMessages
k_EMsgServerToGCTestConnectionResponse: EGCCitadelServerMessages
k_EMsgServerToGCUpdateLobbyServerState: EGCCitadelServerMessages
k_EMsgServerToGCUpdateMatchInfo: EGCCitadelServerMessages
k_EServerLobbyData_AutoTest: EGCServerLobbyData
k_EServerLobbyData_PlayerInfo: EGCServerLobbyData
k_EServerLobbyData_PlayerMMR: EGCServerLobbyData
k_EServerLobbyData_PostMatchSurvey: EGCServerLobbyData
k_EServerSignoutData_AccountStatChanges: EGCServerSignoutData
k_EServerSignoutData_BookRewards: EGCServerSignoutData
k_EServerSignoutData_DetailedStats: EGCServerSignoutData
k_EServerSignoutData_Disconnections: EGCServerSignoutData
k_EServerSignoutData_PenalizedPlayers: EGCServerSignoutData
k_EServerSignoutData_PerfData: EGCServerSignoutData
k_EServerSignoutData_PlayerChat: EGCServerSignoutData
k_EServerSignoutData_ReportCheaters: EGCServerSignoutData
k_EServerSignoutData_ServerPerfStats: EGCServerSignoutData

class CMsgGCToServerAddSpectator(_message.Message):
    __slots__ = ["account_id", "account_to_spectate", "lobby_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TO_SPECTATE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    account_to_spectate: int
    lobby_id: int
    def __init__(self, lobby_id: _Optional[int] = ..., account_id: _Optional[int] = ..., account_to_spectate: _Optional[int] = ...) -> None: ...

class CMsgGCToServerAddSpectatorResponse(_message.Message):
    __slots__ = ["requesting_account_id", "result"]
    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    REQUESTING_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eInternalError: CMsgGCToServerAddSpectatorResponse.EResponse
    k_eServerFull: CMsgGCToServerAddSpectatorResponse.EResponse
    k_eSuccess: CMsgGCToServerAddSpectatorResponse.EResponse
    requesting_account_id: int
    result: CMsgGCToServerAddSpectatorResponse.EResponse
    def __init__(self, result: _Optional[_Union[CMsgGCToServerAddSpectatorResponse.EResponse, str]] = ..., requesting_account_id: _Optional[int] = ...) -> None: ...

class CMsgGCToServerAllocateForMatch(_message.Message):
    __slots__ = ["match_id"]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    def __init__(self, match_id: _Optional[int] = ...) -> None: ...

class CMsgGCToServerAllocateForMatchResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgGCToServerCancelAllocateForMatch(_message.Message):
    __slots__ = ["match_id"]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    def __init__(self, match_id: _Optional[int] = ...) -> None: ...

class CMsgGCToServerRequestPing(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGCToServerSetServerConVar(_message.Message):
    __slots__ = ["convar_name", "convar_value"]
    CONVAR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVAR_VALUE_FIELD_NUMBER: _ClassVar[int]
    convar_name: str
    convar_value: str
    def __init__(self, convar_name: _Optional[str] = ..., convar_value: _Optional[str] = ...) -> None: ...

class CMsgGCToServerSetServerConVarResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgMatchData(_message.Message):
    __slots__ = ["end_reason", "game_mode", "low_pri_pool", "match_duration_s", "match_end_time", "match_mode", "new_player_pool", "objectives_mask_legacy", "objectives_mask_team0", "objectives_mask_team1", "players", "safe_to_abandon", "server_version", "stomp_score", "team_abandon", "winning_team"]
    class EEndReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class PlayerInfo(_message.Message):
        __slots__ = ["abandon_match_time_s", "abandon_time_stamp", "ability_damage", "ability_points", "account_id", "assigned_lane", "assists", "bullet_damage", "deaths", "denies", "gpm_10min", "gpm_15min", "gpm_20min", "gpm_25min", "gpm_30min", "gpm_35min", "gpm_end", "hero_build_id", "hero_bullets_fired", "hero_bullets_hit", "hero_bullets_hit_crit", "hero_bullets_lucky_shots", "hero_id", "hero_incoming_bullets_crit", "hero_incoming_bullets_fired", "hero_incoming_bullets_hit", "hero_mmr", "hero_mmr_with_uncertainty", "items", "kills", "last_hits", "level", "net_worth", "party_index", "platform", "player_ability_damage", "player_bullet_damage", "player_healing", "player_melee_damage", "player_mmr", "player_slot", "player_uncertainty", "team", "time_dead_s", "trooper_kill_excluded"]
        ABANDON_MATCH_TIME_S_FIELD_NUMBER: _ClassVar[int]
        ABANDON_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
        ABILITY_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        ABILITY_POINTS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        ASSIGNED_LANE_FIELD_NUMBER: _ClassVar[int]
        ASSISTS_FIELD_NUMBER: _ClassVar[int]
        BULLET_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        DEATHS_FIELD_NUMBER: _ClassVar[int]
        DENIES_FIELD_NUMBER: _ClassVar[int]
        GPM_10MIN_FIELD_NUMBER: _ClassVar[int]
        GPM_15MIN_FIELD_NUMBER: _ClassVar[int]
        GPM_20MIN_FIELD_NUMBER: _ClassVar[int]
        GPM_25MIN_FIELD_NUMBER: _ClassVar[int]
        GPM_30MIN_FIELD_NUMBER: _ClassVar[int]
        GPM_35MIN_FIELD_NUMBER: _ClassVar[int]
        GPM_END_FIELD_NUMBER: _ClassVar[int]
        HERO_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
        HERO_BULLETS_FIRED_FIELD_NUMBER: _ClassVar[int]
        HERO_BULLETS_HIT_CRIT_FIELD_NUMBER: _ClassVar[int]
        HERO_BULLETS_HIT_FIELD_NUMBER: _ClassVar[int]
        HERO_BULLETS_LUCKY_SHOTS_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        HERO_INCOMING_BULLETS_CRIT_FIELD_NUMBER: _ClassVar[int]
        HERO_INCOMING_BULLETS_FIRED_FIELD_NUMBER: _ClassVar[int]
        HERO_INCOMING_BULLETS_HIT_FIELD_NUMBER: _ClassVar[int]
        HERO_MMR_FIELD_NUMBER: _ClassVar[int]
        HERO_MMR_WITH_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        KILLS_FIELD_NUMBER: _ClassVar[int]
        LAST_HITS_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        NET_WORTH_FIELD_NUMBER: _ClassVar[int]
        PARTY_INDEX_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ABILITY_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        PLAYER_BULLET_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        PLAYER_HEALING_FIELD_NUMBER: _ClassVar[int]
        PLAYER_MELEE_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        PLAYER_MMR_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        PLAYER_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        TIME_DEAD_S_FIELD_NUMBER: _ClassVar[int]
        TROOPER_KILL_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
        abandon_match_time_s: int
        abandon_time_stamp: int
        ability_damage: int
        ability_points: int
        account_id: int
        assigned_lane: int
        assists: int
        bullet_damage: int
        deaths: int
        denies: int
        gpm_10min: int
        gpm_15min: int
        gpm_20min: int
        gpm_25min: int
        gpm_30min: int
        gpm_35min: int
        gpm_end: int
        hero_build_id: int
        hero_bullets_fired: int
        hero_bullets_hit: int
        hero_bullets_hit_crit: int
        hero_bullets_lucky_shots: int
        hero_id: int
        hero_incoming_bullets_crit: int
        hero_incoming_bullets_fired: int
        hero_incoming_bullets_hit: int
        hero_mmr: int
        hero_mmr_with_uncertainty: int
        items: _containers.RepeatedCompositeFieldContainer[CMsgMatchData.PlayerItem]
        kills: int
        last_hits: int
        level: int
        net_worth: int
        party_index: int
        platform: _steammessages_pb2.EGCPlatform
        player_ability_damage: int
        player_bullet_damage: int
        player_healing: int
        player_melee_damage: int
        player_mmr: int
        player_slot: int
        player_uncertainty: int
        team: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
        time_dead_s: int
        trooper_kill_excluded: int
        def __init__(self, account_id: _Optional[int] = ..., team: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]] = ..., player_slot: _Optional[int] = ..., hero_mmr_with_uncertainty: _Optional[int] = ..., player_mmr: _Optional[int] = ..., player_uncertainty: _Optional[int] = ..., hero_id: _Optional[int] = ..., kills: _Optional[int] = ..., deaths: _Optional[int] = ..., net_worth: _Optional[int] = ..., assists: _Optional[int] = ..., hero_mmr: _Optional[int] = ..., items: _Optional[_Iterable[_Union[CMsgMatchData.PlayerItem, _Mapping]]] = ..., gpm_10min: _Optional[int] = ..., gpm_15min: _Optional[int] = ..., gpm_20min: _Optional[int] = ..., gpm_25min: _Optional[int] = ..., gpm_30min: _Optional[int] = ..., gpm_35min: _Optional[int] = ..., gpm_end: _Optional[int] = ..., last_hits: _Optional[int] = ..., denies: _Optional[int] = ..., ability_points: _Optional[int] = ..., level: _Optional[int] = ..., assigned_lane: _Optional[int] = ..., party_index: _Optional[int] = ..., platform: _Optional[_Union[_steammessages_pb2.EGCPlatform, str]] = ..., ability_damage: _Optional[int] = ..., bullet_damage: _Optional[int] = ..., hero_bullets_hit: _Optional[int] = ..., hero_bullets_hit_crit: _Optional[int] = ..., player_healing: _Optional[int] = ..., hero_bullets_fired: _Optional[int] = ..., hero_incoming_bullets_fired: _Optional[int] = ..., hero_incoming_bullets_hit: _Optional[int] = ..., hero_incoming_bullets_crit: _Optional[int] = ..., time_dead_s: _Optional[int] = ..., player_bullet_damage: _Optional[int] = ..., player_ability_damage: _Optional[int] = ..., player_melee_damage: _Optional[int] = ..., abandon_match_time_s: _Optional[int] = ..., abandon_time_stamp: _Optional[int] = ..., trooper_kill_excluded: _Optional[int] = ..., hero_bullets_lucky_shots: _Optional[int] = ..., hero_build_id: _Optional[int] = ...) -> None: ...
    class PlayerItem(_message.Message):
        __slots__ = ["flags", "game_time_s", "imbued_ability_id", "item_id", "sold_time_s", "upgrade_id"]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        GAME_TIME_S_FIELD_NUMBER: _ClassVar[int]
        IMBUED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        SOLD_TIME_S_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_ID_FIELD_NUMBER: _ClassVar[int]
        flags: int
        game_time_s: int
        imbued_ability_id: int
        item_id: int
        sold_time_s: int
        upgrade_id: int
        def __init__(self, item_id: _Optional[int] = ..., game_time_s: _Optional[int] = ..., upgrade_id: _Optional[int] = ..., sold_time_s: _Optional[int] = ..., flags: _Optional[int] = ..., imbued_ability_id: _Optional[int] = ...) -> None: ...
    END_REASON_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    LOW_PRI_POOL_FIELD_NUMBER: _ClassVar[int]
    MATCH_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    MATCH_END_TIME_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    NEW_PLAYER_POOL_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_MASK_LEGACY_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_MASK_TEAM0_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_MASK_TEAM1_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    SAFE_TO_ABANDON_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    STOMP_SCORE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ABANDON_FIELD_NUMBER: _ClassVar[int]
    WINNING_TEAM_FIELD_NUMBER: _ClassVar[int]
    end_reason: CMsgMatchData.EEndReason
    game_mode: _citadel_gcmessages_common_pb2.ECitadelGameMode
    k_EEndReason_AllAbandoned: CMsgMatchData.EEndReason
    k_EEndReason_MatchLength: CMsgMatchData.EEndReason
    k_EEndReason_NetworkIssues: CMsgMatchData.EEndReason
    k_EEndReason_PlayerNeverConnected: CMsgMatchData.EEndReason
    k_EEndReason_TeamWin: CMsgMatchData.EEndReason
    low_pri_pool: bool
    match_duration_s: int
    match_end_time: int
    match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
    new_player_pool: bool
    objectives_mask_legacy: int
    objectives_mask_team0: int
    objectives_mask_team1: int
    players: _containers.RepeatedCompositeFieldContainer[CMsgMatchData.PlayerInfo]
    safe_to_abandon: bool
    server_version: int
    stomp_score: float
    team_abandon: bool
    winning_team: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
    def __init__(self, match_duration_s: _Optional[int] = ..., end_reason: _Optional[_Union[CMsgMatchData.EEndReason, str]] = ..., winning_team: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]] = ..., players: _Optional[_Iterable[_Union[CMsgMatchData.PlayerInfo, _Mapping]]] = ..., objectives_mask_legacy: _Optional[int] = ..., server_version: _Optional[int] = ..., game_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelGameMode, str]] = ..., match_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]] = ..., objectives_mask_team0: _Optional[int] = ..., objectives_mask_team1: _Optional[int] = ..., match_end_time: _Optional[int] = ..., stomp_score: _Optional[float] = ..., safe_to_abandon: bool = ..., team_abandon: bool = ..., new_player_pool: bool = ..., low_pri_pool: bool = ...) -> None: ...

class CMsgServerCrashSentinelFile(_message.Message):
    __slots__ = ["game_info", "instance_id", "pid", "saved_time", "server_cluster", "server_port", "server_private_ip_addr", "server_public_ip_addr", "server_steam_id", "server_version", "version"]
    class GameInfo(_message.Message):
        __slots__ = ["game_mode", "lobby_id", "match_id", "match_mode", "players", "server_state", "was_server_shutdown"]
        GAME_MODE_FIELD_NUMBER: _ClassVar[int]
        LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
        MATCH_ID_FIELD_NUMBER: _ClassVar[int]
        MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        SERVER_STATE_FIELD_NUMBER: _ClassVar[int]
        WAS_SERVER_SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        game_mode: _citadel_gcmessages_common_pb2.ECitadelGameMode
        lobby_id: int
        match_id: int
        match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
        players: _containers.RepeatedCompositeFieldContainer[CMsgServerCrashSentinelFile.Player]
        server_state: int
        was_server_shutdown: bool
        def __init__(self, match_id: _Optional[int] = ..., lobby_id: _Optional[int] = ..., server_state: _Optional[int] = ..., players: _Optional[_Iterable[_Union[CMsgServerCrashSentinelFile.Player, _Mapping]]] = ..., match_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]] = ..., game_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelGameMode, str]] = ..., was_server_shutdown: bool = ...) -> None: ...
    class Player(_message.Message):
        __slots__ = ["account_id", "hero_id"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        hero_id: int
        def __init__(self, account_id: _Optional[int] = ..., hero_id: _Optional[int] = ...) -> None: ...
    GAME_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    SAVED_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    SERVER_PRIVATE_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_PUBLIC_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    game_info: CMsgServerCrashSentinelFile.GameInfo
    instance_id: int
    pid: int
    saved_time: int
    server_cluster: int
    server_port: int
    server_private_ip_addr: int
    server_public_ip_addr: int
    server_steam_id: int
    server_version: int
    version: int
    def __init__(self, version: _Optional[int] = ..., server_steam_id: _Optional[int] = ..., server_public_ip_addr: _Optional[int] = ..., server_port: _Optional[int] = ..., server_cluster: _Optional[int] = ..., pid: _Optional[int] = ..., saved_time: _Optional[int] = ..., server_version: _Optional[int] = ..., game_info: _Optional[_Union[CMsgServerCrashSentinelFile.GameInfo, _Mapping]] = ..., server_private_ip_addr: _Optional[int] = ..., instance_id: _Optional[int] = ...) -> None: ...

class CMsgServerSignoutData_AccountStatChanges(_message.Message):
    __slots__ = ["account_stats"]
    class AccountStats(_message.Message):
        __slots__ = ["account_id", "stats"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        stats: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_AccountStatChanges.Stat]
        def __init__(self, account_id: _Optional[int] = ..., stats: _Optional[_Iterable[_Union[CMsgServerSignoutData_AccountStatChanges.Stat, _Mapping]]] = ...) -> None: ...
    class Stat(_message.Message):
        __slots__ = ["hero_id", "medal", "stat_id", "value"]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        MEDAL_FIELD_NUMBER: _ClassVar[int]
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        hero_id: int
        medal: _citadel_gcmessages_common_pb2.ECitadelAccountStatMedal
        stat_id: int
        value: int
        def __init__(self, hero_id: _Optional[int] = ..., stat_id: _Optional[int] = ..., value: _Optional[int] = ..., medal: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelAccountStatMedal, str]] = ...) -> None: ...
    ACCOUNT_STATS_FIELD_NUMBER: _ClassVar[int]
    account_stats: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_AccountStatChanges.AccountStats]
    def __init__(self, account_stats: _Optional[_Iterable[_Union[CMsgServerSignoutData_AccountStatChanges.AccountStats, _Mapping]]] = ...) -> None: ...

class CMsgServerSignoutData_BookRewards(_message.Message):
    __slots__ = ["account_rewards"]
    class AccountRewards(_message.Message):
        __slots__ = ["account_id", "book_reward"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        BOOK_REWARD_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        book_reward: CMsgServerSignoutData_BookRewards.BookReward
        def __init__(self, account_id: _Optional[int] = ..., book_reward: _Optional[_Union[CMsgServerSignoutData_BookRewards.BookReward, _Mapping]] = ...) -> None: ...
    class BookReward(_message.Message):
        __slots__ = ["book_id", "xp_reward"]
        BOOK_ID_FIELD_NUMBER: _ClassVar[int]
        XP_REWARD_FIELD_NUMBER: _ClassVar[int]
        book_id: int
        xp_reward: int
        def __init__(self, book_id: _Optional[int] = ..., xp_reward: _Optional[int] = ...) -> None: ...
    ACCOUNT_REWARDS_FIELD_NUMBER: _ClassVar[int]
    account_rewards: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_BookRewards.AccountRewards]
    def __init__(self, account_rewards: _Optional[_Iterable[_Union[CMsgServerSignoutData_BookRewards.AccountRewards, _Mapping]]] = ...) -> None: ...

class CMsgServerSignoutData_DetailedStats(_message.Message):
    __slots__ = ["mid_boss", "objectives", "player_stats"]
    class MidBoss(_message.Message):
        __slots__ = ["destroyed_time_s", "team_claimed", "team_killed"]
        DESTROYED_TIME_S_FIELD_NUMBER: _ClassVar[int]
        TEAM_CLAIMED_FIELD_NUMBER: _ClassVar[int]
        TEAM_KILLED_FIELD_NUMBER: _ClassVar[int]
        destroyed_time_s: int
        team_claimed: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
        team_killed: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
        def __init__(self, team_killed: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]] = ..., team_claimed: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]] = ..., destroyed_time_s: _Optional[int] = ...) -> None: ...
    class Objective(_message.Message):
        __slots__ = ["creep_damage", "creep_damage_mitigated", "destroyed_time_s", "first_damage_time_s", "player_damage", "player_damage_mitigated", "team", "team_objective_id"]
        CREEP_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        CREEP_DAMAGE_MITIGATED_FIELD_NUMBER: _ClassVar[int]
        DESTROYED_TIME_S_FIELD_NUMBER: _ClassVar[int]
        FIRST_DAMAGE_TIME_S_FIELD_NUMBER: _ClassVar[int]
        PLAYER_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        PLAYER_DAMAGE_MITIGATED_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        TEAM_OBJECTIVE_ID_FIELD_NUMBER: _ClassVar[int]
        creep_damage: int
        creep_damage_mitigated: int
        destroyed_time_s: int
        first_damage_time_s: int
        player_damage: int
        player_damage_mitigated: int
        team: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
        team_objective_id: _citadel_gcmessages_common_pb2.ECitadelTeamObjective
        def __init__(self, destroyed_time_s: _Optional[int] = ..., creep_damage: _Optional[int] = ..., creep_damage_mitigated: _Optional[int] = ..., player_damage: _Optional[int] = ..., player_damage_mitigated: _Optional[int] = ..., first_damage_time_s: _Optional[int] = ..., team_objective_id: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelTeamObjective, str]] = ..., team: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]] = ...) -> None: ...
    class Player(_message.Message):
        __slots__ = ["player_slot", "time_samples"]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        TIME_SAMPLES_FIELD_NUMBER: _ClassVar[int]
        player_slot: int
        time_samples: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_DetailedStats.TimeSample]
        def __init__(self, player_slot: _Optional[int] = ..., time_samples: _Optional[_Iterable[_Union[CMsgServerSignoutData_DetailedStats.TimeSample, _Mapping]]] = ...) -> None: ...
    class Position(_message.Message):
        __slots__ = ["x", "y", "z"]
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        Z_FIELD_NUMBER: _ClassVar[int]
        x: float
        y: float
        z: float
        def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...
    class TimeSample(_message.Message):
        __slots__ = ["gold_stats", "match_time_s", "stats"]
        class GoldStats(_message.Message):
            __slots__ = ["boss", "boss_orb", "death_loss", "denied", "lane_creep", "lane_creep_orb", "neutral_creep", "neutral_creep_orb", "player", "player_orb", "treasure"]
            BOSS_FIELD_NUMBER: _ClassVar[int]
            BOSS_ORB_FIELD_NUMBER: _ClassVar[int]
            DEATH_LOSS_FIELD_NUMBER: _ClassVar[int]
            DENIED_FIELD_NUMBER: _ClassVar[int]
            LANE_CREEP_FIELD_NUMBER: _ClassVar[int]
            LANE_CREEP_ORB_FIELD_NUMBER: _ClassVar[int]
            NEUTRAL_CREEP_FIELD_NUMBER: _ClassVar[int]
            NEUTRAL_CREEP_ORB_FIELD_NUMBER: _ClassVar[int]
            PLAYER_FIELD_NUMBER: _ClassVar[int]
            PLAYER_ORB_FIELD_NUMBER: _ClassVar[int]
            TREASURE_FIELD_NUMBER: _ClassVar[int]
            boss: int
            boss_orb: int
            death_loss: int
            denied: int
            lane_creep: int
            lane_creep_orb: int
            neutral_creep: int
            neutral_creep_orb: int
            player: int
            player_orb: int
            treasure: int
            def __init__(self, player: _Optional[int] = ..., player_orb: _Optional[int] = ..., lane_creep_orb: _Optional[int] = ..., neutral_creep_orb: _Optional[int] = ..., boss: _Optional[int] = ..., boss_orb: _Optional[int] = ..., treasure: _Optional[int] = ..., denied: _Optional[int] = ..., death_loss: _Optional[int] = ..., lane_creep: _Optional[int] = ..., neutral_creep: _Optional[int] = ...) -> None: ...
        class Stats(_message.Message):
            __slots__ = ["ability_points", "absorption_provided", "assists", "boss_damage", "creep_damage", "creep_kills", "damage_absorbed", "deaths", "denies", "heal_lost", "heal_prevented", "kills", "max_health", "net_worth", "neutral_damage", "neutral_kills", "player_damage", "player_damage_taken", "player_healing", "possible_creeps", "self_healing", "shots_hit", "shots_missed", "tech_power", "weapon_power"]
            ABILITY_POINTS_FIELD_NUMBER: _ClassVar[int]
            ABSORPTION_PROVIDED_FIELD_NUMBER: _ClassVar[int]
            ASSISTS_FIELD_NUMBER: _ClassVar[int]
            BOSS_DAMAGE_FIELD_NUMBER: _ClassVar[int]
            CREEP_DAMAGE_FIELD_NUMBER: _ClassVar[int]
            CREEP_KILLS_FIELD_NUMBER: _ClassVar[int]
            DAMAGE_ABSORBED_FIELD_NUMBER: _ClassVar[int]
            DEATHS_FIELD_NUMBER: _ClassVar[int]
            DENIES_FIELD_NUMBER: _ClassVar[int]
            HEAL_LOST_FIELD_NUMBER: _ClassVar[int]
            HEAL_PREVENTED_FIELD_NUMBER: _ClassVar[int]
            KILLS_FIELD_NUMBER: _ClassVar[int]
            MAX_HEALTH_FIELD_NUMBER: _ClassVar[int]
            NET_WORTH_FIELD_NUMBER: _ClassVar[int]
            NEUTRAL_DAMAGE_FIELD_NUMBER: _ClassVar[int]
            NEUTRAL_KILLS_FIELD_NUMBER: _ClassVar[int]
            PLAYER_DAMAGE_FIELD_NUMBER: _ClassVar[int]
            PLAYER_DAMAGE_TAKEN_FIELD_NUMBER: _ClassVar[int]
            PLAYER_HEALING_FIELD_NUMBER: _ClassVar[int]
            POSSIBLE_CREEPS_FIELD_NUMBER: _ClassVar[int]
            SELF_HEALING_FIELD_NUMBER: _ClassVar[int]
            SHOTS_HIT_FIELD_NUMBER: _ClassVar[int]
            SHOTS_MISSED_FIELD_NUMBER: _ClassVar[int]
            TECH_POWER_FIELD_NUMBER: _ClassVar[int]
            WEAPON_POWER_FIELD_NUMBER: _ClassVar[int]
            ability_points: int
            absorption_provided: int
            assists: int
            boss_damage: int
            creep_damage: int
            creep_kills: int
            damage_absorbed: int
            deaths: int
            denies: int
            heal_lost: int
            heal_prevented: int
            kills: int
            max_health: int
            net_worth: int
            neutral_damage: int
            neutral_kills: int
            player_damage: int
            player_damage_taken: int
            player_healing: int
            possible_creeps: int
            self_healing: int
            shots_hit: int
            shots_missed: int
            tech_power: int
            weapon_power: int
            def __init__(self, net_worth: _Optional[int] = ..., kills: _Optional[int] = ..., deaths: _Optional[int] = ..., assists: _Optional[int] = ..., possible_creeps: _Optional[int] = ..., creep_kills: _Optional[int] = ..., neutral_kills: _Optional[int] = ..., creep_damage: _Optional[int] = ..., neutral_damage: _Optional[int] = ..., boss_damage: _Optional[int] = ..., player_damage: _Optional[int] = ..., denies: _Optional[int] = ..., player_healing: _Optional[int] = ..., ability_points: _Optional[int] = ..., self_healing: _Optional[int] = ..., player_damage_taken: _Optional[int] = ..., max_health: _Optional[int] = ..., weapon_power: _Optional[int] = ..., tech_power: _Optional[int] = ..., shots_hit: _Optional[int] = ..., shots_missed: _Optional[int] = ..., damage_absorbed: _Optional[int] = ..., absorption_provided: _Optional[int] = ..., heal_prevented: _Optional[int] = ..., heal_lost: _Optional[int] = ...) -> None: ...
        GOLD_STATS_FIELD_NUMBER: _ClassVar[int]
        MATCH_TIME_S_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        gold_stats: CMsgServerSignoutData_DetailedStats.TimeSample.GoldStats
        match_time_s: int
        stats: CMsgServerSignoutData_DetailedStats.TimeSample.Stats
        def __init__(self, match_time_s: _Optional[int] = ..., stats: _Optional[_Union[CMsgServerSignoutData_DetailedStats.TimeSample.Stats, _Mapping]] = ..., gold_stats: _Optional[_Union[CMsgServerSignoutData_DetailedStats.TimeSample.GoldStats, _Mapping]] = ...) -> None: ...
    MID_BOSS_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STATS_FIELD_NUMBER: _ClassVar[int]
    mid_boss: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_DetailedStats.MidBoss]
    objectives: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_DetailedStats.Objective]
    player_stats: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_DetailedStats.Player]
    def __init__(self, player_stats: _Optional[_Iterable[_Union[CMsgServerSignoutData_DetailedStats.Player, _Mapping]]] = ..., objectives: _Optional[_Iterable[_Union[CMsgServerSignoutData_DetailedStats.Objective, _Mapping]]] = ..., mid_boss: _Optional[_Iterable[_Union[CMsgServerSignoutData_DetailedStats.MidBoss, _Mapping]]] = ...) -> None: ...

class CMsgServerSignoutData_Disconnections(_message.Message):
    __slots__ = ["disconnections"]
    class CMsgMatchDisconnection(_message.Message):
        __slots__ = ["account_id", "connection_state", "disconnect_time", "match_disconnect_time", "match_reconnect_delay", "reason_code", "reconnect_delay"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
        DISCONNECT_TIME_FIELD_NUMBER: _ClassVar[int]
        MATCH_DISCONNECT_TIME_FIELD_NUMBER: _ClassVar[int]
        MATCH_RECONNECT_DELAY_FIELD_NUMBER: _ClassVar[int]
        REASON_CODE_FIELD_NUMBER: _ClassVar[int]
        RECONNECT_DELAY_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        connection_state: int
        disconnect_time: int
        match_disconnect_time: int
        match_reconnect_delay: int
        reason_code: int
        reconnect_delay: int
        def __init__(self, account_id: _Optional[int] = ..., disconnect_time: _Optional[int] = ..., connection_state: _Optional[int] = ..., reason_code: _Optional[int] = ..., reconnect_delay: _Optional[int] = ..., match_disconnect_time: _Optional[int] = ..., match_reconnect_delay: _Optional[int] = ...) -> None: ...
    DISCONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    disconnections: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_Disconnections.CMsgMatchDisconnection]
    def __init__(self, disconnections: _Optional[_Iterable[_Union[CMsgServerSignoutData_Disconnections.CMsgMatchDisconnection, _Mapping]]] = ...) -> None: ...

class CMsgServerSignoutData_PenalizedPlayers(_message.Message):
    __slots__ = ["penalized_players"]
    class EPenaltyReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Penalty(_message.Message):
        __slots__ = ["account_id", "match_time_s", "reason", "time_stamp"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        MATCH_TIME_S_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        match_time_s: int
        reason: CMsgServerSignoutData_PenalizedPlayers.EPenaltyReason
        time_stamp: int
        def __init__(self, account_id: _Optional[int] = ..., reason: _Optional[_Union[CMsgServerSignoutData_PenalizedPlayers.EPenaltyReason, str]] = ..., match_time_s: _Optional[int] = ..., time_stamp: _Optional[int] = ...) -> None: ...
    PENALIZED_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    k_EPenaltyReason_AFK: CMsgServerSignoutData_PenalizedPlayers.EPenaltyReason
    k_EPenaltyReason_Abandon: CMsgServerSignoutData_PenalizedPlayers.EPenaltyReason
    k_EPenaltyReason_DisconnectedTooLong: CMsgServerSignoutData_PenalizedPlayers.EPenaltyReason
    penalized_players: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_PenalizedPlayers.Penalty]
    def __init__(self, penalized_players: _Optional[_Iterable[_Union[CMsgServerSignoutData_PenalizedPlayers.Penalty, _Mapping]]] = ...) -> None: ...

class CMsgServerSignoutData_PerfData(_message.Message):
    __slots__ = ["average_client_simulate_time", "average_client_tick_time", "average_compute_time", "average_frame_time", "average_frame_update_time", "average_idle_time", "average_input_processing_time", "average_output_time", "average_swap_time", "average_wait_for_rendering_to_complete_time", "max_client_simulate_time", "max_client_tick_time", "max_compute_time", "max_frame_time", "max_frame_update_time", "max_idle_time", "max_input_processing_time", "max_output_time", "max_swap_time", "max_wait_for_rendering_to_complete_time", "server_average_frame_time", "server_max_frame_time"]
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
    SERVER_AVERAGE_FRAME_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_MAX_FRAME_TIME_FIELD_NUMBER: _ClassVar[int]
    average_client_simulate_time: _containers.RepeatedScalarFieldContainer[float]
    average_client_tick_time: _containers.RepeatedScalarFieldContainer[float]
    average_compute_time: _containers.RepeatedScalarFieldContainer[float]
    average_frame_time: _containers.RepeatedScalarFieldContainer[float]
    average_frame_update_time: _containers.RepeatedScalarFieldContainer[float]
    average_idle_time: _containers.RepeatedScalarFieldContainer[float]
    average_input_processing_time: _containers.RepeatedScalarFieldContainer[float]
    average_output_time: _containers.RepeatedScalarFieldContainer[float]
    average_swap_time: _containers.RepeatedScalarFieldContainer[float]
    average_wait_for_rendering_to_complete_time: _containers.RepeatedScalarFieldContainer[float]
    max_client_simulate_time: _containers.RepeatedScalarFieldContainer[float]
    max_client_tick_time: _containers.RepeatedScalarFieldContainer[float]
    max_compute_time: _containers.RepeatedScalarFieldContainer[float]
    max_frame_time: _containers.RepeatedScalarFieldContainer[float]
    max_frame_update_time: _containers.RepeatedScalarFieldContainer[float]
    max_idle_time: _containers.RepeatedScalarFieldContainer[float]
    max_input_processing_time: _containers.RepeatedScalarFieldContainer[float]
    max_output_time: _containers.RepeatedScalarFieldContainer[float]
    max_swap_time: _containers.RepeatedScalarFieldContainer[float]
    max_wait_for_rendering_to_complete_time: _containers.RepeatedScalarFieldContainer[float]
    server_average_frame_time: float
    server_max_frame_time: float
    def __init__(self, average_frame_time: _Optional[_Iterable[float]] = ..., max_frame_time: _Optional[_Iterable[float]] = ..., server_average_frame_time: _Optional[float] = ..., server_max_frame_time: _Optional[float] = ..., average_compute_time: _Optional[_Iterable[float]] = ..., max_compute_time: _Optional[_Iterable[float]] = ..., average_client_tick_time: _Optional[_Iterable[float]] = ..., max_client_tick_time: _Optional[_Iterable[float]] = ..., average_client_simulate_time: _Optional[_Iterable[float]] = ..., max_client_simulate_time: _Optional[_Iterable[float]] = ..., average_output_time: _Optional[_Iterable[float]] = ..., max_output_time: _Optional[_Iterable[float]] = ..., average_wait_for_rendering_to_complete_time: _Optional[_Iterable[float]] = ..., max_wait_for_rendering_to_complete_time: _Optional[_Iterable[float]] = ..., average_swap_time: _Optional[_Iterable[float]] = ..., max_swap_time: _Optional[_Iterable[float]] = ..., average_frame_update_time: _Optional[_Iterable[float]] = ..., max_frame_update_time: _Optional[_Iterable[float]] = ..., average_idle_time: _Optional[_Iterable[float]] = ..., max_idle_time: _Optional[_Iterable[float]] = ..., average_input_processing_time: _Optional[_Iterable[float]] = ..., max_input_processing_time: _Optional[_Iterable[float]] = ...) -> None: ...

class CMsgServerSignoutData_PlayerChat(_message.Message):
    __slots__ = ["chat_lines"]
    class ChatLine(_message.Message):
        __slots__ = ["chat_line", "game_time", "player_slot", "team_only"]
        CHAT_LINE_FIELD_NUMBER: _ClassVar[int]
        GAME_TIME_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        TEAM_ONLY_FIELD_NUMBER: _ClassVar[int]
        chat_line: str
        game_time: float
        player_slot: int
        team_only: bool
        def __init__(self, player_slot: _Optional[int] = ..., game_time: _Optional[float] = ..., team_only: bool = ..., chat_line: _Optional[str] = ...) -> None: ...
    CHAT_LINES_FIELD_NUMBER: _ClassVar[int]
    chat_lines: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_PlayerChat.ChatLine]
    def __init__(self, chat_lines: _Optional[_Iterable[_Union[CMsgServerSignoutData_PlayerChat.ChatLine, _Mapping]]] = ...) -> None: ...

class CMsgServerSignoutData_ServerPerfStats(_message.Message):
    __slots__ = ["end_memory_bytes", "frame_idle_time_95_micro_s", "frame_idle_time_avg_micro_s", "frame_time_80_micro_s", "frame_time_95_micro_s", "frame_time_99_micro_s", "frame_time_avg_micro_s", "frame_time_max_micro_s", "peak_memory_bytes", "perf_samples"]
    class FrameCounts(_message.Message):
        __slots__ = ["longest_run", "num_frames", "num_runs"]
        LONGEST_RUN_FIELD_NUMBER: _ClassVar[int]
        NUM_FRAMES_FIELD_NUMBER: _ClassVar[int]
        NUM_RUNS_FIELD_NUMBER: _ClassVar[int]
        longest_run: int
        num_frames: int
        num_runs: int
        def __init__(self, num_frames: _Optional[int] = ..., longest_run: _Optional[int] = ..., num_runs: _Optional[int] = ...) -> None: ...
    class MatchPerfSamples(_message.Message):
        __slots__ = ["long_frame_threshold", "low_idle_threshold", "samples"]
        LONG_FRAME_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        LOW_IDLE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        SAMPLES_FIELD_NUMBER: _ClassVar[int]
        long_frame_threshold: float
        low_idle_threshold: float
        samples: _containers.RepeatedCompositeFieldContainer[CMsgServerSignoutData_ServerPerfStats.PerfSample]
        def __init__(self, long_frame_threshold: _Optional[float] = ..., low_idle_threshold: _Optional[float] = ..., samples: _Optional[_Iterable[_Union[CMsgServerSignoutData_ServerPerfStats.PerfSample, _Mapping]]] = ...) -> None: ...
    class PerfSample(_message.Message):
        __slots__ = ["avg_frame", "avg_idle", "game_time_s", "long_frames", "low_idle_frames", "memory_bytes", "peak_memory_bytes", "performant_frames", "total_frames"]
        AVG_FRAME_FIELD_NUMBER: _ClassVar[int]
        AVG_IDLE_FIELD_NUMBER: _ClassVar[int]
        GAME_TIME_S_FIELD_NUMBER: _ClassVar[int]
        LONG_FRAMES_FIELD_NUMBER: _ClassVar[int]
        LOW_IDLE_FRAMES_FIELD_NUMBER: _ClassVar[int]
        MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
        PEAK_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
        PERFORMANT_FRAMES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FRAMES_FIELD_NUMBER: _ClassVar[int]
        avg_frame: float
        avg_idle: float
        game_time_s: int
        long_frames: CMsgServerSignoutData_ServerPerfStats.FrameCounts
        low_idle_frames: CMsgServerSignoutData_ServerPerfStats.FrameCounts
        memory_bytes: int
        peak_memory_bytes: int
        performant_frames: CMsgServerSignoutData_ServerPerfStats.FrameCounts
        total_frames: int
        def __init__(self, game_time_s: _Optional[int] = ..., avg_frame: _Optional[float] = ..., avg_idle: _Optional[float] = ..., total_frames: _Optional[int] = ..., performant_frames: _Optional[_Union[CMsgServerSignoutData_ServerPerfStats.FrameCounts, _Mapping]] = ..., long_frames: _Optional[_Union[CMsgServerSignoutData_ServerPerfStats.FrameCounts, _Mapping]] = ..., low_idle_frames: _Optional[_Union[CMsgServerSignoutData_ServerPerfStats.FrameCounts, _Mapping]] = ..., memory_bytes: _Optional[int] = ..., peak_memory_bytes: _Optional[int] = ...) -> None: ...
    END_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    FRAME_IDLE_TIME_95_MICRO_S_FIELD_NUMBER: _ClassVar[int]
    FRAME_IDLE_TIME_AVG_MICRO_S_FIELD_NUMBER: _ClassVar[int]
    FRAME_TIME_80_MICRO_S_FIELD_NUMBER: _ClassVar[int]
    FRAME_TIME_95_MICRO_S_FIELD_NUMBER: _ClassVar[int]
    FRAME_TIME_99_MICRO_S_FIELD_NUMBER: _ClassVar[int]
    FRAME_TIME_AVG_MICRO_S_FIELD_NUMBER: _ClassVar[int]
    FRAME_TIME_MAX_MICRO_S_FIELD_NUMBER: _ClassVar[int]
    PEAK_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    PERF_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    end_memory_bytes: int
    frame_idle_time_95_micro_s: int
    frame_idle_time_avg_micro_s: int
    frame_time_80_micro_s: int
    frame_time_95_micro_s: int
    frame_time_99_micro_s: int
    frame_time_avg_micro_s: int
    frame_time_max_micro_s: int
    peak_memory_bytes: int
    perf_samples: CMsgServerSignoutData_ServerPerfStats.MatchPerfSamples
    def __init__(self, peak_memory_bytes: _Optional[int] = ..., end_memory_bytes: _Optional[int] = ..., frame_time_max_micro_s: _Optional[int] = ..., frame_time_95_micro_s: _Optional[int] = ..., frame_time_avg_micro_s: _Optional[int] = ..., frame_idle_time_95_micro_s: _Optional[int] = ..., frame_idle_time_avg_micro_s: _Optional[int] = ..., frame_time_80_micro_s: _Optional[int] = ..., frame_time_99_micro_s: _Optional[int] = ..., perf_samples: _Optional[_Union[CMsgServerSignoutData_ServerPerfStats.MatchPerfSamples, _Mapping]] = ...) -> None: ...

class CMsgServerToGCAbandonMatch(_message.Message):
    __slots__ = ["additional_data", "cluster_id", "game_mode", "instance_id", "lobby_id", "match_id", "match_mode", "pid", "players", "port", "private_ip_address", "public_ip_address", "reason_code", "server_steam_id", "server_version", "was_server_shutdown"]
    class EReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Player(_message.Message):
        __slots__ = ["account_id", "additional_data", "hero_id"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        additional_data: int
        hero_id: int
        def __init__(self, account_id: _Optional[int] = ..., additional_data: _Optional[int] = ..., hero_id: _Optional[int] = ...) -> None: ...
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    WAS_SERVER_SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    additional_data: int
    cluster_id: int
    eReason_ClientsFailedToConnect: CMsgServerToGCAbandonMatch.EReason
    eReason_ServerCrash: CMsgServerToGCAbandonMatch.EReason
    game_mode: _citadel_gcmessages_common_pb2.ECitadelGameMode
    instance_id: int
    lobby_id: int
    match_id: int
    match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
    pid: int
    players: _containers.RepeatedCompositeFieldContainer[CMsgServerToGCAbandonMatch.Player]
    port: int
    private_ip_address: int
    public_ip_address: int
    reason_code: CMsgServerToGCAbandonMatch.EReason
    server_steam_id: int
    server_version: int
    was_server_shutdown: bool
    def __init__(self, server_steam_id: _Optional[int] = ..., lobby_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., reason_code: _Optional[_Union[CMsgServerToGCAbandonMatch.EReason, str]] = ..., additional_data: _Optional[int] = ..., match_id: _Optional[int] = ..., players: _Optional[_Iterable[_Union[CMsgServerToGCAbandonMatch.Player, _Mapping]]] = ..., public_ip_address: _Optional[int] = ..., port: _Optional[int] = ..., server_version: _Optional[int] = ..., pid: _Optional[int] = ..., instance_id: _Optional[int] = ..., private_ip_address: _Optional[int] = ..., match_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]] = ..., game_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelGameMode, str]] = ..., was_server_shutdown: bool = ...) -> None: ...

class CMsgServerToGCAbandonMatchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgServerToGCEnterMatchmaking(_message.Message):
    __slots__ = ["cluster_id", "region_id", "sdr_address", "search_key", "server_port", "server_private_ip", "server_public_ip", "server_version"]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    SDR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    SERVER_PRIVATE_IP_FIELD_NUMBER: _ClassVar[int]
    SERVER_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    region_id: int
    sdr_address: bytes
    search_key: str
    server_port: int
    server_private_ip: int
    server_public_ip: int
    server_version: int
    def __init__(self, server_version: _Optional[int] = ..., search_key: _Optional[str] = ..., region_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., server_public_ip: _Optional[int] = ..., server_private_ip: _Optional[int] = ..., server_port: _Optional[int] = ..., sdr_address: _Optional[bytes] = ...) -> None: ...

class CMsgServerToGCIdlePing(_message.Message):
    __slots__ = ["server_version"]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    server_version: int
    def __init__(self, server_version: _Optional[int] = ...) -> None: ...

class CMsgServerToGCMatchSignout(_message.Message):
    __slots__ = ["additional_data", "cluster_id", "lobby_id", "match_data", "match_id", "signout_attempt"]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNOUT_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    additional_data: _containers.RepeatedCompositeFieldContainer[_gcsdk_gcmessages_pb2.CExtraMsgBlock]
    cluster_id: int
    lobby_id: int
    match_data: CMsgMatchData
    match_id: int
    signout_attempt: int
    def __init__(self, additional_data: _Optional[_Iterable[_Union[_gcsdk_gcmessages_pb2.CExtraMsgBlock, _Mapping]]] = ..., signout_attempt: _Optional[int] = ..., lobby_id: _Optional[int] = ..., match_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., match_data: _Optional[_Union[CMsgMatchData, _Mapping]] = ...) -> None: ...

class CMsgServerToGCMatchSignoutPermission(_message.Message):
    __slots__ = ["match_id", "match_mode", "permission_request", "signout_start"]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SIGNOUT_START_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
    permission_request: int
    signout_start: int
    def __init__(self, signout_start: _Optional[int] = ..., permission_request: _Optional[int] = ..., match_id: _Optional[int] = ..., match_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]] = ...) -> None: ...

class CMsgServerToGCMatchSignoutPermissionResponse(_message.Message):
    __slots__ = ["can_sign_out", "requested_data", "retry_time_s"]
    CAN_SIGN_OUT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_DATA_FIELD_NUMBER: _ClassVar[int]
    RETRY_TIME_S_FIELD_NUMBER: _ClassVar[int]
    can_sign_out: bool
    requested_data: _containers.RepeatedScalarFieldContainer[EGCServerSignoutData]
    retry_time_s: int
    def __init__(self, can_sign_out: bool = ..., retry_time_s: _Optional[int] = ..., requested_data: _Optional[_Iterable[_Union[EGCServerSignoutData, str]]] = ...) -> None: ...

class CMsgServerToGCMatchSignoutResponse(_message.Message):
    __slots__ = ["result"]
    class ESignoutResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_ESignout_Failed_InFlight: CMsgServerToGCMatchSignoutResponse.ESignoutResult
    k_ESignout_Failed_NoRetry: CMsgServerToGCMatchSignoutResponse.ESignoutResult
    k_ESignout_Failed_Retry: CMsgServerToGCMatchSignoutResponse.ESignoutResult
    k_ESignout_Success: CMsgServerToGCMatchSignoutResponse.ESignoutResult
    k_ESignout_Success_AlreadySignedOut: CMsgServerToGCMatchSignoutResponse.ESignoutResult
    result: CMsgServerToGCMatchSignoutResponse.ESignoutResult
    def __init__(self, result: _Optional[_Union[CMsgServerToGCMatchSignoutResponse.ESignoutResult, str]] = ...) -> None: ...

class CMsgServerToGCReportCheater(_message.Message):
    __slots__ = ["account_id", "cheater_score", "lobby_id", "match_id", "reason", "record_data_only"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CHEATER_SCORE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RECORD_DATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    cheater_score: float
    lobby_id: int
    match_id: int
    reason: str
    record_data_only: bool
    def __init__(self, account_id: _Optional[int] = ..., match_id: _Optional[int] = ..., lobby_id: _Optional[int] = ..., reason: _Optional[str] = ..., record_data_only: bool = ..., cheater_score: _Optional[float] = ...) -> None: ...

class CMsgServerToGCReportCheaterResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgServerToGCTestConnection(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgServerToGCTestConnectionResponse(_message.Message):
    __slots__ = ["lobby_id", "state"]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    lobby_id: int
    state: int
    def __init__(self, state: _Optional[int] = ..., lobby_id: _Optional[int] = ...) -> None: ...

class CMsgServerToGCUpdateLobbyServerState(_message.Message):
    __slots__ = ["lobby_id", "safe_to_abandon", "server_state"]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    SAFE_TO_ABANDON_FIELD_NUMBER: _ClassVar[int]
    SERVER_STATE_FIELD_NUMBER: _ClassVar[int]
    lobby_id: int
    safe_to_abandon: bool
    server_state: _citadel_gcmessages_common_pb2.ELobbyServerState
    def __init__(self, lobby_id: _Optional[int] = ..., server_state: _Optional[_Union[_citadel_gcmessages_common_pb2.ELobbyServerState, str]] = ..., safe_to_abandon: bool = ...) -> None: ...

class CMsgServerToGCUpdateMatchInfo(_message.Message):
    __slots__ = ["kills_team_0", "kills_team_1", "lobby_id", "net_worth_team_0", "net_worth_team_1", "objectives_mask_team0", "objectives_mask_team1", "open_spectator_slots", "spectators"]
    KILLS_TEAM_0_FIELD_NUMBER: _ClassVar[int]
    KILLS_TEAM_1_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    NET_WORTH_TEAM_0_FIELD_NUMBER: _ClassVar[int]
    NET_WORTH_TEAM_1_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_MASK_TEAM0_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_MASK_TEAM1_FIELD_NUMBER: _ClassVar[int]
    OPEN_SPECTATOR_SLOTS_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_FIELD_NUMBER: _ClassVar[int]
    kills_team_0: int
    kills_team_1: int
    lobby_id: int
    net_worth_team_0: int
    net_worth_team_1: int
    objectives_mask_team0: int
    objectives_mask_team1: int
    open_spectator_slots: int
    spectators: int
    def __init__(self, lobby_id: _Optional[int] = ..., kills_team_0: _Optional[int] = ..., kills_team_1: _Optional[int] = ..., net_worth_team_0: _Optional[int] = ..., net_worth_team_1: _Optional[int] = ..., spectators: _Optional[int] = ..., open_spectator_slots: _Optional[int] = ..., objectives_mask_team0: _Optional[int] = ..., objectives_mask_team1: _Optional[int] = ...) -> None: ...

class CMsgServerWelcomeCitadel(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CSOCitadelServerDynamicLobby(_message.Message):
    __slots__ = ["broadcast_active", "left_account_ids", "lobby_id", "spectator_count"]
    BROADCAST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LEFT_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    SPECTATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    broadcast_active: bool
    left_account_ids: _containers.RepeatedScalarFieldContainer[int]
    lobby_id: int
    spectator_count: int
    def __init__(self, lobby_id: _Optional[int] = ..., left_account_ids: _Optional[_Iterable[int]] = ..., broadcast_active: bool = ..., spectator_count: _Optional[int] = ...) -> None: ...

class CSOCitadelServerStaticLobby(_message.Message):
    __slots__ = ["average_badge_team_0", "average_badge_team_1", "bot_difficulty", "broadcast_url", "cheats_enabled", "dev_settings", "duplicate_heroes_enabled", "experimental_gameplay_state", "experimental_heroes_enabled", "extra_messages", "gc_provided_heroes", "is_high_skill_range_parties", "is_restricted_access", "level_name", "lobby_id", "low_pri_pool", "match_start_time", "members", "metadata_salt", "new_player_pool", "region_mode", "replay_salt", "server_steam_id"]
    class EAwardIDs(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class DevSettings(_message.Message):
        __slots__ = ["console_string"]
        CONSOLE_STRING_FIELD_NUMBER: _ClassVar[int]
        console_string: str
        def __init__(self, console_string: _Optional[str] = ...) -> None: ...
    class Member(_message.Message):
        __slots__ = ["account_id", "award_ids", "gc_account_data", "hero_id", "is_comms_restricted", "lane_id", "party_desires_laning_together", "party_index", "persona_name", "platform", "player_slot", "team"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        AWARD_IDS_FIELD_NUMBER: _ClassVar[int]
        GC_ACCOUNT_DATA_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        IS_COMMS_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        LANE_ID_FIELD_NUMBER: _ClassVar[int]
        PARTY_DESIRES_LANING_TOGETHER_FIELD_NUMBER: _ClassVar[int]
        PARTY_INDEX_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        award_ids: _containers.RepeatedScalarFieldContainer[CSOCitadelServerStaticLobby.EAwardIDs]
        gc_account_data: _citadel_gcmessages_common_pb2.CMsgGCAccountData
        hero_id: int
        is_comms_restricted: bool
        lane_id: int
        party_desires_laning_together: bool
        party_index: int
        persona_name: str
        platform: _steammessages_pb2.EGCPlatform
        player_slot: int
        team: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
        def __init__(self, account_id: _Optional[int] = ..., persona_name: _Optional[str] = ..., team: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]] = ..., player_slot: _Optional[int] = ..., hero_id: _Optional[int] = ..., party_index: _Optional[int] = ..., platform: _Optional[_Union[_steammessages_pb2.EGCPlatform, str]] = ..., award_ids: _Optional[_Iterable[_Union[CSOCitadelServerStaticLobby.EAwardIDs, str]]] = ..., is_comms_restricted: bool = ..., lane_id: _Optional[int] = ..., gc_account_data: _Optional[_Union[_citadel_gcmessages_common_pb2.CMsgGCAccountData, _Mapping]] = ..., party_desires_laning_together: bool = ...) -> None: ...
    AVERAGE_BADGE_TEAM_0_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_BADGE_TEAM_1_FIELD_NUMBER: _ClassVar[int]
    BOT_DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_URL_FIELD_NUMBER: _ClassVar[int]
    CHEATS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEV_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_HEROES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_GAMEPLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_HEROES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    GC_PROVIDED_HEROES_FIELD_NUMBER: _ClassVar[int]
    IS_HIGH_SKILL_RANGE_PARTIES_FIELD_NUMBER: _ClassVar[int]
    IS_RESTRICTED_ACCESS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_NAME_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    LOW_PRI_POOL_FIELD_NUMBER: _ClassVar[int]
    MATCH_START_TIME_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_SALT_FIELD_NUMBER: _ClassVar[int]
    NEW_PLAYER_POOL_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SALT_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    average_badge_team_0: int
    average_badge_team_1: int
    bot_difficulty: _citadel_gcmessages_common_pb2.ECitadelBotDifficulty
    broadcast_url: str
    cheats_enabled: bool
    dev_settings: CSOCitadelServerStaticLobby.DevSettings
    duplicate_heroes_enabled: bool
    experimental_gameplay_state: int
    experimental_heroes_enabled: bool
    extra_messages: _containers.RepeatedCompositeFieldContainer[_gcsdk_gcmessages_pb2.CExtraMsgBlock]
    gc_provided_heroes: bool
    is_high_skill_range_parties: bool
    is_restricted_access: bool
    k_eAward_KingPanda: CSOCitadelServerStaticLobby.EAwardIDs
    level_name: str
    lobby_id: int
    low_pri_pool: bool
    match_start_time: int
    members: _containers.RepeatedCompositeFieldContainer[CSOCitadelServerStaticLobby.Member]
    metadata_salt: int
    new_player_pool: bool
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    replay_salt: int
    server_steam_id: int
    def __init__(self, extra_messages: _Optional[_Iterable[_Union[_gcsdk_gcmessages_pb2.CExtraMsgBlock, _Mapping]]] = ..., server_steam_id: _Optional[int] = ..., lobby_id: _Optional[int] = ..., replay_salt: _Optional[int] = ..., level_name: _Optional[str] = ..., members: _Optional[_Iterable[_Union[CSOCitadelServerStaticLobby.Member, _Mapping]]] = ..., dev_settings: _Optional[_Union[CSOCitadelServerStaticLobby.DevSettings, _Mapping]] = ..., gc_provided_heroes: bool = ..., bot_difficulty: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelBotDifficulty, str]] = ..., metadata_salt: _Optional[int] = ..., match_start_time: _Optional[int] = ..., experimental_gameplay_state: _Optional[int] = ..., region_mode: _Optional[_Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]] = ..., broadcast_url: _Optional[str] = ..., new_player_pool: bool = ..., low_pri_pool: bool = ..., is_restricted_access: bool = ..., cheats_enabled: bool = ..., duplicate_heroes_enabled: bool = ..., is_high_skill_range_parties: bool = ..., experimental_heroes_enabled: bool = ..., average_badge_team_0: _Optional[int] = ..., average_badge_team_1: _Optional[int] = ...) -> None: ...

class CServerLobbyData_AutoTest(_message.Message):
    __slots__ = ["max_duration_s"]
    MAX_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    max_duration_s: int
    def __init__(self, max_duration_s: _Optional[int] = ...) -> None: ...

class CServerLobbyData_PlayerInfo(_message.Message):
    __slots__ = ["account_id", "account_stats", "book_info", "mmr_level"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_STATS_FIELD_NUMBER: _ClassVar[int]
    BOOK_INFO_FIELD_NUMBER: _ClassVar[int]
    MMR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    account_stats: _containers.RepeatedCompositeFieldContainer[_citadel_gcmessages_common_pb2.CMsgAccountHeroStats]
    book_info: _containers.RepeatedCompositeFieldContainer[_citadel_gcmessages_common_pb2.CMsgAccountBookStats]
    mmr_level: int
    def __init__(self, account_id: _Optional[int] = ..., account_stats: _Optional[_Iterable[_Union[_citadel_gcmessages_common_pb2.CMsgAccountHeroStats, _Mapping]]] = ..., mmr_level: _Optional[int] = ..., book_info: _Optional[_Iterable[_Union[_citadel_gcmessages_common_pb2.CMsgAccountBookStats, _Mapping]]] = ...) -> None: ...

class CServerLobbyData_PlayerMMR(_message.Message):
    __slots__ = ["players"]
    class Player(_message.Message):
        __slots__ = ["account_id", "hero_mmr", "hero_mmr_with_uncertainty", "player_mmr", "player_uncertainty"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        HERO_MMR_FIELD_NUMBER: _ClassVar[int]
        HERO_MMR_WITH_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
        PLAYER_MMR_FIELD_NUMBER: _ClassVar[int]
        PLAYER_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        hero_mmr: int
        hero_mmr_with_uncertainty: int
        player_mmr: int
        player_uncertainty: int
        def __init__(self, account_id: _Optional[int] = ..., player_mmr: _Optional[int] = ..., player_uncertainty: _Optional[int] = ..., hero_mmr: _Optional[int] = ..., hero_mmr_with_uncertainty: _Optional[int] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CServerLobbyData_PlayerMMR.Player]
    def __init__(self, players: _Optional[_Iterable[_Union[CServerLobbyData_PlayerMMR.Player, _Mapping]]] = ...) -> None: ...

class CServerLobbyData_PostMatchSurvey(_message.Message):
    __slots__ = ["surveys"]
    class PlayerSurvey(_message.Message):
        __slots__ = ["account_id", "question_id"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        question_id: int
        def __init__(self, account_id: _Optional[int] = ..., question_id: _Optional[int] = ...) -> None: ...
    SURVEYS_FIELD_NUMBER: _ClassVar[int]
    surveys: _containers.RepeatedCompositeFieldContainer[CServerLobbyData_PostMatchSurvey.PlayerSurvey]
    def __init__(self, surveys: _Optional[_Iterable[_Union[CServerLobbyData_PostMatchSurvey.PlayerSurvey, _Mapping]]] = ...) -> None: ...

class EGCCitadelServerMessages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EGCServerLobbyData(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EGCServerSignoutData(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
