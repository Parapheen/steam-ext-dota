# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_client_enums.proto
# plugin: python-betterproto

import betterproto


class ETournamentTemplate(betterproto.Enum):
    NONE = 0
    AutomatedWin3 = 1


class ETournamentGameState(betterproto.Enum):
    Unknown = 0
    Canceled = 1
    Scheduled = 2
    Active = 3
    RadVictory = 20
    DireVictory = 21
    RadVictoryByForfeit = 22
    DireVictoryByForfeit = 23
    ServerFailure = 40
    NotNeeded = 41


class ETournamentTeamState(betterproto.Enum):
    Unknown = 0
    Node1 = 1
    NodeMax = 1024
    Eliminated = 14003
    Forfeited = 14004
    Finished1st = 15001
    Finished2nd = 15002
    Finished3rd = 15003
    Finished4th = 15004
    Finished5th = 15005
    Finished6th = 15006
    Finished7th = 15007
    Finished8th = 15008
    Finished9th = 15009
    Finished10th = 15010
    Finished11th = 15011
    Finished12th = 15012
    Finished13th = 15013
    Finished14th = 15014
    Finished15th = 15015
    Finished16th = 15016


class ETournamentState(betterproto.Enum):
    Unknown = 0
    CanceledByAdmin = 1
    Completed = 2
    Merged = 3
    ServerFailure = 4
    TeamAbandoned = 5
    TeamTimeoutForfeit = 6
    TeamTimeoutRefund = 7
    ServerFailureGrantedVictory = 8
    TeamTimeoutGrantedVictory = 9
    InProgress = 100
    WaitingToMerge = 101


class ETournamentNodeState(betterproto.Enum):
    Unknown = 0
    Canceled = 1
    TeamsNotYetAssigned = 2
    InBetweenGames = 3
    GameInProgress = 4
    AWon = 5
    BWon = 6
    AWonByForfeit = 7
    BWonByForfeit = 8
    ABye = 9
    AAbandoned = 10
    ServerFailure = 11
    ATimeoutForfeit = 12
    ATimeoutRefund = 13


class EDOTAGroupMergeResult(betterproto.Enum):
    OK = 0
    FailedGeneric = 1
    NotLeader = 2
    TooManyPlayers = 3
    TooManyCoaches = 4
    EngineMismatch = 5
    NoSuchGroup = 6
    OtherGroupNotOpen = 7
    AlreadyInvited = 8
    NotInvited = 9


class EPartyBeaconType(betterproto.Enum):
    Available = 0
    Joinable = 1