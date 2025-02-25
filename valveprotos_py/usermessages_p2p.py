# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .networkbasetypes_p2p import CEntityMsg
from .networkbasetypes_p2p import CMsgQAngle
from .networkbasetypes_p2p import CMsgQuaternion
from .networkbasetypes_p2p import CMsgVector
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class EBaseUserMessages(IntEnum):
    UM_AchievementEvent = 101
    UM_CloseCaption = 102
    UM_CloseCaptionDirect = 103
    UM_CurrentTimescale = 104
    UM_DesiredTimescale = 105
    UM_Fade = 106
    UM_GameTitle = 107
    UM_HudMsg = 110
    UM_HudText = 111
    UM_ColoredText = 113
    UM_RequestState = 114
    UM_ResetHUD = 115
    UM_Rumble = 116
    UM_SayText = 117
    UM_SayText2 = 118
    UM_SayTextChannel = 119
    UM_Shake = 120
    UM_ShakeDir = 121
    UM_WaterShake = 122
    UM_TextMsg = 124
    UM_ScreenTilt = 125
    UM_VoiceMask = 128
    UM_SendAudio = 130
    UM_ItemPickup = 131
    UM_AmmoDenied = 132
    UM_ShowMenu = 134
    UM_CreditsMsg = 135
    UM_CloseCaptionPlaceholder = 142
    UM_CameraTransition = 143
    UM_AudioParameter = 144
    UM_ParticleManager = 145
    UM_HudError = 146
    UM_CustomGameEvent = 148
    UM_AnimGraphUpdate = 149
    UM_HapticsManagerPulse = 150
    UM_HapticsManagerEffect = 151
    UM_UpdateCssClasses = 153
    UM_ServerFrameTime = 154
    UM_LagCompensationError = 155
    UM_RequestDllStatus = 156
    UM_RequestUtilAction = 157
    UM_UtilActionResponse = 158
    UM_DllStatusResponse = 159
    UM_RequestInventory = 160
    UM_InventoryResponse = 161
    UM_RequestDiagnostic = 162
    UM_DiagnosticResponse = 163
    UM_ExtraUserData = 164
    UM_NotifyResponseFound = 165
    UM_PlayResponseConditional = 166
    UM_MAX_BASE = 200


class EBaseEntityMessages(IntEnum):
    EM_PlayJingle = 136
    EM_ScreenOverlay = 137
    EM_RemoveAllDecals = 138
    EM_PropagateForce = 139
    EM_DoSpark = 140
    EM_FixAngle = 141


class eRollType(IntEnum):
    ROLL_NONE = -1
    ROLL_STATS = 0
    ROLL_CREDITS = 1
    ROLL_LATE_JOIN_LOGO = 2
    ROLL_OUTTRO = 3


