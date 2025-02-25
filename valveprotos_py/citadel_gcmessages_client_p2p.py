# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.0.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.3 
# Pydantic Version: 2.10.6 
from .citadel_gcmessages_common_p2p import CMsgAccountStats
from .citadel_gcmessages_common_p2p import CMsgHeroSelectionMatchInfo
from .citadel_gcmessages_common_p2p import CMsgRegionPingTimesClient
from .citadel_gcmessages_common_p2p import CMsgStartFindingMatchInfo
from .citadel_gcmessages_common_p2p import ECitadelBotDifficulty
from .citadel_gcmessages_common_p2p import ECitadelGameMode
from .citadel_gcmessages_common_p2p import ECitadelLeaderboardRegion
from .citadel_gcmessages_common_p2p import ECitadelLobbyTeam
from .citadel_gcmessages_common_p2p import ECitadelMMPreference
from .citadel_gcmessages_common_p2p import ECitadelMatchMode
from .citadel_gcmessages_common_p2p import ECitadelRegionMode
from .citadel_gcmessages_common_p2p import PrivateLobbySettings
from .gcsdk_gcmessages_p2p import CExtraMsgBlock
from .steammessages_p2p import EGCPlatform
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing

class EGCCitadelClientMessages(IntEnum):
    k_EMsgClientToGCStartMatchmaking = 9010
    k_EMsgClientToGCStartMatchmakingResponse = 9011
    k_EMsgClientToGCStopMatchmaking = 9012
    k_EMsgClientToGCStopMatchmakingResponse = 9013
    k_EMsgGCToClientMatchmakingStopped = 9014
    k_EMsgClientToGCLeaveLobby = 9015
    k_EMsgClientToGCLeaveLobbyResponse = 9016
    k_EMsgClientToGCIsInMatchmaking = 9017
    k_EMsgClientToGCIsInMatchmakingResponse = 9018
    k_EMsgGCToClientDevPlaytestStatus = 9019
    k_EMsgClientToGCDevSetMMBias = 9023
    k_EMsgClientToGCGetProfileCard = 9024
    k_EMsgClientToGCGetProfileCardResponse = 9025
    k_EMsgClientToGCUpdateRoster = 9026
    k_EMsgClientToGCUpdateRosterResponse = 9027
    k_EMsgGCToClientProfileCardUpdated = 9028
    k_EMsgGCToClientDevAnnouncements = 9029
    k_EMsgClientToGCModifyDevAnnouncements = 9030
    k_EMsgClientToGCModifyDevAnnouncementsResponse = 9031
    k_EMsgGCToClientSDRTicket = 9100
    k_EMsgClientToGCReplacementSDRTicket = 9101
    k_EMsgClientToGCReplacementSDRTicketResponse = 9102
    k_EMsgClientToGCSetServerConVar = 9107
    k_EMsgClientToGCSetServerConVarResponse = 9108
    k_EMsgClientToGCSpectateLobby = 9109
    k_EMsgClientToGCSpectateLobbyResponse = 9110
    k_EMsgClientToGCPostMatchSurveyResponse = 9111
    k_EMsgClientToGCGetMatchHistory = 9112
    k_EMsgClientToGCGetMatchHistoryResponse = 9113
    k_EMsgClientToGCSpectateUser = 9116
    k_EMsgClientToGCSpectateUserResponse = 9117
    k_EMsgClientToGCPartyCreate = 9123
    k_EMsgClientToGCPartyCreateResponse = 9124
    k_EMsgClientToGCPartyLeave = 9125
    k_EMsgClientToGCPartyLeaveResponse = 9126
    k_EMsgClientToGCPartyJoin = 9127
    k_EMsgClientToGCPartyJoinResponse = 9128
    k_EMsgClientToGCPartyAction = 9129
    k_EMsgClientToGCPartyActionResponse = 9130
    k_EMsgClientToGCPartyStartMatch = 9131
    k_EMsgClientToGCPartyStartMatchResponse = 9132
    k_EMsgClientToGCPartyInviteUser = 9133
    k_EMsgClientToGCPartyInviteUserResponse = 9134
    k_EMsgGCToClientPartyEvent = 9135
    k_EMsgGCToClientCanRejoinParty = 9137
    k_EMsgClientToGCPartyJoinViaCode = 9138
    k_EMsgClientToGCPartyJoinViaCodeResponse = 9139
    k_EMsgClientToGCPartySetReadyState = 9142
    k_EMsgClientToGCPartySetReadyStateResponse = 9143
    k_EMsgClientToGCGetAccountStats = 9164
    k_EMsgClientToGCGetAccountStatsResponse = 9165
    k_EMsgGCToClientAccountStatsUpdated = 9166
    k_EMsgClientToGCGetMatchMetaData = 9167
    k_EMsgClientToGCGetMatchMetaDataResponse = 9168
    k_EMsgClientToGCDevAction = 9172
    k_EMsgClientToGCDevActionResponse = 9173
    k_EMsgClientToGCRecordClientEvents = 9174
    k_EMsgClientToGCRecordClientEventsResponse = 9175
    k_EMsgClientToGCSetNewPlayerProgress = 9176
    k_EMsgClientToGCSetNewPlayerProgressResponse = 9177
    k_EMsgClientToGCUpdateAccountSync = 9178
    k_EMsgClientToGCUpdateAccountSyncResponse = 9179
    k_EMsgClientToGCGetHeroChoice = 9180
    k_EMsgClientToGCGetHeroChoiceResponse = 9181
    k_EMsgClientToGCUnlockHero = 9182
    k_EMsgClientToGCUnlockHeroResponse = 9183
    k_EMsgClientToGCBookUnlock = 9184
    k_EMsgClientToGCBookUnlockResponse = 9185
    k_EMsgClientToGCGetBook = 9186
    k_EMsgClientToGCGetBookResponse = 9187
    k_EMsgGCToClientBookUpdated = 9188
    k_EMsgClientToGCSubmitPlaytestUser = 9189
    k_EMsgClientToGCSubmitPlaytestUserResponse = 9190
    k_EMsgClientToGCUpdateHeroBuild = 9193
    k_EMsgClientToGCUpdateHeroBuildResponse = 9194
    k_EMsgClientToGCFindHeroBuilds = 9195
    k_EMsgClientToGCFindHeroBuildsResponse = 9196
    k_EMsgClientToGCReportPlayerFromMatch = 9197
    k_EMsgClientToGCReportPlayerFromMatchResponse = 9198
    k_EMsgClientToGCGetAccountMatchReports = 9199
    k_EMsgClientToGCGetAccountMatchReportsResponse = 9200
    k_EMsgClientToGCDeleteHeroBuild = 9201
    k_EMsgClientToGCDeleteHeroBuildResponse = 9202
    k_EMsgClientToGCGetActiveMatches = 9203
    k_EMsgClientToGCGetActiveMatchesResponse = 9204
    k_EMsgClientToGCGetDiscordLink = 9205
    k_EMsgClientToGCGetDiscordLinkResponse = 9206
    k_EMsgClientToGCPartySetMode = 9207
    k_EMsgClientToGCPartySetModeResponse = 9208
    k_EMsgClientToGCGrantForumAccess = 9209
    k_EMsgClientToGCGrantForumAccessResponse = 9210
    k_EMsgClientToGCModeratorRequest = 9211
    k_EMsgClientToGCModeratorRequestResponse = 9212
    k_EMsgClientToGCGetFriendGameStatus = 9213
    k_EMsgClientToGCGetFriendGameStatusResponse = 9214
    k_EMsgClientToGCUpdateHeroBuildPreference = 9215
    k_EMsgClientToGCUpdateHeroBuildPreferenceResponse = 9216
    k_EMsgClientToGCGetOldHeroBuildData = 9217
    k_EMsgClientToGCGetOldHeroBuildDataResponse = 9218
    k_EMsgClientToGCUpdateSpectatorStatus = 9219
    k_EMsgClientToGCCommendPlayerFromMatch = 9223
    k_EMsgClientToGCCommendPlayerFromMatchResponse = 9224
    k_EMsgGCToClientCommendNotification = 9225
    k_EMsgGCToClientHeroLabsSchedule = 9228
    k_EMsgClientToGCDevRequestCheatReports = 9230
    k_EMsgClientToGCDevRequestCheatReportsResponse = 9231
    k_EMsgClientToGCDevBan = 9232
    k_EMsgClientToGCDevBanResponse = 9233
    k_EMsgClientToGCGetHeroMMRRankings = 9234
    k_EMsgClientToGCGetHeroMMRRankingsResponse = 9235
    k_EMsgClientToGCGetLeaderboard = 9236
    k_EMsgClientToGCGetLeaderboardResponse = 9237
    k_EMsgClientToGCGetAccountLeaderboards = 9238
    k_EMsgClientToGCGetAccountLeaderboardsResponse = 9239
    k_EMsgClientToGCSetHideHolidayModels = 9240
    k_EMsgClientToGCSetHideHolidayModelsResponse = 9241


