# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .steammessages_p2p import CGCSystemMsg_GetAccountDetails_Response
from .steammessages_steamlearn.steamworkssdk_p2p import CMsgSteamLearnAccessTokens
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class ESourceEngine(IntEnum):
    k_ESE_Source1 = 0
    k_ESE_Source2 = 1


class PartnerAccountType(IntEnum):
    PARTNER_NONE = 0
    PARTNER_PERFECT_WORLD = 1
    PARTNER_INVALID = 3


class GCConnectionStatus(IntEnum):
    GCConnectionStatus_HAVE_SESSION = 0
    GCConnectionStatus_GC_GOING_DOWN = 1
    GCConnectionStatus_NO_SESSION = 2
    GCConnectionStatus_NO_SESSION_IN_LOGON_QUEUE = 3
    GCConnectionStatus_NO_STEAM = 4
    GCConnectionStatus_SUSPENDED = 5
    GCConnectionStatus_STEAM_GOING_DOWN = 6

class CExtraMsgBlock(BaseModel):
    msg_type: int = Field(default=0)
    contents: bytes = Field(default=b"")
    msg_key: int = Field(default=0)
    is_compressed: bool = Field(default=False)

class CMsgSteamLearnServerInfo(BaseModel):
    class ProjectInfo(BaseModel):
        project_id: int = Field(default=0)
        snapshot_published_version: int = Field(default=0)
        inference_published_version: int = Field(default=0)
        snapshot_percentage: int = Field(default=0)
        snapshot_enabled: bool = Field(default=False)

    access_tokens: CMsgSteamLearnAccessTokens = Field()
    project_infos: typing.List["CMsgSteamLearnServerInfo.ProjectInfo"] = Field(default_factory=list)

class CMsgGCAssertJobData(BaseModel):
    message_type: str = Field(default="")
    message_data: bytes = Field(default=b"")

class CMsgGCConCommand(BaseModel):
    command: str = Field(default="")

class CMsgSDOAssert(BaseModel):
    class Request(BaseModel):
        key: typing.List[int] = Field(default_factory=list)
        requesting_job: str = Field(default="")

    sdo_type: int = Field(default=0)
    requests: typing.List["CMsgSDOAssert.Request"] = Field(default_factory=list)

class CMsgSOIDOwner(BaseModel):
    type: int = Field(default=0)
    id: int = Field(default=0)

class CMsgSOSingleObject(BaseModel):
    type_id: int = Field(default=0)
    object_data: bytes = Field(default=b"")
    version: float = Field(default=0.0)
    owner_soid: CMsgSOIDOwner = Field()
    service_id: int = Field(default=0)

class CMsgSOMultipleObjects(BaseModel):
    class SingleObject(BaseModel):
        type_id: int = Field(default=0)
        object_data: bytes = Field(default=b"")

    objects_modified: typing.List["CMsgSOMultipleObjects.SingleObject"] = Field(default_factory=list)
    version: float = Field(default=0.0)
    objects_added: typing.List["CMsgSOMultipleObjects.SingleObject"] = Field(default_factory=list)
    objects_removed: typing.List["CMsgSOMultipleObjects.SingleObject"] = Field(default_factory=list)
    owner_soid: CMsgSOIDOwner = Field()
    service_id: int = Field(default=0)

class CMsgSOCacheSubscribed(BaseModel):
    class SubscribedType(BaseModel):
        type_id: int = Field(default=0)
        object_data: typing.List[bytes] = Field(default_factory=list)

    objects: typing.List["CMsgSOCacheSubscribed.SubscribedType"] = Field(default_factory=list)
    version: float = Field(default=0.0)
    owner_soid: CMsgSOIDOwner = Field()
    service_id: int = Field(default=0)
    service_list: typing.List[int] = Field(default_factory=list)
    sync_version: float = Field(default=0.0)

class CMsgSOCacheSubscribedUpToDate(BaseModel):
    version: float = Field(default=0.0)
    owner_soid: CMsgSOIDOwner = Field()
    service_id: int = Field(default=0)
    service_list: typing.List[int] = Field(default_factory=list)
    sync_version: float = Field(default=0.0)

class CMsgSOCacheUnsubscribed(BaseModel):
    owner_soid: CMsgSOIDOwner = Field()

class CMsgSOCacheSubscriptionCheck(BaseModel):
    version: float = Field(default=0.0)
    owner_soid: CMsgSOIDOwner = Field()
    service_id: int = Field(default=0)
    service_list: typing.List[int] = Field(default_factory=list)
    sync_version: float = Field(default=0.0)

