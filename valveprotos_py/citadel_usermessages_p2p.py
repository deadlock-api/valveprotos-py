# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .citadel_gcmessages_common_p2p import CMsgLaneColor
from .citadel_gcmessages_common_p2p import CMsgMapLine
from .gameevents_p2p import CMsgSosSetLibraryStackFields
from .gameevents_p2p import CMsgSosSetSoundEventParams
from .gameevents_p2p import CMsgSosStartSoundEvent
from .gameevents_p2p import CMsgSosStopSoundEvent
from .gameevents_p2p import CMsgSosStopSoundEventHash
from .networkbasetypes_p2p import CEntityMsg
from .networkbasetypes_p2p import CMsgQAngle
from .networkbasetypes_p2p import CMsgVector
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class CitadelUserMessageIds(IntEnum):
    k_EUserMsg_Damage = 300
    k_EUserMsg_MapPing = 303
    k_EUserMsg_TeamRewards = 304
    k_EUserMsg_AbilityFailed = 306
    k_EUserMsg_TriggerDamageFlash = 308
    k_EUserMsg_AbilitiesChanged = 309
    k_EUserMsg_RecentDamageSummary = 310
    k_EUserMsg_SpectatorTeamChanged = 311
    k_EUserMsg_ChatWheel = 312
    k_EUserMsg_GoldHistory = 313
    k_EUserMsg_ChatMsg = 314
    k_EUserMsg_QuickResponse = 315
    k_EUserMsg_PostMatchDetails = 316
    k_EUserMsg_ChatEvent = 317
    k_EUserMsg_AbilityInterrupted = 318
    k_EUserMsg_HeroKilled = 319
    k_EUserMsg_ReturnIdol = 320
    k_EUserMsg_SetClientCameraAngles = 321
    k_EUserMsg_MapLine = 322
    k_EUserMsg_BulletHit = 323
    k_EUserMsg_ObjectiveMask = 324
    k_EUserMsg_ModifierApplied = 325
    k_EUserMsg_CameraController = 326
    k_EUserMsg_AuraModifierApplied = 327
    k_EUserMsg_ObstructedShotFired = 329
    k_EUserMsg_AbilityLateFailure = 330
    k_EUserMsg_AbilityPing = 331
    k_EUserMsg_PostProcessingAnim = 332
    k_EUserMsg_DeathReplayData = 333
    k_EUserMsg_PlayerLifetimeStatInfo = 334
    k_EUserMsg_ForceShopClosed = 336
    k_EUserMsg_StaminaDrained = 337
    k_EUserMsg_AbilityNotify = 338
    k_EUserMsg_GetDamageStatsResponse = 339
    k_EUserMsg_ParticipantStartSoundEvent = 340
    k_EUserMsg_ParticipantStopSoundEvent = 341
    k_EUserMsg_ParticipantStopSoundEventHash = 342
    k_EUserMsg_ParticipantSetSoundEventParams = 343
    k_EUserMsg_ParticipantSetLibraryStackFields = 344
    k_EUserMsg_CurrencyChanged = 345
    k_EUserMsg_GameOver = 346
    k_EUserMsg_BossKilled = 347
    k_EUserMsg_BossDamaged = 348
    k_EUserMsg_MidBossSpawned = 349
    k_EUserMsg_RejuvStatus = 350
    k_EUserMsg_KillStreak = 351
    k_EUserMsg_TeamMsg = 352
    k_EUserMsg_PlayerRespawned = 353
    k_EUserMsg_CallCheaterVote = 354
    k_EUserMsg_MeleeHit = 355
    k_EUserMsg_FlexSlotUnlocked = 356
    k_EUserMsg_SeasonalAchievementUnlocked = 357


class CitadelEntityMessageIds(IntEnum):
    k_EEntityMsg_BreakablePropSpawnDebris = 500


