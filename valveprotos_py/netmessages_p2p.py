# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .networkbasetypes_p2p import CMsgQAngle
from .networkbasetypes_p2p import CMsgVector
from .networkbasetypes_p2p import CSVCMsg_GameSessionConfiguration
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class CLC_Messages(IntEnum):
    clc_ClientInfo = 20
    clc_Move = 21
    clc_VoiceData = 22
    clc_BaselineAck = 23
    clc_RespondCvarValue = 25
    clc_FileCRCCheck = 26
    clc_LoadingProgress = 27
    clc_SplitPlayerConnect = 28
    clc_SplitPlayerDisconnect = 30
    clc_ServerStatus = 31
    clc_RequestPause = 33
    clc_CmdKeyValues = 34
    clc_RconServerDetails = 35
    clc_HltvReplay = 36
    clc_Diagnostic = 37


class SVC_Messages(IntEnum):
    svc_ServerInfo = 40
    svc_FlattenedSerializer = 41
    svc_ClassInfo = 42
    svc_SetPause = 43
    svc_CreateStringTable = 44
    svc_UpdateStringTable = 45
    svc_VoiceInit = 46
    svc_VoiceData = 47
    svc_Print = 48
    svc_Sounds = 49
    svc_SetView = 50
    svc_ClearAllStringTables = 51
    svc_CmdKeyValues = 52
    svc_BSPDecal = 53
    svc_SplitScreen = 54
    svc_PacketEntities = 55
    svc_Prefetch = 56
    svc_Menu = 57
    svc_GetCvarValue = 58
    svc_StopSound = 59
    svc_PeerList = 60
    svc_PacketReliable = 61
    svc_HLTVStatus = 62
    svc_ServerSteamID = 63
    svc_FullFrameSplit = 70
    svc_RconServerDetails = 71
    svc_UserMessage = 72
    svc_Broadcast_Command = 74
    svc_HltvFixupOperatorStatus = 75
    svc_UserCmds = 76


class VoiceDataFormat_t(IntEnum):
    VOICEDATA_FORMAT_STEAM = 0
    VOICEDATA_FORMAT_ENGINE = 1
    VOICEDATA_FORMAT_OPUS = 2


class RequestPause_t(IntEnum):
    RP_PAUSE = 0
    RP_UNPAUSE = 1
    RP_TOGGLEPAUSE = 2


class PrefetchType(IntEnum):
    PFT_SOUND = 0


class ESplitScreenMessageType(IntEnum):
    MSG_SPLITSCREEN_ADDUSER = 0
    MSG_SPLITSCREEN_REMOVEUSER = 1


class EQueryCvarValueStatus(IntEnum):
    eQueryCvarValueStatus_ValueIntact = 0
    eQueryCvarValueStatus_CvarNotFound = 1
    eQueryCvarValueStatus_NotACvar = 2
    eQueryCvarValueStatus_CvarProtected = 3


class DIALOG_TYPE(IntEnum):
    DIALOG_MSG = 0
    DIALOG_MENU = 1
    DIALOG_TEXT = 2
    DIALOG_ENTRY = 3
    DIALOG_ASKCONNECT = 4


class SVC_Messages_LowFrequency(IntEnum):
    svc_dummy = 600


class Bidirectional_Messages(IntEnum):
    bi_RebroadcastGameEvent = 16
    bi_RebroadcastSource = 17
    bi_GameEvent = 18
    bi_PredictionEvent = 19


class Bidirectional_Messages_LowFrequency(IntEnum):
    bi_RelayInfo = 700
    bi_RelayPacket = 701


class ReplayEventType_t(IntEnum):
    REPLAY_EVENT_CANCEL = 0
    REPLAY_EVENT_DEATH = 1
    REPLAY_EVENT_GENERIC = 2
    REPLAY_EVENT_STUCK_NEED_FULL_UPDATE = 3
    REPLAY_EVENT_VICTORY = 4