class PARTICLE_MESSAGE(IntEnum):
    GAME_PARTICLE_MANAGER_EVENT_CREATE = 0
    GAME_PARTICLE_MANAGER_EVENT_UPDATE = 1
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_FORWARD = 2
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_ORIENTATION = 3
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_FALLBACK = 4
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENT = 5
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_OFFSET = 6
    GAME_PARTICLE_MANAGER_EVENT_DESTROY = 7
    GAME_PARTICLE_MANAGER_EVENT_DESTROY_INVOLVING = 8
    GAME_PARTICLE_MANAGER_EVENT_RELEASE = 9
    GAME_PARTICLE_MANAGER_EVENT_LATENCY = 10
    GAME_PARTICLE_MANAGER_EVENT_SHOULD_DRAW = 11
    GAME_PARTICLE_MANAGER_EVENT_FROZEN = 12
    GAME_PARTICLE_MANAGER_EVENT_CHANGE_CONTROL_POINT_ATTACHMENT = 13
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENTITY_POSITION = 14
    GAME_PARTICLE_MANAGER_EVENT_SET_FOW_PROPERTIES = 15
    GAME_PARTICLE_MANAGER_EVENT_SET_TEXT = 16
    GAME_PARTICLE_MANAGER_EVENT_SET_SHOULD_CHECK_FOW = 17
    GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_MODEL = 18
    GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_SNAPSHOT = 19
    GAME_PARTICLE_MANAGER_EVENT_SET_TEXTURE_ATTRIBUTE = 20
    GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_GENERIC_FLAG = 21
    GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_TINT_AND_DESAT = 22
    GAME_PARTICLE_MANAGER_EVENT_DESTROY_NAMED = 23
    GAME_PARTICLE_MANAGER_EVENT_SKIP_TO_TIME = 24
    GAME_PARTICLE_MANAGER_EVENT_CAN_FREEZE = 25
    GAME_PARTICLE_MANAGER_EVENT_SET_NAMED_VALUE_CONTEXT = 26
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_TRANSFORM = 27
    GAME_PARTICLE_MANAGER_EVENT_FREEZE_TRANSITION_OVERRIDE = 28
    GAME_PARTICLE_MANAGER_EVENT_FREEZE_INVOLVING = 29
    GAME_PARTICLE_MANAGER_EVENT_ADD_MODELLIST_OVERRIDE_ELEMENT = 30
    GAME_PARTICLE_MANAGER_EVENT_CLEAR_MODELLIST_OVERRIDE = 31
    GAME_PARTICLE_MANAGER_EVENT_CREATE_PHYSICS_SIM = 32
    GAME_PARTICLE_MANAGER_EVENT_DESTROY_PHYSICS_SIM = 33
    GAME_PARTICLE_MANAGER_EVENT_SET_VDATA = 34
    GAME_PARTICLE_MANAGER_EVENT_SET_MATERIAL_OVERRIDE = 35
    GAME_PARTICLE_MANAGER_EVENT_ADD_FAN = 36
    GAME_PARTICLE_MANAGER_EVENT_UPDATE_FAN = 37
    GAME_PARTICLE_MANAGER_EVENT_SET_CLUSTER_GROWTH = 38


class EHapticPulseType(IntEnum):
    VR_HAND_HAPTIC_PULSE_LIGHT = 0
    VR_HAND_HAPTIC_PULSE_MEDIUM = 1
    VR_HAND_HAPTIC_PULSE_STRONG = 2

class CUserMessageAchievementEvent(BaseModel):
    achievement: int = Field(default=0)

class CUserMessageCloseCaption(BaseModel):
    hash: float = Field(default=0.0)
    duration: float = Field(default=0.0)
    from_player: bool = Field(default=False)
    ent_index: int = Field(default=0)

class CUserMessageCloseCaptionDirect(BaseModel):
    hash: float = Field(default=0.0)
    duration: float = Field(default=0.0)
    from_player: bool = Field(default=False)
    ent_index: int = Field(default=0)

class CUserMessageCloseCaptionPlaceholder(BaseModel):
    string: str = Field(default="")
    duration: float = Field(default=0.0)
    from_player: bool = Field(default=False)
    ent_index: int = Field(default=0)

class CUserMessageCurrentTimescale(BaseModel):
    current: float = Field(default=0.0)

class CUserMessageDesiredTimescale(BaseModel):
    desired: float = Field(default=0.0)
    acceleration: float = Field(default=0.0)
    minblendrate: float = Field(default=0.0)
    blenddeltamultiplier: float = Field(default=0.0)

class CUserMessageFade(BaseModel):
    duration: int = Field(default=0)
    hold_time: int = Field(default=0)
    flags: int = Field(default=0)
    color: float = Field(default=0.0)

class CUserMessageShake(BaseModel):
    command: int = Field(default=0)
    amplitude: float = Field(default=0.0)
    frequency: float = Field(default=0.0)
    duration: float = Field(default=0.0)

class CUserMessageShakeDir(BaseModel):
    shake: CUserMessageShake = Field()
    direction: CMsgVector = Field()

class CUserMessageWaterShake(BaseModel):
    command: int = Field(default=0)
    amplitude: float = Field(default=0.0)
    frequency: float = Field(default=0.0)
    duration: float = Field(default=0.0)