class ChatMsgPingMarkerInfo(IntEnum):
    k_EPingMarkerInfo_ShowMarkerAndSound = 0
    k_EPingMarkerInfo_HideMarkerAndSound = 1
    k_EPingMarkerInfo_ShowMarkerOnSender = 2
    k_EPingMarkerInfo_OnlyShowMarker = 3
    k_EPingMarkerInfo_OnlyPlaySound = 4


class CameraOperation(IntEnum):
    k_ECameraOp_Maintain = 2
    k_ECameraOp_Approach = 3
    k_ECameraOp_Spring = 4
    k_ECameraOp_Lerp = 5
    k_ECameraOp_Lag = 6


class CameraParam(IntEnum):
    k_EParam_ClearAllOps = 0
    k_EParam_ClearAllOpsForContext = 1
    k_EParam_Distance = 2
    k_EParam_FOV = 3
    k_EParam_TargetPosition = 4
    k_EParam_VertOffset = 5
    k_EParam_HorizOffset = 6


class CameraParamMode(IntEnum):
    k_EParamMode_AllowInOneContext = 0
    k_EParamMode_AllowInMultipleContexts = 1


class CameraAction(IntEnum):
    k_EAction_AddOp = 0
    k_EAction_ClearAllOps = 1
    k_EAction_ClearOpsForContext = 2


class ECitadelChatMessage(IntEnum):
    CITADEL_CHAT_MESSAGE_UNPAUSE_COUNTDOWN = 1
    CITADEL_CHAT_MESSAGE_UNPAUSED = 2
    CITADEL_CHAT_MESSAGE_AUTO_UNPAUSED = 3
    CITADEL_CHAT_MESSAGE_PAUSE_COUNTDOWN = 4
    CITADEL_CHAT_MESSAGE_PAUSED = 5
    CITADEL_CHAT_MESSAGE_YOUPAUSED = 6
    CITADEL_CHAT_MESSAGE_CANTPAUSE = 7
    CITADEL_CHAT_MESSAGE_CANTUNPAUSETEAM = 8
    CITADEL_CHAT_MESSAGE_NOPAUSESLEFT = 9
    CITADEL_CHAT_MESSAGE_CANTPAUSEYET = 10
    CITADEL_CHAT_MESSAGE_PREGAME_COUNTDOWN = 11
    CITADEL_CHAT_MESSAGE_NOTEAMPAUSESLEFT = 12
    CITADEL_CHAT_MESSAGE_COMMS_RESTRICTED = 13


class PostProcessingGameStates(IntEnum):
    PostProcState_Killed = 0
    PostProcState_Black = 1
    PostProcState_Blinded = 2
    PostProcState_ShivPossessed = 3

class CUserMessageEmpty(BaseModel):
    empty: int = Field(default=0)

class CCitadelUserMessage_Damage(BaseModel):
    damage: int = Field(default=0)
    pre_damage: int = Field(default=0)
    type: int = Field(default=0)
    citadel_type: int = Field(default=0)
    origin: CMsgVector = Field()
    entindex_victim: int = Field(default=0)
    entindex_inflictor: int = Field(default=0)
    entindex_attacker: int = Field(default=0)
    entindex_ability: int = Field(default=0)
    damage_absorbed: int = Field(default=0)
    victim_health_max: int = Field(default=0)
    victim_health_new: int = Field(default=0)
    flags: int = Field(default=0)
    ability_id: int = Field(default=0)
    attacker_class: int = Field(default=0)
    victim_class: int = Field(default=0)
    victim_shield_max: int = Field(default=0)
    victim_shield_new: int = Field(default=0)
    hits: int = Field(default=0)
    health_lost: int = Field(default=0)
    hitgroup_id: int = Field(default=0)
    entindex_attacking_object: int = Field(default=0)
    damage_direction: CMsgVector = Field()

class PingCommonData(BaseModel):
    ping_message_id: int = Field(default=0)
    ping_location: CMsgVector = Field()
    entity_index: int = Field(default=0)
    sender_player_slot: int = Field(default=0)
    speech_concept: int = Field(default=0)
    response_chosen: str = Field(default="")
    cooldown_time: float = Field(default=0.0)