class CMsgSOCacheSubscriptionRefresh(BaseModel):
    owner_soid: CMsgSOIDOwner = Field()

class CMsgSOCacheVersion(BaseModel):
    version: float = Field(default=0.0)

class CMsgGCMultiplexMessage(BaseModel):
    msgtype: int = Field(default=0)
    payload: bytes = Field(default=b"")
    steamids: typing.List[float] = Field(default_factory=list)

class CMsgGCToGCSubGCStarting(BaseModel):
    dir_index: int = Field(default=0)

class CGCToGCMsgMasterAck(BaseModel):
    class Process(BaseModel):
        dir_index: int = Field(default=0)
        type_instances: typing.List[int] = Field(default_factory=list)

    dir_index: int = Field(default=0)
    machine_name: str = Field(default="")
    process_name: str = Field(default="")
    directory: typing.List["CGCToGCMsgMasterAck.Process"] = Field(default_factory=list)

class CGCToGCMsgMasterAck_Response(BaseModel):
    eresult: int = Field(default=0)

class CMsgGCToGCUniverseStartup(BaseModel):
    is_initial_startup: bool = Field(default=False)

class CMsgGCToGCUniverseStartupResponse(BaseModel):
    eresult: int = Field(default=0)

class CGCToGCMsgMasterStartupComplete(BaseModel):
    class GCInfo(BaseModel):
        dir_index: int = Field(default=0)
        machine_name: str = Field(default="")

    gc_info: typing.List["CGCToGCMsgMasterStartupComplete.GCInfo"] = Field(default_factory=list)

class CGCToGCMsgRouted(BaseModel):
    msg_type: int = Field(default=0)
    sender_id: float = Field(default=0.0)
    net_message: bytes = Field(default=b"")

class CGCToGCMsgRoutedReply(BaseModel):
    msg_type: int = Field(default=0)
    net_message: bytes = Field(default=b"")

class CMsgGCUpdateSubGCSessionInfo(BaseModel):
    class CMsgUpdate(BaseModel):
        steamid: float = Field(default=0.0)
        ip: float = Field(default=0.0)
        trusted: bool = Field(default=False)

    updates: typing.List["CMsgGCUpdateSubGCSessionInfo.CMsgUpdate"] = Field(default_factory=list)

class CMsgGCRequestSubGCSessionInfo(BaseModel):
    steamid: float = Field(default=0.0)

class CMsgGCRequestSubGCSessionInfoResponse(BaseModel):
    ip: float = Field(default=0.0)
    trusted: bool = Field(default=False)
    port: int = Field(default=0)
    success: bool = Field(default=False)

class CMsgSOCacheHaveVersion(BaseModel):
    soid: CMsgSOIDOwner = Field()
    version: float = Field(default=0.0)
    service_id: int = Field(default=0)
    cached_file_version: int = Field(default=0)

class CMsgClientHello(BaseModel):
    version: int = Field(default=0)
    socache_have_versions: typing.List[CMsgSOCacheHaveVersion] = Field(default_factory=list)
    client_session_need: int = Field(default=0)
    client_launcher: PartnerAccountType = Field(default=0)
    secret_key: str = Field(default="")
    client_language: int = Field(default=0)
    engine: ESourceEngine = Field(default=0)
    steamdatagram_login: bytes = Field(default=b"")
    platform_id: int = Field(default=0)
    game_msg: bytes = Field(default=b"")
    os_type: int = Field(default=0)
    render_system: int = Field(default=0)
    render_system_req: int = Field(default=0)
    screen_width: int = Field(default=0)
    screen_height: int = Field(default=0)
    screen_refresh: int = Field(default=0)
    render_width: int = Field(default=0)
    render_height: int = Field(default=0)
    swap_width: int = Field(default=0)
    swap_height: int = Field(default=0)
    is_steam_china: bool = Field(default=False)
    is_steam_china_client: bool = Field(default=False)
    platform_name: str = Field(default="")