class ECitadelAccountPermissionFlag(IntEnum):
    k_eAccountPermission_Ranked = 1


class ECitadelNewPlayerProgressFlag(IntEnum):
    k_eNewPlayerProgress_GettingStarted = 1
    k_eNewPlayerProgress_HeroTraining = 2
    k_eNewPlayerProgress_LaneTraining = 3


class EProfileCardSlotType(IntEnum):
    k_EProfileCardSlotType_Empty = 0
    k_EProfileCardSlotType_Stat = 1
    k_EProfileCardSlotType_Hero = 2


class EDevBanReason(IntEnum):
    k_eDevBanReason_Unspecified = 0
    k_eDevBanReason_AimAssist = 1
    k_eDevBanReason_VisionAssist = 2
    k_eDevBanReason_MovementAssist = 3


class ECitadelClientAccountEvent(IntEnum):
    k_eLaunchedHeroTest = 1
    k_eViewedProfile = 2
    k_eViewedSocial = 3
    k_eViewedHeroes = 4
    k_eViewedHeroDetails = 5
    k_eViewedPatchNotes = 6
    k_eViewedEvents = 7
    k_eViewedGettingStarted = 8
    k_eViewedGuidePage = 9
    k_eLaunchedClient = 10
    k_eEditRoster = 11
    k_eViewedWatch = 12
    k_eCreatedParty = 13
    k_eCreatedPartyWithInvite = 14
    k_eViewedSelfProfile = 15
    k_eJoinedPartyCode = 16
    k_eSentPartyInvite = 17
    k_eAcceptPartyInvite = 18
    k_eRejectPartyInvite = 19
    k_eSpectateUser = 20
    k_eSpectateMatch = 21
    k_eEnteredMatchMaking = 22
    k_eLeftMatchMaking = 23
    k_eEnteredPartyMatchMaking = 24
    k_eLeftPartyMatchMaking = 25
    k_eDownloadedReplay = 26
    k_eWatchedReplay = 27
    k_eViewMatchDetails = 28
    k_eMatchDetailsTab = 29
    k_eDeleteReplay = 30
    k_eBotMatch_Guided = 31
    k_eBotMatch_Easy = 32
    k_eBotMatch_Hard = 33
    k_eLiveUpdatedRoster = 34
    k_eMatchMakingIdle_Displayed = 35
    k_eMatchMakingIdle_Stopped = 36
    k_eConnectReacquireTicket = 37
    k_eConnectAttemptReconnect = 38
    k_eDisconnectPresentedPrompt = 39
    k_eDisconnectConfirmed = 40
    k_eViewedSettings_Options = 41
    k_eViewedSettings_Video = 42
    k_eViewedSettings_Audio = 43
    k_eViewedSettings_HotKey = 44
    k_eViewedSettings_ChatWheel = 45
    k_eViewedSettings_About = 46
    k_eOpenedSubmitFeedback = 47
    k_eTutorialSkip_Pressed = 48
    k_eTutorialSkip_Confirmed = 49
    k_eViewedGuidePage_5s = 50
    k_eViewedGuidePage_15s = 51
    k_eViewedGuidePage_30s = 52
    k_eViewedGuidePage_60s = 53
    k_eOpenedBookTest = 54
    k_eSandboxViaHeroPage = 55
    k_eViewedSettings_SteamInput = 56
    k_eViewedSettings_Social = 57


class ECommendType(IntEnum):
    k_eInvalid = 0
    k_eGeneric = 1
    k_eFriendly = 2
    k_eTeamwork = 3
    k_eSkilled = 4

class CSOGameAccountClient(BaseModel):
    class EFlags(IntEnum):
        k_eDeveloper = 1
        k_eExternalModerator = 2
        k_eGotInitialHeroes = 4
        k_eHideHolidayModels = 8
        k_eClaimedDiscordLink = 16
        k_eClaimedForum = 32
        k_eAccountBanned = 64

    account_id: int = Field(default=0)
    flags: int = Field(default=0)
    wins: int = Field(default=0)
    losses: int = Field(default=0)
    kills: int = Field(default=0)
    most_played_hero_id: int = Field(default=0)
    permissions: int = Field(default=0)
    new_player_progress: int = Field(default=0)
    hero_unlock_credits: int = Field(default=0)
    mm_ban_until: int = Field(default=0)
    comms_ban_until: int = Field(default=0)
    low_priority_games_remaining: int = Field(default=0)
    report_ban_until: int = Field(default=0)
    ranked_badge_level: int = Field(default=0)
    hero_labs_matches_since_test_hero: int = Field(default=0)

class CSOAccountSyncStorage(BaseModel):
    account_id: int = Field(default=0)
    id: int = Field(default=0)
    value: int = Field(default=0)

class CSOAccountHeroInfo(BaseModel):
    class EHeroStatus(IntEnum):
        k_eLocked = 0
        k_eOwned = 1

    account_id: int = Field(default=0)
    hero_id: int = Field(default=0)
    status: "CSOAccountHeroInfo.EHeroStatus" = Field(default=0)
    wins: int = Field(default=0)
    kills: int = Field(default=0)

class CMsgCitadelClientHello(BaseModel):
    pass

class CMsgClientToGCStartMatchmaking(BaseModel):
    client_version: int = Field(default=0)
    client_platform: EGCPlatform = Field(default=0)
    match_info: CMsgStartFindingMatchInfo = Field()
    ping_times: CMsgRegionPingTimesClient = Field()
    heroes: CMsgHeroSelectionMatchInfo = Field()

