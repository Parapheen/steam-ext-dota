# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto

from ...protobufs.foobar import *


class GCProtoBufMsgSrc(GCProtoBufMsgSrc):
    SpoofedSteamID = 5


class EMobilePaymentProvider(betterproto.Enum):
    Invalid = 0
    GooglePlay = 1
    AppleAppStore = 2


class EDACPlatform(betterproto.Enum):
    NONE = 0
    PC = 1
    Mac = 2
    Linux = 3
    Android = 4
    iOS = 5


class CMsgGCRoutingInfoRoutingMethod(betterproto.Enum):
    Random = 0
    Discard = 1
    ClientSteamid = 2
    ProtobufFieldUint64 = 3
    WebapiParam = 4
    WebapiParamSteamidAccountid = 5


class CMsgGCMsgSetOptionsOption(betterproto.Enum):
    UserSessions = 0
    ServerSessions = 1
    Achievements = 2
    VACAction = 3


class CMsgGCMsgSetOptionsGCSQLVersion(betterproto.Enum):
    Baseline = 1
    Booltype = 2


class CMsgDPPartnerMicroTxnsResponseEErrorCode(betterproto.Enum):
    Valid = 0
    InvalidAppID = 1
    InvalidPartnerInfo = 2
    NoTransactions = 3
    SQLFailure = 4
    PartnerInfoDiscrepancy = 5
    TransactionInsertFailed = 7
    AlreadyRunning = 8
    InvalidTransactionData = 9


@dataclass
class CMsgWebAPIKey(betterproto.Message):
    status: int = betterproto.uint32_field(1)
    account_id: int = betterproto.uint32_field(2)
    publisher_group_id: int = betterproto.uint32_field(3)
    key_id: int = betterproto.uint32_field(4)
    domain: str = betterproto.string_field(5)


@dataclass
class CMsgHttpRequest(betterproto.Message):
    request_method: int = betterproto.uint32_field(1)
    hostname: str = betterproto.string_field(2)
    url: str = betterproto.string_field(3)
    headers: List["CMsgHttpRequestRequestHeader"] = betterproto.message_field(4)
    get_params: List["CMsgHttpRequestQueryParam"] = betterproto.message_field(5)
    post_params: List["CMsgHttpRequestQueryParam"] = betterproto.message_field(6)
    body: bytes = betterproto.bytes_field(7)
    absolute_timeout: int = betterproto.uint32_field(8)