class CMsgClientWelcome(BaseModel):
    class Location(BaseModel):
        latitude: float = Field(default=0.0)
        longitude: float = Field(default=0.0)
        country: str = Field(default="")

    version: int = Field(default=0)
    game_data: bytes = Field(default=b"")
    outofdate_subscribed_caches: typing.List[CMsgSOCacheSubscribed] = Field(default_factory=list)
    uptodate_subscribed_caches: typing.List[CMsgSOCacheSubscriptionCheck] = Field(default_factory=list)
    location: "CMsgClientWelcome.Location" = Field()
    gc_socache_file_version: int = Field(default=0)
    txn_country_code: str = Field(default="")
    game_data2: bytes = Field(default=b"")
    rtime32_gc_welcome_timestamp: int = Field(default=0)
    currency: int = Field(default=0)
    balance: int = Field(default=0)
    balance_url: str = Field(default="")
    has_accepted_china_ssa: bool = Field(default=False)
    is_banned_steam_china: bool = Field(default=False)
    additional_welcome_msgs: CExtraMsgBlock = Field()
    steam_learn_server_info: CMsgSteamLearnServerInfo = Field()

class CMsgConnectionStatus(BaseModel):
    status: GCConnectionStatus = Field(default=0)
    client_session_need: int = Field(default=0)
    queue_position: int = Field(default=0)
    queue_size: int = Field(default=0)
    wait_seconds: int = Field(default=0)
    estimated_wait_seconds_remaining: int = Field(default=0)

class CMsgGCToGCSOCacheSubscribe(BaseModel):
    class CMsgHaveVersions(BaseModel):
        service_id: int = Field(default=0)
        version: int = Field(default=0)

    subscriber: float = Field(default=0.0)
    subscribe_to_id: float = Field(default=0.0)
    sync_version: float = Field(default=0.0)
    have_versions: typing.List["CMsgGCToGCSOCacheSubscribe.CMsgHaveVersions"] = Field(default_factory=list)
    subscribe_to_type: int = Field(default=0)

class CMsgGCToGCSOCacheUnsubscribe(BaseModel):
    subscriber: float = Field(default=0.0)
    unsubscribe_from_id: float = Field(default=0.0)
    unsubscribe_from_type: int = Field(default=0)

class CMsgGCClientPing(BaseModel):
    pass

class CMsgGCToGCForwardAccountDetails(BaseModel):
    steamid: float = Field(default=0.0)
    account_details: CGCSystemMsg_GetAccountDetails_Response = Field()
    age_seconds: int = Field(default=0)

class CMsgGCToGCLoadSessionSOCache(BaseModel):
    account_id: int = Field(default=0)
    forward_account_details: CMsgGCToGCForwardAccountDetails = Field()

class CMsgGCToGCLoadSessionSOCacheResponse(BaseModel):
    pass

class CMsgGCToGCUpdateSessionStats(BaseModel):
    user_sessions: int = Field(default=0)
    server_sessions: int = Field(default=0)
    in_logon_surge: bool = Field(default=False)

class CMsgGCToClientRequestDropped(BaseModel):
    pass

class CWorkshop_PopulateItemDescriptions_Request(BaseModel):
    class SingleItemDescription(BaseModel):
        gameitemid: int = Field(default=0)
        item_description: str = Field(default="")

    class ItemDescriptionsLanguageBlock(BaseModel):
        language: str = Field(default="")
        descriptions: typing.List["CWorkshop_PopulateItemDescriptions_Request.SingleItemDescription"] = Field(default_factory=list)

    appid: int = Field(default=0)
    languages: typing.List["CWorkshop_PopulateItemDescriptions_Request.ItemDescriptionsLanguageBlock"] = Field(default_factory=list)

class CWorkshop_GetContributors_Request(BaseModel):
    appid: int = Field(default=0)
    gameitemid: int = Field(default=0)

class CWorkshop_GetContributors_Response(BaseModel):
    contributors: typing.List[float] = Field(default_factory=list)

class CWorkshop_SetItemPaymentRules_Request(BaseModel):
    class WorkshopItemPaymentRule(BaseModel):
        workshop_file_id: int = Field(default=0)
        revenue_percentage: float = Field(default=0.0)
        rule_description: str = Field(default="")
        rule_type: int = Field(default=0)

    class WorkshopDirectPaymentRule(BaseModel):
        workshop_file_id: int = Field(default=0)
        rule_description: str = Field(default="")

    class PartnerItemPaymentRule(BaseModel):
        account_id: int = Field(default=0)
        revenue_percentage: float = Field(default=0.0)
        rule_description: str = Field(default="")

    appid: int = Field(default=0)
    gameitemid: int = Field(default=0)
    associated_workshop_files: typing.List["CWorkshop_SetItemPaymentRules_Request.WorkshopItemPaymentRule"] = Field(default_factory=list)
    partner_accounts: typing.List["CWorkshop_SetItemPaymentRules_Request.PartnerItemPaymentRule"] = Field(default_factory=list)
    validate_only: bool = Field(default=False)
    make_workshop_files_subscribable: bool = Field(default=False)
    associated_workshop_file_for_direct_payments: "CWorkshop_SetItemPaymentRules_Request.WorkshopDirectPaymentRule" = Field()

