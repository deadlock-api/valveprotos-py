# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .citadel_gcmessages_common_p2p import CMsgAccountBookStats
from .citadel_gcmessages_common_p2p import CMsgAccountHeroStats
from .citadel_gcmessages_common_p2p import CMsgGCAccountData
from .citadel_gcmessages_common_p2p import ECitadelAccountStatMedal
from .citadel_gcmessages_common_p2p import ECitadelBotDifficulty
from .citadel_gcmessages_common_p2p import ECitadelGameMode
from .citadel_gcmessages_common_p2p import ECitadelLobbyTeam
from .citadel_gcmessages_common_p2p import ECitadelMatchMode
from .citadel_gcmessages_common_p2p import ECitadelRegionMode
from .citadel_gcmessages_common_p2p import ECitadelTeamObjective
from .citadel_gcmessages_common_p2p import ELobbyServerState
from .gcsdk_gcmessages_p2p import CExtraMsgBlock
from .steammessages_p2p import EGCPlatform
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class EGCCitadelServerMessages(IntEnum):
    k_EMsgServerToGCMatchSignoutPermission = 10012
    k_EMsgServerToGCMatchSignoutPermissionResponse = 10013
    k_EMsgServerToGCMatchSignout = 10014
    k_EMsgServerToGCMatchSignoutResponse = 10015
    k_EMsgGCToServerAddSpectator = 10016
    k_EMsgGCToServerAddSpectatorResponse = 10017
    k_EMsgServerToGCIdlePing = 10018
    k_EMsgGCToServerRequestPing = 10019
    k_EMsgGCToServerAllocateForMatch = 10021
    k_EMsgGCToServerAllocateForMatchResponse = 10022
    k_EMsgServerToGCEnterMatchmaking = 10023
    k_EMsgGCToServerCancelAllocateForMatch = 10024
    k_EMsgServerToGCUpdateLobbyServerState = 10025
    k_EMsgServerToGCAbandonMatch = 10026
    k_EMsgServerToGCAbandonMatchResponse = 10027
    k_EMsgServerToGCTestConnection = 10028
    k_EMsgServerToGCTestConnectionResponse = 10029
    k_EMsgGCToServerSetServerConVar = 10039
    k_EMsgGCToServerSetServerConVarResponse = 10040
    k_EMsgServerToGCUpdateMatchInfo = 10041
    k_EMsgServerToGCReportCheater = 10042
    k_EMsgServerToGCReportCheaterResponse = 10043


class EGCServerLobbyData(IntEnum):
    k_EServerLobbyData_PlayerMMR = 1
    k_EServerLobbyData_PlayerInfo = 2
    k_EServerLobbyData_PostMatchSurvey = 3
    k_EServerLobbyData_AutoTest = 4


class EGCServerSignoutData(IntEnum):
    k_EServerSignoutData_Disconnections = 2
    k_EServerSignoutData_AccountStatChanges = 3
    k_EServerSignoutData_DetailedStats = 4
    k_EServerSignoutData_ServerPerfStats = 5
    k_EServerSignoutData_PerfData = 6
    k_EServerSignoutData_PlayerChat = 7
    k_EServerSignoutData_BookRewards = 8
    k_EServerSignoutData_PenalizedPlayers = 9
    k_EServerSignoutData_ReportCheaters = 10
    k_EServerSignoutData_MatchDevStats = 11