class CCitadelUserMsg_MapPing(BaseModel):
    ping_data: PingCommonData = Field()
    event_type: int = Field(default=0)
    ping_marker_and_sound_info: ChatMsgPingMarkerInfo = Field(default=0)
    pinged_enemy_entity: bool = Field(default=False)
    pinged_entity_class: int = Field(default=0)
    is_minimap_ping: bool = Field(default=False)
    pinged_hero_name: str = Field(default="")
    is_blind_ping: bool = Field(default=False)

class CCitadelUserMsg_PingWheel(BaseModel):
    ping_data: PingCommonData = Field()
    ping_wheel_option_id: int = Field(default=0)

class CCitadelUserMsg_AbilityPing(BaseModel):
    ping_data: PingCommonData = Field()
    ability_id: int = Field(default=0)
    ability_cooldown: float = Field(default=0.0)
    ping_marker_and_sound_info: ChatMsgPingMarkerInfo = Field(default=0)

class CCitadelUserMsg_QuickResponse(BaseModel):
    ping_data: PingCommonData = Field()
    responding_to_ping_message_id: int = Field(default=0)
    responding_to_player_slot: int = Field(default=0)
    lane_color: CMsgLaneColor = Field(default=0)

class CCitadelUserMsg_MapLine(BaseModel):
    sender_player_slot: int = Field(default=0)
    mapline: CMsgMapLine = Field()

class CCitadelUserMsg_TeamRewards(BaseModel):
    xp: int = Field(default=0)
    gold: int = Field(default=0)
    winner: bool = Field(default=False)

class CCitadelUserMsg_TriggerDamageFlash(BaseModel):
    entindex_flash_victim: int = Field(default=0)
    entindex_flash_attacker: int = Field(default=0)
    entindex_flash_hitgroup: int = Field(default=0)
    flash_value: int = Field(default=0)
    flash_type: int = Field(default=0)
    flash_flags: int = Field(default=0)
    flash_position: CMsgVector = Field()

class CCitadelUserMsg_AbilitiesChanged(BaseModel):
    class Change(IntEnum):
        EInvalid = -1
        EPurchased = 0
        EUpgraded = 1
        ESold = 2
        ESwappedActivatedAbility = 3

    purchaser_player_slot: int = Field(default=0)
    ability_id: int = Field(default=0)
    change: "CCitadelUserMsg_AbilitiesChanged.Change" = Field(default=0)

class CCitadelUserMsg_AbilityInterrupted(BaseModel):
    entindex_victim: int = Field(default=0)
    entindex_interrupter: int = Field(default=0)
    ability_id_interrupted: int = Field(default=0)
    ability_id_interrupter: int = Field(default=0)
    hero_id_interrupter: int = Field(default=0)

class CCitadelUserMsg_AbilityLateFailure(BaseModel):
    entindex_caster: int = Field(default=0)
    entindex_ability: int = Field(default=0)
    failure_type: int = Field(default=0)

class CCitadelUserMsg_RecentDamageSummary(BaseModel):
    class DamageRecord(BaseModel):
        damage: int = Field(default=0)
        hits: int = Field(default=0)
        damage_type: int = Field(default=0)
        hero_id: int = Field(default=0)
        ability_id: int = Field(default=0)
        attacker_class: int = Field(default=0)
        damage_absorbed: int = Field(default=0)
        is_killing_blow: bool = Field(default=False)
        victim_hero_id: int = Field(default=0)

    class ModifierRecord(BaseModel):
        ability_id: int = Field(default=0)
        modifier_type_id: int = Field(default=0)
        entindex_caster: int = Field(default=0)
        start_time: float = Field(default=0.0)
        end_time: float = Field(default=0.0)
        debuff: bool = Field(default=False)

    player_slot: int = Field(default=0)
    damage_records: typing.List["CCitadelUserMsg_RecentDamageSummary.DamageRecord"] = Field(default_factory=list)
    start_time: float = Field(default=0.0)
    end_time: float = Field(default=0.0)
    total_damage: int = Field(default=0)
    lost_gold: int = Field(default=0)
    modifier_records: typing.List["CCitadelUserMsg_RecentDamageSummary.ModifierRecord"] = Field(default_factory=list)

