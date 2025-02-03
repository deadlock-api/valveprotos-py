# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .gcsdk_gcmessages_p2p import CExtraMsgBlock
from .steammessages_p2p import EGCPlatform
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class CMsgLaneColor(IntEnum):
    k_ELaneColor_Invalid = 0
    k_ELaneColor_Yellow = 1
    k_ELaneColor_Green = 3
    k_ELaneColor_Blue = 4
    k_ELaneColor_Purple = 6


class EGCCitadelCommonMessages(IntEnum):
    k_EMsgAnyToGCReportAsserts = 7000
    k_EMsgAnyToGCReportAssertsResponse = 7001


class ECitadelMatchMode(IntEnum):
    k_ECitadelMatchMode_Invalid = 0
    k_ECitadelMatchMode_Unranked = 1
    k_ECitadelMatchMode_PrivateLobby = 2
    k_ECitadelMatchMode_CoopBot = 3
    k_ECitadelMatchMode_Ranked = 4
    k_ECitadelMatchMode_ServerTest = 5
    k_ECitadelMatchMode_Tutorial = 6
    k_ECitadelMatchMode_HeroLabs = 7


class ECitadelLobbyTeam(IntEnum):
    k_ECitadelLobbyTeam_Team0 = 0
    k_ECitadelLobbyTeam_Team1 = 1
    k_ECitadelLobbyTeam_Spectator = 16


class ECitadelAccountStatMedal(IntEnum):
    k_eNone = 0
    k_eBronze = 1
    k_eSilver = 2
    k_eGold = 3


class ECitadelMMPreference(IntEnum):
    k_ECitadelMMPreference_Invalid = 0
    k_ECitadelMMPreference_Casual = 1
    k_ECitadelMMPreference_Serious = 2


class ECitadelObjective(IntEnum):
    k_eCitadelObjective_Team0_Core = 0
    k_eCitadelObjective_Team0_Tier1_Lane1 = 1
    k_eCitadelObjective_Team0_Tier1_Lane2 = 2
    k_eCitadelObjective_Team0_Tier1_Lane3 = 3
    k_eCitadelObjective_Team0_Tier1_Lane4 = 4
    k_eCitadelObjective_Team0_Tier2_Lane1 = 5
    k_eCitadelObjective_Team0_Tier2_Lane2 = 6
    k_eCitadelObjective_Team0_Tier2_Lane3 = 7
    k_eCitadelObjective_Team0_Tier2_Lane4 = 8
    k_eCitadelObjective_Team0_Titan = 9
    k_eCitadelObjective_Team0_TitanShieldGenerator_1 = 10
    k_eCitadelObjective_Team0_TitanShieldGenerator_2 = 11
    k_eCitadelObjective_Team0_BarrackBoss_Lane1 = 12
    k_eCitadelObjective_Team0_BarrackBoss_Lane2 = 13
    k_eCitadelObjective_Team0_BarrackBoss_Lane3 = 14
    k_eCitadelObjective_Team0_BarrackBoss_Lane4 = 15
    k_eCitadelObjective_Team1_Core = 16
    k_eCitadelObjective_Team1_Tier1_Lane1 = 17
    k_eCitadelObjective_Team1_Tier1_Lane2 = 18
    k_eCitadelObjective_Team1_Tier1_Lane3 = 19
    k_eCitadelObjective_Team1_Tier1_Lane4 = 20
    k_eCitadelObjective_Team1_Tier2_Lane1 = 21
    k_eCitadelObjective_Team1_Tier2_Lane2 = 22
    k_eCitadelObjective_Team1_Tier2_Lane3 = 23
    k_eCitadelObjective_Team1_Tier2_Lane4 = 24
    k_eCitadelObjective_Team1_Titan = 25
    k_eCitadelObjective_Team1_TitanShieldGenerator_1 = 26
    k_eCitadelObjective_Team1_TitanShieldGenerator_2 = 27
    k_eCitadelObjective_Team1_BarrackBoss_Lane1 = 28
    k_eCitadelObjective_Team1_BarrackBoss_Lane2 = 29
    k_eCitadelObjective_Team1_BarrackBoss_Lane3 = 30
    k_eCitadelObjective_Team1_BarrackBoss_Lane4 = 31
    k_eCitadelObjective_Neutral_Mid = 32