class CUserMessageScreenTilt(BaseModel):
    command: int = Field(default=0)
    ease_in_out: bool = Field(default=False)
    angle: CMsgVector = Field()
    duration: float = Field(default=0.0)
    time: float = Field(default=0.0)

class CUserMessageSayText(BaseModel):
    playerindex: int = Field(default=0)
    text: str = Field(default="")
    chat: bool = Field(default=False)

class CUserMessageSayText2(BaseModel):
    entityindex: int = Field(default=0)
    chat: bool = Field(default=False)
    messagename: str = Field(default="")
    param1: str = Field(default="")
    param2: str = Field(default="")
    param3: str = Field(default="")
    param4: str = Field(default="")

class CUserMessageHudMsg(BaseModel):
    channel: int = Field(default=0)
    x: float = Field(default=0.0)
    y: float = Field(default=0.0)
    color1: float = Field(default=0.0)
    color2: float = Field(default=0.0)
    effect: int = Field(default=0)
    message: str = Field(default="")

class CUserMessageHudText(BaseModel):
    message: str = Field(default="")

class CUserMessageTextMsg(BaseModel):
    dest: int = Field(default=0)
    param: typing.List[str] = Field(default_factory=list)

class CUserMessageGameTitle(BaseModel):
    pass

class CUserMessageResetHUD(BaseModel):
    pass

class CUserMessageSendAudio(BaseModel):
    soundname: str = Field(default="")
    stop: bool = Field(default=False)

class CUserMessageAudioParameter(BaseModel):
    parameter_type: int = Field(default=0)
    name_hash_code: int = Field(default=0)
    value: float = Field(default=0.0)
    int_value: int = Field(default=0)

class CUserMessageVoiceMask(BaseModel):
    gamerules_masks: typing.List[int] = Field(default_factory=list)
    ban_masks: typing.List[int] = Field(default_factory=list)
    mod_enable: bool = Field(default=False)

class CUserMessageRequestState(BaseModel):
    pass

class CUserMessageRumble(BaseModel):
    index: int = Field(default=0)
    data: int = Field(default=0)
    flags: int = Field(default=0)

class CUserMessageSayTextChannel(BaseModel):
    player: int = Field(default=0)
    channel: int = Field(default=0)
    text: str = Field(default="")

class CUserMessageColoredText(BaseModel):
    color: int = Field(default=0)
    text: str = Field(default="")
    reset: bool = Field(default=False)
    context_player_slot: int = Field(default=0)
    context_value: int = Field(default=0)
    context_team_id: int = Field(default=0)

class CUserMessageItemPickup(BaseModel):
    itemname: str = Field(default="")

class CUserMessageAmmoDenied(BaseModel):
    ammo_id: int = Field(default=0)

class CUserMessageShowMenu(BaseModel):
    validslots: int = Field(default=0)
    displaytime: int = Field(default=0)
    needmore: bool = Field(default=False)
    menustring: str = Field(default="")

class CUserMessageCreditsMsg(BaseModel):
    rolltype: eRollType = Field(default=0)
    logo_length: float = Field(default=0.0)

class CEntityMessagePlayJingle(BaseModel):
    entity_msg: CEntityMsg = Field()

class CEntityMessageScreenOverlay(BaseModel):
    start_effect: bool = Field(default=False)
    entity_msg: CEntityMsg = Field()

class CEntityMessageRemoveAllDecals(BaseModel):
    remove_decals: bool = Field(default=False)
    entity_msg: CEntityMsg = Field()

class CEntityMessagePropagateForce(BaseModel):
    impulse: CMsgVector = Field()
    entity_msg: CEntityMsg = Field()

class CEntityMessageDoSpark(BaseModel):
    origin: CMsgVector = Field()
    entityindex: int = Field(default=0)
    radius: float = Field(default=0.0)
    color: float = Field(default=0.0)
    beams: int = Field(default=0)
    thick: float = Field(default=0.0)
    duration: float = Field(default=0.0)
    entity_msg: CEntityMsg = Field()

