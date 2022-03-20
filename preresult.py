from dataclasses import dataclass

from performance import Performance
from statistics_full import StatisticsFull


@dataclass()
class PreResult:
    id: int
    home_accurateCrosses: float
    home_accurateFinalThirdPassesAgainst: float
    home_accurateLongBalls: float
    home_accurateOppositionHalfPasses: float
    home_accurateOppositionHalfPassesAgainst: float
    home_accurateOwnHalfPasses: float
    home_accurateOwnHalfPassesAgainst: float
    home_accuratePasses: float
    home_accuratePassesAgainst: float
    home_aerialDuelsWon: float
    home_assists: float
    home_averageBallPossession: float
    home_avgRating: float
    home_bigChances: float
    home_bigChancesAgainst: float
    home_bigChancesCreated: float
    home_bigChancesCreatedAgainst: float
    home_bigChancesMissed: float
    home_bigChancesMissedAgainst: float
    home_cleanSheets: float
    home_clearances: float
    home_clearancesAgainst: float
    home_clearancesOffLine: float
    home_corners: float
    home_cornersAgainst: float
    home_crossesSuccessfulAgainst: float
    home_crossesTotalAgainst: float
    home_dribbleAttempts: float
    home_dribbleAttemptsTotalAgainst: float
    home_dribbleAttemptsWonAgainst: float
    home_duelsWon: float
    home_errorsLeadingToGoal: float
    home_errorsLeadingToGoalAgainst: float
    home_errorsLeadingToShot: float
    home_errorsLeadingToShotAgainst: float
    home_fastBreakGoals: float
    home_fastBreakShots: float
    home_fastBreaks: float
    home_fouls: float
    home_freeKickGoals: float
    home_freeKickShots: float
    home_goalsConceded: float
    home_goalsFromInsideTheBox: float
    home_goalsFromOutsideTheBox: float
    home_goalsScored: float
    home_groundDuelsWon: float
    home_headedGoals: float
    home_hitWoodwork: float
    home_hitWoodworkAgainst: float
    home_interceptions: float
    home_interceptionsAgainst: float
    home_keyPassesAgainst: float
    home_lastManTackles: float
    home_leftFootGoals: float
    home_longBallsSuccessfulAgainst: float
    home_longBallsTotalAgainst: float
    home_matches: float
    home_offsides: float
    home_offsidesAgainst: float
    home_oppositionHalfPassesTotalAgainst: float
    home_ownGoals: float
    home_ownHalfPassesTotalAgainst: float
    home_penaltiesCommited: float
    home_penaltiesTaken: float
    home_penaltyGoals: float
    home_penaltyGoalsConceded: float
    home_possessionLost: float
    home_redCards: float
    home_redCardsAgainst: float
    home_rightFootGoals: float
    home_saves: float
    home_shots: float
    home_shotsAgainst: float
    home_shotsBlockedAgainst: float
    home_shotsFromInsideTheBox: float
    home_shotsFromInsideTheBoxAgainst: float
    home_shotsFromOutsideTheBox: float
    home_shotsFromOutsideTheBoxAgainst: float
    home_shotsOffTarget: float
    home_shotsOffTargetAgainst: float
    home_shotsOnTarget: float
    home_shotsOnTargetAgainst: float
    home_successfulDribbles: float
    home_tackles: float
    home_tacklesAgainst: float
    home_totalAerialDuels: float
    home_totalCrosses: float
    home_totalDuels: float
    home_totalFinalThirdPassesAgainst: float
    home_totalGroundDuels: float
    home_totalLongBalls: float
    home_totalOppositionHalfPasses: float
    home_totalOwnHalfPasses: float
    home_totalPasses: float
    home_totalPassesAgainst: float
    home_yellowCards: float
    home_yellowCardsAgainst: float
    home_yellowRedCards: float
    away_accurateCrosses: float
    away_accurateFinalThirdPassesAgainst: float
    away_accurateLongBalls: float
    away_accurateOppositionHalfPasses: float
    away_accurateOppositionHalfPassesAgainst: float
    away_accurateOwnHalfPasses: float
    away_accurateOwnHalfPassesAgainst: float
    away_accuratePasses: float
    away_accuratePassesAgainst: float
    away_aerialDuelsWon: float
    away_assists: float
    away_averageBallPossession: float
    away_avgRating: float
    away_bigChances: float
    away_bigChancesAgainst: float
    away_bigChancesCreated: float
    away_bigChancesCreatedAgainst: float
    away_bigChancesMissed: float
    away_bigChancesMissedAgainst: float
    away_cleanSheets: float
    away_clearances: float
    away_clearancesAgainst: float
    away_clearancesOffLine: float
    away_corners: float
    away_cornersAgainst: float
    away_crossesSuccessfulAgainst: float
    away_crossesTotalAgainst: float
    away_dribbleAttempts: float
    away_dribbleAttemptsTotalAgainst: float
    away_dribbleAttemptsWonAgainst: float
    away_duelsWon: float
    away_errorsLeadingToGoal: float
    away_errorsLeadingToGoalAgainst: float
    away_errorsLeadingToShot: float
    away_errorsLeadingToShotAgainst: float
    away_fastBreakGoals: float
    away_fastBreakShots: float
    away_fastBreaks: float
    away_fouls: float
    away_freeKickGoals: float
    away_freeKickShots: float
    away_goalsConceded: float
    away_goalsFromInsideTheBox: float
    away_goalsFromOutsideTheBox: float
    away_goalsScored: float
    away_groundDuelsWon: float
    away_headedGoals: float
    away_hitWoodwork: float
    away_hitWoodworkAgainst: float
    away_interceptions: float
    away_interceptionsAgainst: float
    away_keyPassesAgainst: float
    away_lastManTackles: float
    away_leftFootGoals: float
    away_longBallsSuccessfulAgainst: float
    away_longBallsTotalAgainst: float
    away_matches: float
    away_offsides: float
    away_offsidesAgainst: float
    away_oppositionHalfPassesTotalAgainst: float
    away_ownGoals: float
    away_ownHalfPassesTotalAgainst: float
    away_penaltiesCommited: float
    away_penaltiesTaken: float
    away_penaltyGoals: float
    away_penaltyGoalsConceded: float
    away_possessionLost: float
    away_redCards: float
    away_redCardsAgainst: float
    away_rightFootGoals: float
    away_saves: float
    away_shots: float
    away_shotsAgainst: float
    away_shotsBlockedAgainst: float
    away_shotsFromInsideTheBox: float
    away_shotsFromInsideTheBoxAgainst: float
    away_shotsFromOutsideTheBox: float
    away_shotsFromOutsideTheBoxAgainst: float
    away_shotsOffTarget: float
    away_shotsOffTargetAgainst: float
    away_shotsOnTarget: float
    away_shotsOnTargetAgainst: float
    away_successfulDribbles: float
    away_tackles: float
    away_tacklesAgainst: float
    away_totalAerialDuels: float
    away_totalCrosses: float
    away_totalDuels: float
    away_totalFinalThirdPassesAgainst: float
    away_totalGroundDuels: float
    away_totalLongBalls: float
    away_totalOppositionHalfPasses: float
    away_totalOwnHalfPasses: float
    away_totalPasses: float
    away_totalPassesAgainst: float
    away_yellowCards: float
    away_yellowCardsAgainst: float
    away_yellowRedCards: float
    home_last_goals: int
    home_last_goals_against: int
    home_last_possession: int
    home_last_totalShots: int
    home_last_shotsOnTarget: int
    home_last_blockedShots: int
    home_last_fouls: int
    home_last_yellowCard: int
    home_last_redCard: int
    home_last_bigChances: int
    home_last_bigChancesMissed: int
    home_last_shotsInsideTheBox: int
    home_last_shotsOutsideTheBox: int
    home_last_goalkeeperSaves: int
    home_last_offside: int
    home_last_totalPasses: int
    home_last_accuratePasses: int
    home_last_totalLongBalls: int
    home_last_accurateLongBalls: int
    home_last_totalCrosses: int
    home_last_accurateCrosses: int
    home_last_totalDribles: int
    home_last_accurateDribles: int
    home_last_duelsWon: int
    home_last_aerialDuelsWon: int
    home_last_tackles: int
    home_last_interceptions: int
    home_last_clearances: int
    home_last_cornerKicks: int
    home_last_possession_against: int
    home_last_totalShots_against: int
    home_last_shotsOnTarget_against: int
    home_last_blockedShots_against: int
    home_last_fouls_against: int
    home_last_yellowCard_against: int
    home_last_redCard_against: int
    home_last_bigChances_against: int
    home_last_bigChancesMissed_against: int
    home_last_shotsInsideTheBox_against: int
    home_last_shotsOutsideTheBox_against: int
    home_last_goalkeeperSaves_against: int
    home_last_offside_against: int
    home_last_totalPasses_against: int
    home_last_accuratePasses_against: int
    home_last_totalLongBalls_against: int
    home_last_accurateLongBalls_against: int
    home_last_totalCrosses_against: int
    home_last_accurateCrosses_against: int
    home_last_totalDribles_against: int
    home_last_accurateDribles_against: int
    home_last_duelsWon_against: int
    home_last_aerialDuelsWon_against: int
    home_last_tackles_against: int
    home_last_interceptions_against: int
    home_last_clearances_against: int
    home_last_cornerKicks_against: int
    away_last_goals: int
    away_last_goals_against: int
    away_last_possession: int
    away_last_totalShots: int
    away_last_shotsOnTarget: int
    away_last_blockedShots: int
    away_last_fouls: int
    away_last_yellowCard: int
    away_last_redCard: int
    away_last_bigChances: int
    away_last_bigChancesMissed: int
    away_last_shotsInsideTheBox: int
    away_last_shotsOutsideTheBox: int
    away_last_goalkeeperSaves: int
    away_last_offside: int
    away_last_totalPasses: int
    away_last_accuratePasses: int
    away_last_totalLongBalls: int
    away_last_accurateLongBalls: int
    away_last_totalCrosses: int
    away_last_accurateCrosses: int
    away_last_totalDribles: int
    away_last_accurateDribles: int
    away_last_duelsWon: int
    away_last_aerialDuelsWon: int
    away_last_tackles: int
    away_last_interceptions: int
    away_last_clearances: int
    away_last_cornerKicks: int
    away_last_possession_against: int
    away_last_totalShots_against: int
    away_last_shotsOnTarget_against: int
    away_last_blockedShots_against: int
    away_last_fouls_against: int
    away_last_yellowCard_against: int
    away_last_redCard_against: int
    away_last_bigChances_against: int
    away_last_bigChancesMissed_against: int
    away_last_shotsInsideTheBox_against: int
    away_last_shotsOutsideTheBox_against: int
    away_last_goalkeeperSaves_against: int
    away_last_offside_against: int
    away_last_totalPasses_against: int
    away_last_accuratePasses_against: int
    away_last_totalLongBalls_against: int
    away_last_accurateLongBalls_against: int
    away_last_totalCrosses_against: int
    away_last_accurateCrosses_against: int
    away_last_totalDribles_against: int
    away_last_accurateDribles_against: int
    away_last_duelsWon_against: int
    away_last_aerialDuelsWon_against: int
    away_last_tackles_against: int
    away_last_interceptions_against: int
    away_last_clearances_against: int
    away_last_cornerKicks_against: int
    home_head_goals: int
    home_head_possession: int
    home_head_totalShots: int
    home_head_shotsOnTarget: int
    home_head_blockedShots: int
    home_head_fouls: int
    home_head_yellowCard: int
    home_head_redCard: int
    home_head_bigChances: int
    home_head_bigChancesMissed: int
    home_head_shotsInsideTheBox: int
    home_head_shotsOutsideTheBox: int
    home_head_goalkeeperSaves: int
    home_head_offside: int
    home_head_totalPasses: int
    home_head_accuratePasses: int
    home_head_totalLongBalls: int
    home_head_accurateLongBalls: int
    home_head_totalCrosses: int
    home_head_accurateCrosses: int
    home_head_totalDribles: int
    home_head_accurateDribles: int
    home_head_duelsWon: int
    home_head_aerialDuelsWon: int
    home_head_tackles: int
    home_head_interceptions: int
    home_head_clearances: int
    home_head_cornerKicks: int
    away_head_goals: int
    away_head_possession: int
    away_head_totalShots: int
    away_head_shotsOnTarget: int
    away_head_blockedShots: int
    away_head_fouls: int
    away_head_yellowCard: int
    away_head_redCard: int
    away_head_bigChances: int
    away_head_bigChancesMissed: int
    away_head_shotsInsideTheBox: int
    away_head_shotsOutsideTheBox: int
    away_head_goalkeeperSaves: int
    away_head_offside: int
    away_head_totalPasses: int
    away_head_accuratePasses: int
    away_head_totalLongBalls: int
    away_head_accurateLongBalls: int
    away_head_totalCrosses: int
    away_head_accurateCrosses: int
    away_head_totalDribles: int
    away_head_accurateDribles: int
    away_head_duelsWon: int
    away_head_aerialDuelsWon: int
    away_head_tackles: int
    away_head_interceptions: int
    away_head_clearances: int
    away_head_cornerKicks: int

    def __init__(self, match_id, home: Performance, away: Performance,
                 homeLast: StatisticsFull, awayLast: StatisticsFull,
                 homeHead: StatisticsFull, awayHead: StatisticsFull):
        self.id = match_id
        self.home_accurateCrosses = home.accurateCrosses
        self.home_accurateFinalThirdPassesAgainst = home.accurateFinalThirdPassesAgainst
        self.home_accurateLongBalls = home.accurateLongBalls
        self.home_accurateOppositionHalfPasses = home.accurateOppositionHalfPasses
        self.home_accurateOppositionHalfPassesAgainst = home.accurateOppositionHalfPassesAgainst
        self.home_accurateOwnHalfPasses = home.accurateOwnHalfPasses
        self.home_accurateOwnHalfPassesAgainst = home.accurateOwnHalfPassesAgainst
        self.home_accuratePasses = home.accuratePasses
        self.home_accuratePassesAgainst = home.accuratePassesAgainst
        self.home_aerialDuelsWon = home.aerialDuelsWon
        self.home_assists = home.assists
        self.home_averageBallPossession = home.averageBallPossession
        self.home_avgRating = home.avgRating
        self.home_bigChances = home.bigChances
        self.home_bigChancesAgainst = home.bigChancesAgainst
        self.home_bigChancesCreated = home.bigChancesCreated
        self.home_bigChancesCreatedAgainst = home.bigChancesCreatedAgainst
        self.home_bigChancesMissed = home.bigChancesMissed
        self.home_bigChancesMissedAgainst = home.bigChancesMissedAgainst
        self.home_cleanSheets = home.cleanSheets
        self.home_clearances = home.clearances
        self.home_clearancesAgainst = home.clearancesAgainst
        self.home_clearancesOffLine = home.clearancesOffLine
        self.home_corners = home.corners
        self.home_cornersAgainst = home.cornersAgainst
        self.home_crossesSuccessfulAgainst = home.crossesSuccessfulAgainst
        self.home_crossesTotalAgainst = home.crossesTotalAgainst
        self.home_dribbleAttempts = home.dribbleAttempts
        self.home_dribbleAttemptsTotalAgainst = home.dribbleAttemptsTotalAgainst
        self.home_dribbleAttemptsWonAgainst = home.dribbleAttemptsWonAgainst
        self.home_duelsWon = home.duelsWon
        self.home_errorsLeadingToGoal = home.errorsLeadingToGoal
        self.home_errorsLeadingToGoalAgainst = home.errorsLeadingToGoalAgainst
        self.home_errorsLeadingToShot = home.errorsLeadingToShot
        self.home_errorsLeadingToShotAgainst = home.errorsLeadingToShotAgainst
        self.home_fastBreakGoals = home.fastBreakGoals
        self.home_fastBreakShots = home.fastBreakShots
        self.home_fastBreaks = home.fastBreaks
        self.home_fouls = home.fouls
        self.home_freeKickGoals = home.freeKickGoals
        self.home_freeKickShots = home.freeKickShots
        self.home_goalsConceded = home.goalsConceded
        self.home_goalsFromInsideTheBox = home.goalsFromInsideTheBox
        self.home_goalsFromOutsideTheBox = home.goalsFromOutsideTheBox
        self.home_goalsScored = home.goalsScored
        self.home_groundDuelsWon = home.groundDuelsWon
        self.home_headedGoals = home.headedGoals
        self.home_hitWoodwork = home.hitWoodwork
        self.home_hitWoodworkAgainst = home.hitWoodworkAgainst
        self.home_erceptions = home.interceptions
        self.home_erceptionsAgainst = home.interceptionsAgainst
        self.home_keyPassesAgainst = home.keyPassesAgainst
        self.home_lastManTackles = home.lastManTackles
        self.home_leftFootGoals = home.leftFootGoals
        self.home_longBallsSuccessfulAgainst = home.longBallsSuccessfulAgainst
        self.home_longBallsTotalAgainst = home.longBallsTotalAgainst
        self.home_matches = home.matches
        self.home_offsides = home.offsides
        self.home_offsidesAgainst = home.offsidesAgainst
        self.home_oppositionHalfPassesTotalAgainst = home.oppositionHalfPassesTotalAgainst
        self.home_ownGoals = home.ownGoals
        self.home_ownHalfPassesTotalAgainst = home.ownHalfPassesTotalAgainst
        self.home_penaltiesCommited = home.penaltiesCommited
        self.home_penaltiesTaken = home.penaltiesTaken
        self.home_penaltyGoals = home.penaltyGoals
        self.home_penaltyGoalsConceded = home.penaltyGoalsConceded
        self.home_possessionLost = home.possessionLost
        self.home_redCards = home.redCards
        self.home_redCardsAgainst = home.redCardsAgainst
        self.home_rightFootGoals = home.rightFootGoals
        self.home_saves = home.saves
        self.home_shots = home.shots
        self.home_shotsAgainst = home.shotsAgainst
        self.home_shotsBlockedAgainst = home.shotsBlockedAgainst
        self.home_shotsFromInsideTheBox = home.shotsFromInsideTheBox
        self.home_shotsFromInsideTheBoxAgainst = home.shotsFromInsideTheBoxAgainst
        self.home_shotsFromOutsideTheBox = home.shotsFromOutsideTheBox
        self.home_shotsFromOutsideTheBoxAgainst = home.shotsFromOutsideTheBoxAgainst
        self.home_shotsOffTarget = home.shotsOffTarget
        self.home_shotsOffTargetAgainst = home.shotsOffTargetAgainst
        self.home_shotsOnTarget = home.shotsOnTarget
        self.home_shotsOnTargetAgainst = home.shotsOnTargetAgainst
        self.home_successfulDribbles = home.successfulDribbles
        self.home_tackles = home.tackles
        self.home_tacklesAgainst = home.tacklesAgainst
        self.home_totalAerialDuels = home.totalAerialDuels
        self.home_totalCrosses = home.totalCrosses
        self.home_totalDuels = home.totalDuels
        self.home_totalFinalThirdPassesAgainst = home.totalFinalThirdPassesAgainst
        self.home_totalGroundDuels = home.totalGroundDuels
        self.home_totalLongBalls = home.totalLongBalls
        self.home_totalOppositionHalfPasses = home.totalOppositionHalfPasses
        self.home_totalOwnHalfPasses = home.totalOwnHalfPasses
        self.home_totalPasses = home.totalPasses
        self.home_totalPassesAgainst = home.totalPassesAgainst
        self.home_yellowCards = home.yellowCards
        self.home_yellowCardsAgainst = home.yellowCardsAgainst
        self.home_yellowRedCards = home.yellowRedCards
        self.away_accurateCrosses = away.accurateCrosses
        self.away_accurateFinalThirdPassesAgainst = away.accurateFinalThirdPassesAgainst
        self.away_accurateLongBalls = away.accurateLongBalls
        self.away_accurateOppositionHalfPasses = away.accurateOppositionHalfPasses
        self.away_accurateOppositionHalfPassesAgainst = away.accurateOppositionHalfPassesAgainst
        self.away_accurateOwnHalfPasses = away.accurateOwnHalfPasses
        self.away_accurateOwnHalfPassesAgainst = away.accurateOwnHalfPassesAgainst
        self.away_accuratePasses = away.accuratePasses
        self.away_accuratePassesAgainst = away.accuratePassesAgainst
        self.away_aerialDuelsWon = away.aerialDuelsWon
        self.away_assists = away.assists
        self.away_averageBallPossession = away.averageBallPossession
        self.away_avgRating = away.avgRating
        self.away_bigChances = away.bigChances
        self.away_bigChancesAgainst = away.bigChancesAgainst
        self.away_bigChancesCreated = away.bigChancesCreated
        self.away_bigChancesCreatedAgainst = away.bigChancesCreatedAgainst
        self.away_bigChancesMissed = away.bigChancesMissed
        self.away_bigChancesMissedAgainst = away.bigChancesMissedAgainst
        self.away_cleanSheets = away.cleanSheets
        self.away_clearances = away.clearances
        self.away_clearancesAgainst = away.clearancesAgainst
        self.away_clearancesOffLine = away.clearancesOffLine
        self.away_corners = away.corners
        self.away_cornersAgainst = away.cornersAgainst
        self.away_crossesSuccessfulAgainst = away.crossesSuccessfulAgainst
        self.away_crossesTotalAgainst = away.crossesTotalAgainst
        self.away_dribbleAttempts = away.dribbleAttempts
        self.away_dribbleAttemptsTotalAgainst = away.dribbleAttemptsTotalAgainst
        self.away_dribbleAttemptsWonAgainst = away.dribbleAttemptsWonAgainst
        self.away_duelsWon = away.duelsWon
        self.away_errorsLeadingToGoal = away.errorsLeadingToGoal
        self.away_errorsLeadingToGoalAgainst = away.errorsLeadingToGoalAgainst
        self.away_errorsLeadingToShot = away.errorsLeadingToShot
        self.away_errorsLeadingToShotAgainst = away.errorsLeadingToShotAgainst
        self.away_fastBreakGoals = away.fastBreakGoals
        self.away_fastBreakShots = away.fastBreakShots
        self.away_fastBreaks = away.fastBreaks
        self.away_fouls = away.fouls
        self.away_freeKickGoals = away.freeKickGoals
        self.away_freeKickShots = away.freeKickShots
        self.away_goalsConceded = away.goalsConceded
        self.away_goalsFromInsideTheBox = away.goalsFromInsideTheBox
        self.away_goalsFromOutsideTheBox = away.goalsFromOutsideTheBox
        self.away_goalsScored = away.goalsScored
        self.away_groundDuelsWon = away.groundDuelsWon
        self.away_headedGoals = away.headedGoals
        self.away_hitWoodwork = away.hitWoodwork
        self.away_hitWoodworkAgainst = away.hitWoodworkAgainst
        self.away_erceptions = away.interceptions
        self.away_erceptionsAgainst = away.interceptionsAgainst
        self.away_keyPassesAgainst = away.keyPassesAgainst
        self.away_lastManTackles = away.lastManTackles
        self.away_leftFootGoals = away.leftFootGoals
        self.away_longBallsSuccessfulAgainst = away.longBallsSuccessfulAgainst
        self.away_longBallsTotalAgainst = away.longBallsTotalAgainst
        self.away_matches = away.matches
        self.away_offsides = away.offsides
        self.away_offsidesAgainst = away.offsidesAgainst
        self.away_oppositionHalfPassesTotalAgainst = away.oppositionHalfPassesTotalAgainst
        self.away_ownGoals = away.ownGoals
        self.away_ownHalfPassesTotalAgainst = away.ownHalfPassesTotalAgainst
        self.away_penaltiesCommited = away.penaltiesCommited
        self.away_penaltiesTaken = away.penaltiesTaken
        self.away_penaltyGoals = away.penaltyGoals
        self.away_penaltyGoalsConceded = away.penaltyGoalsConceded
        self.away_possessionLost = away.possessionLost
        self.away_redCards = away.redCards
        self.away_redCardsAgainst = away.redCardsAgainst
        self.away_rightFootGoals = away.rightFootGoals
        self.away_saves = away.saves
        self.away_shots = away.shots
        self.away_shotsAgainst = away.shotsAgainst
        self.away_shotsBlockedAgainst = away.shotsBlockedAgainst
        self.away_shotsFromInsideTheBox = away.shotsFromInsideTheBox
        self.away_shotsFromInsideTheBoxAgainst = away.shotsFromInsideTheBoxAgainst
        self.away_shotsFromOutsideTheBox = away.shotsFromOutsideTheBox
        self.away_shotsFromOutsideTheBoxAgainst = away.shotsFromOutsideTheBoxAgainst
        self.away_shotsOffTarget = away.shotsOffTarget
        self.away_shotsOffTargetAgainst = away.shotsOffTargetAgainst
        self.away_shotsOnTarget = away.shotsOnTarget
        self.away_shotsOnTargetAgainst = away.shotsOnTargetAgainst
        self.away_successfulDribbles = away.successfulDribbles
        self.away_tackles = away.tackles
        self.away_tacklesAgainst = away.tacklesAgainst
        self.away_totalAerialDuels = away.totalAerialDuels
        self.away_totalCrosses = away.totalCrosses
        self.away_totalDuels = away.totalDuels
        self.away_totalFinalThirdPassesAgainst = away.totalFinalThirdPassesAgainst
        self.away_totalGroundDuels = away.totalGroundDuels
        self.away_totalLongBalls = away.totalLongBalls
        self.away_totalOppositionHalfPasses = away.totalOppositionHalfPasses
        self.away_totalOwnHalfPasses = away.totalOwnHalfPasses
        self.away_totalPasses = away.totalPasses
        self.away_totalPassesAgainst = away.totalPassesAgainst
        self.away_yellowCards = away.yellowCards
        self.away_yellowCardsAgainst = away.yellowCardsAgainst
        self.away_yellowRedCards = away.yellowRedCards
        self.home_last_goals = homeLast.goals
        self.home_last_goals_against = homeLast.goals_against
        self.home_last_possession = homeLast.possession
        self.home_last_totalShots = homeLast.totalShots
        self.home_last_shotsOnTarget = homeLast.shotsOnTarget
        self.home_last_blockedShots = homeLast.blockedShots
        self.home_last_fouls = homeLast.fouls
        self.home_last_yellowCard = homeLast.yellowCard
        self.home_last_redCard = homeLast.redCard
        self.home_last_bigChances = homeLast.bigChances
        self.home_last_bigChancesMissed = homeLast.bigChancesMissed
        self.home_last_shotsInsideTheBox = homeLast.shotsInsideTheBox
        self.home_last_shotsOutsideTheBox = homeLast.shotsOutsideTheBox
        self.home_last_goalkeeperSaves = homeLast.goalkeeperSaves
        self.home_last_offside = homeLast.offside
        self.home_last_totalPasses = homeLast.totalPasses
        self.home_last_accuratePasses = homeLast.accuratePasses
        self.home_last_totalLongBalls = homeLast.totalLongBalls
        self.home_last_accurateLongBalls = homeLast.accurateLongBalls
        self.home_last_totalCrosses = homeLast.totalCrosses
        self.home_last_accurateCrosses = homeLast.accurateCrosses
        self.home_last_totalDribles = homeLast.totalDribles
        self.home_last_accurateDribles = homeLast.accurateDribles
        self.home_last_duelsWon = homeLast.duelsWon
        self.home_last_aerialDuelsWon = homeLast.aerialDuelsWon
        self.home_last_tackles = homeLast.tackles
        self.home_last_erceptions = homeLast.interceptions
        self.home_last_clearances = homeLast.clearances
        self.home_last_cornerKicks = homeLast.cornerKicks
        self.home_last_possession_against = homeLast.possession_against
        self.home_last_totalShots_against = homeLast.totalShots_against
        self.home_last_shotsOnTarget_against = homeLast.shotsOnTarget_against
        self.home_last_blockedShots_against = homeLast.blockedShots_against
        self.home_last_fouls_against = homeLast.fouls_against
        self.home_last_yellowCard_against = homeLast.yellowCard_against
        self.home_last_redCard_against = homeLast.redCard_against
        self.home_last_bigChances_against = homeLast.bigChances_against
        self.home_last_bigChancesMissed_against = homeLast.bigChancesMissed_against
        self.home_last_shotsInsideTheBox_against = homeLast.shotsInsideTheBox_against
        self.home_last_shotsOutsideTheBox_against = homeLast.shotsOutsideTheBox_against
        self.home_last_goalkeeperSaves_against = homeLast.goalkeeperSaves_against
        self.home_last_offside_against = homeLast.offside_against
        self.home_last_totalPasses_against = homeLast.totalPasses_against
        self.home_last_accuratePasses_against = homeLast.accuratePasses_against
        self.home_last_totalLongBalls_against = homeLast.totalLongBalls_against
        self.home_last_accurateLongBalls_against = homeLast.accurateLongBalls_against
        self.home_last_totalCrosses_against = homeLast.totalCrosses_against
        self.home_last_accurateCrosses_against = homeLast.accurateCrosses_against
        self.home_last_totalDribles_against = homeLast.totalDribles_against
        self.home_last_accurateDribles_against = homeLast.accurateDribles_against
        self.home_last_duelsWon_against = homeLast.duelsWon_against
        self.home_last_aerialDuelsWon_against = homeLast.aerialDuelsWon_against
        self.home_last_tackles_against = homeLast.tackles_against
        self.home_last_erceptions_against = homeLast.interceptions_against
        self.home_last_clearances_against = homeLast.clearances_against
        self.home_last_cornerKicks_against = homeLast.cornerKicks_against
        self.away_last_goals = awayLast.goals
        self.away_last_goals_against = awayLast.goals_against
        self.away_last_possession = awayLast.possession
        self.away_last_totalShots = awayLast.totalShots
        self.away_last_shotsOnTarget = awayLast.shotsOnTarget
        self.away_last_blockedShots = awayLast.blockedShots
        self.away_last_fouls = awayLast.fouls
        self.away_last_yellowCard = awayLast.yellowCard
        self.away_last_redCard = awayLast.redCard
        self.away_last_bigChances = awayLast.bigChances
        self.away_last_bigChancesMissed = awayLast.bigChancesMissed
        self.away_last_shotsInsideTheBox = awayLast.shotsInsideTheBox
        self.away_last_shotsOutsideTheBox = awayLast.shotsOutsideTheBox
        self.away_last_goalkeeperSaves = awayLast.goalkeeperSaves
        self.away_last_offside = awayLast.offside
        self.away_last_totalPasses = awayLast.totalPasses
        self.away_last_accuratePasses = awayLast.accuratePasses
        self.away_last_totalLongBalls = awayLast.totalLongBalls
        self.away_last_accurateLongBalls = awayLast.accurateLongBalls
        self.away_last_totalCrosses = awayLast.totalCrosses
        self.away_last_accurateCrosses = awayLast.accurateCrosses
        self.away_last_totalDribles = awayLast.totalDribles
        self.away_last_accurateDribles = awayLast.accurateDribles
        self.away_last_duelsWon = awayLast.duelsWon
        self.away_last_aerialDuelsWon = awayLast.aerialDuelsWon
        self.away_last_tackles = awayLast.tackles
        self.away_last_erceptions = awayLast.interceptions
        self.away_last_clearances = awayLast.clearances
        self.away_last_cornerKicks = awayLast.cornerKicks
        self.away_last_possession_against = awayLast.possession_against
        self.away_last_totalShots_against = awayLast.totalShots_against
        self.away_last_shotsOnTarget_against = awayLast.shotsOnTarget_against
        self.away_last_blockedShots_against = awayLast.blockedShots_against
        self.away_last_fouls_against = awayLast.fouls_against
        self.away_last_yellowCard_against = awayLast.yellowCard_against
        self.away_last_redCard_against = awayLast.redCard_against
        self.away_last_bigChances_against = awayLast.bigChances_against
        self.away_last_bigChancesMissed_against = awayLast.bigChancesMissed_against
        self.away_last_shotsInsideTheBox_against = awayLast.shotsInsideTheBox_against
        self.away_last_shotsOutsideTheBox_against = awayLast.shotsOutsideTheBox_against
        self.away_last_goalkeeperSaves_against = awayLast.goalkeeperSaves_against
        self.away_last_offside_against = awayLast.offside_against
        self.away_last_totalPasses_against = awayLast.totalPasses_against
        self.away_last_accuratePasses_against = awayLast.accuratePasses_against
        self.away_last_totalLongBalls_against = awayLast.totalLongBalls_against
        self.away_last_accurateLongBalls_against = awayLast.accurateLongBalls_against
        self.away_last_totalCrosses_against = awayLast.totalCrosses_against
        self.away_last_accurateCrosses_against = awayLast.accurateCrosses_against
        self.away_last_totalDribles_against = awayLast.totalDribles_against
        self.away_last_accurateDribles_against = awayLast.accurateDribles_against
        self.away_last_duelsWon_against = awayLast.duelsWon_against
        self.away_last_aerialDuelsWon_against = awayLast.aerialDuelsWon_against
        self.away_last_tackles_against = awayLast.tackles_against
        self.away_last_erceptions_against = awayLast.interceptions_against
        self.away_last_clearances_against = awayLast.clearances_against
        self.away_last_cornerKicks_against = awayLast.cornerKicks_against
        self.home_head_goals = homeHead.goals
        self.home_head_possession = homeHead.possession
        self.home_head_totalShots = homeHead.totalShots
        self.home_head_shotsOnTarget = homeHead.shotsOnTarget
        self.home_head_blockedShots = homeHead.blockedShots
        self.home_head_fouls = homeHead.fouls
        self.home_head_yellowCard = homeHead.yellowCard
        self.home_head_redCard = homeHead.redCard
        self.home_head_bigChances = homeHead.bigChances
        self.home_head_bigChancesMissed = homeHead.bigChancesMissed
        self.home_head_shotsInsideTheBox = homeHead.shotsInsideTheBox
        self.home_head_shotsOutsideTheBox = homeHead.shotsOutsideTheBox
        self.home_head_goalkeeperSaves = homeHead.goalkeeperSaves
        self.home_head_offside = homeHead.offside
        self.home_head_totalPasses = homeHead.totalPasses
        self.home_head_accuratePasses = homeHead.accuratePasses
        self.home_head_totalLongBalls = homeHead.totalLongBalls
        self.home_head_accurateLongBalls = homeHead.accurateLongBalls
        self.home_head_totalCrosses = homeHead.totalCrosses
        self.home_head_accurateCrosses = homeHead.accurateCrosses
        self.home_head_totalDribles = homeHead.totalDribles
        self.home_head_accurateDribles = homeHead.accurateDribles
        self.home_head_duelsWon = homeHead.duelsWon
        self.home_head_aerialDuelsWon = homeHead.aerialDuelsWon
        self.home_head_tackles = homeHead.tackles
        self.home_head_erceptions = homeHead.interceptions
        self.home_head_clearances = homeHead.clearances
        self.home_head_cornerKicks = homeHead.cornerKicks
        self.away_head_goals = awayHead.goals
        self.away_head_possession = awayHead.possession
        self.away_head_totalShots = awayHead.totalShots
        self.away_head_shotsOnTarget = awayHead.shotsOnTarget
        self.away_head_blockedShots = awayHead.blockedShots
        self.away_head_fouls = awayHead.fouls
        self.away_head_yellowCard = awayHead.yellowCard
        self.away_head_redCard = awayHead.redCard
        self.away_head_bigChances = awayHead.bigChances
        self.away_head_bigChancesMissed = awayHead.bigChancesMissed
        self.away_head_shotsInsideTheBox = awayHead.shotsInsideTheBox
        self.away_head_shotsOutsideTheBox = awayHead.shotsOutsideTheBox
        self.away_head_goalkeeperSaves = awayHead.goalkeeperSaves
        self.away_head_offside = awayHead.offside
        self.away_head_totalPasses = awayHead.totalPasses
        self.away_head_accuratePasses = awayHead.accuratePasses
        self.away_head_totalLongBalls = awayHead.totalLongBalls
        self.away_head_accurateLongBalls = awayHead.accurateLongBalls
        self.away_head_totalCrosses = awayHead.totalCrosses
        self.away_head_accurateCrosses = awayHead.accurateCrosses
        self.away_head_totalDribles = awayHead.totalDribles
        self.away_head_accurateDribles = awayHead.accurateDribles
        self.away_head_duelsWon = awayHead.duelsWon
        self.away_head_aerialDuelsWon = awayHead.aerialDuelsWon
        self.away_head_tackles = awayHead.tackles
        self.away_head_erceptions = awayHead.interceptions
        self.away_head_clearances = awayHead.clearances
        self.away_head_cornerKicks = awayHead.cornerKicks