class ECitadelTeamObjective(IntEnum):
    k_eCitadelTeamObjective_Core = 0
    k_eCitadelTeamObjective_Tier1_Lane1 = 1
    k_eCitadelTeamObjective_Tier1_Lane2 = 2
    k_eCitadelTeamObjective_Tier1_Lane3 = 3
    k_eCitadelTeamObjective_Tier1_Lane4 = 4
    k_eCitadelTeamObjective_Tier2_Lane1 = 5
    k_eCitadelTeamObjective_Tier2_Lane2 = 6
    k_eCitadelTeamObjective_Tier2_Lane3 = 7
    k_eCitadelTeamObjective_Tier2_Lane4 = 8
    k_eCitadelTeamObjective_Titan = 9
    k_eCitadelTeamObjective_TitanShieldGenerator_1 = 10
    k_eCitadelTeamObjective_TitanShieldGenerator_2 = 11
    k_eCitadelTeamObjective_BarrackBoss_Lane1 = 12
    k_eCitadelTeamObjective_BarrackBoss_Lane2 = 13
    k_eCitadelTeamObjective_BarrackBoss_Lane3 = 14
    k_eCitadelTeamObjective_BarrackBoss_Lane4 = 15


class ECitadelBotDifficulty(IntEnum):
    k_ECitadelBotDifficulty_None = 0
    k_ECitadelBotDifficulty_Easy = 1
    k_ECitadelBotDifficulty_Medium = 2
    k_ECitadelBotDifficulty_Hard = 3
    k_ECitadelBotDifficulty_Nightmare = 4
    k_ECitadelBotDifficulty_Guided = 5


class ECitadelRegionMode(IntEnum):
    k_ECitadelRegionMode_ROW = 0
    k_ECitadelRegionMode_Europe = 1
    k_ECitadelRegionMode_SEAsia = 2
    k_ECitadelRegionMode_SAmerica = 3
    k_ECitadelRegionMode_Russia = 4
    k_ECitadelRegionMode_Oceania = 5


class ECitadelLeaderboardRegion(IntEnum):
    k_ECitadelLeaderboardRegion_None = 0
    k_ECitadelLeaderboardRegion_Europe = 1
    k_ECitadelLeaderboardRegion_Asia = 2
    k_ECitadelLeaderboardRegion_NAmerica = 3
    k_ECitadelLeaderboardRegion_SAmerica = 4
    k_ECitadelLeaderboardRegion_Oceania = 5


class ECitadelGameMode(IntEnum):
    k_ECitadelGameMode_Invalid = 0
    k_ECitadelGameMode_Normal = 1
    k_ECitadelGameMode_1v1Test = 2
    k_ECitadelGameMode_Sandbox = 3


class ELobbyServerState(IntEnum):
    k_eLobbyServerState_Assign = 0
    k_eLobbyServerState_InGame = 1
    k_eLobbyServerState_PostMatch = 2
    k_eLobbyServerState_SignedOut = 3
    k_eLobbyServerState_Abandoned = 4


class EBannedFeature(IntEnum):
    k_eBannedFeature_Invalid = 0
    k_eBannedFeature_LowPriorityMatchmaking = 1
    k_eBannedFeature_CommsRestricted = 2
    k_eBannedFeature_ReportingDisabled = 3


class EFeatureBanReason(IntEnum):
    k_eFeatureBanReason_Invalid = 0
    k_eFeatureBanReason_DevCommand = 1
    k_eFeatureBanReason_PlayerReports = 2
    k_eFeatureBanReason_MatchAbandons = 3
    k_eFeatureBanReason_ExcessivePlayerReports = 4