class CCitadelUserMsg_SpectatorTeamChanged(BaseModel):
    teamnumber: int = Field(default=0)

class CCitadelUserMsg_ChatWheel(BaseModel):
    chat_message_id: int = Field(default=0)
    player_slot: int = Field(default=0)
    pawn_entindex: int = Field(default=0)
    account_id: int = Field(default=0)
    hero_id: int = Field(default=0)
    param_1: str = Field(default="")
    lane_color: CMsgLaneColor = Field(default=0)

class CCitadelUserMsg_ChatMsg(BaseModel):
    player_slot: int = Field(default=0)
    text: str = Field(default="")
    all_chat: bool = Field(default=False)
    lane_color: CMsgLaneColor = Field(default=0)

class CCitadelUserMsg_GoldHistory(BaseModel):
    class GoldRecord(BaseModel):
        currency_source: int = Field(default=0)
        gold: int = Field(default=0)
        events: int = Field(default=0)

    class MinuteRecord(BaseModel):
        match_minute: int = Field(default=0)
        gold_records: typing.List["CCitadelUserMsg_GoldHistory.GoldRecord"] = Field(default_factory=list)

    entindex_player: int = Field(default=0)
    minute_records: typing.List["CCitadelUserMsg_GoldHistory.MinuteRecord"] = Field(default_factory=list)

class CCitadelUserMsg_CameraController(BaseModel):
    class Maintain(BaseModel):
        duration: float = Field(default=0.0)

    class Approach(BaseModel):
        speed: float = Field(default=0.0)
        default_speed: float = Field(default=0.0)
        acceleration: float = Field(default=0.0)
        min_duration: float = Field(default=0.0)
        approach_float: float = Field(default=0.0)
        approach_vector: CMsgVector = Field()
        chase_default: bool = Field(default=False)

    class Spring(BaseModel):
        spring_strength: float = Field(default=0.0)
        min_speed: float = Field(default=0.0)
        max_duration: float = Field(default=0.0)
        target_float: float = Field(default=0.0)
        target_vector: CMsgVector = Field()

    class Lerp(BaseModel):
        start_float: float = Field(default=0.0)
        start_vector: CMsgVector = Field()
        end_float: float = Field(default=0.0)
        end_vector: CMsgVector = Field()
        bias: float = Field(default=0.0)
        gain: float = Field(default=0.0)
        duration: float = Field(default=0.0)

    class Lag(BaseModel):
        min_duration: float = Field(default=0.0)
        lag_time: float = Field(default=0.0)
        max_speed: float = Field(default=0.0)
        spring_strength: float = Field(default=0.0)
        increase_spring_strength_to_keep_target_on_screen: bool = Field(default=False)

    action: CameraAction = Field(default=0)
    operation: CameraOperation = Field(default=0)
    param: CameraParam = Field(default=0)
    param_mode: CameraParamMode = Field(default=0)
    delay: float = Field(default=0.0)
    relative_values: bool = Field(default=False)
    context_symbol_id: int = Field(default=0)
    priority: int = Field(default=0)
    maintain: "CCitadelUserMsg_CameraController.Maintain" = Field()
    approach: "CCitadelUserMsg_CameraController.Approach" = Field()
    spring: "CCitadelUserMsg_CameraController.Spring" = Field()
    lerp: "CCitadelUserMsg_CameraController.Lerp" = Field()
    lag: "CCitadelUserMsg_CameraController.Lag" = Field()

class CCitadelUserMsg_PostMatchDetails(BaseModel):
    match_details: bytes = Field(default=b"")

class CCitadelUserMsg_ChatEvent(BaseModel):
    type: ECitadelChatMessage = Field(default=0)
    values: typing.List[int] = Field(default_factory=list)
    player_slots: typing.List[int] = Field(default_factory=list)

