# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_match_metadata.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CDOTAMatchMetadataFile(betterproto.Message):
    version: int = betterproto.int32_field(1)
    match_id: int = betterproto.uint64_field(2)
    metadata: "CDOTAMatchMetadata" = betterproto.message_field(3)
    private_metadata: bytes = betterproto.bytes_field(5)


@dataclass
class CDOTAMatchMetadata(betterproto.Message):
    teams: List["CDOTAMatchMetadataTeam"] = betterproto.message_field(1)
    item_rewards: List["CLobbyTimedRewardDetails"] = betterproto.message_field(2)
    lobby_id: float = betterproto.fixed64_field(3)
    report_until_time: float = betterproto.fixed64_field(4)
    event_game_custom_table: bytes = betterproto.bytes_field(5)
    primary_event_id: int = betterproto.uint32_field(6)
    match_tips: List["CMsgMatchTips"] = betterproto.message_field(7)
    matchmaking_stats: "CMsgMatchMatchmakingStats" = betterproto.message_field(8)
    mvp_data: "CMvpData" = betterproto.message_field(9)
    guild_challenge_progress: List[
        "CDOTAMatchMetadataGuildChallengeProgress"
    ] = betterproto.message_field(10)


@dataclass
class CDOTAMatchMetadataTeam(betterproto.Message):
    dota_team: int = betterproto.uint32_field(1)
    players: List["CDOTAMatchMetadataTeamPlayer"] = betterproto.message_field(2)
    graph_experience: List[float] = betterproto.float_field(3)
    graph_gold_earned: List[float] = betterproto.float_field(4)
    graph_net_worth: List[float] = betterproto.float_field(5)
    cm_first_pick: bool = betterproto.bool_field(6)
    cm_captain_player_id: int = betterproto.uint32_field(7)
    cm_bans: List[int] = betterproto.uint32_field(8)
    cm_picks: List[int] = betterproto.uint32_field(9)
    cm_penalty: int = betterproto.uint32_field(10)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamPlayerKill(betterproto.Message):
    victim_slot: int = betterproto.uint32_field(1)
    count: int = betterproto.uint32_field(2)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamItemPurchase(betterproto.Message):
    item_id: int = betterproto.uint32_field(1)
    purchase_time: int = betterproto.int32_field(2)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamInventorySnapshot(betterproto.Message):
    item_id: List[int] = betterproto.uint32_field(1)
    game_time: int = betterproto.int32_field(2)
    kills: int = betterproto.uint32_field(3)
    deaths: int = betterproto.uint32_field(4)
    assists: int = betterproto.uint32_field(5)
    level: int = betterproto.uint32_field(6)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamAutoStyleCriteria(betterproto.Message):
    name_token: int = betterproto.uint32_field(1)
    value: float = betterproto.float_field(2)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamStrangeGemProgress(betterproto.Message):
    kill_eater_type: int = betterproto.uint32_field(1)
    gem_item_def_index: int = betterproto.uint32_field(2)
    required_hero_id: int = betterproto.uint32_field(3)
    starting_value: int = betterproto.uint32_field(4)
    ending_value: int = betterproto.uint32_field(5)
    owner_item_def_index: int = betterproto.uint32_field(6)
    owner_item_id: int = betterproto.uint64_field(7)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamVictoryPrediction(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    item_def_index: int = betterproto.uint32_field(2)
    starting_value: int = betterproto.uint32_field(3)
    is_victory: bool = betterproto.bool_field(4)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamSubChallenge(betterproto.Message):
    slot_id: int = betterproto.uint32_field(1)
    start_value: int = betterproto.uint32_field(2)
    end_value: int = betterproto.uint32_field(3)
    completed: bool = betterproto.bool_field(4)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamCavernChallengeResult(
    betterproto.Message
):
    completed_path_id: int = betterproto.uint32_field(1)
    claimed_room_id: int = betterproto.uint32_field(2)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamActionGrant(betterproto.Message):
    action_id: int = betterproto.uint32_field(1)
    quantity: int = betterproto.uint32_field(2)
    audit: int = betterproto.uint32_field(3)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamEventData(betterproto.Message):
    event_id: int = betterproto.uint32_field(1)
    event_points: int = betterproto.uint32_field(2)
    challenge_instance_id: int = betterproto.uint32_field(3)
    challenge_quest_id: int = betterproto.uint32_field(4)
    challenge_quest_challenge_id: int = betterproto.uint32_field(5)
    challenge_completed: bool = betterproto.bool_field(6)
    challenge_rank_completed: int = betterproto.uint32_field(7)
    challenge_rank_previously_completed: int = betterproto.uint32_field(8)
    event_owned: bool = betterproto.bool_field(9)
    sub_challenges_with_progress: List[
        "CDOTAMatchMetadataTeamSubChallenge"
    ] = betterproto.message_field(10)
    wager_winnings: int = betterproto.uint32_field(11)
    cavern_challenge_active: bool = betterproto.bool_field(12)
    cavern_challenge_winnings: int = betterproto.uint32_field(13)
    amount_wagered: int = betterproto.uint32_field(14)
    periodic_point_adjustments: int = betterproto.uint32_field(16)
    cavern_challenge_map_results: List[
        "CDOTAMatchMetadataTeamCavernChallengeResult"
    ] = betterproto.message_field(17)
    cavern_challenge_plus_shard_winnings: int = betterproto.uint32_field(18)
    actions_granted: List[
        "CDOTAMatchMetadataTeamActionGrant"
    ] = betterproto.message_field(19)
    cavern_crawl_map_variant: int = betterproto.uint32_field(20)
    team_wager_bonus_pct: int = betterproto.uint32_field(21)
    wager_streak_pct: int = betterproto.uint32_field(22)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamGauntletProgress(betterproto.Message):
    gauntlet_tier: int = betterproto.uint32_field(2)
    gauntlet_wins: int = betterproto.uint32_field(3)
    gauntlet_losses: int = betterproto.uint32_field(4)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamPlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    ability_upgrades: List[int] = betterproto.uint32_field(2)
    player_slot: int = betterproto.uint32_field(3)
    equipped_econ_items: List["CSOEconItem"] = betterproto.message_field(4)
    kills: List["CDOTAMatchMetadataTeamPlayerKill"] = betterproto.message_field(5)
    items: List["CDOTAMatchMetadataTeamItemPurchase"] = betterproto.message_field(6)
    avg_kills_x16: int = betterproto.uint32_field(7)
    avg_deaths_x16: int = betterproto.uint32_field(8)
    avg_assists_x16: int = betterproto.uint32_field(9)
    avg_gpm_x16: int = betterproto.uint32_field(10)
    avg_xpm_x16: int = betterproto.uint32_field(11)
    best_kills_x16: int = betterproto.uint32_field(12)
    best_assists_x16: int = betterproto.uint32_field(13)
    best_gpm_x16: int = betterproto.uint32_field(14)
    best_xpm_x16: int = betterproto.uint32_field(15)
    win_streak: int = betterproto.uint32_field(16)
    best_win_streak: int = betterproto.uint32_field(17)
    fight_score: float = betterproto.float_field(18)
    farm_score: float = betterproto.float_field(19)
    support_score: float = betterproto.float_field(20)
    push_score: float = betterproto.float_field(21)
    level_up_times: List[int] = betterproto.uint32_field(22)
    graph_net_worth: List[float] = betterproto.float_field(23)
    inventory_snapshot: List[
        "CDOTAMatchMetadataTeamInventorySnapshot"
    ] = betterproto.message_field(24)
    avg_stats_calibrated: bool = betterproto.bool_field(25)
    auto_style_criteria: List[
        "CDOTAMatchMetadataTeamAutoStyleCriteria"
    ] = betterproto.message_field(26)
    event_data: List["CDOTAMatchMetadataTeamEventData"] = betterproto.message_field(29)
    strange_gem_progress: List[
        "CDOTAMatchMetadataTeamStrangeGemProgress"
    ] = betterproto.message_field(30)
    hero_xp: int = betterproto.uint32_field(31)
    camps_stacked: int = betterproto.uint32_field(32)
    victory_prediction: List[
        "CDOTAMatchMetadataTeamVictoryPrediction"
    ] = betterproto.message_field(33)
    lane_selection_flags: int = betterproto.uint32_field(34)
    rampages: int = betterproto.uint32_field(35)
    triple_kills: int = betterproto.uint32_field(36)
    aegis_snatched: int = betterproto.uint32_field(37)
    rapiers_purchased: int = betterproto.uint32_field(38)
    couriers_killed: int = betterproto.uint32_field(39)
    net_worth_rank: int = betterproto.uint32_field(40)
    support_gold_spent: int = betterproto.uint32_field(41)
    observer_wards_placed: int = betterproto.uint32_field(42)
    sentry_wards_placed: int = betterproto.uint32_field(43)
    wards_dewarded: int = betterproto.uint32_field(44)
    stun_duration: float = betterproto.float_field(45)
    rank_mmr_boost_type: "EDOTAMMRBoostType" = betterproto.enum_field(46)
    gauntlet_progress: "CDOTAMatchMetadataTeamGauntletProgress" = (
        betterproto.message_field(47)
    )
    contract_progress: List[
        "CDOTAMatchMetadataTeamPlayerContractProgress"
    ] = betterproto.message_field(48)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataTeamCDOTAMatchMetadataCDOTAMatchMetadataTeamPlayerContractProgress(
    betterproto.Message
):
    guild_id: int = betterproto.uint32_field(1)
    event_id: int = betterproto.uint32_field(2)
    challenge_instance_id: int = betterproto.uint32_field(3)
    challenge_parameter: int = betterproto.uint32_field(4)
    contract_stars: int = betterproto.uint32_field(5)
    contract_slot: int = betterproto.uint32_field(6)
    completed: bool = betterproto.bool_field(7)


@dataclass
class CDOTAMatchMetadataGuildChallengeProgress(betterproto.Message):
    guild_id: int = betterproto.uint32_field(1)
    event_id: "EEvent" = betterproto.enum_field(2)
    challenge_instance_id: int = betterproto.uint32_field(3)
    challenge_parameter: int = betterproto.uint32_field(4)
    challenge_timestamp: int = betterproto.uint32_field(5)
    challenge_progress_at_start: int = betterproto.uint32_field(6)
    challenge_progress_accumulated: int = betterproto.uint32_field(7)
    individual_progress: List[
        "CDOTAMatchMetadataGuildChallengeProgressIndividualProgress"
    ] = betterproto.message_field(8)


@dataclass
class CDOTAMatchMetadataCDOTAMatchMetadataGuildChallengeProgressIndividualProgress(
    betterproto.Message
):
    account_id: int = betterproto.uint32_field(1)
    progress: int = betterproto.uint32_field(2)


@dataclass
class CDOTAMatchPrivateMetadata(betterproto.Message):
    teams: List["CDOTAMatchPrivateMetadataTeam"] = betterproto.message_field(1)
    graph_win_probability: List[float] = betterproto.float_field(2)
    string_names: List[
        "CDOTAMatchPrivateMetadataStringName"
    ] = betterproto.message_field(3)


@dataclass
class CDOTAMatchPrivateMetadataStringName(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)


@dataclass
class CDOTAMatchPrivateMetadataTeam(betterproto.Message):
    dota_team: int = betterproto.uint32_field(1)
    players: List["CDOTAMatchPrivateMetadataTeamPlayer"] = betterproto.message_field(2)
    buildings: List[
        "CDOTAMatchPrivateMetadataTeamBuilding"
    ] = betterproto.message_field(3)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    player_slot: int = betterproto.uint32_field(2)
    position_stream: bytes = betterproto.bytes_field(3)
    combat_segments: List[
        "CDOTAMatchPrivateMetadataTeamPlayerCombatSegment"
    ] = betterproto.message_field(4)
    damage_unit_names: List[str] = betterproto.string_field(5)
    buff_records: List[
        "CDOTAMatchPrivateMetadataTeamPlayerBuffRecord"
    ] = betterproto.message_field(6)
    graph_kills: List[float] = betterproto.float_field(7)
    graph_deaths: List[float] = betterproto.float_field(8)
    graph_assists: List[float] = betterproto.float_field(9)
    graph_lasthits: List[float] = betterproto.float_field(10)
    graph_denies: List[float] = betterproto.float_field(11)
    gold_received: "CDOTAMatchPrivateMetadataTeamPlayerGoldReceived" = (
        betterproto.message_field(12)
    )
    xp_received: "CDOTAMatchPrivateMetadataTeamPlayerXPReceived" = (
        betterproto.message_field(13)
    )


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCombatSegment(
    betterproto.Message
):
    game_time: int = betterproto.int32_field(1)
    damage_by_ability: List[
        "CDOTAMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbility"
    ] = betterproto.message_field(2)
    healing_by_ability: List[
        "CDOTAMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbility"
    ] = betterproto.message_field(3)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbility(
    betterproto.Message
):
    source_unit_index: int = betterproto.uint32_field(3)
    ability_id: int = betterproto.uint32_field(1)
    by_hero_targets: List[
        "CDOTAMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbilityByHeroTarget"
    ] = betterproto.message_field(2)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCombatSegmentCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbilityByHeroTarget(
    betterproto.Message
):
    hero_id: int = betterproto.uint32_field(1)
    damage: int = betterproto.uint32_field(2)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbility(
    betterproto.Message
):
    source_unit_index: int = betterproto.uint32_field(3)
    ability_id: int = betterproto.uint32_field(1)
    by_hero_targets: List[
        "CDOTAMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbilityByHeroTarget"
    ] = betterproto.message_field(2)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCombatSegmentCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbilityByHeroTarget(
    betterproto.Message
):
    hero_id: int = betterproto.uint32_field(1)
    healing: int = betterproto.uint32_field(2)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerBuffRecord(
    betterproto.Message
):
    buff_ability_id: int = betterproto.uint32_field(1)
    buff_modifier_name: str = betterproto.string_field(3)
    by_hero_targets: List[
        "CDOTAMatchPrivateMetadataTeamPlayerBuffRecordByHeroTarget"
    ] = betterproto.message_field(2)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerBuffRecordByHeroTarget(
    betterproto.Message
):
    hero_id: int = betterproto.uint32_field(1)
    elapsed_duration: float = betterproto.float_field(2)
    is_hidden: bool = betterproto.bool_field(3)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerGoldReceived(
    betterproto.Message
):
    creep: int = betterproto.uint32_field(1)
    heroes: int = betterproto.uint32_field(2)
    bounty_runes: int = betterproto.uint32_field(3)
    passive: int = betterproto.uint32_field(4)
    buildings: int = betterproto.uint32_field(5)
    abilities: int = betterproto.uint32_field(6)
    wards: int = betterproto.uint32_field(7)
    other: int = betterproto.uint32_field(8)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamCDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamPlayerXPReceived(
    betterproto.Message
):
    creep: int = betterproto.uint32_field(1)
    heroes: int = betterproto.uint32_field(2)
    roshan: int = betterproto.uint32_field(3)
    tome_of_knowledge: int = betterproto.uint32_field(4)
    outpost: int = betterproto.uint32_field(5)
    other: int = betterproto.uint32_field(6)


@dataclass
class CDOTAMatchPrivateMetadataCDOTAMatchPrivateMetadataTeamBuilding(
    betterproto.Message
):
    unit_name: str = betterproto.string_field(1)
    position_quant_x: int = betterproto.uint32_field(2)
    position_quant_y: int = betterproto.uint32_field(3)
    death_time: float = betterproto.float_field(4)


@dataclass
class CMsgDOTADPCMatch(betterproto.Message):
    match: "CMsgDOTAMatch" = betterproto.message_field(1)
    metadata: "CDOTAMatchMetadata" = betterproto.message_field(2)