class CSOCitadelLobby(BaseModel):
    lobby_id: int = Field(default=0)
    match_id: int = Field(default=0)
    match_mode: ECitadelMatchMode = Field(default=0)
    game_mode: ECitadelGameMode = Field(default=0)
    compatibility_version: int = Field(default=0)
    extra_messages: typing.List[CExtraMsgBlock] = Field(default_factory=list)
    server_steam_id: float = Field(default=0.0)
    server_state: ELobbyServerState = Field(default=0)
    udp_connect_ip: int = Field(default=0)
    udp_connect_port: int = Field(default=0)
    sdr_address: bytes = Field(default=b"")
    server_version: int = Field(default=0)
    safe_to_abandon: bool = Field(default=False)
    match_punishes_abandons: bool = Field(default=False)

class CLobbyData_PostMatchSurvey(BaseModel):
    class PlayerSurvey(BaseModel):
        account_id: int = Field(default=0)
        question_id: int = Field(default=0)

    surveys: typing.List["CLobbyData_PostMatchSurvey.PlayerSurvey"] = Field(default_factory=list)

class CMsgHeroSelectionMatchInfo(BaseModel):
    class Hero(BaseModel):
        hero_id: int = Field(default=0)
        priority: int = Field(default=0)

    hero_selections: typing.List["CMsgHeroSelectionMatchInfo.Hero"] = Field(default_factory=list)

class CMsgStartFindingMatchInfo(BaseModel):
    server_search_key: str = Field(default="")
    server_command_string: str = Field(default="")
    match_mode: ECitadelMatchMode = Field(default=0)
    game_mode: ECitadelGameMode = Field(default=0)
    bot_difficulty: ECitadelBotDifficulty = Field(default=0)
    region_mode: ECitadelRegionMode = Field(default=0)
    prefer_solo_only: bool = Field(default=False)
    mm_preference: ECitadelMMPreference = Field(default=0)

class CMsgAnyToGCReportAsserts(BaseModel):
    class TrackedAssert(BaseModel):
        filename: str = Field(default="")
        line_number: int = Field(default=0)
        sample_msg: str = Field(default="")
        sample_stack: str = Field(default="")
        times_fired: int = Field(default=0)
        function_name: str = Field(default="")
        condition: str = Field(default="")
        total_times_fired: int = Field(default=0)

    version: int = Field(default=0)
    asserts: typing.List["CMsgAnyToGCReportAsserts.TrackedAssert"] = Field(default_factory=list)

class CMsgAnyToGCReportAssertsResponse(BaseModel):
    success: bool = Field(default=False)

class CMsgRegionPingTimesClient(BaseModel):
    data_center_codes: typing.List[float] = Field(default_factory=list)
    ping_times: typing.List[int] = Field(default_factory=list)

class CSOCitadelParty(BaseModel):
    class PrivateLobbySlot(BaseModel):
        slot_id: int = Field(default=0)
        player_account_id: int = Field(default=0)

    class ServerRegion(BaseModel):
        region_id: int = Field(default=0)

    class PrivateLobbySettings(BaseModel):
        min_roster_size: int = Field(default=0)
        match_slots: typing.List["CSOCitadelParty.PrivateLobbySlot"] = Field(default_factory=list)
        randomize_lanes: bool = Field(default=False)
        server_region: int = Field(default=0)
        is_publicly_visible: bool = Field(default=False)
        cheats_enabled: bool = Field(default=False)
        available_regions: typing.List["CSOCitadelParty.ServerRegion"] = Field(default_factory=list)
        duplicate_heroes_enabled: bool = Field(default=False)
        experimental_heroes_enabled: bool = Field(default=False)

    class Member(BaseModel):
        account_id: int = Field(default=0)
        persona_name: str = Field(default="")
        rights_flags: int = Field(default=0)
        is_ready: bool = Field(default=False)
        player_type: "CSOCitadelParty.EPlayerType" = Field(default=0)
        compatibility_version: int = Field(default=0)
        platform: EGCPlatform = Field(default=0)
        team: int = Field(default=0)
        hero_roster: CMsgHeroSelectionMatchInfo = Field()
        permissions: int = Field(default=0)
        new_player_progress: int = Field(default=0)
        owned_heroes: typing.List[int] = Field(default_factory=list)

    class LeftMember(BaseModel):
        account_id: int = Field(default=0)
        rights_flags: int = Field(default=0)
        player_type: "CSOCitadelParty.EPlayerType" = Field(default=0)

    class Invite(BaseModel):
        account_id: int = Field(default=0)
        persona_name: str = Field(default="")
        invited_by: int = Field(default=0)

    class EMemberRights(IntEnum):
        k_eMemberRights_Admin = 1
        k_eMemberRights_Creator = 2

    class EPlayerType(IntEnum):
        k_ePlayerType_Player = 0
        k_ePlayerType_Spectator = 1

    class EChatMode(IntEnum):
        k_eNone = 0
        k_ePartyChat = 1
        k_eTeamChat = 2

    party_id: int = Field(default=0)
    members: typing.List["CSOCitadelParty.Member"] = Field(default_factory=list)
    invites: typing.List["CSOCitadelParty.Invite"] = Field(default_factory=list)
    dev_server_command: str = Field(default="")
    left_members: typing.List["CSOCitadelParty.LeftMember"] = Field(default_factory=list)
    join_code: int = Field(default=0)
    bot_difficulty: ECitadelBotDifficulty = Field(default=0)
    match_mode: ECitadelMatchMode = Field(default=0)
    game_mode: ECitadelGameMode = Field(default=0)
    match_making_start_time: int = Field(default=0)
    server_search_key: str = Field(default="")
    is_high_skill_range_party: bool = Field(default=False)
    chat_mode: "CSOCitadelParty.EChatMode" = Field(default=0)
    region_mode: ECitadelRegionMode = Field(default=0)
    is_private_lobby: bool = Field(default=False)
    private_lobby_settings: "CSOCitadelParty.PrivateLobbySettings" = Field()
    desires_laning_together: bool = Field(default=False)
    mm_preference: ECitadelMMPreference = Field(default=0)