class CMsgClientToGCStartMatchmakingResponse(BaseModel):
    class EResultCode(IntEnum):
        k_EResult_OK = 0
        k_EResult_AlreadyFindingMatch = 1
        k_EResult_PartyMemberInLobby = 2
        k_EResult_InvalidClientVersion = 3
        k_EResult_MatchmakingDisabled = 4
        k_EResult_MatchmakingTooBusy = 5
        k_EResult_InternalError = 6
        k_EResult_NoRegionPings = 7
        k_EResult_InParty = 8
        k_EResult_ModeLocked = 9
        k_EResult_ModeBanned = 10
        k_EResult_RegionInfoNotProvided = 11
        k_EResult_DurationControlBlocked = 12
        k_EResult_InvalidHeroSelection = 13
        k_EResult_HeroesNotUnlocked = 14
        k_EResult_PermanentBan = 15
        k_EResult_RankedMMNotOpen = 16
        k_EResult_RankedNotUnlocked = 17
        k_EResult_NoRankedWhileInLowPri = 18
        k_EResult_NoRankedWhileCommsBanned = 19
        k_EResult_NoRankedWhileReportBanned = 20
        k_EResult_HeroLabsMMNotOpen = 21
        k_EResult_HeroLabsNotUnlocked = 22
        k_EResult_NoHeroLabsWhileInLowPri = 23
        k_EResult_AccountLocked = 24
        k_EResult_TooManyLimitedHeroes = 25

    result: "CMsgClientToGCStartMatchmakingResponse.EResultCode" = Field(default=0)
    time_stamp: int = Field(default=0)
    debug_message: str = Field(default="")

class CMsgClientToGCStopMatchmaking(BaseModel):
    pass

class CMsgClientToGCStopMatchmakingResponse(BaseModel):
    success: bool = Field(default=False)

class CMsgGCToClientMatchmakingStopped(BaseModel):
    class EReason(IntEnum):
        k_EResult_Unspecified = 0
        k_EResult_VersionUpdated = 1
        k_EResult_RankedClosed = 2
        k_EResult_HeroLabsClosed = 3

    reason: "CMsgGCToClientMatchmakingStopped.EReason" = Field(default=0)

class CMsgClientToGCLeaveLobby(BaseModel):
    lobby_id: int = Field(default=0)

class CMsgClientToGCLeaveLobbyResponse(BaseModel):
    pass

class CMsgClientWelcomeCitadel(BaseModel):
    currency: int = Field(default=0)
    extra_messages: typing.List[CExtraMsgBlock] = Field(default_factory=list)
    compatibility_version: int = Field(default=0)
    region_mode: ECitadelRegionMode = Field(default=0)

class CMsgClientToGCIsInMatchmaking(BaseModel):
    pass

class CMsgClientToGCIsInMatchmakingResponse(BaseModel):
    in_matchmaking: bool = Field(default=False)

class CMsgDevMatchInfo(BaseModel):
    class MatchPlayer(BaseModel):
        account_id: int = Field(default=0)
        team: ECitadelLobbyTeam = Field(default=0)
        abandoned: bool = Field(default=False)
        hero_id: int = Field(default=0)

    start_time: int = Field(default=0)
    winning_team: ECitadelLobbyTeam = Field(default=0)
    match_id: int = Field(default=0)
    players: typing.List["CMsgDevMatchInfo.MatchPlayer"] = Field(default_factory=list)
    lobby_id: float = Field(default=0.0)
    game_mode_version: int = Field(default=0)
    net_worth_team_0: int = Field(default=0)
    net_worth_team_1: int = Field(default=0)
    duration_s: int = Field(default=0)
    spectators: int = Field(default=0)
    open_spectator_slots: int = Field(default=0)
    objectives_mask_team0: int = Field(default=0)
    objectives_mask_team1: int = Field(default=0)
    match_mode: ECitadelMatchMode = Field(default=0)
    game_mode: ECitadelGameMode = Field(default=0)
    match_score: int = Field(default=0)
    region_mode: ECitadelRegionMode = Field(default=0)
    compat_version: int = Field(default=0)

class CMsgGCToClientHeroLabsSchedule(BaseModel):
    class TimeRange(BaseModel):
        start_time: int = Field(default=0)
        end_time: int = Field(default=0)

    class Schedule(BaseModel):
        schedule_id: int = Field(default=0)
        weekends: typing.List["CMsgGCToClientHeroLabsSchedule.TimeRange"] = Field(default_factory=list)
        weekdays: typing.List["CMsgGCToClientHeroLabsSchedule.TimeRange"] = Field(default_factory=list)
        is_open: bool = Field(default=False)
        regions: typing.List[ECitadelRegionMode] = Field(default_factory=list)

    schedules: typing.List["CMsgGCToClientHeroLabsSchedule.Schedule"] = Field(default_factory=list)

class CMsgGCToClientDevPlaytestStatus(BaseModel):
    class HeroWhitelist(BaseModel):
        hero_id: int = Field(default=0)
        account_ids: typing.List[int] = Field(default_factory=list)

    class DevQueueSize(BaseModel):
        match_mode: ECitadelMatchMode = Field(default=0)
        queue_size: int = Field(default=0)

    dev_queue_size: typing.List["CMsgGCToClientDevPlaytestStatus.DevQueueSize"] = Field(default_factory=list)
    dev_available_servers: int = Field(default=0)
    coop_bot_max_wait_s: int = Field(default=0)
    is_mm_enabled: bool = Field(default=False)
    locked_heroes: bool = Field(default=False)
    party_shared_heroes: bool = Field(default=False)
    hero_whitelists: typing.List["CMsgGCToClientDevPlaytestStatus.HeroWhitelist"] = Field(default_factory=list)
    mm_pause_time: int = Field(default=0)
    valid_client_versions: typing.List[int] = Field(default_factory=list)
    active_match_count: int = Field(default=0)
    roster_non_limited_heroes: int = Field(default=0)

class CMsgGCToClientSDRTicket(BaseModel):
    ticket: bytes = Field(default=b"")

class CMsgClientToGCReplacementSDRTicket(BaseModel):
    lobby_id: float = Field(default=0.0)

class CMsgClientToGCReplacementSDRTicketResponse(BaseModel):
    ticket: bytes = Field(default=b"")
    error_message: str = Field(default="")

class CMsgClientToGCSetServerConVar(BaseModel):
    convar_name: str = Field(default="")
    convar_value: str = Field(default="")
    lobby_id: float = Field(default=0.0)

class CMsgClientToGCSetServerConVarResponse(BaseModel):
    message: str = Field(default="")

class CMsgClientToGCPostMatchSurveyResponse(BaseModel):
    class PostMatchSurvey(BaseModel):
        question_id: int = Field(default=0)
        response_value: int = Field(default=0)
        response_freeform: str = Field(default="")

    post_match_survey: typing.List["CMsgClientToGCPostMatchSurveyResponse.PostMatchSurvey"] = Field(default_factory=list)
    match_id: int = Field(default=0)

class CMsgPartyMMInfo(BaseModel):
    platform: EGCPlatform = Field(default=0)
    ping_times: CMsgRegionPingTimesClient = Field()
    client_version: int = Field(default=0)
    region_mode: ECitadelRegionMode = Field(default=0)