class CMsgServerCrashSentinelFile(BaseModel):
    class Player(BaseModel):
        account_id: int = Field(default=0)
        hero_id: int = Field(default=0)

    class GameInfo(BaseModel):
        match_id: int = Field(default=0)
        lobby_id: float = Field(default=0.0)
        server_state: int = Field(default=0)
        players: typing.List["CMsgServerCrashSentinelFile.Player"] = Field(default_factory=list)
        match_mode: ECitadelMatchMode = Field(default=0)
        game_mode: ECitadelGameMode = Field(default=0)
        was_server_shutdown: bool = Field(default=False)

    version: int = Field(default=0)
    server_steam_id: float = Field(default=0.0)
    server_public_ip_addr: float = Field(default=0.0)
    server_port: int = Field(default=0)
    server_cluster_id: int = Field(default=0)
    pid: int = Field(default=0)
    saved_time: int = Field(default=0)
    server_version: int = Field(default=0)
    game_info: "CMsgServerCrashSentinelFile.GameInfo" = Field()
    server_private_ip_addr: int = Field(default=0)
    instance_id: int = Field(default=0)
    server_region_id: int = Field(default=0)

class CServerLobbyData_PlayerMMR(BaseModel):
    class Player(BaseModel):
        account_id: int = Field(default=0)
        player_mmr: int = Field(default=0)
        player_uncertainty: int = Field(default=0)
        hero_mmr: int = Field(default=0)
        hero_mmr_with_uncertainty: int = Field(default=0)

    players: typing.List["CServerLobbyData_PlayerMMR.Player"] = Field(default_factory=list)

class CServerLobbyData_PlayerInfo(BaseModel):
    account_id: int = Field(default=0)
    account_stats: typing.List[CMsgAccountHeroStats] = Field(default_factory=list)
    mmr_level: int = Field(default=0)
    book_info: typing.List[CMsgAccountBookStats] = Field(default_factory=list)

class CServerLobbyData_PostMatchSurvey(BaseModel):
    class PlayerSurvey(BaseModel):
        account_id: int = Field(default=0)
        question_id: int = Field(default=0)

    surveys: typing.List["CServerLobbyData_PostMatchSurvey.PlayerSurvey"] = Field(default_factory=list)

class CServerLobbyData_AutoTest(BaseModel):
    max_duration_s: int = Field(default=0)

class CSOCitadelServerDynamicLobby(BaseModel):
    lobby_id: int = Field(default=0)
    left_account_ids: typing.List[int] = Field(default_factory=list)
    broadcast_active: bool = Field(default=False)
    spectator_count: int = Field(default=0)

class CSOCitadelServerStaticLobby(BaseModel):
    class Member(BaseModel):
        account_id: int = Field(default=0)
        persona_name: str = Field(default="")
        team: ECitadelLobbyTeam = Field(default=0)
        player_slot: int = Field(default=0)
        hero_id: int = Field(default=0)
        party_index: int = Field(default=0)
        platform: EGCPlatform = Field(default=0)
        award_ids: typing.List["CSOCitadelServerStaticLobby.EAwardIDs"] = Field(default_factory=list)
        is_comms_restricted: bool = Field(default=False)
        lane_id: int = Field(default=0)
        gc_account_data: CMsgGCAccountData = Field()
        party_desires_laning_together: bool = Field(default=False)
        hide_holiday_models: bool = Field(default=False)

    class DevSettings(BaseModel):
        console_string: str = Field(default="")

    class EAwardIDs(IntEnum):
        k_eAward_KingPanda = 1

    extra_messages: typing.List[CExtraMsgBlock] = Field(default_factory=list)
    server_steam_id: float = Field(default=0.0)
    lobby_id: int = Field(default=0)
    replay_salt: float = Field(default=0.0)
    level_name: str = Field(default="")
    members: typing.List["CSOCitadelServerStaticLobby.Member"] = Field(default_factory=list)
    dev_settings: "CSOCitadelServerStaticLobby.DevSettings" = Field()
    gc_provided_heroes: bool = Field(default=False)
    bot_difficulty: ECitadelBotDifficulty = Field(default=0)
    metadata_salt: float = Field(default=0.0)
    match_start_time: int = Field(default=0)
    region_mode: ECitadelRegionMode = Field(default=0)
    broadcast_url: str = Field(default="")
    new_player_pool: bool = Field(default=False)
    low_pri_pool: bool = Field(default=False)
    is_restricted_access: bool = Field(default=False)
    cheats_enabled: bool = Field(default=False)
    duplicate_heroes_enabled: bool = Field(default=False)
    is_high_skill_range_parties: bool = Field(default=False)
    experimental_heroes_enabled: bool = Field(default=False)
    average_badge_team_0: int = Field(default=0)
    average_badge_team_1: int = Field(default=0)
    gameplay_experiment: str = Field(default="")

