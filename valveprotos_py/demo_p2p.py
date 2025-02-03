# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class EDemoCommands(IntEnum):
    DEM_Error = -1
    DEM_Stop = 0
    DEM_FileHeader = 1
    DEM_FileInfo = 2
    DEM_SyncTick = 3
    DEM_SendTables = 4
    DEM_ClassInfo = 5
    DEM_StringTables = 6
    DEM_Packet = 7
    DEM_SignonPacket = 8
    DEM_ConsoleCmd = 9
    DEM_CustomData = 10
    DEM_CustomDataCallbacks = 11
    DEM_UserCmd = 12
    DEM_FullPacket = 13
    DEM_SaveGame = 14
    DEM_SpawnGroups = 15
    DEM_AnimationData = 16
    DEM_AnimationHeader = 17
    DEM_Recovery = 18
    DEM_Max = 19
    DEM_IsCompressed = 64

class CDemoFileHeader(BaseModel):
    demo_file_stamp: str = Field(default="")
    network_protocol: int = Field(default=0)
    server_name: str = Field(default="")
    client_name: str = Field(default="")
    map_name: str = Field(default="")
    game_directory: str = Field(default="")
    fullpackets_version: int = Field(default=0)
    allow_clientside_entities: bool = Field(default=False)
    allow_clientside_particles: bool = Field(default=False)
    addons: str = Field(default="")
    demo_version_name: str = Field(default="")
    demo_version_guid: str = Field(default="")
    build_num: int = Field(default=0)
    game: str = Field(default="")
    server_start_tick: int = Field(default=0)

class CGameInfo(BaseModel):
    class CDotaGameInfo(BaseModel):
        class CPlayerInfo(BaseModel):
            hero_name: str = Field(default="")
            player_name: str = Field(default="")
            is_fake_client: bool = Field(default=False)
            steamid: int = Field(default=0)
            game_team: int = Field(default=0)

        class CHeroSelectEvent(BaseModel):
            is_pick: bool = Field(default=False)
            team: int = Field(default=0)
            hero_id: int = Field(default=0)

        match_id: int = Field(default=0)
        game_mode: int = Field(default=0)
        game_winner: int = Field(default=0)
        player_info: typing.List[CPlayerInfo] = Field(default_factory=list)
        leagueid: int = Field(default=0)
        picks_bans: typing.List[CHeroSelectEvent] = Field(default_factory=list)
        radiant_team_id: int = Field(default=0)
        dire_team_id: int = Field(default=0)
        radiant_team_tag: str = Field(default="")
        dire_team_tag: str = Field(default="")
        end_time: int = Field(default=0)

    class CCSGameInfo(BaseModel):
        round_start_ticks: typing.List[int] = Field(default_factory=list)

    dota: "CGameInfo.CDotaGameInfo" = Field()
    cs: "CGameInfo.CCSGameInfo" = Field()

class CDemoFileInfo(BaseModel):
    playback_time: float = Field(default=0.0)
    playback_ticks: int = Field(default=0)
    playback_frames: int = Field(default=0)
    game_info: CGameInfo = Field()

class CDemoPacket(BaseModel):
    data: bytes = Field(default=b"")

class CDemoStringTables(BaseModel):
    class items_t(BaseModel):
        str: str = Field(default="")
        data: bytes = Field(default=b"")

    class table_t(BaseModel):
        table_name: str = Field(default="")
        items: typing.List["CDemoStringTables.items_t"] = Field(default_factory=list)
        items_clientside: typing.List["CDemoStringTables.items_t"] = Field(default_factory=list)
        table_flags: int = Field(default=0)

    tables: typing.List[table_t] = Field(default_factory=list)

class CDemoFullPacket(BaseModel):
    string_table: CDemoStringTables = Field()
    packet: CDemoPacket = Field()

class CDemoSaveGame(BaseModel):
    data: bytes = Field(default=b"")
    steam_id: float = Field(default=0.0)
    signature: float = Field(default=0.0)
    version: int = Field(default=0)

class CDemoSyncTick(BaseModel):
    pass

class CDemoConsoleCmd(BaseModel):
    cmdstring: str = Field(default="")

class CDemoSendTables(BaseModel):
    data: bytes = Field(default=b"")

class CDemoClassInfo(BaseModel):
    class class_t(BaseModel):
        class_id: int = Field(default=0)
        network_name: str = Field(default="")
        table_name: str = Field(default="")

    classes: typing.List["CDemoClassInfo.class_t"] = Field(default_factory=list)

class CDemoCustomData(BaseModel):
    callback_index: int = Field(default=0)
    data: bytes = Field(default=b"")

class CDemoCustomDataCallbacks(BaseModel):
    save_id: typing.List[str] = Field(default_factory=list)

class CDemoAnimationHeader(BaseModel):
    entity_id: int = Field(default=0)
    tick: int = Field(default=0)
    data: bytes = Field(default=b"")

class CDemoAnimationData(BaseModel):
    entity_id: int = Field(default=0)
    start_tick: int = Field(default=0)
    end_tick: int = Field(default=0)
    data: bytes = Field(default=b"")
    data_checksum: int = Field(default=0)

class CDemoStop(BaseModel):
    pass

class CDemoUserCmd(BaseModel):
    cmd_number: int = Field(default=0)
    data: bytes = Field(default=b"")

class CDemoSpawnGroups(BaseModel):
    msgs: typing.List[bytes] = Field(default_factory=list)

class CDemoRecovery(BaseModel):
    class DemoInitialSpawnGroupEntry(BaseModel):
        spawngrouphandle: int = Field(default=0)
        was_created: bool = Field(default=False)

    initial_spawn_group: "CDemoRecovery.DemoInitialSpawnGroupEntry" = Field()
    spawn_group_message: bytes = Field(default=b"")