@dataclass
class CMsgHttpRequestRequestHeader(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CMsgHttpRequestQueryParam(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: bytes = betterproto.bytes_field(2)


@dataclass
class CMsgWebAPIRequest(betterproto.Message):
    unused_job_name: str = betterproto.string_field(1)
    interface_name: str = betterproto.string_field(2)
    method_name: str = betterproto.string_field(3)
    version: int = betterproto.uint32_field(4)
    api_key: "CMsgWebAPIKey" = betterproto.message_field(5)
    request: "CMsgHttpRequest" = betterproto.message_field(6)
    routing_app_id: int = betterproto.uint32_field(7)


@dataclass
class CMsgHttpResponse(betterproto.Message):
    status_code: int = betterproto.uint32_field(1)
    headers: List["CMsgHttpResponseResponseHeader"] = betterproto.message_field(2)
    body: bytes = betterproto.bytes_field(3)


@dataclass
class CMsgHttpResponseResponseHeader(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CMsgAMFindAccounts(betterproto.Message):
    search_type: int = betterproto.uint32_field(1)
    search_string: str = betterproto.string_field(2)


@dataclass
class CMsgAMFindAccountsResponse(betterproto.Message):
    steam_id: List[float] = betterproto.fixed64_field(1)


@dataclass
class CMsgNotifyWatchdog(betterproto.Message):
    source: int = betterproto.uint32_field(1)
    alert_type: int = betterproto.uint32_field(2)
    critical: bool = betterproto.bool_field(4)
    time: int = betterproto.uint32_field(5)
    appid: int = betterproto.uint32_field(6)
    text: str = betterproto.string_field(7)
    recipient: str = betterproto.string_field(12)


@dataclass
class CMsgAMGetLicenses(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CMsgPackageLicense(betterproto.Message):
    package_id: int = betterproto.uint32_field(1)
    time_created: int = betterproto.uint32_field(2)
    owner_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgAMGetLicensesResponse(betterproto.Message):
    license: List["CMsgPackageLicense"] = betterproto.message_field(1)
    result: int = betterproto.uint32_field(2)


@dataclass
class CMsgAMGetUserGameStats(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    game_id: float = betterproto.fixed64_field(2)
    stats: List[int] = betterproto.uint32_field(3)


@dataclass
class CMsgAMGetUserGameStatsResponse(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    game_id: float = betterproto.fixed64_field(2)
    eresult: int = betterproto.int32_field(3)
    stats: List["CMsgAMGetUserGameStatsResponseStats"] = betterproto.message_field(4)
    achievement_blocks: List["CMsgAMGetUserGameStatsResponseAchievementBlocks"] = betterproto.message_field(5)


@dataclass
class CMsgAMGetUserGameStatsResponseStats(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    stat_value: int = betterproto.uint32_field(2)


@dataclass
class CMsgAMGetUserGameStatsResponseAchievementBlocks(betterproto.Message):
    achievement_id: int = betterproto.uint32_field(1)
    achievement_bit_id: int = betterproto.uint32_field(2)
    unlock_time: float = betterproto.fixed32_field(3)


@dataclass
class CMsgGCGetCommandList(betterproto.Message):
    app_id: int = betterproto.uint32_field(1)
    command_prefix: str = betterproto.string_field(2)


@dataclass
class CMsgGCGetCommandListResponse(betterproto.Message):
    command_name: List[str] = betterproto.string_field(1)


@dataclass
class CGCMsgMemCachedGet(betterproto.Message):
    keys: List[str] = betterproto.string_field(1)


@dataclass
class CGCMsgMemCachedGetResponse(betterproto.Message):
    values: List["CGCMsgMemCachedGetResponseValueTag"] = betterproto.message_field(1)


@dataclass
class CGCMsgMemCachedGetResponseValueTag(betterproto.Message):
    found: bool = betterproto.bool_field(1)
    value: bytes = betterproto.bytes_field(2)


@dataclass
class CGCMsgMemCachedSet(betterproto.Message):
    keys: List["CGCMsgMemCachedSetKeyPair"] = betterproto.message_field(1)


@dataclass
class CGCMsgMemCachedSetKeyPair(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: bytes = betterproto.bytes_field(2)


@dataclass
class CGCMsgMemCachedDelete(betterproto.Message):
    keys: List[str] = betterproto.string_field(1)


@dataclass
class CGCMsgMemCachedStats(betterproto.Message):
    pass


@dataclass
class CGCMsgMemCachedStatsResponse(betterproto.Message):
    curr_connections: int = betterproto.uint64_field(1)
    cmd_get: int = betterproto.uint64_field(2)
    cmd_set: int = betterproto.uint64_field(3)
    cmd_flush: int = betterproto.uint64_field(4)
    get_hits: int = betterproto.uint64_field(5)
    get_misses: int = betterproto.uint64_field(6)
    delete_hits: int = betterproto.uint64_field(7)
    delete_misses: int = betterproto.uint64_field(8)
    bytes_read: int = betterproto.uint64_field(9)
    bytes_written: int = betterproto.uint64_field(10)
    limit_maxbytes: int = betterproto.uint64_field(11)
    curr_items: int = betterproto.uint64_field(12)
    evictions: int = betterproto.uint64_field(13)
    bytes: int = betterproto.uint64_field(14)


@dataclass
class CGCMsgSQLStats(betterproto.Message):
    schema_catalog: int = betterproto.uint32_field(1)


@dataclass
class CGCMsgSQLStatsResponse(betterproto.Message):
    threads: int = betterproto.uint32_field(1)
    threads_connected: int = betterproto.uint32_field(2)
    threads_active: int = betterproto.uint32_field(3)
    operations_submitted: int = betterproto.uint32_field(4)
    prepared_statements_executed: int = betterproto.uint32_field(5)
    non_prepared_statements_executed: int = betterproto.uint32_field(6)
    deadlock_retries: int = betterproto.uint32_field(7)
    operations_timed_out_in_queue: int = betterproto.uint32_field(8)
    errors: int = betterproto.uint32_field(9)


@dataclass
class CMsgAMAddFreeLicense(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    ip_public: int = betterproto.uint32_field(2)
    packageid: int = betterproto.uint32_field(3)
    store_country_code: str = betterproto.string_field(4)


@dataclass
class CMsgAMAddFreeLicenseResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)
    purchase_result_detail: int = betterproto.int32_field(2)
    transid: float = betterproto.fixed64_field(3)


@dataclass
class CGCMsgGetIPLocation(betterproto.Message):
    ips: List[float] = betterproto.fixed32_field(1)


@dataclass
class CIPLocationInfo(betterproto.Message):
    ip: int = betterproto.uint32_field(1)
    latitude: float = betterproto.float_field(2)
    longitude: float = betterproto.float_field(3)
    country: str = betterproto.string_field(4)
    state: str = betterproto.string_field(5)
    city: str = betterproto.string_field(6)


@dataclass
class CGCMsgGetIPLocationResponse(betterproto.Message):
    infos: List["CIPLocationInfo"] = betterproto.message_field(1)


@dataclass
class CGCMsgGetIPASN(betterproto.Message):
    ips: List[float] = betterproto.fixed32_field(1)


@dataclass
class CIPASNInfo(betterproto.Message):
    ip: float = betterproto.fixed32_field(1)
    asn: int = betterproto.uint32_field(2)


@dataclass
class CGCMsgGetIPASNResponse(betterproto.Message):
    infos: List["CIPASNInfo"] = betterproto.message_field(1)


@dataclass
class CGCMsgSystemStatsSchema(betterproto.Message):
    gc_app_id: int = betterproto.uint32_field(1)
    schema_kv: bytes = betterproto.bytes_field(2)


@dataclass
class CGCMsgGetSystemStats(betterproto.Message):
    pass


@dataclass
class CGCMsgGetSystemStatsResponse(betterproto.Message):
    gc_app_id: int = betterproto.uint32_field(1)
    stats_kv: bytes = betterproto.bytes_field(2)
    active_jobs: int = betterproto.uint32_field(3)
    yielding_jobs: int = betterproto.uint32_field(4)
    user_sessions: int = betterproto.uint32_field(5)
    game_server_sessions: int = betterproto.uint32_field(6)
    socaches: int = betterproto.uint32_field(7)
    socaches_to_unload: int = betterproto.uint32_field(8)
    socaches_loading: int = betterproto.uint32_field(9)
    writeback_queue: int = betterproto.uint32_field(10)
    steamid_locks: int = betterproto.uint32_field(11)
    logon_queue: int = betterproto.uint32_field(12)
    logon_jobs: int = betterproto.uint32_field(13)


@dataclass
class CMsgAMSendEmail(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    email_msg_type: int = betterproto.uint32_field(2)
    email_format: int = betterproto.uint32_field(3)
    persona_name_tokens: List["CMsgAMSendEmailPersonaNameReplacementToken"] = betterproto.message_field(5)
    source_gc: int = betterproto.uint32_field(6)
    tokens: List["CMsgAMSendEmailReplacementToken"] = betterproto.message_field(7)


@dataclass
class CMsgAMSendEmailReplacementToken(betterproto.Message):
    token_name: str = betterproto.string_field(1)
    token_value: str = betterproto.string_field(2)


@dataclass
class CMsgAMSendEmailPersonaNameReplacementToken(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    token_name: str = betterproto.string_field(2)


@dataclass
class CMsgAMSendEmailResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)


@dataclass
class CMsgGCGetEmailTemplate(betterproto.Message):
    app_id: int = betterproto.uint32_field(1)
    email_msg_type: int = betterproto.uint32_field(2)
    email_lang: int = betterproto.int32_field(3)
    email_format: int = betterproto.int32_field(4)


@dataclass
class CMsgGCGetEmailTemplateResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)
    template_exists: bool = betterproto.bool_field(2)
    template: str = betterproto.string_field(3)


@dataclass
class CMsgAMGrantGuestPasses2(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    package_id: int = betterproto.uint32_field(2)
    passes_to_grant: int = betterproto.int32_field(3)
    days_to_expiration: int = betterproto.int32_field(4)
    action: int = betterproto.int32_field(5)


@dataclass
class CMsgAMGrantGuestPasses2Response(betterproto.Message):
    eresult: int = betterproto.int32_field(1)
    passes_granted: int = betterproto.int32_field(2)


@dataclass
class CGCSystemMsgGetAccountDetails(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    appid: int = betterproto.uint32_field(2)


@dataclass
class CGCSystemMsgGetAccountDetailsResponse(betterproto.Message):
    eresult_deprecated: int = betterproto.uint32_field(1)
    account_name: str = betterproto.string_field(2)
    persona_name: str = betterproto.string_field(3)
    is_profile_created: bool = betterproto.bool_field(26)
    is_profile_public: bool = betterproto.bool_field(4)
    is_inventory_public: bool = betterproto.bool_field(5)
    is_vac_banned: bool = betterproto.bool_field(7)
    is_cyber_cafe: bool = betterproto.bool_field(8)
    is_school_account: bool = betterproto.bool_field(9)
    is_limited: bool = betterproto.bool_field(10)
    is_subscribed: bool = betterproto.bool_field(11)
    package: int = betterproto.uint32_field(12)
    is_free_trial_account: bool = betterproto.bool_field(13)
    free_trial_expiration: int = betterproto.uint32_field(14)
    is_low_violence: bool = betterproto.bool_field(15)
    is_account_locked_down: bool = betterproto.bool_field(16)
    is_community_banned: bool = betterproto.bool_field(17)
    is_trade_banned: bool = betterproto.bool_field(18)
    trade_ban_expiration: int = betterproto.uint32_field(19)
    accountid: int = betterproto.uint32_field(20)
    suspension_end_time: int = betterproto.uint32_field(21)
    currency: str = betterproto.string_field(22)
    steam_level: int = betterproto.uint32_field(23)
    friend_count: int = betterproto.uint32_field(24)
    account_creation_time: int = betterproto.uint32_field(25)
    is_steamguard_enabled: bool = betterproto.bool_field(27)
    is_phone_verified: bool = betterproto.bool_field(28)
    is_two_factor_auth_enabled: bool = betterproto.bool_field(29)
    two_factor_enabled_time: int = betterproto.uint32_field(30)
    phone_verification_time: int = betterproto.uint32_field(31)
    phone_id: int = betterproto.uint64_field(33)
    is_phone_identifying: bool = betterproto.bool_field(34)
    rt_identity_linked: int = betterproto.uint32_field(35)
    rt_birth_date: int = betterproto.uint32_field(36)
    txn_country_code: str = betterproto.string_field(37)


@dataclass
class CMsgGCGetPersonaNames(betterproto.Message):
    steamids: List[float] = betterproto.fixed64_field(1)


@dataclass
class CMsgGCGetPersonaNamesResponse(betterproto.Message):
    succeeded_lookups: List["CMsgGCGetPersonaNamesResponsePersonaName"] = betterproto.message_field(1)
    failed_lookup_steamids: List[float] = betterproto.fixed64_field(2)


@dataclass
class CMsgGCGetPersonaNamesResponsePersonaName(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    persona_name: str = betterproto.string_field(2)


@dataclass
class CMsgGCCheckFriendship(betterproto.Message):
    steamid_left: float = betterproto.fixed64_field(1)
    steamid_right: float = betterproto.fixed64_field(2)


@dataclass
class CMsgGCCheckFriendshipResponse(betterproto.Message):
    success: bool = betterproto.bool_field(1)
    found_friendship: bool = betterproto.bool_field(2)


@dataclass
class CMsgGCGetAppFriendsList(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    include_friendship_timestamps: bool = betterproto.bool_field(2)


@dataclass
class CMsgGCGetAppFriendsListResponse(betterproto.Message):
    success: bool = betterproto.bool_field(1)
    steamids: List[float] = betterproto.fixed64_field(2)
    friendship_timestamps: List[float] = betterproto.fixed32_field(3)
    last_playtimes: List[float] = betterproto.fixed32_field(4)


@dataclass
class CMsgGCMsgMasterSetDirectory(betterproto.Message):
    master_dir_index: int = betterproto.uint32_field(1)
    dir: List["CMsgGCMsgMasterSetDirectorySubGC"] = betterproto.message_field(2)


@dataclass
class CMsgGCMsgMasterSetDirectorySubGC(betterproto.Message):
    dir_index: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    box: str = betterproto.string_field(3)
    command_line: str = betterproto.string_field(4)
    gc_binary: str = betterproto.string_field(5)


@dataclass
class CMsgGCMsgMasterSetDirectoryResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)
    message: str = betterproto.string_field(2)


@dataclass
class CMsgGCMsgWebAPIJobRequestForwardResponse(betterproto.Message):
    dir_index: int = betterproto.uint32_field(1)


@dataclass
class CGCSystemMsgGetPurchaseTrustRequest(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CGCSystemMsgGetPurchaseTrustResponse(betterproto.Message):
    has_prior_purchase_history: bool = betterproto.bool_field(1)
    has_no_recent_password_resets: bool = betterproto.bool_field(2)
    is_wallet_cash_trusted: bool = betterproto.bool_field(3)
    time_all_trusted: int = betterproto.uint32_field(4)


@dataclass
class CMsgGCHAccountVacStatusChange(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    app_id: int = betterproto.uint32_field(2)
    rtime_vacban_starts: int = betterproto.uint32_field(3)
    is_banned_now: bool = betterproto.bool_field(4)
    is_banned_future: bool = betterproto.bool_field(5)


@dataclass
class CMsgGCGetPartnerAccountLink(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CMsgGCGetPartnerAccountLinkResponse(betterproto.Message):
    pwid: int = betterproto.uint32_field(1)
    nexonid: int = betterproto.uint32_field(2)
    ageclass: int = betterproto.int32_field(3)
    id_verified: bool = betterproto.bool_field(4)
    is_adult: bool = betterproto.bool_field(5)


@dataclass
class CMsgGCRoutingInfo(betterproto.Message):
    dir_index: List[int] = betterproto.uint32_field(1)
    method: "CMsgGCRoutingInfoRoutingMethod" = betterproto.enum_field(2)
    fallback: "CMsgGCRoutingInfoRoutingMethod" = betterproto.enum_field(3)
    protobuf_field: int = betterproto.uint32_field(4)
    webapi_param: str = betterproto.string_field(5)


@dataclass
class CMsgGCMsgMasterSetWebAPIRouting(betterproto.Message):
    entries: List["CMsgGCMsgMasterSetWebAPIRoutingEntry"] = betterproto.message_field(1)


@dataclass
class CMsgGCMsgMasterSetWebAPIRoutingEntry(betterproto.Message):
    interface_name: str = betterproto.string_field(1)
    method_name: str = betterproto.string_field(2)
    routing: "CMsgGCRoutingInfo" = betterproto.message_field(3)


@dataclass
class CMsgGCMsgMasterSetClientMsgRouting(betterproto.Message):
    entries: List["CMsgGCMsgMasterSetClientMsgRoutingEntry"] = betterproto.message_field(1)


@dataclass
class CMsgGCMsgMasterSetClientMsgRoutingEntry(betterproto.Message):
    msg_type: int = betterproto.uint32_field(1)
    routing: "CMsgGCRoutingInfo" = betterproto.message_field(2)


@dataclass
class CMsgGCMsgMasterSetWebAPIRoutingResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)


@dataclass
class CMsgGCMsgMasterSetClientMsgRoutingResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)


@dataclass
class CMsgGCMsgSetOptions(betterproto.Message):
    options: List["CMsgGCMsgSetOptionsOption"] = betterproto.enum_field(1)
    client_msg_ranges: List["CMsgGCMsgSetOptionsMessageRange"] = betterproto.message_field(2)
    gcsql_version: "CMsgGCMsgSetOptionsGCSQLVersion" = betterproto.enum_field(3)


@dataclass
class CMsgGCMsgSetOptionsMessageRange(betterproto.Message):
    low: int = betterproto.uint32_field(1)
    high: int = betterproto.uint32_field(2)


@dataclass
class CMsgGCHUpdateSession(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    app_id: int = betterproto.uint32_field(2)
    online: bool = betterproto.bool_field(3)
    server_steam_id: float = betterproto.fixed64_field(4)
    server_addr: int = betterproto.uint32_field(5)
    server_port: int = betterproto.uint32_field(6)
    os_type: int = betterproto.uint32_field(7)
    client_addr: int = betterproto.uint32_field(8)
    extra_fields: List["CMsgGCHUpdateSessionExtraField"] = betterproto.message_field(9)


@dataclass
class CMsgGCHUpdateSessionExtraField(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CMsgNotificationOfSuspiciousActivity(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    appid: int = betterproto.uint32_field(2)
    multiple_instances: "CMsgNotificationOfSuspiciousActivityMultipleGameInstances" = betterproto.message_field(3)


@dataclass
class CMsgNotificationOfSuspiciousActivityMultipleGameInstances(betterproto.Message):
    app_instance_count: int = betterproto.uint32_field(1)
    other_steamids: List[float] = betterproto.fixed64_field(2)


@dataclass
class CMsgDPPartnerMicroTxns(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    gc_name: str = betterproto.string_field(2)
    partner: "CMsgDPPartnerMicroTxnsPartnerInfo" = betterproto.message_field(3)
    transactions: List["CMsgDPPartnerMicroTxnsPartnerMicroTxn"] = betterproto.message_field(4)


@dataclass
class CMsgDPPartnerMicroTxnsPartnerMicroTxn(betterproto.Message):
    init_time: int = betterproto.uint32_field(1)
    last_update_time: int = betterproto.uint32_field(2)
    txn_id: int = betterproto.uint64_field(3)
    account_id: int = betterproto.uint32_field(4)
    line_item: int = betterproto.uint32_field(5)
    item_id: int = betterproto.uint64_field(6)
    def_index: int = betterproto.uint32_field(7)
    price: int = betterproto.uint64_field(8)
    tax: int = betterproto.uint64_field(9)
    price_usd: int = betterproto.uint64_field(10)
    tax_usd: int = betterproto.uint64_field(11)
    purchase_type: int = betterproto.uint32_field(12)
    steam_txn_type: int = betterproto.uint32_field(13)
    country_code: str = betterproto.string_field(14)
    region_code: str = betterproto.string_field(15)
    quantity: int = betterproto.int32_field(16)
    ref_trans_id: int = betterproto.uint64_field(17)


@dataclass
class CMsgDPPartnerMicroTxnsPartnerInfo(betterproto.Message):
    partner_id: int = betterproto.uint32_field(1)
    partner_name: str = betterproto.string_field(2)
    currency_code: str = betterproto.string_field(3)
    currency_name: str = betterproto.string_field(4)


@dataclass
class CMsgDPPartnerMicroTxnsResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)
    eerrorcode: "CMsgDPPartnerMicroTxnsResponseEErrorCode" = betterproto.enum_field(2)


@dataclass
class CMsgGCHVacVerificationChange(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    appid: int = betterproto.uint32_field(2)
    is_verified: bool = betterproto.bool_field(3)


@dataclass
class CMsgGCHAccountTwoFactorChange(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    appid: int = betterproto.uint32_field(2)
    twofactor_enabled: bool = betterproto.bool_field(3)


@dataclass
class CMsgGCCheckClanMembership(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    clanid: int = betterproto.uint32_field(2)


@dataclass
class CMsgGCCheckClanMembershipResponse(betterproto.Message):
    ismember: bool = betterproto.bool_field(1)


@dataclass
class CGCSystemMsgReportExternalPurchaseRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    steamid: float = betterproto.fixed64_field(2)
    provider: "EMobilePaymentProvider" = betterproto.enum_field(3)
    orderid: int = betterproto.uint64_field(4)
    provider_orderid: str = betterproto.string_field(5)
    amount: int = betterproto.int64_field(6)
    currency: str = betterproto.string_field(7)
    quantity: int = betterproto.uint32_field(8)
    itemid: int = betterproto.uint32_field(9)
    item_description: str = betterproto.string_field(10)
    language: str = betterproto.string_field(11)
    category: str = betterproto.string_field(12)
    time_created: int = betterproto.uint32_field(13)


@dataclass
class CGCSystemMsgReportExternalPurchaseResponse(betterproto.Message):
    transid: float = betterproto.fixed64_field(1)
    orderid: int = betterproto.uint64_field(2)


@dataclass
class CWorkshopAddSpecialPaymentRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    gameitemid: int = betterproto.uint32_field(2)
    date: str = betterproto.string_field(3)
    payment_us_usd: int = betterproto.uint64_field(4)
    payment_row_usd: int = betterproto.uint64_field(5)


@dataclass
class CWorkshopAddSpecialPaymentResponse(betterproto.Message):
    pass


@dataclass
class CWorkshopGetSpecialPaymentsRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    gameitemid: int = betterproto.uint32_field(2)
    date: str = betterproto.string_field(3)


@dataclass
class CWorkshopGetSpecialPaymentsResponse(betterproto.Message):
    special_payments: List["CWorkshopGetSpecialPaymentsResponseSpecialPayment"] = betterproto.message_field(1)


@dataclass
class CWorkshopGetSpecialPaymentsResponseSpecialPayment(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    gameitemid: int = betterproto.uint32_field(2)
    date: str = betterproto.string_field(3)
    net_payment_us_usd: int = betterproto.uint64_field(4)
    net_payment_row_usd: int = betterproto.uint64_field(5)