class CMsgClientToGCPartyCreate(BaseModel):
    party_mm_info: CMsgPartyMMInfo = Field()
    invite_account_id: int = Field(default=0)
    disable_party_code: bool = Field(default=False)
    is_private_lobby: bool = Field(default=False)
    region_mode: ECitadelRegionMode = Field(default=0)
    server_search_key: str = Field(default="")
    mm_preference: ECitadelMMPreference = Field(default=0)
    private_lobby_settings: PrivateLobbySettings = Field()
    bot_difficulty: ECitadelBotDifficulty = Field(default=0)

class CMsgClientToGCPartyCreateResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eAlreadyInParty = 2
        k_eDisabled = 3
        k_eInvalidVersion = 4
        k_eNoRegionPings = 5
        k_eTooBusy = 6
        k_eRateLimited = 7
        k_eNotFriends = 8
        k_eRegionInfoNotProvided = 9
        k_eDurationControlBlocked = 10
        k_eInMatchmaking = 11
        k_ePlayerDoesntHaveGame = 12

    result: "CMsgClientToGCPartyCreateResponse.EResponse" = Field(default=0)
    party_id: float = Field(default=0.0)

class CMsgClientToGCPartyLeave(BaseModel):
    party_id: float = Field(default=0.0)

class CMsgClientToGCPartyLeaveResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eNotInParty = 2
        k_eInMatchMaking = 3

    result: "CMsgClientToGCPartyLeaveResponse.EResponse" = Field(default=0)

class CMsgClientToGCPartyJoin(BaseModel):
    party_id: float = Field(default=0.0)
    is_rejoin: bool = Field(default=False)
    party_mm_info: CMsgPartyMMInfo = Field()

class CMsgClientToGCPartyJoinResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eAlreadyInParty = 2
        k_eDisabled = 3
        k_eInvalidPartyID = 4
        k_eInvalidPermissions = 5
        k_eInvalidVersion = 6
        k_eNoRegionPings = 7
        k_eTooBusy = 8
        k_eInvalidCode = 9
        k_eRateLimited = 10
        k_eRegionInfoNotProvided = 11
        k_eDurationControlBlocked = 12
        k_ePartyInMatchMaking = 13
        k_eInMatchmaking = 14
        k_ePartyFull = 15

    result: "CMsgClientToGCPartyJoinResponse.EResponse" = Field(default=0)

class CMsgClientToGCPartyAction(BaseModel):
    class EAction(IntEnum):
        k_eKickUser = 1
        k_eCancelInvite = 2
        k_eCancelFindMatch = 3
        k_eSetPlayerType = 5
        k_eEnablePartyCode = 7
        k_eSetMemberTeam = 8
        k_eSetChatMode = 9
        k_eSetPlayerSlot = 10
        k_eSetRegionMode = 11
        k_eSetSearchKey = 12
        k_eSetBotDifficulty = 13
        k_eSetRandomizedLanes = 14
        k_eSetServerRegion = 15
        k_eSetPubliclyVisible = 16
        k_eSetCheatsEnabled = 17
        k_eSwapTeams = 18
        k_eShuffleLobby = 19
        k_eShuffleLanes = 20
        k_eSetDuplicateHeroesEnabled = 21
        k_eSetExperimentalHeroesEnabled = 22
        k_eSetDesiresLaningTogether = 23
        k_eSetMMPreference = 24

    party_id: float = Field(default=0.0)
    target_account_id: int = Field(default=0)
    action_id: "CMsgClientToGCPartyAction.EAction" = Field(default=0)
    uint_value: int = Field(default=0)
    bool_value: bool = Field(default=False)
    str_value: str = Field(default="")

class CMsgClientToGCPartyActionResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eInvalidPartyID = 2
        k_eInvalidPermissions = 3
        k_eInvalidTarget = 4
        k_eInvalidValue = 5
        k_eInMatchMaking = 6
        k_eInMatch = 7
        k_eDisabled = 8
        k_eTooBusy = 9
        k_eRateLimited = 10
        k_eCannotChangeWhileReady = 12
        k_eSlotTaken = 13

    result: "CMsgClientToGCPartyActionResponse.EResponse" = Field(default=0)

class CMsgClientToGCPartySetMode(BaseModel):
    party_id: float = Field(default=0.0)
    match_mode: ECitadelMatchMode = Field(default=0)
    game_mode: ECitadelGameMode = Field(default=0)
    bot_difficulty: ECitadelBotDifficulty = Field(default=0)
    dev_server_command: str = Field(default="")
    region_mode: ECitadelRegionMode = Field(default=0)

class CMsgClientToGCPartySetModeResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eInvalidPartyID = 2
        k_eInvalidPermissions = 3
        k_ePlayerPermanentBanned = 4
        k_eInvalidValue = 5
        k_eInMatchMaking = 6
        k_eInMatch = 7
        k_eDisabled = 8
        k_eTooBusy = 9
        k_eRateLimited = 10
        k_eAlreadyDrafting = 11
        k_eCannotChangeWhileReady = 12
        k_eTooFewPlayers = 13
        k_eTooManyPlayers = 14
        k_ePlayerBanned = 15
        k_eTooManyHighMMR = 16
        k_eFiveStacksNotAllowed = 18
        k_eRankedMMNotOpen = 19
        k_eRankedNotunlocked = 20
        k_eHeroLabsMMNotOpen = 21
        k_eHeroLabsNotUnlocked = 22
        k_eNoHeroLabsWhileInLowPri = 23
        k_eNoHighRangeFiveStack = 24
        k_eAccountLocked = 25

    result: "CMsgClientToGCPartySetModeResponse.EResponse" = Field(default=0)
    time_stamp: int = Field(default=0)
    account_id: int = Field(default=0)

class CMsgClientToGCPartyStartMatch(BaseModel):
    party_id: float = Field(default=0.0)

class CMsgClientToGCPartyStartMatchResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDisabled = 2
        k_eInvalidPartyID = 3
        k_eInvalidPermissions = 4
        k_eTooBusy = 5
        k_eInMatchmaking = 6
        k_eInMatch = 7
        k_eInvalidVersion = 10
        k_ePlayersNotReady = 11
        k_eCannotSelectRegion = 12
        k_eNotAllPlayersAvailable = 13
        k_eTooManyPlayersForMM = 14
        k_eTooManyPlayersForPrivate = 15
        k_eTooManySpectatorsForMM = 16
        k_eTooManySpectatorsForPrivate = 17
        k_eTooFewPlayersForMM = 18
        k_eTooFewPlayersForPrivate = 19
        k_eMismatchedVersions = 20
        k_eInvalidPartyMatchMode = 21
        k_ePlayerBannedFromMode = 22
        k_eTooManyPlayersOnTeam = 23
        k_eInvalidTeam = 24
        k_eInvalidHeroLineup = 25
        k_eInvalidGroupHeroLineup = 26
        k_eUnassignedPlayers = 27
        k_eRankedMMNotOpen = 28
        k_eHeroLabsMMNotOpen = 29
        k_eHeroLabsNotUnlocked = 30
        k_eNoHeroLabsWhileInLowPri = 31

    result: "CMsgClientToGCPartyStartMatchResponse.EResponse" = Field(default=0)
    account_id: int = Field(default=0)