class CMsgMatchPlayerPathsData(BaseModel):
    class Path(BaseModel):
        player_slot: int = Field(default=0)
        x_min: float = Field(default=0.0)
        y_min: float = Field(default=0.0)
        x_max: float = Field(default=0.0)
        y_max: float = Field(default=0.0)
        x_pos: typing.List[int] = Field(default_factory=list)
        y_pos: typing.List[int] = Field(default_factory=list)
        alive: typing.List[bool] = Field(default_factory=list)
        health: typing.List[int] = Field(default_factory=list)

    version: int = Field(default=0)
    interval_s: float = Field(default=0.0)
    x_resolution: int = Field(default=0)
    y_resolution: int = Field(default=0)
    paths: typing.List["CMsgMatchPlayerPathsData.Path"] = Field(default_factory=list)

class CMsgMatchPlayerDamageMatrix(BaseModel):
    class DamageToPlayer(BaseModel):
        target_player_slot: int = Field(default=0)
        damage: typing.List[int] = Field(default_factory=list)

    class DamageSource(BaseModel):
        damage_to_players: typing.List["CMsgMatchPlayerDamageMatrix.DamageToPlayer"] = Field(default_factory=list)
        source_details_index: int = Field(default=0)

    class DamageDealer(BaseModel):
        dealer_player_slot: int = Field(default=0)
        damage_sources: typing.List["CMsgMatchPlayerDamageMatrix.DamageSource"] = Field(default_factory=list)

    class SourceDetails(BaseModel):
        stat_type: typing.List["CMsgMatchPlayerDamageMatrix.EStatType"] = Field(default_factory=list)
        source_name: typing.List[str] = Field(default_factory=list)

    class EStatType(IntEnum):
        k_eType_Damage = 0
        k_eType_Healing = 1
        k_eType_HealPrevented = 2
        k_eType_Mitigated = 3
        k_eType_LethalDamage = 4

    damage_dealers: typing.List["CMsgMatchPlayerDamageMatrix.DamageDealer"] = Field(default_factory=list)
    sample_time_s: typing.List[int] = Field(default_factory=list)
    source_details: "CMsgMatchPlayerDamageMatrix.SourceDetails" = Field()