class CMsgServerSignoutData_ServerPerfStats(BaseModel):
    class FrameCounts(BaseModel):
        num_frames: int = Field(default=0)
        longest_run: int = Field(default=0)
        num_runs: int = Field(default=0)

    class PerfSample(BaseModel):
        game_time_s: int = Field(default=0)
        avg_frame: float = Field(default=0.0)
        avg_idle: float = Field(default=0.0)
        total_frames: int = Field(default=0)
        performant_frames: "CMsgServerSignoutData_ServerPerfStats.FrameCounts" = Field()
        long_frames: "CMsgServerSignoutData_ServerPerfStats.FrameCounts" = Field()
        low_idle_frames: "CMsgServerSignoutData_ServerPerfStats.FrameCounts" = Field()
        memory_bytes: int = Field(default=0)
        peak_memory_bytes: int = Field(default=0)

    class MatchPerfSamples(BaseModel):
        long_frame_threshold: float = Field(default=0.0)
        low_idle_threshold: float = Field(default=0.0)
        samples: typing.List["CMsgServerSignoutData_ServerPerfStats.PerfSample"] = Field(default_factory=list)

    peak_memory_bytes: int = Field(default=0)
    end_memory_bytes: int = Field(default=0)
    frame_time_max_micro_s: int = Field(default=0)
    frame_time_95_micro_s: int = Field(default=0)
    frame_time_avg_micro_s: int = Field(default=0)
    frame_idle_time_95_micro_s: int = Field(default=0)
    frame_idle_time_avg_micro_s: int = Field(default=0)
    frame_time_80_micro_s: int = Field(default=0)
    frame_time_99_micro_s: int = Field(default=0)
    perf_samples: "CMsgServerSignoutData_ServerPerfStats.MatchPerfSamples" = Field()

class CMsgServerToGCUpdateMatchInfo(BaseModel):
    lobby_id: int = Field(default=0)
    kills_team_0: int = Field(default=0)
    kills_team_1: int = Field(default=0)
    net_worth_team_0: int = Field(default=0)
    net_worth_team_1: int = Field(default=0)
    spectators: int = Field(default=0)
    open_spectator_slots: int = Field(default=0)
    objectives_mask_team0: int = Field(default=0)
    objectives_mask_team1: int = Field(default=0)

class CMsgServerToGCMatchSignoutPermission(BaseModel):
    signout_start: int = Field(default=0)
    permission_request: int = Field(default=0)
    match_id: int = Field(default=0)
    match_mode: ECitadelMatchMode = Field(default=0)

class CMsgServerToGCMatchSignoutPermissionResponse(BaseModel):
    can_sign_out: bool = Field(default=False)
    retry_time_s: int = Field(default=0)
    requested_data: typing.List[EGCServerSignoutData] = Field(default_factory=list)

class CMsgServerSignoutData_Disconnections(BaseModel):
    class CMsgMatchDisconnection(BaseModel):
        account_id: int = Field(default=0)
        disconnect_time: int = Field(default=0)
        connection_state: int = Field(default=0)
        reason_code: int = Field(default=0)
        reconnect_delay: int = Field(default=0)
        match_disconnect_time: int = Field(default=0)
        match_reconnect_delay: int = Field(default=0)

    disconnections: typing.List["CMsgServerSignoutData_Disconnections.CMsgMatchDisconnection"] = Field(default_factory=list)

