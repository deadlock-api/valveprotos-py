# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class ECitadelGameMessages(IntEnum):
    k_EMsgGameServerToClientConnectionStatus = 10
    k_EMsgGameServerToClientInitialGameState = 12
    k_EMsgGameServerToClientGameCompleted = 13
    k_EMsgGameServerToClientGoodbye = 15


class ECitadelDisconnectReason(IntEnum):
    k_ECitadelDisconnectReason_UserLeaveMatch = 1001
    k_ECitadelDisconnectReason_UserQuitApp = 1002
    k_ECitadelDisconnectReason_UserCancel = 1003
    k_ECitadelDisconnectReason_Goodbye = 1004
    k_ECitadelDisconnectReason_BadMessage = 2001
    k_ECitadelDisconnectReason_GameDestroyedUnexpectedly = 2002
    k_ECitadelDisconnectReason_ChangingServer = 2003
    k_ECitadelDisconnectReason_OldConnection = 2004
    k_ECitadelDisconnectReason_GoodbyeUnrecognizedGame = 2005

class CMsgClientServerHeader(BaseModel):
    game_instance_id: int = Field(default=0)
    local_player_index: int = Field(default=0)
    payload: bytes = Field(default=b"")
    msg_id: ECitadelGameMessages = Field(default=0)

class CMsgGameServerToClientGameCompleted(BaseModel):
    pass

class CMsgGameServerToClientGoodbye(BaseModel):
    pass

class CMsgGameServerToClientConnectionStatus(BaseModel):
    class Player(BaseModel):
        player_slot: int = Field(default=0)
        status: "CMsgGameServerToClientConnectionStatus.EStatus" = Field(default=0)
        inactivity_ticking: bool = Field(default=False)
        inactivity_ms_remaining: int = Field(default=0)
        inactivity_anim_ms_remaining: int = Field(default=0)

    class EStatus(IntEnum):
        k_EConnected = 1
        k_EDisconnected = 2

    players: typing.List["CMsgGameServerToClientConnectionStatus.Player"] = Field(default_factory=list)

class CClientReconnectInfo(BaseModel):
    server_steam_id: float = Field(default=0.0)
    lobby_id: int = Field(default=0)
    time_updated: int = Field(default=0)
    udp_connect_ip: int = Field(default=0)
    udp_connect_port: int = Field(default=0)
    compatibility_version: int = Field(default=0)

class CMsgClientAccountSyncStorageFile(BaseModel):
    version: int = Field(default=0)
    ids: typing.List[int] = Field(default_factory=list)
    values: typing.List[int] = Field(default_factory=list)