class CEntityMessageFixAngle(BaseModel):
    relative: bool = Field(default=False)
    angle: CMsgQAngle = Field()
    entity_msg: CEntityMsg = Field()

class CUserMessageCameraTransition(BaseModel):
    class Transition_DataDriven(BaseModel):
        filename: str = Field(default="")
        attach_ent_index: int = Field(default=0)
        duration: float = Field(default=0.0)

    camera_type: int = Field(default=0)
    duration: float = Field(default=0.0)
    params_data_driven: "CUserMessageCameraTransition.Transition_DataDriven" = Field()

class CUserMsg_ParticleManager(BaseModel):
    class ReleaseParticleIndex(BaseModel):
        pass

    class CreateParticle(BaseModel):
        particle_name_index: float = Field(default=0.0)
        attach_type: int = Field(default=0)
        entity_handle: int = Field(default=0)
        entity_handle_for_modifiers: int = Field(default=0)
        apply_voice_ban_rules: bool = Field(default=False)
        team_behavior: int = Field(default=0)
        control_point_configuration: str = Field(default="")
        cluster: bool = Field(default=False)
        endcap_time: float = Field(default=0.0)
        aggregation_position: CMsgVector = Field()

    class DestroyParticle(BaseModel):
        destroy_immediately: bool = Field(default=False)

    class DestroyParticleInvolving(BaseModel):
        destroy_immediately: bool = Field(default=False)
        entity_handle: int = Field(default=0)

    class DestroyParticleNamed(BaseModel):
        particle_name_index: float = Field(default=0.0)
        entity_handle: int = Field(default=0)
        destroy_immediately: bool = Field(default=False)
        play_endcap: bool = Field(default=False)

    class UpdateParticle_OBSOLETE(BaseModel):
        control_point: int = Field(default=0)
        position: CMsgVector = Field()

    class UpdateParticleFwd_OBSOLETE(BaseModel):
        control_point: int = Field(default=0)
        forward: CMsgVector = Field()

    class UpdateParticleOrient_OBSOLETE(BaseModel):
        control_point: int = Field(default=0)
        forward: CMsgVector = Field()
        deprecated_right: CMsgVector = Field()
        up: CMsgVector = Field()
        left: CMsgVector = Field()

    class UpdateParticleTransform(BaseModel):
        control_point: int = Field(default=0)
        position: CMsgVector = Field()
        orientation: CMsgQuaternion = Field()
        interpolation_interval: float = Field(default=0.0)

    class UpdateParticleFallback(BaseModel):
        control_point: int = Field(default=0)
        position: CMsgVector = Field()

    class UpdateParticleOffset(BaseModel):
        control_point: int = Field(default=0)
        origin_offset: CMsgVector = Field()
        angle_offset: CMsgQAngle = Field()

    class UpdateParticleEnt(BaseModel):
        control_point: int = Field(default=0)
        entity_handle: int = Field(default=0)
        attach_type: int = Field(default=0)
        attachment: int = Field(default=0)
        fallback_position: CMsgVector = Field()
        include_wearables: bool = Field(default=False)
        offset_position: CMsgVector = Field()
        offset_angles: CMsgQAngle = Field()

    class UpdateParticleSetFrozen(BaseModel):
        set_frozen: bool = Field(default=False)
        transition_duration: float = Field(default=0.0)

    class UpdateParticleShouldDraw(BaseModel):
        should_draw: bool = Field(default=False)

    class ChangeControlPointAttachment(BaseModel):
        attachment_old: int = Field(default=0)
        attachment_new: int = Field(default=0)
        entity_handle: int = Field(default=0)

    class UpdateEntityPosition(BaseModel):
        entity_handle: int = Field(default=0)
        position: CMsgVector = Field()

    class SetParticleFoWProperties(BaseModel):
        fow_control_point: int = Field(default=0)
        fow_control_point2: int = Field(default=0)
        fow_radius: float = Field(default=0.0)

    class SetParticleShouldCheckFoW(BaseModel):
        check_fow: bool = Field(default=False)

    class SetControlPointModel(BaseModel):
        control_point: int = Field(default=0)
        model_name: str = Field(default="")

    class SetControlPointSnapshot(BaseModel):
        control_point: int = Field(default=0)
        snapshot_name: str = Field(default="")

    class SetParticleText(BaseModel):
        text: str = Field(default="")

    class SetTextureAttribute(BaseModel):
        attribute_name: str = Field(default="")
        texture_name: str = Field(default="")

    class SetSceneObjectGenericFlag(BaseModel):
        flag_value: bool = Field(default=False)

    class SetSceneObjectTintAndDesat(BaseModel):
        tint: float = Field(default=0.0)
        desat: float = Field(default=0.0)

    class ParticleSkipToTime(BaseModel):
        skip_to_time: float = Field(default=0.0)

    class ParticleCanFreeze(BaseModel):
        can_freeze: bool = Field(default=False)

    class ParticleFreezeTransitionOverride(BaseModel):
        freeze_transition_override: float = Field(default=0.0)

    class FreezeParticleInvolving(BaseModel):
        set_frozen: bool = Field(default=False)
        transition_duration: float = Field(default=0.0)
        entity_handle: int = Field(default=0)

    class AddModellistOverrideElement(BaseModel):
        model_name: str = Field(default="")
        spawn_probability: float = Field(default=0.0)
        groupid: int = Field(default=0)

    class ClearModellistOverride(BaseModel):
        groupid: int = Field(default=0)

    class SetParticleNamedValueContext(BaseModel):
        class FloatContextValue(BaseModel):
            value_name_hash: int = Field(default=0)
            value: float = Field(default=0.0)

        class VectorContextValue(BaseModel):
            value_name_hash: int = Field(default=0)
            value: CMsgVector = Field()

        class TransformContextValue(BaseModel):
            value_name_hash: int = Field(default=0)
            angles: CMsgQAngle = Field()
            translation: CMsgVector = Field()

        class EHandleContext(BaseModel):
            value_name_hash: int = Field(default=0)
            ent_index: int = Field(default=0)

        float_values: typing.List[FloatContextValue] = Field(default_factory=list)
        vector_values: typing.List[VectorContextValue] = Field(default_factory=list)
        transform_values: typing.List[TransformContextValue] = Field(default_factory=list)
        ehandle_values: typing.List[EHandleContext] = Field(default_factory=list)

    class CreatePhysicsSim(BaseModel):
        prop_group_name: str = Field(default="")
        use_high_quality_simulation: bool = Field(default=False)
        max_particle_count: int = Field(default=0)

    class DestroyPhysicsSim(BaseModel):
        pass

    class SetVData(BaseModel):
        vdata_name: str = Field(default="")

    class SetMaterialOverride(BaseModel):
        material_name: str = Field(default="")
        include_children: bool = Field(default=False)

    class AddFan(BaseModel):
        active: bool = Field(default=False)
        bounds_mins: CMsgVector = Field()
        bounds_maxs: CMsgVector = Field()
        fan_origin: CMsgVector = Field()
        fan_origin_offset: CMsgVector = Field()
        fan_direction: CMsgVector = Field()
        force: float = Field(default=0.0)
        fan_force_curve: str = Field(default="")
        falloff: bool = Field(default=False)
        pull_towards_point: bool = Field(default=False)
        curve_min_dist: float = Field(default=0.0)
        curve_max_dist: float = Field(default=0.0)

    class UpdateFan(BaseModel):
        active: bool = Field(default=False)
        fan_origin: CMsgVector = Field()
        fan_origin_offset: CMsgVector = Field()
        fan_direction: CMsgVector = Field()
        fan_ramp_ratio: float = Field(default=0.0)
        bounds_mins: CMsgVector = Field()
        bounds_maxs: CMsgVector = Field()

    class SetParticleClusterGrowth(BaseModel):
        duration: float = Field(default=0.0)
        origin: CMsgVector = Field()

    type: PARTICLE_MESSAGE = Field(default=0)
    index: int = Field(default=0)
    release_particle_index: "CUserMsg_ParticleManager.ReleaseParticleIndex" = Field()
    create_particle: "CUserMsg_ParticleManager.CreateParticle" = Field()
    destroy_particle: "CUserMsg_ParticleManager.DestroyParticle" = Field()
    destroy_particle_involving: "CUserMsg_ParticleManager.DestroyParticleInvolving" = Field()
    update_particle: "CUserMsg_ParticleManager.UpdateParticle_OBSOLETE" = Field()
    update_particle_fwd: "CUserMsg_ParticleManager.UpdateParticleFwd_OBSOLETE" = Field()
    update_particle_orient: "CUserMsg_ParticleManager.UpdateParticleOrient_OBSOLETE" = Field()
    update_particle_fallback: "CUserMsg_ParticleManager.UpdateParticleFallback" = Field()
    update_particle_offset: "CUserMsg_ParticleManager.UpdateParticleOffset" = Field()
    update_particle_ent: "CUserMsg_ParticleManager.UpdateParticleEnt" = Field()
    update_particle_should_draw: "CUserMsg_ParticleManager.UpdateParticleShouldDraw" = Field()
    update_particle_set_frozen: "CUserMsg_ParticleManager.UpdateParticleSetFrozen" = Field()
    change_control_point_attachment: "CUserMsg_ParticleManager.ChangeControlPointAttachment" = Field()
    update_entity_position: "CUserMsg_ParticleManager.UpdateEntityPosition" = Field()
    set_particle_fow_properties: "CUserMsg_ParticleManager.SetParticleFoWProperties" = Field()
    set_particle_text: "CUserMsg_ParticleManager.SetParticleText" = Field()
    set_particle_should_check_fow: "CUserMsg_ParticleManager.SetParticleShouldCheckFoW" = Field()
    set_control_point_model: "CUserMsg_ParticleManager.SetControlPointModel" = Field()
    set_control_point_snapshot: "CUserMsg_ParticleManager.SetControlPointSnapshot" = Field()
    set_texture_attribute: "CUserMsg_ParticleManager.SetTextureAttribute" = Field()
    set_scene_object_generic_flag: "CUserMsg_ParticleManager.SetSceneObjectGenericFlag" = Field()
    set_scene_object_tint_and_desat: "CUserMsg_ParticleManager.SetSceneObjectTintAndDesat" = Field()
    destroy_particle_named: "CUserMsg_ParticleManager.DestroyParticleNamed" = Field()
    particle_skip_to_time: "CUserMsg_ParticleManager.ParticleSkipToTime" = Field()
    particle_can_freeze: "CUserMsg_ParticleManager.ParticleCanFreeze" = Field()
    set_named_value_context: "CUserMsg_ParticleManager.SetParticleNamedValueContext" = Field()
    update_particle_transform: "CUserMsg_ParticleManager.UpdateParticleTransform" = Field()
    particle_freeze_transition_override: "CUserMsg_ParticleManager.ParticleFreezeTransitionOverride" = Field()
    freeze_particle_involving: "CUserMsg_ParticleManager.FreezeParticleInvolving" = Field()
    add_modellist_override_element: "CUserMsg_ParticleManager.AddModellistOverrideElement" = Field()
    clear_modellist_override: "CUserMsg_ParticleManager.ClearModellistOverride" = Field()
    create_physics_sim: "CUserMsg_ParticleManager.CreatePhysicsSim" = Field()
    destroy_physics_sim: "CUserMsg_ParticleManager.DestroyPhysicsSim" = Field()
    set_vdata: "CUserMsg_ParticleManager.SetVData" = Field()
    set_material_override: "CUserMsg_ParticleManager.SetMaterialOverride" = Field()
    add_fan: "CUserMsg_ParticleManager.AddFan" = Field()
    update_fan: "CUserMsg_ParticleManager.UpdateFan" = Field()
    set_particle_cluster_growth: "CUserMsg_ParticleManager.SetParticleClusterGrowth" = Field()