class CMsgClientToGCPartyInviteUser(BaseModel):
    party_id: float = Field(default=0.0)
    invite_account_id: int = Field(default=0)

class CMsgClientToGCPartyInviteUserResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eAlreadyInvited = 2
        k_eInvalidPermissions = 3
        k_eInvalidPartyID = 4
        k_eDisabled = 5
        k_eTooManyInvites = 6
        k_eNotFriends = 7
        k_eTooBusy = 8
        k_eRateLimited = 9
        k_eInvalidPartyMode = 10
        k_ePlayerDoesntHaveGame = 11

    result: "CMsgClientToGCPartyInviteUserResponse.EResponse" = Field(default=0)
    user_online: bool = Field(default=False)

class CMsgGCToClientPartyEvent(BaseModel):
    class EEvent(IntEnum):
        k_ePlayerKicked = 1
        k_eJoinedParty = 3
        k_eMatchCompleted = 4
        k_eMatchMakingStopped_User = 5
        k_eMatchMakingStopped_Version = 6
        k_eMatchMakingStopped_NoServerRegion = 7
        k_eLeftParty = 8
        k_eDeclinedInvite = 9
        k_eMatchMakingStopped_FailedOther = 10
        k_eDraftEnded_User = 11
        k_eStartDraftMMFailed = 12
        k_eMatchMakingStopped_Cancelled = 13

    party_id: float = Field(default=0.0)
    event: "CMsgGCToClientPartyEvent.EEvent" = Field(default=0)
    initiator_account_id: int = Field(default=0)
    target_account_id: int = Field(default=0)
    bytes_data: bytes = Field(default=b"")
    str_data: str = Field(default="")
    uint_data: int = Field(default=0)

class CMsgGCToClientCanRejoinParty(BaseModel):
    party_id: float = Field(default=0.0)

class CMsgClientToGCPartyJoinViaCode(BaseModel):
    join_code: int = Field(default=0)
    party_mm_info: CMsgPartyMMInfo = Field()

class CMsgClientToGCPartyJoinViaCodeResponse(BaseModel):
    result: EResponse = Field(default=0)
    party_id: float = Field(default=0.0)

class CMsgClientToGCPartySetReadyState(BaseModel):
    party_id: float = Field(default=0.0)
    ready_state: bool = Field(default=False)
    hero_roster: CMsgHeroSelectionMatchInfo = Field()

class CMsgClientToGCPartySetReadyStateResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eInvalidPermissions = 2
        k_eDisabled = 3
        k_eTooBusy = 4
        k_eRateLimited = 5
        k_eInvalidRoster = 6
        k_eMatchForming = 7
        k_eInvalidGroupRoster = 8
        k_eInMatch = 9
        k_eHeroesNotUnlocked = 10
        k_eModeLocked = 11
        k_eModeBanned = 12
        k_eTooManyLimitedHeroes = 13

    result: "CMsgClientToGCPartySetReadyStateResponse.EResponse" = Field(default=0)

class CMsgClientToGCDevSetMMBias(BaseModel):
    account_id: int = Field(default=0)
    value: int = Field(default=0)

class CMsgClientToGCGetMatchHistory(BaseModel):
    account_id: int = Field(default=0)
    continue_cursor: int = Field(default=0)
    ranked_interval: int = Field(default=0)

class CMsgClientToGCGetMatchHistoryResponse(BaseModel):
    class Match(BaseModel):
        match_id: int = Field(default=0)
        hero_id: int = Field(default=0)
        match_duration_s: int = Field(default=0)
        start_time: int = Field(default=0)
        match_result: int = Field(default=0)
        player_team: ECitadelLobbyTeam = Field(default=0)
        player_kills: int = Field(default=0)
        player_deaths: int = Field(default=0)
        player_assists: int = Field(default=0)
        last_hits: int = Field(default=0)
        denies: int = Field(default=0)
        hero_level: int = Field(default=0)
        net_worth: int = Field(default=0)
        objectives_mask_team0: int = Field(default=0)
        objectives_mask_team1: int = Field(default=0)
        team_abandoned: bool = Field(default=False)
        abandoned_time_s: int = Field(default=0)
        match_mode: ECitadelMatchMode = Field(default=0)
        game_mode: ECitadelGameMode = Field(default=0)
        not_scored: bool = Field(default=False)
        game_mode_version: int = Field(default=0)

    class EResult(IntEnum):
        k_eResult_InternalError = 0
        k_eResult_Success = 1
        k_eResult_InvalidPermission = 2
        k_eResult_TemporarilyDisabled = 3
        k_eResult_TooBusy = 4
        k_eResult_RateLimited = 5

    result: "CMsgClientToGCGetMatchHistoryResponse.EResult" = Field(default=0)
    continue_cursor: int = Field(default=0)
    matches: typing.List["CMsgClientToGCGetMatchHistoryResponse.Match"] = Field(default_factory=list)

class CMsgClientToGCSpectateUser(BaseModel):
    spectate_account_id: int = Field(default=0)
    client_version: int = Field(default=0)
    client_platform: EGCPlatform = Field(default=0)

class CMsgClientToGCSpectateUserResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDisabled = 2
        k_eTooBusy = 3
        k_eRateLimited = 4
        k_eNotInGame = 5
        k_eDisabledForGame = 6
        k_eServerFull = 7
        k_eNotFriends = 8
        k_eRegionInfoNotProvided = 9
        k_eDurationControlBlocked = 10
        k_eInvalidClientVersion = 11
        k_eInvalidRegion = 12

    result: "CMsgClientToGCSpectateUserResponse.EResponse" = Field(default=0)
    server_steam_id: float = Field(default=0.0)
    sdr_key: bytes = Field(default=b"")
    udp_connect_ip: int = Field(default=0)
    udp_connect_port: int = Field(default=0)
    lobby_id: float = Field(default=0.0)
    client_broadcast_url: str = Field(default="")

class CMsgClientToGCSpectateLobby(BaseModel):
    lobby_id: int = Field(default=0)
    client_version: int = Field(default=0)
    client_platform: EGCPlatform = Field(default=0)
    match_id: int = Field(default=0)

class CMsgClientToGCSpectateLobbyResponse(BaseModel):
    result: CMsgClientToGCSpectateUserResponse = Field()

class CMsgClientToGCGetProfileCard(BaseModel):
    account_id: int = Field(default=0)
    dev_access_hint: bool = Field(default=False)
    friend_access_hint: bool = Field(default=False)

class CMsgCitadelProfileCard(BaseModel):
    class Slot(BaseModel):
        class Stat(BaseModel):
            stat_id: EStatID = Field(default=0)
            stat_score: int = Field(default=0)

        class Hero(BaseModel):
            hero_id: int = Field(default=0)
            hero_wins: int = Field(default=0)
            hero_kills: int = Field(default=0)

        slot_id: int = Field(default=0)
        stat: Stat = Field()
        hero: Hero = Field()

    class EStatID(IntEnum):
        k_eStat_Invalid = 0
        k_eStat_Wins = 1
        k_eStat_Kills = 2
        k_eStat_GamesPlayed = 3

    account_id: int = Field(default=0)
    slots: typing.List["CMsgCitadelProfileCard.Slot"] = Field(default_factory=list)
    ranked_badge_level: int = Field(default=0)