class CCLCMsg_ClientInfo(BaseModel):
    send_table_crc: float = Field(default=0.0)
    server_count: int = Field(default=0)
    is_hltv: bool = Field(default=False)
    friends_id: int = Field(default=0)
    friends_name: str = Field(default="")

class CCLCMsg_Move(BaseModel):
    data: bytes = Field(default=b"")
    last_command_number: int = Field(default=0)

class CMsgVoiceAudio(BaseModel):
    format: VoiceDataFormat_t = Field(default=0)
    voice_data: bytes = Field(default=b"")
    sequence_bytes: int = Field(default=0)
    section_number: int = Field(default=0)
    sample_rate: int = Field(default=0)
    uncompressed_sample_offset: int = Field(default=0)
    num_packets: int = Field(default=0)
    packet_offsets: typing.List[int] = Field(default_factory=list)
    voice_level: float = Field(default=0.0)

class CCLCMsg_VoiceData(BaseModel):
    audio: CMsgVoiceAudio = Field()
    xuid: float = Field(default=0.0)
    tick: int = Field(default=0)

class CCLCMsg_BaselineAck(BaseModel):
    baseline_tick: int = Field(default=0)
    baseline_nr: int = Field(default=0)

class CCLCMsg_ListenEvents(BaseModel):
    event_mask: typing.List[float] = Field(default_factory=list)

class CCLCMsg_RespondCvarValue(BaseModel):
    cookie: int = Field(default=0)
    status_code: int = Field(default=0)
    name: str = Field(default="")
    value: str = Field(default="")

class CCLCMsg_FileCRCCheck(BaseModel):
    code_path: int = Field(default=0)
    path: str = Field(default="")
    code_filename: int = Field(default=0)
    filename: str = Field(default="")
    crc: float = Field(default=0.0)

class CCLCMsg_LoadingProgress(BaseModel):
    progress: int = Field(default=0)

class CCLCMsg_SplitPlayerConnect(BaseModel):
    playername: str = Field(default="")

class CCLCMsg_SplitPlayerDisconnect(BaseModel):
    slot: int = Field(default=0)

class CCLCMsg_ServerStatus(BaseModel):
    simplified: bool = Field(default=False)

class CCLCMsg_RequestPause(BaseModel):
    pause_type: RequestPause_t = Field(default=0)
    pause_group: int = Field(default=0)

class CCLCMsg_CmdKeyValues(BaseModel):
    data: bytes = Field(default=b"")

class CCLCMsg_RconServerDetails(BaseModel):
    token: bytes = Field(default=b"")

class CMsgSource2SystemSpecs(BaseModel):
    cpu_id: str = Field(default="")
    cpu_brand: str = Field(default="")
    cpu_model: int = Field(default=0)
    cpu_num_physical: int = Field(default=0)
    ram_physical_total_mb: int = Field(default=0)
    gpu_rendersystem_dll_name: str = Field(default="")
    gpu_vendor_id: int = Field(default=0)
    gpu_driver_name: str = Field(default="")
    gpu_driver_version_high: int = Field(default=0)
    gpu_driver_version_low: int = Field(default=0)
    gpu_dx_support_level: int = Field(default=0)
    gpu_texture_memory_size_mb: int = Field(default=0)

class CMsgSource2VProfLiteReportItem(BaseModel):
    name: str = Field(default="")
    active_samples: int = Field(default=0)
    usec_max: int = Field(default=0)
    usec_avg_active: int = Field(default=0)
    usec_p50_active: int = Field(default=0)
    usec_p99_active: int = Field(default=0)
    usec_avg_all: int = Field(default=0)
    usec_p50_all: int = Field(default=0)
    usec_p99_all: int = Field(default=0)

class CMsgSource2VProfLiteReport(BaseModel):
    total: CMsgSource2VProfLiteReportItem = Field()
    items: typing.List[CMsgSource2VProfLiteReportItem] = Field(default_factory=list)
    discarded_frames: int = Field(default=0)

class CCLCMsg_Diagnostic(BaseModel):
    system_specs: CMsgSource2SystemSpecs = Field()
    vprof_report: CMsgSource2VProfLiteReport = Field()

