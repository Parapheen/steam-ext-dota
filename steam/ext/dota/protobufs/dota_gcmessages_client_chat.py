# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_client_chat.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


class CMsgGCToClientPrivateChatResponseResult(betterproto.Enum):
    Success = 0
    FailureCreationLock = 1
    FailureSqlTransaction = 2
    FailureSdoLoad = 3
    FailureNoPermission = 4
    FailureAlreadyMember = 5
    FailureNotAMember = 7
    FailureNoRemainingAdmins = 8
    FailureNoRoom = 9
    FailureCreationRateLimited = 10
    FailureUnknownChannelName = 11
    FailureUnknownUser = 12
    FailureUnknownError = 13
    FailureCannotKickAdmin = 14
    FailureAlreadyAdmin = 15


class CMsgDOTAJoinChatChannelResponseResult(betterproto.Enum):
    JoinSuccess = 0
    InvalidChannelType = 1
    AccountNotFound = 2
    AchFailed = 3
    UserInTooManyChannels = 4
    RateLimitExceeded = 5
    ChannelFull = 6
    ChannelFullOverflowed = 7
    FailedToAddUser = 8
    ChannelTypeDisabled = 9
    PrivateChatCreateFailed = 10
    PrivateChatNoPermission = 11
    PrivateChatCreateLockFailed = 12
    PrivateChatKicked = 13
    UserNotAllowed = 14


@dataclass
class CMsgClientToGCPrivateChatInvite(betterproto.Message):
    private_chat_channel_name: str = betterproto.string_field(1)
    invited_account_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgClientToGCPrivateChatKick(betterproto.Message):
    private_chat_channel_name: str = betterproto.string_field(1)
    kick_account_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgClientToGCPrivateChatPromote(betterproto.Message):
    private_chat_channel_name: str = betterproto.string_field(1)
    promote_account_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgClientToGCPrivateChatDemote(betterproto.Message):
    private_chat_channel_name: str = betterproto.string_field(1)
    demote_account_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgGCToClientPrivateChatResponse(betterproto.Message):
    private_chat_channel_name: str = betterproto.string_field(1)
    result: "CMsgGCToClientPrivateChatResponseResult" = betterproto.enum_field(2)
    username: str = betterproto.string_field(3)


@dataclass
class CMsgClientToGCPrivateChatInfoRequest(betterproto.Message):
    private_chat_channel_name: str = betterproto.string_field(1)


@dataclass
class CMsgGCToClientPrivateChatInfoResponse(betterproto.Message):
    private_chat_channel_name: str = betterproto.string_field(1)
    members: List["CMsgGCToClientPrivateChatInfoResponseMember"] = betterproto.message_field(2)
    creator: int = betterproto.uint32_field(3)
    creation_date: int = betterproto.uint32_field(4)


@dataclass
class CMsgGCToClientPrivateChatInfoResponseMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    status: int = betterproto.uint32_field(3)


@dataclass
class CMsgDOTAJoinChatChannel(betterproto.Message):
    channel_name: str = betterproto.string_field(2)
    channel_type: "DOTAChatChannelTypeT" = betterproto.enum_field(4)


@dataclass
class CMsgDOTALeaveChatChannel(betterproto.Message):
    channel_id: int = betterproto.uint64_field(1)