class CMsgMatchMetaDataContents(BaseModel):
    class Position(BaseModel):
        x: float = Field(default=0.0)
        y: float = Field(default=0.0)
        z: float = Field(default=0.0)

    class Deaths(BaseModel):
        game_time_s: int = Field(default=0)
        killer_player_slot: int = Field(default=0)
        death_pos: "CMsgMatchMetaDataContents.Position" = Field()
        killer_pos: "CMsgMatchMetaDataContents.Position" = Field()
        death_duration_s: int = Field(default=0)

    class Items(BaseModel):
        game_time_s: int = Field(default=0)
        item_id: int = Field(default=0)
        upgrade_id: int = Field(default=0)
        sold_time_s: int = Field(default=0)
        flags: int = Field(default=0)
        imbued_ability_id: int = Field(default=0)

    class Ping(BaseModel):
        ping_type: int = Field(default=0)
        ping_data: int = Field(default=0)
        game_time_s: int = Field(default=0)

    class GoldSource(BaseModel):
        source: "CMsgMatchMetaDataContents.EGoldSource" = Field(default=0)
        kills: int = Field(default=0)
        damage: int = Field(default=0)
        gold: int = Field(default=0)
        gold_orbs: int = Field(default=0)

    class CustomUserStatInfo(BaseModel):
        name: str = Field(default="")
        id: int = Field(default=0)

    class CustomUserStat(BaseModel):
        value: int = Field(default=0)
        id: int = Field(default=0)

    class PlayerStats(BaseModel):
        time_stamp_s: int = Field(default=0)
        net_worth: int = Field(default=0)
        gold_player: int = Field(default=0)
        gold_player_orbs: int = Field(default=0)
        gold_lane_creep_orbs: int = Field(default=0)
        gold_neutral_creep_orbs: int = Field(default=0)
        gold_boss: int = Field(default=0)
        gold_boss_orb: int = Field(default=0)
        gold_treasure: int = Field(default=0)
        gold_denied: int = Field(default=0)
        gold_death_loss: int = Field(default=0)
        gold_lane_creep: int = Field(default=0)
        gold_neutral_creep: int = Field(default=0)
        kills: int = Field(default=0)
        deaths: int = Field(default=0)
        assists: int = Field(default=0)
        creep_kills: int = Field(default=0)
        neutral_kills: int = Field(default=0)
        possible_creeps: int = Field(default=0)
        creep_damage: int = Field(default=0)
        player_damage: int = Field(default=0)
        neutral_damage: int = Field(default=0)
        boss_damage: int = Field(default=0)
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
        hero_bullets_hit: int = Field(default=0)
        hero_bullets_hit_crit: int = Field(default=0)
        heal_prevented: int = Field(default=0)
        heal_lost: int = Field(default=0)
        gold_sources: typing.List["CMsgMatchMetaDataContents.GoldSource"] = Field(default_factory=list)
        custom_user_stats: typing.List["CMsgMatchMetaDataContents.CustomUserStat"] = Field(default_factory=list)
        damage_mitigated: int = Field(default=0)
        level: int = Field(default=0)

    class AbilityStat(BaseModel):
        ability_id: int = Field(default=0)
        ability_value: int = Field(default=0)

    class BookReward(BaseModel):
        book_id: int = Field(default=0)
        xp_amount: int = Field(default=0)
        starting_xp: int = Field(default=0)

    class Players(BaseModel):
        account_id: int = Field(default=0)
        player_slot: int = Field(default=0)
        death_details: typing.List["CMsgMatchMetaDataContents.Deaths"] = Field(default_factory=list)
        items: typing.List["CMsgMatchMetaDataContents.Items"] = Field(default_factory=list)
        stats: typing.List["CMsgMatchMetaDataContents.PlayerStats"] = Field(default_factory=list)
        team: ECitadelLobbyTeam = Field(default=0)
        kills: int = Field(default=0)
        deaths: int = Field(default=0)
        assists: int = Field(default=0)
        net_worth: int = Field(default=0)
        hero_id: int = Field(default=0)
        last_hits: int = Field(default=0)
        denies: int = Field(default=0)
        ability_points: int = Field(default=0)
        party: int = Field(default=0)
        assigned_lane: int = Field(default=0)
        level: int = Field(default=0)
        pings: typing.List["CMsgMatchMetaDataContents.Ping"] = Field(default_factory=list)
        ability_stats: typing.List["CMsgMatchMetaDataContents.AbilityStat"] = Field(default_factory=list)
        stats_type_stat: typing.List[float] = Field(default_factory=list)
        book_rewards: typing.List["CMsgMatchMetaDataContents.BookReward"] = Field(default_factory=list)
        abandon_match_time_s: int = Field(default=0)

    class Objective(BaseModel):
        legacy_objective_id: ECitadelObjective = Field(default=0)
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

    class Pause(BaseModel):
        game_time_s: int = Field(default=0)
        pause_duration_s: int = Field(default=0)
        player_slot: int = Field(default=0)

    class WatchedDeathReplay(BaseModel):
        game_time_s: int = Field(default=0)
        player_slot: int = Field(default=0)

    class MatchInfo(BaseModel):
        duration_s: int = Field(default=0)
        match_outcome: "CMsgMatchMetaDataContents.EMatchOutcome" = Field(default=0)
        winning_team: ECitadelLobbyTeam = Field(default=0)
        players: typing.List["CMsgMatchMetaDataContents.Players"] = Field(default_factory=list)
        start_time: int = Field(default=0)
        match_id: int = Field(default=0)
        legacy_objectives_mask: int = Field(default=0)
        game_mode: ECitadelGameMode = Field(default=0)
        match_mode: ECitadelMatchMode = Field(default=0)
        objectives: typing.List["CMsgMatchMetaDataContents.Objective"] = Field(default_factory=list)
        match_paths: CMsgMatchPlayerPathsData = Field()
        damage_matrix: CMsgMatchPlayerDamageMatrix = Field()
        match_pauses: typing.List["CMsgMatchMetaDataContents.Pause"] = Field(default_factory=list)
        custom_user_stats: typing.List["CMsgMatchMetaDataContents.CustomUserStatInfo"] = Field(default_factory=list)
        watched_death_replays: typing.List["CMsgMatchMetaDataContents.WatchedDeathReplay"] = Field(default_factory=list)
        objectives_mask_team0: int = Field(default=0)
        objectives_mask_team1: int = Field(default=0)
        mid_boss: typing.List["CMsgMatchMetaDataContents.MidBoss"] = Field(default_factory=list)
        is_high_skill_range_parties: bool = Field(default=False)
        low_pri_pool: bool = Field(default=False)
        new_player_pool: bool = Field(default=False)
        average_badge_team0: int = Field(default=0)
        average_badge_team1: int = Field(default=0)

    class EMatchOutcome(IntEnum):
        k_eOutcome_TeamWin = 0
        k_eOutcome_Error = 1

    class EGoldSource(IntEnum):
        k_ePlayers = 1
        k_eLaneCreeps = 2
        k_eNeutrals = 3
        k_eBosses = 4
        k_eTreasure = 5
        k_eAssists = 6
        k_eDenies = 7
        k_eTeamBonus = 8

    match_info: "CMsgMatchMetaDataContents.MatchInfo" = Field()

class CMsgMatchMetaData(BaseModel):
    version: int = Field(default=0)
    match_details: bytes = Field(default=b"")
    match_id: int = Field(default=0)

class CMsgMapLine(BaseModel):
    x: int = Field(default=0)
    y: int = Field(default=0)
    initial: bool = Field(default=False)

class CMsgAccountHeroStats(BaseModel):
    hero_id: int = Field(default=0)
    stat_id: typing.List[int] = Field(default_factory=list)
    total_value: typing.List[int] = Field(default_factory=list)
    medals_bronze: typing.List[int] = Field(default_factory=list)
    medals_silver: typing.List[int] = Field(default_factory=list)
    medals_gold: typing.List[int] = Field(default_factory=list)

class CMsgAccountBookStats(BaseModel):
    book_id: int = Field(default=0)
    book_xp: int = Field(default=0)
    book_max_xp: int = Field(default=0)

class CMsgAccountStats(BaseModel):
    account_id: int = Field(default=0)
    stats: typing.List[CMsgAccountHeroStats] = Field(default_factory=list)

class CMsgGCAccountData(BaseModel):
    account_id: int = Field(default=0)
    cheater_report_score: float = Field(default=0.0)