class CMsgServerSignoutData_MatchDevStats(BaseModel):
    class PlayerSlot(BaseModel):
        player_slot: int = Field(default=0)

    players: typing.List["CMsgServerSignoutData_MatchDevStats.PlayerSlot"] = Field(default_factory=list)

class CMsgServerSignoutData_DetailedStats(BaseModel):
    class Position(BaseModel):
        x: float = Field(default=0.0)
        y: float = Field(default=0.0)
        z: float = Field(default=0.0)

    class TimeSample(BaseModel):
        class Stats(BaseModel):
            net_worth: int = Field(default=0)
            kills: int = Field(default=0)
            deaths: int = Field(default=0)
            assists: int = Field(default=0)
            possible_creeps: int = Field(default=0)
            creep_kills: int = Field(default=0)
            neutral_kills: int = Field(default=0)
            creep_damage: int = Field(default=0)
            neutral_damage: int = Field(default=0)
            boss_damage: int = Field(default=0)
            player_damage: int = Field(default=0)
            denies: int = Field(default=0)
            player_healing: int = Field(default=0)
            ability_points: int = Field(default=0)
            self_healing: int = Field(default=0)
            player_damage_taken: int = Field(default=0)
            max_health: int = Field(default=0)
            weapon_power: int = Field(default=0)
            tech_power: int = Field(default=0)
            shots_hit: int = Field(default=0)
            shots_missed: int = Field(default=0)
            damage_absorbed: int = Field(default=0)
            absorption_provided: int = Field(default=0)
            heal_prevented: int = Field(default=0)
            heal_lost: int = Field(default=0)

        class GoldStats(BaseModel):
            player: int = Field(default=0)
            player_orb: int = Field(default=0)
            lane_creep_orb: int = Field(default=0)
            neutral_creep_orb: int = Field(default=0)
            boss: int = Field(default=0)
            boss_orb: int = Field(default=0)
            treasure: int = Field(default=0)
            denied: int = Field(default=0)
            death_loss: int = Field(default=0)
            lane_creep: int = Field(default=0)
            neutral_creep: int = Field(default=0)
            team_bonus: int = Field(default=0)

        match_time_s: int = Field(default=0)
        stats: Stats = Field()
        gold_stats: GoldStats = Field()

    class Objective(BaseModel):
        destroyed_time_s: int = Field(default=0)
        creep_damage: int = Field(default=0)
        creep_damage_mitigated: int = Field(default=0)
        player_damage: int = Field(default=0)
        player_damage_mitigated: int = Field(default=0)
        first_damage_time_s: int = Field(default=0)
        team_objective_id: ECitadelTeamObjective = Field(default=0)
        team: ECitadelLobbyTeam = Field(default=0)

    class MidBoss(BaseModel):
        team_killed: ECitadelLobbyTeam = Field(default=0)
        team_claimed: ECitadelLobbyTeam = Field(default=0)
        destroyed_time_s: int = Field(default=0)

    class Player(BaseModel):
        player_slot: int = Field(default=0)
        time_samples: typing.List["CMsgServerSignoutData_DetailedStats.TimeSample"] = Field(default_factory=list)

    player_stats: typing.List["CMsgServerSignoutData_DetailedStats.Player"] = Field(default_factory=list)
    objectives: typing.List["CMsgServerSignoutData_DetailedStats.Objective"] = Field(default_factory=list)
    mid_boss: typing.List["CMsgServerSignoutData_DetailedStats.MidBoss"] = Field(default_factory=list)