@dataclass
class CMsgGCChatReportPublicSpam(betterproto.Message):
    channel_id: int = betterproto.uint64_field(1)
    channel_user_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTAClientIgnoredUser(betterproto.Message):
    ignored_account_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgDOTAChatMessage(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    channel_id: int = betterproto.uint64_field(2)
    persona_name: str = betterproto.string_field(3)
    text: str = betterproto.string_field(4)
    timestamp: int = betterproto.uint32_field(5)
    suggest_invite_account_id: int = betterproto.uint32_field(6)
    suggest_invite_name: str = betterproto.string_field(7)
    fantasy_draft_owner_account_id: int = betterproto.uint32_field(8)
    fantasy_draft_player_account_id: int = betterproto.uint32_field(9)
    event_id: int = betterproto.uint32_field(10)
    suggest_invite_to_lobby: bool = betterproto.bool_field(11)
    event_points: int = betterproto.uint32_field(12)
    coin_flip: bool = betterproto.bool_field(13)
    player_id: int = betterproto.int32_field(14)
    share_profile_account_id: int = betterproto.uint32_field(15)
    channel_user_id: int = betterproto.uint32_field(16)
    dice_roll: "CMsgDOTAChatMessageDiceRoll" = betterproto.message_field(17)
    share_party_id: int = betterproto.uint64_field(18)
    share_lobby_id: int = betterproto.uint64_field(19)
    share_lobby_custom_game_id: int = betterproto.uint64_field(20)
    share_lobby_passkey: str = betterproto.string_field(21)
    private_chat_channel_id: int = betterproto.uint32_field(22)
    status: int = betterproto.uint32_field(23)
    legacy_battle_cup_victory: bool = betterproto.bool_field(24)
    battle_cup_streak: int = betterproto.uint32_field(29)
    badge_level: int = betterproto.uint32_field(25)
    suggest_pick_hero_id: int = betterproto.uint32_field(26)
    suggest_pick_hero_role: str = betterproto.string_field(27)
    suggest_ban_hero_id: int = betterproto.uint32_field(30)
    trivia_answer: "CMsgDOTAChatMessageTriviaAnswered" = betterproto.message_field(32)
    requested_ability_id: int = betterproto.uint32_field(33)
    chat_flags: int = betterproto.uint32_field(34)
    started_finding_match: bool = betterproto.bool_field(35)
    ctrl_is_down: bool = betterproto.bool_field(36)


@dataclass
class CMsgDOTAChatMessageDiceRoll(betterproto.Message):
    roll_min: int = betterproto.int32_field(1)
    roll_max: int = betterproto.int32_field(2)
    result: int = betterproto.int32_field(3)


@dataclass
class CMsgDOTAChatMessageTriviaAnswered(betterproto.Message):
    question_id: int = betterproto.uint32_field(1)
    answer_index: int = betterproto.uint32_field(2)
    party_questions_correct: int = betterproto.uint32_field(3)
    party_questions_viewed: int = betterproto.uint32_field(4)
    party_trivia_points: int = betterproto.uint32_field(5)


@dataclass
class CMsgDOTAChatMember(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    persona_name: str = betterproto.string_field(2)
    channel_user_id: int = betterproto.uint32_field(3)
    status: int = betterproto.uint32_field(4)


@dataclass
class CMsgDOTAJoinChatChannelResponse(betterproto.Message):
    response: int = betterproto.uint32_field(1)
    channel_name: str = betterproto.string_field(2)
    channel_id: float = betterproto.fixed64_field(3)
    max_members: int = betterproto.uint32_field(4)
    members: List["CMsgDOTAChatMember"] = betterproto.message_field(5)
    channel_type: "DOTAChatChannelTypeT" = betterproto.enum_field(6)
    result: "CMsgDOTAJoinChatChannelResponseResult" = betterproto.enum_field(7)
    gc_initiated_join: bool = betterproto.bool_field(8)
    channel_user_id: int = betterproto.uint32_field(9)
    welcome_message: str = betterproto.string_field(10)


@dataclass
class CMsgDOTAChatChannelFullUpdate(betterproto.Message):
    channel_id: float = betterproto.fixed64_field(1)
    members: List["CMsgDOTAChatMember"] = betterproto.message_field(2)


@dataclass
class CMsgDOTAOtherJoinedChatChannel(betterproto.Message):
    channel_id: float = betterproto.fixed64_field(1)
    persona_name: str = betterproto.string_field(2)
    steam_id: float = betterproto.fixed64_field(3)
    channel_user_id: int = betterproto.uint32_field(4)
    status: int = betterproto.uint32_field(5)


@dataclass
class CMsgDOTAOtherLeftChatChannel(betterproto.Message):
    channel_id: float = betterproto.fixed64_field(1)
    steam_id: float = betterproto.fixed64_field(2)
    channel_user_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgDOTAChatChannelMemberUpdate(betterproto.Message):
    channel_id: float = betterproto.fixed64_field(1)
    left_steam_ids: List[float] = betterproto.fixed64_field(2)
    joined_members: List["CMsgDOTAChatChannelMemberUpdateJoinedMember"] = betterproto.message_field(3)


@dataclass
class CMsgDOTAChatChannelMemberUpdateJoinedMember(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    persona_name: str = betterproto.string_field(2)
    channel_user_id: int = betterproto.uint32_field(3)
    status: int = betterproto.uint32_field(4)


@dataclass
class CMsgDOTARequestChatChannelList(betterproto.Message):
    pass


@dataclass
class CMsgDOTARequestChatChannelListResponse(betterproto.Message):
    channels: List["CMsgDOTARequestChatChannelListResponseChatChannel"] = betterproto.message_field(1)


@dataclass
class CMsgDOTARequestChatChannelListResponseChatChannel(betterproto.Message):
    channel_name: str = betterproto.string_field(1)
    num_members: int = betterproto.uint32_field(2)
    channel_type: "DOTAChatChannelTypeT" = betterproto.enum_field(3)


@dataclass
class CMsgDOTAChatGetUserList(betterproto.Message):
    channel_id: float = betterproto.fixed64_field(1)


@dataclass
class CMsgDOTAChatGetUserListResponse(betterproto.Message):
    channel_id: float = betterproto.fixed64_field(1)
    members: List["CMsgDOTAChatGetUserListResponseMember"] = betterproto.message_field(2)


@dataclass
class CMsgDOTAChatGetUserListResponseMember(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    persona_name: str = betterproto.string_field(2)
    channel_user_id: int = betterproto.uint32_field(3)
    status: int = betterproto.uint32_field(4)


@dataclass
class CMsgDOTAChatGetMemberCount(betterproto.Message):
    channel_name: str = betterproto.string_field(1)
    channel_type: "DOTAChatChannelTypeT" = betterproto.enum_field(2)


@dataclass
class CMsgDOTAChatGetMemberCountResponse(betterproto.Message):
    channel_name: str = betterproto.string_field(1)
    channel_type: "DOTAChatChannelTypeT" = betterproto.enum_field(2)
    member_count: int = betterproto.uint32_field(3)


@dataclass
class CMsgDOTAChatRegionsEnabled(betterproto.Message):
    enable_all_regions: bool = betterproto.bool_field(1)
    enabled_regions: List["CMsgDOTAChatRegionsEnabledRegion"] = betterproto.message_field(2)


@dataclass
class CMsgDOTAChatRegionsEnabledRegion(betterproto.Message):
    min_latitude: float = betterproto.float_field(1)
    max_latitude: float = betterproto.float_field(2)
    min_longitude: float = betterproto.float_field(3)
    max_longitude: float = betterproto.float_field(4)
