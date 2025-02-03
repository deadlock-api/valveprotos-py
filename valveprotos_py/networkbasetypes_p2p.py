# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class SignonState_t(IntEnum):
    SIGNONSTATE_NONE = 0
    SIGNONSTATE_CHALLENGE = 1
    SIGNONSTATE_CONNECTED = 2
    SIGNONSTATE_NEW = 3
    SIGNONSTATE_PRESPAWN = 4
    SIGNONSTATE_SPAWN = 5
    SIGNONSTATE_FULL = 6
    SIGNONSTATE_CHANGELEVEL = 7


class NET_Messages(IntEnum):
    net_NOP = 0
    net_Disconnect_Legacy = 1
    net_SplitScreenUser = 3
    net_Tick = 4
    net_StringCmd = 5
    net_SetConVar = 6
    net_SignonState = 7
    net_SpawnGroup_Load = 8
    net_SpawnGroup_ManifestUpdate = 9
    net_SpawnGroup_SetCreationTick = 11
    net_SpawnGroup_Unload = 12
    net_SpawnGroup_LoadCompleted = 13
    net_DebugOverlay = 15


class SpawnGroupFlags_t(IntEnum):
    SPAWN_GROUP_LOAD_ENTITIES_FROM_SAVE = 1
    SPAWN_GROUP_DONT_SPAWN_ENTITIES = 2
    SPAWN_GROUP_SYNCHRONOUS_SPAWN = 4
    SPAWN_GROUP_IS_INITIAL_SPAWN_GROUP = 8
    SPAWN_GROUP_CREATE_CLIENT_ONLY_ENTITIES = 16
    SPAWN_GROUP_BLOCK_UNTIL_LOADED = 64
    SPAWN_GROUP_LOAD_STREAMING_DATA = 128
    SPAWN_GROUP_CREATE_NEW_SCENE_WORLD = 256

class CMsgVector(BaseModel):
    x: float = Field(default=0.0)
    y: float = Field(default=0.0)
    z: float = Field(default=0.0)
    w: float = Field(default=0.0)

class CMsgVector2D(BaseModel):
    x: float = Field(default=0.0)
    y: float = Field(default=0.0)

class CMsgQAngle(BaseModel):
    x: float = Field(default=0.0)
    y: float = Field(default=0.0)
    z: float = Field(default=0.0)

class CMsgQuaternion(BaseModel):
    x: float = Field(default=0.0)
    y: float = Field(default=0.0)
    z: float = Field(default=0.0)
    w: float = Field(default=0.0)

class CMsgTransform(BaseModel):
    position: CMsgVector = Field()
    scale: float = Field(default=0.0)
    orientation: CMsgQuaternion = Field()

class CMsgRGBA(BaseModel):
    r: int = Field(default=0)
    g: int = Field(default=0)
    b: int = Field(default=0)
    a: int = Field(default=0)

class CMsgPlayerInfo(BaseModel):
    name: str = Field(default="")
    xuid: float = Field(default=0.0)
    userid: int = Field(default=0)
    steamid: float = Field(default=0.0)
    fakeplayer: bool = Field(default=False)
    ishltv: bool = Field(default=False)

class CEntityMsg(BaseModel):
    target_entity: int = Field(default=0)

class CMsg_CVars(BaseModel):
    class CVar(BaseModel):
        name: str = Field(default="")
        value: str = Field(default="")

    cvars: typing.List["CMsg_CVars.CVar"] = Field(default_factory=list)

class CNETMsg_NOP(BaseModel):
    pass

class CNETMsg_SplitScreenUser(BaseModel):
    slot: int = Field(default=0)

class CNETMsg_Tick(BaseModel):
    tick: int = Field(default=0)
    host_computationtime: int = Field(default=0)
    host_computationtime_std_deviation: int = Field(default=0)
    legacy_host_loss: int = Field(default=0)
    host_unfiltered_frametime: int = Field(default=0)
    hltv_replay_flags: int = Field(default=0)
    expected_long_tick: int = Field(default=0)
    expected_long_tick_reason: str = Field(default="")
    host_frame_dropped_pct_x10: int = Field(default=0)
    host_frame_irregular_arrival_pct_x10: int = Field(default=0)

class CNETMsg_StringCmd(BaseModel):
    command: str = Field(default="")
    prediction_sync: int = Field(default=0)

class CNETMsg_SetConVar(BaseModel):
    convars: CMsg_CVars = Field()

