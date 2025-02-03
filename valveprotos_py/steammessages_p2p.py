# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class EGCPlatform(IntEnum):
    k_eGCPlatform_None = 0
    k_eGCPlatform_PC = 1
    k_eGCPlatform_Mac = 2
    k_eGCPlatform_Linux = 3
    k_eGCPlatform_Android = 4
    k_eGCPlatform_iOS = 5


class GCProtoBufMsgSrc(IntEnum):
    GCProtoBufMsgSrc_Unspecified = 0
    GCProtoBufMsgSrc_FromSystem = 1
    GCProtoBufMsgSrc_FromSteamID = 2
    GCProtoBufMsgSrc_FromGC = 3
    GCProtoBufMsgSrc_ReplySystem = 4
    GCProtoBufMsgSrc_SpoofedSteamID = 5

class CMsgProtoBufHeader(BaseModel):
    client_steam_id: float = Field(default=0.0)
    client_session_id: int = Field(default=0)
    source_app_id: int = Field(default=0)
    job_id_source: float = Field(default=0.0)
    job_id_target: float = Field(default=0.0)
    target_job_name: str = Field(default="")
    eresult: int = Field(default=0)
    error_message: str = Field(default="")
    gc_msg_src: GCProtoBufMsgSrc = Field(default=0)
    gc_dir_index_source: int = Field(default=0)

class CGCSystemMsg_GetAccountDetails(BaseModel):
    steamid: float = Field(default=0.0)
    appid: int = Field(default=0)

class CGCSystemMsg_GetAccountDetails_Response(BaseModel):
    eresult_deprecated: int = Field(default=0)
    account_name: str = Field(default="")
    persona_name: str = Field(default="")
    is_profile_created: bool = Field(default=False)
    is_profile_public: bool = Field(default=False)
    is_inventory_public: bool = Field(default=False)
    is_vac_banned: bool = Field(default=False)
    is_cyber_cafe: bool = Field(default=False)
    is_school_account: bool = Field(default=False)
    is_limited: bool = Field(default=False)
    is_subscribed: bool = Field(default=False)
    package: int = Field(default=0)
    is_free_trial_account: bool = Field(default=False)
    free_trial_expiration: int = Field(default=0)
    is_low_violence: bool = Field(default=False)
    is_account_locked_down: bool = Field(default=False)
    is_community_banned: bool = Field(default=False)
    is_trade_banned: bool = Field(default=False)
    trade_ban_expiration: int = Field(default=0)
    accountid: int = Field(default=0)
    suspension_end_time: int = Field(default=0)
    currency: str = Field(default="")
    steam_level: int = Field(default=0)
    friend_count: int = Field(default=0)
    account_creation_time: int = Field(default=0)
    is_steamguard_enabled: bool = Field(default=False)
    is_phone_verified: bool = Field(default=False)
    is_two_factor_auth_enabled: bool = Field(default=False)
    two_factor_enabled_time: int = Field(default=0)
    phone_verification_time: int = Field(default=0)
    phone_id: int = Field(default=0)
    is_phone_identifying: bool = Field(default=False)
    rt_identity_linked: int = Field(default=0)
    rt_birth_date: int = Field(default=0)
    txn_country_code: str = Field(default="")
    has_accepted_china_ssa: bool = Field(default=False)
    is_banned_steam_china: bool = Field(default=False)

class CIPLocationInfo(BaseModel):
    ip: int = Field(default=0)
    latitude: float = Field(default=0.0)
    longitude: float = Field(default=0.0)
    country: str = Field(default="")
    state: str = Field(default="")
    city: str = Field(default="")

class CGCMsgGetIPLocationResponse(BaseModel):
    infos: typing.List[CIPLocationInfo] = Field(default_factory=list)