class CUserMsg_HudError(BaseModel):
    order_id: int = Field(default=0)

class CUserMsg_CustomGameEvent(BaseModel):
    event_name: str = Field(default="")
    data: bytes = Field(default=b"")

class CUserMessageHapticsManagerPulse(BaseModel):
    hand_id: int = Field(default=0)
    effect_amplitude: float = Field(default=0.0)
    effect_frequency: float = Field(default=0.0)
    effect_duration: float = Field(default=0.0)

class CUserMessageHapticsManagerEffect(BaseModel):
    hand_id: int = Field(default=0)
    effect_name_hash_code: int = Field(default=0)
    effect_scale: float = Field(default=0.0)

class CUserMessageAnimStateGraphState(BaseModel):
    entity_index: int = Field(default=0)
    data: bytes = Field(default=b"")

class CUserMessageUpdateCssClasses(BaseModel):
    target_world_panel: int = Field(default=0)
    css_classes: str = Field(default="")
    is_add: bool = Field(default=False)

class CUserMessageServerFrameTime(BaseModel):
    frame_time: float = Field(default=0.0)

class CUserMessageLagCompensationError(BaseModel):
    distance: float = Field(default=0.0)

class CUserMessageRequestDllStatus(BaseModel):
    dll_action: str = Field(default="")
    full_report: bool = Field(default=False)

