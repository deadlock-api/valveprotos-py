# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .networkbasetypes_p2p import CMsgVector
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class EBaseGameEvents(IntEnum):
    GE_VDebugGameSessionIDEvent = 200
    GE_PlaceDecalEvent = 201
    GE_ClearWorldDecalsEvent = 202
    GE_ClearEntityDecalsEvent = 203
    GE_ClearDecalsForSkeletonInstanceEvent = 204
    GE_Source1LegacyGameEventList = 205
    GE_Source1LegacyListenEvents = 206
    GE_Source1LegacyGameEvent = 207
    GE_SosStartSoundEvent = 208
    GE_SosStopSoundEvent = 209
    GE_SosSetSoundEventParams = 210
    GE_SosSetLibraryStackFields = 211
    GE_SosStopSoundEventHash = 212

class CMsgVDebugGameSessionIDEvent(BaseModel):
    clientid: int = Field(default=0)
    gamesessionid: str = Field(default="")

class CMsgPlaceDecalEvent(BaseModel):
    position: CMsgVector = Field()
    normal: CMsgVector = Field()
    saxis: CMsgVector = Field()
    decalmaterialindex: int = Field(default=0)
    flags: int = Field(default=0)
    color: float = Field(default=0.0)
    width: float = Field(default=0.0)
    height: float = Field(default=0.0)
    depth: float = Field(default=0.0)
    entityhandleindex: int = Field(default=0)
    skeletoninstancehash: float = Field(default=0.0)
    boneindex: int = Field(default=0)
    translucenthit: bool = Field(default=False)
    is_adjacent: bool = Field(default=False)

class CMsgClearWorldDecalsEvent(BaseModel):
    flagstoclear: int = Field(default=0)

class CMsgClearEntityDecalsEvent(BaseModel):
    flagstoclear: int = Field(default=0)

class CMsgClearDecalsForSkeletonInstanceEvent(BaseModel):
    flagstoclear: int = Field(default=0)
    entityhandleindex: int = Field(default=0)
    skeletoninstancehash: int = Field(default=0)

class CMsgSource1LegacyGameEventList(BaseModel):
    class key_t(BaseModel):
        type: int = Field(default=0)
        name: str = Field(default="")

    class descriptor_t(BaseModel):
        eventid: int = Field(default=0)
        name: str = Field(default="")
        keys: typing.List["CMsgSource1LegacyGameEventList.key_t"] = Field(default_factory=list)

    descriptors: typing.List["CMsgSource1LegacyGameEventList.descriptor_t"] = Field(default_factory=list)

class CMsgSource1LegacyListenEvents(BaseModel):
    playerslot: int = Field(default=0)
    eventarraybits: typing.List[int] = Field(default_factory=list)

class CMsgSource1LegacyGameEvent(BaseModel):
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
    keys: typing.List["CMsgSource1LegacyGameEvent.key_t"] = Field(default_factory=list)
    server_tick: int = Field(default=0)
    passthrough: int = Field(default=0)

class CMsgSosStartSoundEvent(BaseModel):
    soundevent_guid: int = Field(default=0)
    soundevent_hash: float = Field(default=0.0)
    source_entity_index: int = Field(default=0)
    seed: int = Field(default=0)
    packed_params: bytes = Field(default=b"")
    start_time: float = Field(default=0.0)

class CMsgSosStopSoundEvent(BaseModel):
    soundevent_guid: int = Field(default=0)

class CMsgSosStopSoundEventHash(BaseModel):
    soundevent_hash: float = Field(default=0.0)
    source_entity_index: int = Field(default=0)

class CMsgSosSetSoundEventParams(BaseModel):
    soundevent_guid: int = Field(default=0)
    packed_params: bytes = Field(default=b"")

class CMsgSosSetLibraryStackFields(BaseModel):
    stack_hash: float = Field(default=0.0)
    packed_fields: bytes = Field(default=b"")