class CMsgServerSignoutData_PerfData(BaseModel):
    average_frame_time: typing.List[float] = Field(default_factory=list)
    max_frame_time: typing.List[float] = Field(default_factory=list)
    server_average_frame_time: float = Field(default=0.0)
    server_max_frame_time: float = Field(default=0.0)
    average_compute_time: typing.List[float] = Field(default_factory=list)
    max_compute_time: typing.List[float] = Field(default_factory=list)
    average_client_tick_time: typing.List[float] = Field(default_factory=list)
    max_client_tick_time: typing.List[float] = Field(default_factory=list)
    average_client_simulate_time: typing.List[float] = Field(default_factory=list)
    max_client_simulate_time: typing.List[float] = Field(default_factory=list)
    average_output_time: typing.List[float] = Field(default_factory=list)
    max_output_time: typing.List[float] = Field(default_factory=list)
    average_wait_for_rendering_to_complete_time: typing.List[float] = Field(default_factory=list)
    max_wait_for_rendering_to_complete_time: typing.List[float] = Field(default_factory=list)
    average_swap_time: typing.List[float] = Field(default_factory=list)
    max_swap_time: typing.List[float] = Field(default_factory=list)
    average_frame_update_time: typing.List[float] = Field(default_factory=list)
    max_frame_update_time: typing.List[float] = Field(default_factory=list)
    average_idle_time: typing.List[float] = Field(default_factory=list)
    max_idle_time: typing.List[float] = Field(default_factory=list)
    average_input_processing_time: typing.List[float] = Field(default_factory=list)
    max_input_processing_time: typing.List[float] = Field(default_factory=list)

class CMsgServerSignoutData_BookRewards(BaseModel):
    class BookReward(BaseModel):
        book_id: int = Field(default=0)
        xp_reward: int = Field(default=0)

    class AccountRewards(BaseModel):
        account_id: int = Field(default=0)
        book_reward: "CMsgServerSignoutData_BookRewards.BookReward" = Field()

    account_rewards: typing.List["CMsgServerSignoutData_BookRewards.AccountRewards"] = Field(default_factory=list)

class CMsgServerSignoutData_AccountStatChanges(BaseModel):
    class Stat(BaseModel):
        hero_id: int = Field(default=0)
        stat_id: int = Field(default=0)
        value: int = Field(default=0)
        medal: ECitadelAccountStatMedal = Field(default=0)

    class AccountStats(BaseModel):
        account_id: int = Field(default=0)
        stats: typing.List["CMsgServerSignoutData_AccountStatChanges.Stat"] = Field(default_factory=list)

    account_stats: typing.List["CMsgServerSignoutData_AccountStatChanges.AccountStats"] = Field(default_factory=list)

class CMsgServerSignoutData_PlayerChat(BaseModel):
    class ChatLine(BaseModel):
        player_slot: int = Field(default=0)
        game_time: float = Field(default=0.0)
        team_only: bool = Field(default=False)
        chat_line: str = Field(default="")

    chat_lines: typing.List["CMsgServerSignoutData_PlayerChat.ChatLine"] = Field(default_factory=list)

class CMsgServerSignoutData_PenalizedPlayers(BaseModel):
    class Penalty(BaseModel):
        account_id: int = Field(default=0)
        reason: "CMsgServerSignoutData_PenalizedPlayers.EPenaltyReason" = Field(default=0)
        match_time_s: int = Field(default=0)
        time_stamp: int = Field(default=0)

    class EPenaltyReason(IntEnum):
        k_EPenaltyReason_Abandon = 0
        k_EPenaltyReason_DisconnectedTooLong = 1
        k_EPenaltyReason_AFK = 2

    penalized_players: typing.List["CMsgServerSignoutData_PenalizedPlayers.Penalty"] = Field(default_factory=list)