class CUserMessageRequestUtilAction(BaseModel):
    util1: int = Field(default=0)
    util2: int = Field(default=0)
    util3: int = Field(default=0)
    util4: int = Field(default=0)
    util5: int = Field(default=0)

class CUserMessage_UtilMsg_Response(BaseModel):
    class ItemDetail(BaseModel):
        index: int = Field(default=0)
        hash: int = Field(default=0)
        crc: int = Field(default=0)
        name: str = Field(default="")

    crc: float = Field(default=0.0)
    item_count: int = Field(default=0)
    crc2: float = Field(default=0.0)
    item_count2: int = Field(default=0)
    crc_part: typing.List[int] = Field(default_factory=list)
    crc_part2: typing.List[int] = Field(default_factory=list)
    client_timestamp: int = Field(default=0)
    platform: int = Field(default=0)
    itemdetails: typing.List["CUserMessage_UtilMsg_Response.ItemDetail"] = Field(default_factory=list)
    itemgroup: int = Field(default=0)
    total_count: int = Field(default=0)
    total_count2: int = Field(default=0)

class CUserMessage_DllStatus(BaseModel):
    class CVDiagnostic(BaseModel):
        id: int = Field(default=0)
        extended: int = Field(default=0)
        value: int = Field(default=0)
        string_value: str = Field(default="")

    class CModule(BaseModel):
        base_addr: int = Field(default=0)
        name: str = Field(default="")
        size: int = Field(default=0)
        timestamp: int = Field(default=0)

    file_report: str = Field(default="")
    command_line: str = Field(default="")
    total_files: int = Field(default=0)
    process_id: int = Field(default=0)
    osversion: int = Field(default=0)
    client_time: int = Field(default=0)
    diagnostics: typing.List["CUserMessage_DllStatus.CVDiagnostic"] = Field(default_factory=list)
    modules: typing.List["CUserMessage_DllStatus.CModule"] = Field(default_factory=list)