class CMsgClientToGCUpdateRoster(BaseModel):
    heroes: CMsgHeroSelectionMatchInfo = Field()
    game_mode: ECitadelGameMode = Field(default=0)
    match_mode: ECitadelMatchMode = Field(default=0)

class CMsgClientToGCUpdateRosterResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDisabled = 2
        k_eTooBusy = 3
        k_eRateLimited = 4
        k_eMMBusy = 5
        k_eInvalidHeroSelection = 6
        k_eHeroesNotUnlocked = 7

    result: "CMsgClientToGCUpdateRosterResponse.EResponse" = Field(default=0)

class CMsgClientToGCGetAccountStats(BaseModel):
    account_id: int = Field(default=0)
    dev_access_hint: bool = Field(default=False)
    friend_access_hint: bool = Field(default=False)

class CMsgClientToGCGetAccountStatsResponse(BaseModel):
    class EResult(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDisabled = 2
        k_eTooBusy = 3
        k_eRateLimited = 4
        k_eInvalidPermissions = 5

    result: "CMsgClientToGCGetAccountStatsResponse.EResult" = Field(default=0)
    stats: CMsgAccountStats = Field()

class CMsgClientToGCGetMatchMetaData(BaseModel):
    match_id: int = Field(default=0)
    metadata_salt: int = Field(default=0)
    target_account_id: int = Field(default=0)

class CMsgClientToGCGetMatchMetaDataResponse(BaseModel):
    class EResult(IntEnum):
        k_eResult_InternalError = 0
        k_eResult_Success = 1
        k_eResult_InvalidPermission = 2
        k_eResult_TemporarilyDisabled = 3
        k_eResult_TooBusy = 4
        k_eResult_RateLimited = 5
        k_eResult_InvalidMatch = 6
        k_eResult_MatchInFlight = 7

    result: "CMsgClientToGCGetMatchMetaDataResponse.EResult" = Field(default=0)
    replay_salt: int = Field(default=0)
    metadata_salt: int = Field(default=0)
    replay_valid_through: int = Field(default=0)
    replay_group_id: int = Field(default=0)
    replay_processing_through: int = Field(default=0)

class CMsgGCToClientDevAnnouncements(BaseModel):
    class Announcement(BaseModel):
        priority: int = Field(default=0)
        title: str = Field(default="")
        message: str = Field(default="")
        url: str = Field(default="")
        unique_id: int = Field(default=0)
        posted_time: int = Field(default=0)
        patch_version: str = Field(default="")

    announcements: typing.List["CMsgGCToClientDevAnnouncements.Announcement"] = Field(default_factory=list)

class CMsgClientToGCModifyDevAnnouncements(BaseModel):
    class EOperation(IntEnum):
        k_eCreate = 0
        k_eUpdate = 1
        k_eDelete = 2

    operation: "CMsgClientToGCModifyDevAnnouncements.EOperation" = Field(default=0)
    target_id: int = Field(default=0)
    priority: int = Field(default=0)
    title: str = Field(default="")
    message: str = Field(default="")
    url: str = Field(default="")
    patch_version: str = Field(default="")

class CMsgClientToGCModifyDevAnnouncementsResponse(BaseModel):
    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInvalidPermission = 1
        k_eInvalidTarget = 2
        k_eInternalError = 3

    result: "CMsgClientToGCModifyDevAnnouncementsResponse.EResult" = Field(default=0)

class CMsgClientToGCDevAction(BaseModel):
    class EAction(IntEnum):
        k_eSetDeveloper = 1
        k_eSetMMR = 2
        k_eSetMMRUncertainty = 3
        k_eSetHeroStatus = 4
        k_eSetPermission = 5
        k_eSetNewPlayerProgress = 6
        k_eForceAccountStorage = 7
        k_eBookReset = 9
        k_eBookXPGrant = 10
        k_eBanAccount = 11
        k_eExonerateAccount = 12
        k_eRequireAccountInMM = 13

    action: "CMsgClientToGCDevAction.EAction" = Field(default=0)
    account_id: int = Field(default=0)
    uint_value: int = Field(default=0)
    int_value: int = Field(default=0)
    bool_value: bool = Field(default=False)
    str_value: str = Field(default="")
    match_id: int = Field(default=0)

class CMsgClientToGCDevActionResponse(BaseModel):
    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInvalidPermission = 1
        k_eInvalidTarget = 2
        k_eInternalError = 3

    result: "CMsgClientToGCDevActionResponse.EResult" = Field(default=0)

class CMsgClientToGCRecordClientEvents(BaseModel):
    class Event(BaseModel):
        time_stamp: int = Field(default=0)
        event_id: ECitadelClientAccountEvent = Field(default=0)
        event_data: int = Field(default=0)
        client_event_index: int = Field(default=0)

    events: typing.List["CMsgClientToGCRecordClientEvents.Event"] = Field(default_factory=list)
    client_run_token: int = Field(default=0)

class CMsgClientToGCRecordClientEventsResponse(BaseModel):
    success: bool = Field(default=False)

class CMsgClientToGCSetNewPlayerProgress(BaseModel):
    flag: ECitadelNewPlayerProgressFlag = Field(default=0)

class CMsgClientToGCSetNewPlayerProgressResponse(BaseModel):
    success: bool = Field(default=False)

class CMsgClientToGCUpdateAccountSync(BaseModel):
    ids: typing.List[int] = Field(default_factory=list)
    values: typing.List[int] = Field(default_factory=list)

class CMsgClientToGCUpdateAccountSyncResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDisabled = 2
        k_eTooBusy = 3
        k_eInvalidMessage = 4

    result: "CMsgClientToGCUpdateAccountSyncResponse.EResponse" = Field(default=0)

class CMsgClientToGCGetHeroChoice(BaseModel):
    pass

class CMsgClientToGCGetHeroChoiceResponse(BaseModel):
    class Hero(BaseModel):
        hero_id: int = Field(default=0)

    class EResult(IntEnum):
        k_eSuccess = 0
        k_eNoChoices = 1
        k_eInvalidTarget = 2
        k_eInternalError = 3
        k_eDisabled = 4
        k_eTooBusy = 5
        k_eChoiceClosed = 6

    result: "CMsgClientToGCGetHeroChoiceResponse.EResult" = Field(default=0)
    hero_selections: typing.List["CMsgClientToGCGetHeroChoiceResponse.Hero"] = Field(default_factory=list)
    hero_choice_id: int = Field(default=0)
    select_count: int = Field(default=0)

class CMsgClientToGCUnlockHero(BaseModel):
    hero_ids: typing.List[int] = Field(default_factory=list)
    hero_choice_id: int = Field(default=0)

class CMsgClientToGCUnlockHeroResponse(BaseModel):
    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInternalError = 1
        k_eInvalidHero = 2
        k_eOutOfSync = 3
        k_eDisabled = 4
        k_eTooBusy = 5

    result: "CMsgClientToGCUnlockHeroResponse.EResult" = Field(default=0)

class CMsgAccountBook(BaseModel):
    class Unlock(BaseModel):
        unlock_id: int = Field(default=0)
        flags: int = Field(default=0)

    book_id: int = Field(default=0)
    book_xp: int = Field(default=0)
    spent_xp: int = Field(default=0)
    unlocks: typing.List["CMsgAccountBook.Unlock"] = Field(default_factory=list)

class CMsgClientToGCBookUnlock(BaseModel):
    book_id: int = Field(default=0)
    unlock_id: int = Field(default=0)
    expected_cost: int = Field(default=0)
    client_version: int = Field(default=0)

class CMsgClientToGCBookUnlockResponse(BaseModel):
    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInternalError = 1
        k_eOutOfDateClient = 2
        k_eInvalidFunds = 3
        k_eDisabled = 4
        k_eTooBusy = 5
        k_eAlreadyUnlocked = 6

    result: "CMsgClientToGCBookUnlockResponse.EResult" = Field(default=0)
    updated_book: CMsgAccountBook = Field()

class CMsgClientToGCGetBook(BaseModel):
    book_id: int = Field(default=0)

class CMsgClientToGCGetBookResponse(BaseModel):
    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInternalError = 1
        k_eInvalidBook = 2
        k_eDisabled = 3
        k_eTooBusy = 4

    result: "CMsgClientToGCGetBookResponse.EResult" = Field(default=0)
    book: CMsgAccountBook = Field()

class CMsgGCToClientBookUpdated(BaseModel):
    book: CMsgAccountBook = Field()

class CMsgClientToGCSubmitPlaytestUser(BaseModel):
    location: str = Field(default="")
    target_account_id: int = Field(default=0)

class CMsgClientToGCSubmitPlaytestUserResponse(BaseModel):
    class EResponse(IntEnum):
        eResponse_Success = 0
        eResponse_InternalError = 1
        eResponse_InvalidFriend = 3
        eResponse_NotFriendsLongEnough = 4
        eResponse_AlreadyHasGame = 5
        eResponse_LimitedUser = 6
        eResponse_InviteLimitReached = 7

    response: "CMsgClientToGCSubmitPlaytestUserResponse.EResponse" = Field(default=0)

class CMsgHeroBuild(BaseModel):
    class BuildModEntry(BaseModel):
        ability_id: int = Field(default=0)
        annotation: str = Field(default="")

    class BuildModCategory(BaseModel):
        mods: "CMsgHeroBuild.BuildModEntry" = Field()
        name: str = Field(default="")
        description: str = Field(default="")
        width: float = Field(default=0.0)
        height: float = Field(default=0.0)

    class CurrencyChange(BaseModel):
        ability_id: int = Field(default=0)
        currency_type: int = Field(default=0)
        delta: int = Field(default=0)
        annotation: str = Field(default="")

    class AbilityOrder(BaseModel):
        currency_changes: typing.List["CMsgHeroBuild.CurrencyChange"] = Field(default_factory=list)

    class Details_V0(BaseModel):
        mod_categories: typing.List["CMsgHeroBuild.BuildModCategory"] = Field(default_factory=list)
        ability_order: "CMsgHeroBuild.AbilityOrder" = Field()

    hero_build_id: int = Field(default=0)
    hero_id: int = Field(default=0)
    author_account_id: int = Field(default=0)
    last_updated_timestamp: int = Field(default=0)
    name: str = Field(default="")
    description: str = Field(default="")
    language: int = Field(default=0)
    version: int = Field(default=0)
    origin_build_id: int = Field(default=0)
    details: "CMsgHeroBuild.Details_V0" = Field()

class CMsgClientToGCUpdateHeroBuild(BaseModel):
    hero_build: CMsgHeroBuild = Field()

class CMsgClientToGCUpdateHeroBuildResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1

    response: "CMsgClientToGCUpdateHeroBuildResponse.EResponse" = Field(default=0)
    hero_build_id: int = Field(default=0)
    version: int = Field(default=0)

class CMsgClientToGCFindHeroBuilds(BaseModel):
    author_account_id: int = Field(default=0)
    hero_id: int = Field(default=0)
    language: typing.List[int] = Field(default_factory=list)
    search_text: str = Field(default="")
    hero_build_id: int = Field(default=0)

class CMsgHeroBuildPreference(BaseModel):
    favorited: bool = Field(default=False)
    ignored: bool = Field(default=False)
    reported: bool = Field(default=False)

class CMsgClientToGCFindHeroBuildsResponse(BaseModel):
    class HeroBuildResult(BaseModel):
        hero_build: CMsgHeroBuild = Field()
        preference: CMsgHeroBuildPreference = Field()
        num_favorites: int = Field(default=0)
        num_ignores: int = Field(default=0)
        num_reports: int = Field(default=0)
        num_weekly_favorites: int = Field(default=0)
        num_daily_favorites: int = Field(default=0)
        rollup_category: int = Field(default=0)

    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eTooBusy = 2

    response: "CMsgClientToGCFindHeroBuildsResponse.EResponse" = Field(default=0)
    results: typing.List["CMsgClientToGCFindHeroBuildsResponse.HeroBuildResult"] = Field(default_factory=list)
    build_window_start_time_override: int = Field(default=0)

class CMsgClientToGCUpdateHeroBuildPreference(BaseModel):
    hero_build_id: int = Field(default=0)
    preference: CMsgHeroBuildPreference = Field()

class CMsgClientToGCUpdateHeroBuildPreferenceResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1

    response: "CMsgClientToGCUpdateHeroBuildPreferenceResponse.EResponse" = Field(default=0)

class CMsgClientToGCGetOldHeroBuildData(BaseModel):
    author_account_id: int = Field(default=0)

class CMsgClientToGCGetOldHeroBuildDataResponse(BaseModel):
    class OldDetails_V0(BaseModel):
        recommended_mod_ability_ids: typing.List[int] = Field(default_factory=list)

    class OldBuild(BaseModel):
        name: str = Field(default="")
        hero_id: int = Field(default=0)
        description: str = Field(default="")
        details: "CMsgClientToGCGetOldHeroBuildDataResponse.OldDetails_V0" = Field()

    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1

    response: "CMsgClientToGCGetOldHeroBuildDataResponse.EResponse" = Field(default=0)
    author_account_id: int = Field(default=0)
    results: typing.List["CMsgClientToGCGetOldHeroBuildDataResponse.OldBuild"] = Field(default_factory=list)

class CMsgClientToGCReportPlayerFromMatch(BaseModel):
    class EReportType(IntEnum):
        k_eReport_None = 0
        k_eReport_VoiceChat = 1
        k_eReport_Griefing = 2
        k_eReport_LeftMatch = 3
        k_eReport_Matchmaking = 4
        k_eReport_Cheating = 5

    match_id: int = Field(default=0)
    target_account_id: int = Field(default=0)
    report_type: "CMsgClientToGCReportPlayerFromMatch.EReportType" = Field(default=0)
    report_text: str = Field(default="")

class CMsgClientToGCReportPlayerFromMatchResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eRateLimited = 2
        k_eAlreadyReported = 3
        k_eDisabled = 4
        k_eInvalidPermissions = 5
        k_eReportingWindowExpired = 6
        k_eTooBusy = 7
        k_eBannedFromReporting = 8

    response: "CMsgClientToGCReportPlayerFromMatchResponse.EResponse" = Field(default=0)

class CMsgClientToGCGetAccountMatchReports(BaseModel):
    match_id: int = Field(default=0)

class CMsgClientToGCGetAccountMatchReportsResponse(BaseModel):
    class Report(BaseModel):
        account_id: int = Field(default=0)

    class Commend(BaseModel):
        account_id: int = Field(default=0)

    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDisabled = 4
        k_eTooBusy = 7

    response: "CMsgClientToGCGetAccountMatchReportsResponse.EResponse" = Field(default=0)
    reports: typing.List["CMsgClientToGCGetAccountMatchReportsResponse.Report"] = Field(default_factory=list)
    commends: typing.List["CMsgClientToGCGetAccountMatchReportsResponse.Commend"] = Field(default_factory=list)

class CMsgClientToGCDeleteHeroBuild(BaseModel):
    author_account_id: int = Field(default=0)
    hero_build_id: int = Field(default=0)

class CMsgClientToGCDeleteHeroBuildResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1

    response: "CMsgClientToGCDeleteHeroBuildResponse.EResponse" = Field(default=0)
    builds_deleted: int = Field(default=0)

class CMsgClientToGCGetActiveMatches(BaseModel):
    pass

class CMsgClientToGCGetActiveMatchesResponse(BaseModel):
    active_matches: typing.List[CMsgDevMatchInfo] = Field(default_factory=list)

class CMsgClientToGCGetDiscordLink(BaseModel):
    pass

class CMsgClientToGCGetDiscordLinkResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDiscordTooBusy = 2
        k_eAlreadyClaimed = 3
        k_eDisabled = 4

    response: "CMsgClientToGCGetDiscordLinkResponse.EResponse" = Field(default=0)
    discord_link: str = Field(default="")
    valid_hours: int = Field(default=0)

class CMsgClientToGCGrantForumAccess(BaseModel):
    email: str = Field(default="")

class CMsgClientToGCGrantForumAccessResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eAlreadyClaimed = 2
        k_eDisabled = 3
        k_eEmailUsed = 4

    response: "CMsgClientToGCGrantForumAccessResponse.EResponse" = Field(default=0)
    email: str = Field(default="")
    username: str = Field(default="")
    forum_password: str = Field(default="")

class CMsgClientToGCModeratorRequest(BaseModel):
    account_id: int = Field(default=0)

class CMsgClientToGCModeratorRequestResponse(BaseModel):
    success: bool = Field(default=False)
    response_text: typing.List[str] = Field(default_factory=list)

class CMsgClientToGCGetFriendGameStatus(BaseModel):
    include_invited: bool = Field(default=False)

class CMsgClientToGCGetFriendGameStatusResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eTooBusy = 2
        k_eDisabled = 3

    response: "CMsgClientToGCGetFriendGameStatusResponse.EResponse" = Field(default=0)
    friends_played_game: typing.List[int] = Field(default_factory=list)
    friends_invited: typing.List[int] = Field(default_factory=list)
    friends_invites_sent: typing.List[int] = Field(default_factory=list)

class CMsgClientToGCUpdateSpectatorStatus(BaseModel):
    spectating_lobby_id: float = Field(default=0.0)
    stopped_spectating: bool = Field(default=False)

class CMsgClientToGCCommendPlayerFromMatch(BaseModel):
    match_id: int = Field(default=0)
    target_account_id: int = Field(default=0)
    commend_type: ECommendType = Field(default=0)
    fake_commend_hero_id: int = Field(default=0)

class CMsgClientToGCCommendPlayerFromMatchResponse(BaseModel):
    class EResponse(IntEnum):
        k_eInternalError = 0
        k_eSuccess = 1
        k_eDisabled = 2
        k_eTooBusy = 3
        k_eRateLimited = 4

    result: "CMsgClientToGCCommendPlayerFromMatchResponse.EResponse" = Field(default=0)

class CMsgGCToClientCommendNotification(BaseModel):
    commender_account_id: int = Field(default=0)
    commender_name: str = Field(default="")
    commender_hero_id: int = Field(default=0)
    commend_type: ECommendType = Field(default=0)
    match_id: int = Field(default=0)
    enemy_commend: bool = Field(default=False)

class CMsgClientToGCRequestCheatReports(BaseModel):
    pass

class CMsgClientToGCRequestCheatReportsResponse(BaseModel):
    class RecentCheatReport(BaseModel):
        account_id: int = Field(default=0)
        match_id: int = Field(default=0)
        hero_id: int = Field(default=0)

    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInvalidPermission = 1
        k_eInternalError = 2

    result: "CMsgClientToGCRequestCheatReportsResponse.EResult" = Field(default=0)
    cheat_reports: typing.List["CMsgClientToGCRequestCheatReportsResponse.RecentCheatReport"] = Field(default_factory=list)

class CMsgClientToGCGetHeroMMRRankings(BaseModel):
    target_account_id: int = Field(default=0)

class CMsgClientToGCGetHeroMMRRankingsResponse(BaseModel):
    class Hero(BaseModel):
        hero_id: int = Field(default=0)
        relative_mmr: int = Field(default=0)

    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInvalidPermission = 1
        k_eInternalError = 2
        k_eTooBusy = 3

    result: "CMsgClientToGCGetHeroMMRRankingsResponse.EResult" = Field(default=0)
    heroes: typing.List["CMsgClientToGCGetHeroMMRRankingsResponse.Hero"] = Field(default_factory=list)

class CMsgClientToGCGetLeaderboard(BaseModel):
    leaderboard_region: ECitadelLeaderboardRegion = Field(default=0)
    hero_id: int = Field(default=0)

class CMsgClientToGCGetLeaderboardResponse(BaseModel):
    class LeaderboardEntry(BaseModel):
        account_name: str = Field(default="")
        rank: int = Field(default=0)
        top_hero_ids: typing.List[int] = Field(default_factory=list)
        badge_level: int = Field(default=0)

    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInvalidArguments = 1
        k_eInternalError = 2
        k_eTooBusy = 3

    result: "CMsgClientToGCGetLeaderboardResponse.EResult" = Field(default=0)
    entries: "CMsgClientToGCGetLeaderboardResponse.LeaderboardEntry" = Field()
    local_player_index: int = Field(default=0)

class CMsgClientToGCGetAccountLeaderboards(BaseModel):
    account_id: int = Field(default=0)

class CMsgClientToGCGetAccountLeaderboardsResponse(BaseModel):
    class LeaderboardEntry(BaseModel):
        region: ECitadelLeaderboardRegion = Field(default=0)
        hero_id: int = Field(default=0)
        rank: int = Field(default=0)

    class EResult(IntEnum):
        k_eSuccess = 0
        k_eInvalidPermission = 1
        k_eInternalError = 2
        k_eTooBusy = 3

    result: "CMsgClientToGCGetAccountLeaderboardsResponse.EResult" = Field(default=0)
    account_name: str = Field(default="")
    entries: "CMsgClientToGCGetAccountLeaderboardsResponse.LeaderboardEntry" = Field()

class CMsgClientToGCSetHideHolidayModels(BaseModel):
    hide_holiday_models: bool = Field(default=False)

class CMsgClientToGCSetHideHolidayModelsResponse(BaseModel):
    success: bool = Field(default=False)