class CMsgMatchData(BaseModel):
    class PlayerItem(BaseModel):
        item_id: int = Field(default=0)
        game_time_s: int = Field(default=0)
        upgrade_id: int = Field(default=0)
        sold_time_s: int = Field(default=0)
        flags: int = Field(default=0)
        imbued_ability_id: int = Field(default=0)

    class PlayerInfo(BaseModel):
        account_id: int = Field(default=0)
        team: ECitadelLobbyTeam = Field(default=0)
        player_slot: int = Field(default=0)
        hero_mmr_with_uncertainty: int = Field(default=0)
        player_mmr: int = Field(default=0)
        player_uncertainty: int = Field(default=0)
        hero_id: int = Field(default=0)
        kills: int = Field(default=0)
        deaths: int = Field(default=0)
        net_worth: int = Field(default=0)
        assists: int = Field(default=0)
        hero_mmr: int = Field(default=0)
        items: typing.List["CMsgMatchData.PlayerItem"] = Field(default_factory=list)
        gpm_10min: int = Field(default=0)
        gpm_15min: int = Field(default=0)
        gpm_20min: int = Field(default=0)
        gpm_25min: int = Field(default=0)
        gpm_30min: int = Field(default=0)
        gpm_35min: int = Field(default=0)
        gpm_end: int = Field(default=0)
        last_hits: int = Field(default=0)
        denies: int = Field(default=0)
        ability_points: int = Field(default=0)
        level: int = Field(default=0)
        assigned_lane: int = Field(default=0)
        party_index: int = Field(default=0)
        platform: EGCPlatform = Field(default=0)
        ability_damage: int = Field(default=0)
        bullet_damage: int = Field(default=0)
        hero_bullets_hit: int = Field(default=0)
        hero_bullets_hit_crit: int = Field(default=0)
        player_healing: int = Field(default=0)
        hero_bullets_fired: int = Field(default=0)
        hero_incoming_bullets_fired: int = Field(default=0)
        hero_incoming_bullets_hit: int = Field(default=0)
        hero_incoming_bullets_crit: int = Field(default=0)
        time_dead_s: int = Field(default=0)
        player_bullet_damage: int = Field(default=0)
        player_ability_damage: int = Field(default=0)
        player_melee_damage: int = Field(default=0)
        abandon_match_time_s: int = Field(default=0)
        abandon_time_stamp: int = Field(default=0)
        trooper_kill_excluded: int = Field(default=0)
        hero_bullets_lucky_shots: int = Field(default=0)
        hero_build_id: int = Field(default=0)
        objective_damage: int = Field(default=0)

    class EEndReason(IntEnum):
        k_EEndReason_TeamWin = 0
        k_EEndReason_AllAbandoned = 2
        k_EEndReason_NetworkIssues = 3
        k_EEndReason_MatchLength = 4
        k_EEndReason_PlayerNeverConnected = 5

    match_duration_s: int = Field(default=0)
    end_reason: "CMsgMatchData.EEndReason" = Field(default=0)
    winning_team: ECitadelLobbyTeam = Field(default=0)
    players: typing.List["CMsgMatchData.PlayerInfo"] = Field(default_factory=list)
    objectives_mask_legacy: int = Field(default=0)
    server_version: int = Field(default=0)
    game_mode: ECitadelGameMode = Field(default=0)
    match_mode: ECitadelMatchMode = Field(default=0)
    objectives_mask_team0: int = Field(default=0)
    objectives_mask_team1: int = Field(default=0)
    match_end_time: int = Field(default=0)
    stomp_score: float = Field(default=0.0)
    safe_to_abandon: bool = Field(default=False)
    team_abandon: bool = Field(default=False)
    new_player_pool: bool = Field(default=False)
    low_pri_pool: bool = Field(default=False)
    not_scored: bool = Field(default=False)

class CMsgServerToGCMatchSignout(BaseModel):
    additional_data: typing.List[CExtraMsgBlock] = Field(default_factory=list)
    signout_attempt: int = Field(default=0)
    lobby_id: int = Field(default=0)
    match_id: int = Field(default=0)
    cluster_id: int = Field(default=0)
    match_data: CMsgMatchData = Field()

class CMsgServerToGCMatchSignoutResponse(BaseModel):
    class ESignoutResult(IntEnum):
        k_ESignout_Failed_Retry = 1
        k_ESignout_Failed_NoRetry = 2
        k_ESignout_Failed_InFlight = 3
        k_ESignout_Success = 4
        k_ESignout_Success_AlreadySignedOut = 5

    result: "CMsgServerToGCMatchSignoutResponse.ESignoutResult" = Field(default=0)