class CUserMessageRequestInventory(BaseModel):
    inventory: int = Field(default=0)
    offset: int = Field(default=0)
    options: int = Field(default=0)

class CUserMessage_Inventory_Response(BaseModel):
    class InventoryDetail(BaseModel):
        index: int = Field(default=0)
        primary: int = Field(default=0)
        offset: int = Field(default=0)
        first: int = Field(default=0)
        base: int = Field(default=0)
        name: str = Field(default="")
        base_name: str = Field(default="")
        base_detail: int = Field(default=0)
        base_time: int = Field(default=0)
        base_hash: int = Field(default=0)

    crc: float = Field(default=0.0)
    item_count: int = Field(default=0)
    osversion: int = Field(default=0)
    perf_time: int = Field(default=0)
    client_timestamp: int = Field(default=0)
    platform: int = Field(default=0)
    inventories: typing.List["CUserMessage_Inventory_Response.InventoryDetail"] = Field(default_factory=list)
    inventories2: typing.List["CUserMessage_Inventory_Response.InventoryDetail"] = Field(default_factory=list)
    inventories3: typing.List["CUserMessage_Inventory_Response.InventoryDetail"] = Field(default_factory=list)
    inv_type: int = Field(default=0)
    build_version: int = Field(default=0)
    instance: int = Field(default=0)
    start_time: int = Field(default=0)