class CSource2Metrics_MatchPerfSummary_Notification(BaseModel):
    class Client(BaseModel):
        system_specs: CMsgSource2SystemSpecs = Field()
        profile: CMsgSource2VProfLiteReport = Field()
        build_id: int = Field(default=0)
        steamid: float = Field(default=0.0)

    appid: int = Field(default=0)
    game_mode: str = Field(default="")
    server_build_id: int = Field(default=0)
    server_profile: CMsgSource2VProfLiteReport = Field()
    clients: typing.List["CSource2Metrics_MatchPerfSummary_Notification.Client"] = Field(default_factory=list)
    map: str = Field(default="")

class CSVCMsg_ServerInfo(BaseModel):
    protocol: int = Field(default=0)
    server_count: int = Field(default=0)
    is_dedicated: bool = Field(default=False)
    is_hltv: bool = Field(default=False)
    c_os: int = Field(default=0)
    max_clients: int = Field(default=0)
    max_classes: int = Field(default=0)
    player_slot: int = Field(default=0)
    tick_interval: float = Field(default=0.0)
    game_dir: str = Field(default="")
    map_name: str = Field(default="")
    sky_name: str = Field(default="")
    host_name: str = Field(default="")
    addon_name: str = Field(default="")
    game_session_config: CSVCMsg_GameSessionConfiguration = Field()
    game_session_manifest: bytes = Field(default=b"")

class CSVCMsg_ClassInfo(BaseModel):
    class class_t(BaseModel):
        class_id: int = Field(default=0)
        class_name: str = Field(default="")

    create_on_client: bool = Field(default=False)
    classes: typing.List["CSVCMsg_ClassInfo.class_t"] = Field(default_factory=list)

class CSVCMsg_SetPause(BaseModel):
    paused: bool = Field(default=False)

class CSVCMsg_VoiceInit(BaseModel):
    quality: int = Field(default=0)
    codec: str = Field(default="")
    version: int = Field(default=0)

class CSVCMsg_Print(BaseModel):
    text: str = Field(default="")

class CSVCMsg_Sounds(BaseModel):
    class sounddata_t(BaseModel):
        origin_x: int = Field(default=0)
        origin_y: int = Field(default=0)
        origin_z: int = Field(default=0)
        volume: int = Field(default=0)
        delay_value: float = Field(default=0.0)
        sequence_number: int = Field(default=0)
        entity_index: int = Field(default=0)
        channel: int = Field(default=0)
        pitch: int = Field(default=0)
        flags: int = Field(default=0)
        sound_num: int = Field(default=0)
        sound_num_handle: float = Field(default=0.0)
        speaker_entity: int = Field(default=0)
        random_seed: int = Field(default=0)
        sound_level: int = Field(default=0)
        is_sentence: bool = Field(default=False)
        is_ambient: bool = Field(default=False)
        guid: int = Field(default=0)
        sound_resource_id: float = Field(default=0.0)

    reliable_sound: bool = Field(default=False)
    sounds: typing.List["CSVCMsg_Sounds.sounddata_t"] = Field(default_factory=list)

class CSVCMsg_Prefetch(BaseModel):
    sound_index: int = Field(default=0)
    resource_type: PrefetchType = Field(default=0)

class CSVCMsg_SetView(BaseModel):
    entity_index: int = Field(default=0)
    slot: int = Field(default=0)

class CSVCMsg_FixAngle(BaseModel):
    relative: bool = Field(default=False)
    angle: CMsgQAngle = Field()

class CSVCMsg_CrosshairAngle(BaseModel):
    angle: CMsgQAngle = Field()

class CSVCMsg_BSPDecal(BaseModel):
    pos: CMsgVector = Field()
    decal_texture_index: int = Field(default=0)
    entity_index: int = Field(default=0)
    model_index: int = Field(default=0)
    low_priority: bool = Field(default=False)