class CCitadelUserMsg_HeroKilled(BaseModel):
    entindex_victim: int = Field(default=0)
    entindex_inflictor: int = Field(default=0)
    entindex_attacker: int = Field(default=0)
    entindex_assisters: typing.List[int] = Field(default_factory=list)
    entindex_scorer: int = Field(default=0)
    respawn_reason: int = Field(default=0)
    victim_team_number: int = Field(default=0)

class CCitadelEntityMsg_BreakablePropSpawnDebris(BaseModel):
    entity_msg: CEntityMsg = Field()
    damage_pos: CMsgVector = Field()
    damage: float = Field(default=0.0)

class CCitadelUserMsg_ReturnIdol(BaseModel):
    location_index: int = Field(default=0)
    return_location: CMsgVector = Field()
    location_enabled: bool = Field(default=False)

class CCitadelUserMsg_SetClientCameraAngles(BaseModel):
    player_slot: int = Field(default=0)
    camera_angles: CMsgQAngle = Field()

class CCitadelUserMessage_BulletHit(BaseModel):
    shotid: int = Field(default=0)
    pellet: int = Field(default=0)
    hit_entindex: int = Field(default=0)
    weapon_entindex: int = Field(default=0)
    is_predicted: bool = Field(default=False)

class CCitadelUserMessage_ObjectiveMask(BaseModel):
    objective_mask_team0: int = Field(default=0)
    objective_mask_team1: int = Field(default=0)

class CCitadelUserMessage_ModifierApplied(BaseModel):
    entindex_caster: int = Field(default=0)
    entindex_parent: int = Field(default=0)
    serial_number: int = Field(default=0)

class CCitadelUserMessage_AuraModifierApplied(BaseModel):
    entindex_caster: int = Field(default=0)
    entindex_target: int = Field(default=0)
    modifier_type_id: int = Field(default=0)
    modifier_serial_number: int = Field(default=0)
    aura_start_time: float = Field(default=0.0)
    aura_end_time: float = Field(default=0.0)

class CCitadelUserMsg_ObstructedShotFired(BaseModel):
    pass

class CCitadelUserMsg_PostProcessingAnim(BaseModel):
    entindex_owner: int = Field(default=0)
    clear_all_states: bool = Field(default=False)
    state: PostProcessingGameStates = Field(default=0)
    start_time: float = Field(default=0.0)
    fade_in_time: float = Field(default=0.0)
    hold_time: float = Field(default=0.0)
    fade_out_time: float = Field(default=0.0)
    scale: float = Field(default=0.0)

class CCitadelUserMsg_DeathReplayData(BaseModel):
    killer_scorer: int = Field(default=0)
    killer_inflictor: int = Field(default=0)
    damage_summary: CCitadelUserMsg_RecentDamageSummary = Field()

class CCitadelUserMsg_ForceShopClosed(BaseModel):
    pass

class CCitadelUserMsg_PlayerLifetimeStatInfo(BaseModel):
    class Stat(BaseModel):
        stat_name: str = Field(default="")
        match_total: int = Field(default=0)
        lifetime_value: int = Field(default=0)
        priority: int = Field(default=0)
        prev_lifetime_max: int = Field(default=0)
        stat_type: int = Field(default=0)
        stat_type_id: int = Field(default=0)

    stats: typing.List["CCitadelUserMsg_PlayerLifetimeStatInfo.Stat"] = Field(default_factory=list)
    match_id: int = Field(default=0)
    end_of_match: bool = Field(default=False)
    is_official_match: bool = Field(default=False)

class CCitadelUserMsg_StaminaDrained(BaseModel):
    entindex_victim: int = Field(default=0)
    stamina_drained: int = Field(default=0)

class CCitadelUserMessage_AbilityNotify(BaseModel):
    entindex_victim: int = Field(default=0)
    entindex_attacker: int = Field(default=0)
    ability_id: int = Field(default=0)