class CNETMsg_SignonState(BaseModel):
    signon_state: SignonState_t = Field(default=0)
    spawn_count: int = Field(default=0)
    num_server_players: int = Field(default=0)
    players_networkids: typing.List[str] = Field(default_factory=list)
    map_name: str = Field(default="")
    addons: str = Field(default="")

class CSVCMsg_GameEvent(BaseModel):
    class key_t(BaseModel):
        type: int = Field(default=0)
        val_string: str = Field(default="")
        val_float: float = Field(default=0.0)
        val_long: int = Field(default=0)
        val_short: int = Field(default=0)
        val_byte: int = Field(default=0)
        val_bool: bool = Field(default=False)
        val_uint64: int = Field(default=0)

    event_name: str = Field(default="")
    eventid: int = Field(default=0)
    keys: typing.List["CSVCMsg_GameEvent.key_t"] = Field(default_factory=list)

class CSVCMsgList_GameEvents(BaseModel):
    class event_t(BaseModel):
        tick: int = Field(default=0)
        event: CSVCMsg_GameEvent = Field()

    events: typing.List["CSVCMsgList_GameEvents.event_t"] = Field(default_factory=list)

class CNETMsg_SpawnGroup_Load(BaseModel):
    worldname: str = Field(default="")
    entitylumpname: str = Field(default="")
    entityfiltername: str = Field(default="")
    spawngrouphandle: int = Field(default=0)
    spawngroupownerhandle: int = Field(default=0)
    world_offset_pos: CMsgVector = Field()
    world_offset_angle: CMsgQAngle = Field()
    spawngroupmanifest: bytes = Field(default=b"")
    flags: int = Field(default=0)
    tickcount: int = Field(default=0)
    manifestincomplete: bool = Field(default=False)
    localnamefixup: str = Field(default="")
    parentnamefixup: str = Field(default="")
    manifestloadpriority: int = Field(default=0)
    worldgroupid: int = Field(default=0)
    creationsequence: int = Field(default=0)
    savegamefilename: str = Field(default="")
    spawngroupparenthandle: int = Field(default=0)
    leveltransition: bool = Field(default=False)
    worldgroupname: str = Field(default="")

class CNETMsg_SpawnGroup_ManifestUpdate(BaseModel):
    spawngrouphandle: int = Field(default=0)
    spawngroupmanifest: bytes = Field(default=b"")
    manifestincomplete: bool = Field(default=False)

class CNETMsg_SpawnGroup_SetCreationTick(BaseModel):
    spawngrouphandle: int = Field(default=0)
    tickcount: int = Field(default=0)
    creationsequence: int = Field(default=0)

class CNETMsg_SpawnGroup_Unload(BaseModel):
    spawngrouphandle: int = Field(default=0)
    flags: int = Field(default=0)
    tickcount: int = Field(default=0)

class CNETMsg_SpawnGroup_LoadCompleted(BaseModel):
    spawngrouphandle: int = Field(default=0)

class CSVCMsg_GameSessionConfiguration(BaseModel):
    is_multiplayer: bool = Field(default=False)
    is_loadsavegame: bool = Field(default=False)
    is_background_map: bool = Field(default=False)
    is_headless: bool = Field(default=False)
    min_client_limit: int = Field(default=0)
    max_client_limit: int = Field(default=0)
    max_clients: int = Field(default=0)
    tick_interval: float = Field(default=0.0)
    hostname: str = Field(default="")
    savegamename: str = Field(default="")
    s1_mapname: str = Field(default="")
    gamemode: str = Field(default="")
    server_ip_address: str = Field(default="")
    data: bytes = Field(default=b"")
    is_localonly: bool = Field(default=False)
    no_steam_server: bool = Field(default=False)
    is_transition: bool = Field(default=False)
    previouslevel: str = Field(default="")
    landmarkname: str = Field(default="")

class CNETMsg_DebugOverlay(BaseModel):
    etype: int = Field(default=0)
    vectors: typing.List[CMsgVector] = Field(default_factory=list)
    colors: typing.List[CMsgRGBA] = Field(default_factory=list)
    dimensions: typing.List[float] = Field(default_factory=list)
    times: typing.List[float] = Field(default_factory=list)
    bools: typing.List[bool] = Field(default_factory=list)
    uint64s: typing.List[int] = Field(default_factory=list)
    strings: typing.List[str] = Field(default_factory=list)