class CSVCMsg_SplitScreen(BaseModel):
    type: ESplitScreenMessageType = Field(default=0)
    slot: int = Field(default=0)
    player_index: int = Field(default=0)

class CSVCMsg_GetCvarValue(BaseModel):
    cookie: int = Field(default=0)
    cvar_name: str = Field(default="")

class CSVCMsg_Menu(BaseModel):
    dialog_type: int = Field(default=0)
    menu_key_values: bytes = Field(default=b"")

class CSVCMsg_UserMessage(BaseModel):
    msg_type: int = Field(default=0)
    msg_data: bytes = Field(default=b"")
    passthrough: int = Field(default=0)

class CSVCMsg_SendTable(BaseModel):
    class sendprop_t(BaseModel):
        type: int = Field(default=0)
        var_name: str = Field(default="")
        flags: int = Field(default=0)
        priority: int = Field(default=0)
        dt_name: str = Field(default="")
        num_elements: int = Field(default=0)
        low_value: float = Field(default=0.0)
        high_value: float = Field(default=0.0)
        num_bits: int = Field(default=0)

    is_end: bool = Field(default=False)
    net_table_name: str = Field(default="")
    needs_decoder: bool = Field(default=False)
    props: typing.List["CSVCMsg_SendTable.sendprop_t"] = Field(default_factory=list)

class CSVCMsg_GameEventList(BaseModel):
    class key_t(BaseModel):
        type: int = Field(default=0)
        name: str = Field(default="")

    class descriptor_t(BaseModel):
        eventid: int = Field(default=0)
        name: str = Field(default="")
        keys: typing.List["CSVCMsg_GameEventList.key_t"] = Field(default_factory=list)

    descriptors: typing.List["CSVCMsg_GameEventList.descriptor_t"] = Field(default_factory=list)

class CSVCMsg_PacketEntities(BaseModel):
    class alternate_baseline_t(BaseModel):
        entity_index: int = Field(default=0)
        baseline_index: int = Field(default=0)

    class non_transmitted_entities_t(BaseModel):
        header_count: int = Field(default=0)
        data: bytes = Field(default=b"")

    max_entries: int = Field(default=0)
    updated_entries: int = Field(default=0)
    legacy_is_delta: bool = Field(default=False)
    update_baseline: bool = Field(default=False)
    baseline: int = Field(default=0)
    delta_from: int = Field(default=0)
    entity_data: bytes = Field(default=b"")
    pending_full_frame: bool = Field(default=False)
    active_spawngroup_handle: int = Field(default=0)
    max_spawngroup_creationsequence: int = Field(default=0)
    last_cmd_number_executed: int = Field(default=0)
    last_cmd_number_recv_delta: int = Field(default=0)
    server_tick: int = Field(default=0)
    serialized_entities: bytes = Field(default=b"")
    alternate_baselines: typing.List["CSVCMsg_PacketEntities.alternate_baseline_t"] = Field(default_factory=list)
    has_pvs_vis_bits_deprecated: int = Field(default=0)
    cmd_recv_status: typing.List[int] = Field(default_factory=list)
    non_transmitted_entities: "CSVCMsg_PacketEntities.non_transmitted_entities_t" = Field()
    cq_starved_command_ticks: int = Field(default=0)
    cq_discarded_command_ticks: int = Field(default=0)
    dev_padding: bytes = Field(default=b"")

class CSVCMsg_TempEntities(BaseModel):
    reliable: bool = Field(default=False)
    num_entries: int = Field(default=0)
    entity_data: bytes = Field(default=b"")

class CSVCMsg_CreateStringTable(BaseModel):
    name: str = Field(default="")
    num_entries: int = Field(default=0)
    user_data_fixed_size: bool = Field(default=False)
    user_data_size: int = Field(default=0)
    user_data_size_bits: int = Field(default=0)
    flags: int = Field(default=0)
    string_data: bytes = Field(default=b"")
    uncompressed_size: int = Field(default=0)
    data_compressed: bool = Field(default=False)
    using_varint_bitcounts: bool = Field(default=False)