class CCitadelUserMessage_CurrencyChanged(BaseModel):
    entindex_hero_pawn: int = Field(default=0)
    currency_type: int = Field(default=0)
    currency_source: int = Field(default=0)
    delta: int = Field(default=0)
    notification: bool = Field(default=False)
    entindex_victim: int = Field(default=0)
    victim_pos: CMsgVector = Field()
    playsound: int = Field(default=0)
    ability_id: int = Field(default=0)
    new_value: int = Field(default=0)

class CCitadelUserMessage_GameOver(BaseModel):
    winning_team: int = Field(default=0)
    just_a_test: bool = Field(default=False)

class CCitadelUserMsg_GetDamageStatsResponse(BaseModel):
    class StatType(BaseModel):
        target_player_slot: typing.List[int] = Field(default_factory=list)
        value: typing.List[int] = Field(default_factory=list)

    player_slot: int = Field(default=0)
    ability_name: str = Field(default="")
    damage: "CCitadelUserMsg_GetDamageStatsResponse.StatType" = Field()
    healing: "CCitadelUserMsg_GetDamageStatsResponse.StatType" = Field()

class CCitadelUserMsg_ParticipantStartSoundEvent(BaseModel):
    event: CMsgSosStartSoundEvent = Field()
    player_slots: typing.List[int] = Field(default_factory=list)

class CCitadelUserMsg_ParticipantStopSoundEvent(BaseModel):
    event: CMsgSosStopSoundEvent = Field()
    player_slots: typing.List[int] = Field(default_factory=list)

class CCitadelUserMsg_ParticipantStopSoundEventHash(BaseModel):
    event: CMsgSosStopSoundEventHash = Field()
    player_slots: typing.List[int] = Field(default_factory=list)

class CCitadelUserMsg_ParticipantSetSoundEventParams(BaseModel):
    event: CMsgSosSetSoundEventParams = Field()
    player_slots: typing.List[int] = Field(default_factory=list)

class CCitadelUserMsg_ParticipantSetLibraryStackFields(BaseModel):
    event: CMsgSosSetLibraryStackFields = Field()
    player_slots: typing.List[int] = Field(default_factory=list)

class CCitadelUserMsg_BossKilled(BaseModel):
    objective_team: int = Field(default=0)
    objective_mask_change: int = Field(default=0)
    entity_killed: int = Field(default=0)
    entity_killed_class: int = Field(default=0)
    entity_killer: int = Field(default=0)
    gametime: float = Field(default=0.0)
    bosses_remaining: int = Field(default=0)
    entity_position: CMsgVector = Field()

class CCitadelUserMsg_BossDamaged(BaseModel):
    objective_team: int = Field(default=0)
    objective_id: int = Field(default=0)
    entity_damaged: int = Field(default=0)

class CCitadelUserMsg_MidBossSpawned(BaseModel):
    pass

class CCitadelUserMsg_RejuvStatus(BaseModel):
    killing_team: int = Field(default=0)
    player_pawn: int = Field(default=0)
    user_team: int = Field(default=0)
    event_type: int = Field(default=0)

class CCitadelUserMsg_KillStreak(BaseModel):
    player_pawn: int = Field(default=0)
    num_kills: int = Field(default=0)
    is_first_blood: bool = Field(default=False)

class CCitadelUserMsg_TeamMsg(BaseModel):
    event_type: int = Field(default=0)
    team_number: int = Field(default=0)
    lane_color: int = Field(default=0)
    player_controller: int = Field(default=0)

class CCitadelUserMsg_PlayerRespawned(BaseModel):
    player_pawn: int = Field(default=0)
    facing_yaw: float = Field(default=0.0)

class CCitadelUserMsg_CallCheaterVote(BaseModel):
    player_slot: int = Field(default=0)

class CCitadelUserMessage_MeleeHit(BaseModel):
    hit_entindex: int = Field(default=0)
    heavy: bool = Field(default=False)

class CCitadelUserMsg_FlexSlotUnlocked(BaseModel):
    team_number: int = Field(default=0)
    flexslot_unlocked: int = Field(default=0)

class CCitadelUserMsg_SeasonalAchievementUnlocked(BaseModel):
    account_id: int = Field(default=0)
    hero_id: int = Field(default=0)