class CWorkshop_SetItemPaymentRules_Response(BaseModel):
    validation_errors: typing.List[str] = Field(default_factory=list)

class CCommunity_ClanAnnouncementInfo(BaseModel):
    gid: int = Field(default=0)
    clanid: int = Field(default=0)
    posterid: int = Field(default=0)
    headline: str = Field(default="")
    posttime: int = Field(default=0)
    updatetime: int = Field(default=0)
    body: str = Field(default="")
    commentcount: int = Field(default=0)
    tags: typing.List[str] = Field(default_factory=list)
    language: int = Field(default=0)
    hidden: bool = Field(default=False)
    forum_topic_id: float = Field(default=0.0)

class CCommunity_GetClanAnnouncements_Request(BaseModel):
    steamid: int = Field(default=0)
    offset: int = Field(default=0)
    count: int = Field(default=0)
    maxchars: int = Field(default=0)
    strip_html: bool = Field(default=False)
    required_tags: typing.List[str] = Field(default_factory=list)
    require_no_tags: bool = Field(default=False)
    language_preference: typing.List[int] = Field(default_factory=list)
    hidden_only: bool = Field(default=False)
    only_gid: bool = Field(default=False)
    rtime_oldest_date: int = Field(default=0)
    include_hidden: bool = Field(default=False)
    include_partner_events: bool = Field(default=False)

class CCommunity_GetClanAnnouncements_Response(BaseModel):
    maxchars: int = Field(default=0)
    strip_html: bool = Field(default=False)
    announcements: typing.List[CCommunity_ClanAnnouncementInfo] = Field(default_factory=list)

class CBroadcast_PostGameDataFrame_Request(BaseModel):
    appid: int = Field(default=0)
    steamid: float = Field(default=0.0)
    broadcast_id: float = Field(default=0.0)
    frame_data: bytes = Field(default=b"")

class CMsgSerializedSOCache(BaseModel):
    class TypeCache(BaseModel):
        type: int = Field(default=0)
        objects: typing.List[bytes] = Field(default_factory=list)
        service_id: int = Field(default=0)

    class Cache(BaseModel):
        class Version(BaseModel):
            service: int = Field(default=0)
            version: int = Field(default=0)

        type: int = Field(default=0)
        id: int = Field(default=0)
        versions: typing.List[Version] = Field(default_factory=list)
        type_caches: typing.List["CMsgSerializedSOCache.TypeCache"] = Field(default_factory=list)

    file_version: int = Field(default=0)
    caches: typing.List["CMsgSerializedSOCache.Cache"] = Field(default_factory=list)
    gc_socache_file_version: int = Field(default=0)

class CMsgGCToClientPollConvarRequest(BaseModel):
    convar_name: str = Field(default="")
    poll_id: int = Field(default=0)

class CMsgGCToClientPollConvarResponse(BaseModel):
    poll_id: int = Field(default=0)
    convar_value: str = Field(default="")

class CGCMsgCompressedMsgToClient(BaseModel):
    msg_id: int = Field(default=0)
    compressed_msg: bytes = Field(default=b"")

class CMsgGCToGCMasterBroadcastMessage(BaseModel):
    users_per_second: int = Field(default=0)
    send_to_users: bool = Field(default=False)
    send_to_servers: bool = Field(default=False)
    msg_id: int = Field(default=0)
    msg_data: bytes = Field(default=b"")

class CMsgGCToGCMasterSubscribeToCache(BaseModel):
    soid_type: int = Field(default=0)
    soid_id: float = Field(default=0.0)
    account_ids: typing.List[int] = Field(default_factory=list)
    steam_ids: typing.List[float] = Field(default_factory=list)

class CMsgGCToGCMasterSubscribeToCacheResponse(BaseModel):
    pass

class CMsgGCToGCMasterSubscribeToCacheAsync(BaseModel):
    subscribe_msg: CMsgGCToGCMasterSubscribeToCache = Field()

class CMsgGCToGCMasterUnsubscribeFromCache(BaseModel):
    soid_type: int = Field(default=0)
    soid_id: float = Field(default=0.0)
    account_ids: typing.List[int] = Field(default_factory=list)
    steam_ids: typing.List[float] = Field(default_factory=list)

class CMsgGCToGCMasterDestroyCache(BaseModel):
    soid_type: int = Field(default=0)
    soid_id: float = Field(default=0.0)