class CSVCMsg_UpdateStringTable(BaseModel):
    table_id: int = Field(default=0)
    num_changed_entries: int = Field(default=0)
    string_data: bytes = Field(default=b"")

class CSVCMsg_VoiceData(BaseModel):
    audio: CMsgVoiceAudio = Field()
    client: int = Field(default=0)
    proximity: bool = Field(default=False)
    xuid: float = Field(default=0.0)
    audible_mask: int = Field(default=0)
    tick: int = Field(default=0)
    passthrough: int = Field(default=0)

class CSVCMsg_PacketReliable(BaseModel):
    tick: int = Field(default=0)
    messagessize: int = Field(default=0)
    state: bool = Field(default=False)

class CSVCMsg_FullFrameSplit(BaseModel):
    tick: int = Field(default=0)
    section: int = Field(default=0)
    total: int = Field(default=0)
    data: bytes = Field(default=b"")

class CSVCMsg_HLTVStatus(BaseModel):
    master: str = Field(default="")
    clients: int = Field(default=0)
    slots: int = Field(default=0)
    proxies: int = Field(default=0)

class CSVCMsg_ServerSteamID(BaseModel):
    steam_id: int = Field(default=0)

class CSVCMsg_CmdKeyValues(BaseModel):
    data: bytes = Field(default=b"")

class CSVCMsg_RconServerDetails(BaseModel):
    token: bytes = Field(default=b"")
    details: str = Field(default="")

class CMsgIPCAddress(BaseModel):
    computer_guid: float = Field(default=0.0)
    process_id: int = Field(default=0)

class CMsgServerPeer(BaseModel):
    player_slot: int = Field(default=0)
    steamid: float = Field(default=0.0)
    ipc: CMsgIPCAddress = Field()
    they_hear_you: bool = Field(default=False)
    you_hear_them: bool = Field(default=False)
    is_listenserver_host: bool = Field(default=False)

class CSVCMsg_PeerList(BaseModel):
    peer: typing.List[CMsgServerPeer] = Field(default_factory=list)

class CSVCMsg_ClearAllStringTables(BaseModel):
    mapname: str = Field(default="")
    create_tables_skipped: bool = Field(default=False)

class ProtoFlattenedSerializerField_t(BaseModel):
    class polymorphic_field_t(BaseModel):
        polymorphic_field_serializer_name_sym: int = Field(default=0)
        polymorphic_field_serializer_version: int = Field(default=0)

    var_type_sym: int = Field(default=0)
    var_name_sym: int = Field(default=0)
    bit_count: int = Field(default=0)
    low_value: float = Field(default=0.0)
    high_value: float = Field(default=0.0)
    encode_flags: int = Field(default=0)
    field_serializer_name_sym: int = Field(default=0)
    field_serializer_version: int = Field(default=0)
    send_node_sym: int = Field(default=0)
    var_encoder_sym: int = Field(default=0)
    polymorphic_types: typing.List["ProtoFlattenedSerializerField_t.polymorphic_field_t"] = Field(default_factory=list)
    var_serializer_sym: int = Field(default=0)

class ProtoFlattenedSerializer_t(BaseModel):
    serializer_name_sym: int = Field(default=0)
    serializer_version: int = Field(default=0)
    fields_index: typing.List[int] = Field(default_factory=list)

class CSVCMsg_FlattenedSerializer(BaseModel):
    serializers: typing.List[ProtoFlattenedSerializer_t] = Field(default_factory=list)
    symbols: typing.List[str] = Field(default_factory=list)
    fields: typing.List[ProtoFlattenedSerializerField_t] = Field(default_factory=list)

class CSVCMsg_StopSound(BaseModel):
    guid: float = Field(default=0.0)

class CBidirMsg_RebroadcastGameEvent(BaseModel):
    posttoserver: bool = Field(default=False)
    buftype: int = Field(default=0)
    clientbitcount: int = Field(default=0)
    receivingclients: int = Field(default=0)