class CUserMessageRequestDiagnostic(BaseModel):
    class Diagnostic(BaseModel):
        index: int = Field(default=0)
        offset: int = Field(default=0)
        param: int = Field(default=0)
        length: int = Field(default=0)
        type: int = Field(default=0)
        base: int = Field(default=0)
        range: int = Field(default=0)
        extent: int = Field(default=0)
        detail: int = Field(default=0)
        name: str = Field(default="")
        alias: str = Field(default="")
        vardetail: bytes = Field(default=b"")
        context: int = Field(default=0)

    diagnostics: typing.List["CUserMessageRequestDiagnostic.Diagnostic"] = Field(default_factory=list)

class CUserMessage_Diagnostic_Response(BaseModel):
    class Diagnostic(BaseModel):
        index: int = Field(default=0)
        offset: int = Field(default=0)
        param: int = Field(default=0)
        length: int = Field(default=0)
        detail: bytes = Field(default=b"")
        base: int = Field(default=0)
        range: int = Field(default=0)
        type: int = Field(default=0)
        name: str = Field(default="")
        alias: str = Field(default="")
        backup: bytes = Field(default=b"")
        context: int = Field(default=0)
        control: int = Field(default=0)
        augment: int = Field(default=0)
        placebo: int = Field(default=0)

    diagnostics: typing.List["CUserMessage_Diagnostic_Response.Diagnostic"] = Field(default_factory=list)
    build_version: int = Field(default=0)
    instance: int = Field(default=0)
    start_time: int = Field(default=0)
    osversion: int = Field(default=0)
    platform: int = Field(default=0)

class CUserMessage_ExtraUserData(BaseModel):
    item: int = Field(default=0)
    value1: int = Field(default=0)
    value2: int = Field(default=0)
    detail1: typing.List[bytes] = Field(default_factory=list)
    detail2: typing.List[bytes] = Field(default_factory=list)

class CUserMessage_NotifyResponseFound(BaseModel):
    class Criteria(BaseModel):
        name_symbol: int = Field(default=0)
        value: str = Field(default="")

    ent_index: int = Field(default=0)
    rule_name: str = Field(default="")
    response_value: str = Field(default="")
    response_concept: str = Field(default="")
    criteria: typing.List["CUserMessage_NotifyResponseFound.Criteria"] = Field(default_factory=list)
    int_criteria_names: typing.List[int] = Field(default_factory=list)
    int_criteria_values: typing.List[int] = Field(default_factory=list)
    float_criteria_names: typing.List[int] = Field(default_factory=list)
    float_criteria_values: typing.List[float] = Field(default_factory=list)
    symbol_criteria_names: typing.List[int] = Field(default_factory=list)
    symbol_criteria_values: typing.List[int] = Field(default_factory=list)
    speak_result: int = Field(default=0)

class CUserMessage_PlayResponseConditional(BaseModel):
    ent_index: int = Field(default=0)
    player_slots: typing.List[int] = Field(default_factory=list)
    response: str = Field(default="")
    ent_origin: CMsgVector = Field()
    pre_delay: float = Field(default=0.0)
    mix_priority: int = Field(default=0)
