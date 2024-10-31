import citadel_gcmessages_common_pb2 as _citadel_gcmessages_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
k_ECitadelDisconnectReason_BadMessage: ECitadelDisconnectReason
k_ECitadelDisconnectReason_ChangingServer: ECitadelDisconnectReason
k_ECitadelDisconnectReason_GameDestroyedUnexpectedly: ECitadelDisconnectReason
k_ECitadelDisconnectReason_Goodbye: ECitadelDisconnectReason
k_ECitadelDisconnectReason_GoodbyeUnrecognizedGame: ECitadelDisconnectReason
k_ECitadelDisconnectReason_OldConnection: ECitadelDisconnectReason
k_ECitadelDisconnectReason_UserCancel: ECitadelDisconnectReason
k_ECitadelDisconnectReason_UserLeaveMatch: ECitadelDisconnectReason
k_ECitadelDisconnectReason_UserQuitApp: ECitadelDisconnectReason
k_EMsgGameServerToClientConnectionStatus: ECitadelGameMessages
k_EMsgGameServerToClientGameCompleted: ECitadelGameMessages
k_EMsgGameServerToClientGoodbye: ECitadelGameMessages
k_EMsgGameServerToClientInitialGameState: ECitadelGameMessages

class CClientReconnectInfo(_message.Message):
    __slots__ = ["compatibility_version", "lobby_id", "server_steam_id", "time_updated", "udp_connect_ip", "udp_connect_port"]
    COMPATIBILITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
    UDP_CONNECT_IP_FIELD_NUMBER: _ClassVar[int]
    UDP_CONNECT_PORT_FIELD_NUMBER: _ClassVar[int]
    compatibility_version: int
    lobby_id: int
    server_steam_id: int
    time_updated: int
    udp_connect_ip: int
    udp_connect_port: int
    def __init__(self, server_steam_id: _Optional[int] = ..., lobby_id: _Optional[int] = ..., time_updated: _Optional[int] = ..., udp_connect_ip: _Optional[int] = ..., udp_connect_port: _Optional[int] = ..., compatibility_version: _Optional[int] = ...) -> None: ...

class CMsgClientAccountSyncStorageFile(_message.Message):
    __slots__ = ["ids", "values", "version"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    version: int
    def __init__(self, version: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientServerHeader(_message.Message):
    __slots__ = ["game_instance_id", "local_player_index", "msg_id", "payload"]
    GAME_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PLAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    MSG_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    game_instance_id: int
    local_player_index: int
    msg_id: ECitadelGameMessages
    payload: bytes
    def __init__(self, game_instance_id: _Optional[int] = ..., local_player_index: _Optional[int] = ..., payload: _Optional[bytes] = ..., msg_id: _Optional[_Union[ECitadelGameMessages, str]] = ...) -> None: ...

class CMsgGameServerToClientConnectionStatus(_message.Message):
    __slots__ = ["players"]
    class EStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Player(_message.Message):
        __slots__ = ["inactivity_anim_ms_remaining", "inactivity_ms_remaining", "inactivity_ticking", "player_slot", "status"]
        INACTIVITY_ANIM_MS_REMAINING_FIELD_NUMBER: _ClassVar[int]
        INACTIVITY_MS_REMAINING_FIELD_NUMBER: _ClassVar[int]
        INACTIVITY_TICKING_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        inactivity_anim_ms_remaining: int
        inactivity_ms_remaining: int
        inactivity_ticking: bool
        player_slot: int
        status: CMsgGameServerToClientConnectionStatus.EStatus
        def __init__(self, player_slot: _Optional[int] = ..., status: _Optional[_Union[CMsgGameServerToClientConnectionStatus.EStatus, str]] = ..., inactivity_ticking: bool = ..., inactivity_ms_remaining: _Optional[int] = ..., inactivity_anim_ms_remaining: _Optional[int] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    k_EConnected: CMsgGameServerToClientConnectionStatus.EStatus
    k_EDisconnected: CMsgGameServerToClientConnectionStatus.EStatus
    players: _containers.RepeatedCompositeFieldContainer[CMsgGameServerToClientConnectionStatus.Player]
    def __init__(self, players: _Optional[_Iterable[_Union[CMsgGameServerToClientConnectionStatus.Player, _Mapping]]] = ...) -> None: ...

class CMsgGameServerToClientGameCompleted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgGameServerToClientGoodbye(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ECitadelGameMessages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelDisconnectReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