class CMsgServerWelcomeCitadel(BaseModel):
    pass

class CMsgServerToGCIdlePing(BaseModel):
    server_version: int = Field(default=0)

class CMsgGCToServerRequestPing(BaseModel):
    pass

class CMsgGCToServerAllocateForMatch(BaseModel):
    match_id: int = Field(default=0)

class CMsgGCToServerAllocateForMatchResponse(BaseModel):
    success: bool = Field(default=False)

class CMsgServerToGCEnterMatchmaking(BaseModel):
    server_version: int = Field(default=0)
    search_key: str = Field(default="")
    region_id: int = Field(default=0)
    cluster_id: int = Field(default=0)
    server_public_ip: int = Field(default=0)
    server_private_ip: int = Field(default=0)
    server_port: int = Field(default=0)
    sdr_address: bytes = Field(default=b"")
    replay_group_id: int = Field(default=0)

class CMsgGCToServerCancelAllocateForMatch(BaseModel):
    match_id: int = Field(default=0)

class CMsgServerToGCUpdateLobbyServerState(BaseModel):
    lobby_id: int = Field(default=0)
    server_state: ELobbyServerState = Field(default=0)
    safe_to_abandon: bool = Field(default=False)

class CMsgServerToGCAbandonMatch(BaseModel):
    class Player(BaseModel):
        account_id: int = Field(default=0)
        additional_data: int = Field(default=0)
        hero_id: int = Field(default=0)

    class EReason(IntEnum):
        eReason_ServerCrash = 1
        eReason_ClientsFailedToConnect = 2

    server_steam_id: float = Field(default=0.0)
    lobby_id: float = Field(default=0.0)
    cluster_id: int = Field(default=0)
    reason_code: "CMsgServerToGCAbandonMatch.EReason" = Field(default=0)
    additional_data: int = Field(default=0)
    match_id: int = Field(default=0)
    players: typing.List["CMsgServerToGCAbandonMatch.Player"] = Field(default_factory=list)
    public_ip_address: float = Field(default=0.0)
    port: int = Field(default=0)
    server_version: int = Field(default=0)
    pid: int = Field(default=0)
    instance_id: int = Field(default=0)
    private_ip_address: int = Field(default=0)
    match_mode: ECitadelMatchMode = Field(default=0)
    game_mode: ECitadelGameMode = Field(default=0)
    was_server_shutdown: bool = Field(default=False)
    region_id: int = Field(default=0)

class CMsgServerToGCAbandonMatchResponse(BaseModel):
    pass

class CMsgServerToGCTestConnection(BaseModel):
    pass

class CMsgServerToGCTestConnectionResponse(BaseModel):
    state: int = Field(default=0)
    lobby_id: int = Field(default=0)

class CMsgGCToServerSetServerConVar(BaseModel):
    convar_name: str = Field(default="")
    convar_value: str = Field(default="")

class CMsgGCToServerSetServerConVarResponse(BaseModel):
    success: bool = Field(default=False)

class CMsgGCToServerAddSpectator(BaseModel):
    lobby_id: int = Field(default=0)
    account_id: int = Field(default=0)
    account_to_spectate: int = Field(default=0)

class CMsgGCToServerAddSpectatorResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eServerFull = 2

    result: "CMsgGCToServerAddSpectatorResponse.EResponse" = Field(default=0)
    requesting_account_id: int = Field(default=0)

class CMsgServerToGCReportCheater(BaseModel):
    account_id: int = Field(default=0)
    match_id: int = Field(default=0)
    lobby_id: float = Field(default=0.0)
    reason: str = Field(default="")
    record_data_only: bool = Field(default=False)
    cheater_score: float = Field(default=0.0)

class CMsgServerToGCReportCheaterResponse(BaseModel):
    success: bool = Field(default=False)