class CBidirMsg_RebroadcastSource(BaseModel):
    eventsource: int = Field(default=0)

class CBidirMsg_PredictionEvent(BaseModel):
    class ESyncType(IntEnum):
        ST_Tick = 0
        ST_UserCmdNum = 1

    event_id: int = Field(default=0)
    event_data: bytes = Field(default=b"")
    sync_type: int = Field(default=0)
    sync_val_uint32: int = Field(default=0)

class CMsgServerNetworkStats(BaseModel):
    class Port(BaseModel):
        port: int = Field(default=0)
        name: str = Field(default="")

    class Player(BaseModel):
        steamid: int = Field(default=0)
        remote_addr: str = Field(default="")
        ping_avg_ms: int = Field(default=0)
        packet_loss_pct: float = Field(default=0.0)
        is_bot: bool = Field(default=False)
        loss_in: float = Field(default=0.0)
        loss_out: float = Field(default=0.0)
        engine_latency_ms: int = Field(default=0)

    dedicated: bool = Field(default=False)
    cpu_usage: int = Field(default=0)
    memory_used_mb: int = Field(default=0)
    memory_free_mb: int = Field(default=0)
    uptime: int = Field(default=0)
    spawn_count: int = Field(default=0)
    num_clients: int = Field(default=0)
    num_bots: int = Field(default=0)
    num_spectators: int = Field(default=0)
    num_tv_relays: int = Field(default=0)
    fps: float = Field(default=0.0)
    ports: typing.List["CMsgServerNetworkStats.Port"] = Field(default_factory=list)
    avg_ping_ms: float = Field(default=0.0)
    avg_engine_latency_out: float = Field(default=0.0)
    avg_packets_out: float = Field(default=0.0)
    avg_packets_in: float = Field(default=0.0)
    avg_loss_out: float = Field(default=0.0)
    avg_loss_in: float = Field(default=0.0)
    avg_data_out: float = Field(default=0.0)
    avg_data_in: float = Field(default=0.0)
    total_data_in: int = Field(default=0)
    total_packets_in: int = Field(default=0)
    total_data_out: int = Field(default=0)
    total_packets_out: int = Field(default=0)
    players: typing.List["CMsgServerNetworkStats.Player"] = Field(default_factory=list)

class CSVCMsg_HltvReplay(BaseModel):
    delay: int = Field(default=0)
    primary_target: int = Field(default=0)
    replay_stop_at: int = Field(default=0)
    replay_start_at: int = Field(default=0)
    replay_slowdown_begin: int = Field(default=0)
    replay_slowdown_end: int = Field(default=0)
    replay_slowdown_rate: float = Field(default=0.0)
    reason: int = Field(default=0)

class CCLCMsg_HltvReplay(BaseModel):
    request: int = Field(default=0)
    slowdown_length: float = Field(default=0.0)
    slowdown_rate: float = Field(default=0.0)
    primary_target: int = Field(default=0)
    event_time: float = Field(default=0.0)

class CSVCMsg_Broadcast_Command(BaseModel):
    cmd: str = Field(default="")

class CCLCMsg_HltvFixupOperatorTick(BaseModel):
    tick: int = Field(default=0)
    props_data: bytes = Field(default=b"")
    origin: CMsgVector = Field()
    eye_angles: CMsgQAngle = Field()
    observer_mode: int = Field(default=0)
    cameraman_scoreboard: bool = Field(default=False)
    observer_target: int = Field(default=0)
    view_offset: CMsgVector = Field()

class CSVCMsg_HltvFixupOperatorStatus(BaseModel):
    mode: int = Field(default=0)
    override_operator_name: str = Field(default="")

class CMsgServerUserCmd(BaseModel):
    data: bytes = Field(default=b"")
    cmd_number: int = Field(default=0)
    player_slot: int = Field(default=0)
    server_tick_executed: int = Field(default=0)
    client_tick: int = Field(default=0)

class CSVCMsg_UserCommands(BaseModel):
    commands: typing.List[CMsgServerUserCmd] = Field(default_factory=list)
