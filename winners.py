from dataclasses import dataclass

from preresult import PreResult
from schedule import Schedule


@dataclass()
class Winners:
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
    home: int = 0
    draw: int = 0
    away: int = 0

    def __init__(self, match: Schedule, pre: PreResult):
        if match.home_win():
            self.home = 1
        elif match.draw():
            self.draw = 1
        elif match.away_win():
            self.away = 1
        self.id = pre.id
        self.home_accurateCrosses = pre.home_accurateCrosses
        self.home_accurateFinalThirdPassesAgainst = pre.home_accurateFinalThirdPassesAgainst
        self.home_accurateLongBalls = pre.home_accurateLongBalls
        self.home_accurateOppositionHalfPasses = pre.home_accurateOppositionHalfPasses
        self.home_accurateOppositionHalfPassesAgainst = pre.home_accurateOppositionHalfPassesAgainst
        self.home_accurateOwnHalfPasses = pre.home_accurateOwnHalfPasses
        self.home_accurateOwnHalfPassesAgainst = pre.home_accurateOwnHalfPassesAgainst
        self.home_accuratePasses = pre.home_accuratePasses
        self.home_accuratePassesAgainst = pre.home_accuratePassesAgainst
        self.home_aerialDuelsWon = pre.home_aerialDuelsWon
        self.home_assists = pre.home_assists
        self.home_averageBallPossession = pre.home_averageBallPossession
        self.home_avgRating = pre.home_avgRating
        self.home_bigChances = pre.home_bigChances
        self.home_bigChancesAgainst = pre.home_bigChancesAgainst
        self.home_bigChancesCreated = pre.home_bigChancesCreated
        self.home_bigChancesCreatedAgainst = pre.home_bigChancesCreatedAgainst
        self.home_bigChancesMissed = pre.home_bigChancesMissed
        self.home_bigChancesMissedAgainst = pre.home_bigChancesMissedAgainst
        self.home_cleanSheets = pre.home_cleanSheets
        self.home_clearances = pre.home_clearances
        self.home_clearancesAgainst = pre.home_clearancesAgainst
        self.home_clearancesOffLine = pre.home_clearancesOffLine
        self.home_corners = pre.home_corners
        self.home_cornersAgainst = pre.home_cornersAgainst
        self.home_crossesSuccessfulAgainst = pre.home_crossesSuccessfulAgainst
        self.home_crossesTotalAgainst = pre.home_crossesTotalAgainst
        self.home_dribbleAttempts = pre.home_dribbleAttempts
        self.home_dribbleAttemptsTotalAgainst = pre.home_dribbleAttemptsTotalAgainst
        self.home_dribbleAttemptsWonAgainst = pre.home_dribbleAttemptsWonAgainst
        self.home_duelsWon = pre.home_duelsWon
        self.home_errorsLeadingToGoal = pre.home_errorsLeadingToGoal
        self.home_errorsLeadingToGoalAgainst = pre.home_errorsLeadingToGoalAgainst
        self.home_errorsLeadingToShot = pre.home_errorsLeadingToShot
        self.home_errorsLeadingToShotAgainst = pre.home_errorsLeadingToShotAgainst
        self.home_fastBreakGoals = pre.home_fastBreakGoals
        self.home_fastBreakShots = pre.home_fastBreakShots
        self.home_fastBreaks = pre.home_fastBreaks
        self.home_fouls = pre.home_fouls
        self.home_freeKickGoals = pre.home_freeKickGoals
        self.home_freeKickShots = pre.home_freeKickShots
        self.home_goalsConceded = pre.home_goalsConceded
        self.home_goalsFromInsideTheBox = pre.home_goalsFromInsideTheBox
        self.home_goalsFromOutsideTheBox = pre.home_goalsFromOutsideTheBox
        self.home_goalsScored = pre.home_goalsScored
        self.home_groundDuelsWon = pre.home_groundDuelsWon
        self.home_headedGoals = pre.home_headedGoals
        self.home_hitWoodwork = pre.home_hitWoodwork
        self.home_hitWoodworkAgainst = pre.home_hitWoodworkAgainst
        self.home_interceptions = pre.home_interceptions
        self.home_interceptionsAgainst = pre.home_interceptionsAgainst
        self.home_keyPassesAgainst = pre.home_keyPassesAgainst
        self.home_lastManTackles = pre.home_lastManTackles
        self.home_leftFootGoals = pre.home_leftFootGoals
        self.home_longBallsSuccessfulAgainst = pre.home_longBallsSuccessfulAgainst
        self.home_longBallsTotalAgainst = pre.home_longBallsTotalAgainst
        self.home_matches = pre.home_matches
        self.home_offsides = pre.home_offsides
        self.home_offsidesAgainst = pre.home_offsidesAgainst
        self.home_oppositionHalfPassesTotalAgainst = pre.home_oppositionHalfPassesTotalAgainst
        self.home_ownGoals = pre.home_ownGoals
        self.home_ownHalfPassesTotalAgainst = pre.home_ownHalfPassesTotalAgainst
        self.home_penaltiesCommited = pre.home_penaltiesCommited
        self.home_penaltiesTaken = pre.home_penaltiesTaken
        self.home_penaltyGoals = pre.home_penaltyGoals
        self.home_penaltyGoalsConceded = pre.home_penaltyGoalsConceded
        self.home_possessionLost = pre.home_possessionLost
        self.home_redCards = pre.home_redCards
        self.home_redCardsAgainst = pre.home_redCardsAgainst
        self.home_rightFootGoals = pre.home_rightFootGoals
        self.home_saves = pre.home_saves
        self.home_shots = pre.home_shots
        self.home_shotsAgainst = pre.home_shotsAgainst
        self.home_shotsBlockedAgainst = pre.home_shotsBlockedAgainst
        self.home_shotsFromInsideTheBox = pre.home_shotsFromInsideTheBox
        self.home_shotsFromInsideTheBoxAgainst = pre.home_shotsFromInsideTheBoxAgainst
        self.home_shotsFromOutsideTheBox = pre.home_shotsFromOutsideTheBox
        self.home_shotsFromOutsideTheBoxAgainst = pre.home_shotsFromOutsideTheBoxAgainst
        self.home_shotsOffTarget = pre.home_shotsOffTarget
        self.home_shotsOffTargetAgainst = pre.home_shotsOffTargetAgainst
        self.home_shotsOnTarget = pre.home_shotsOnTarget
        self.home_shotsOnTargetAgainst = pre.home_shotsOnTargetAgainst
        self.home_successfulDribbles = pre.home_successfulDribbles
        self.home_tackles = pre.home_tackles
        self.home_tacklesAgainst = pre.home_tacklesAgainst
        self.home_totalAerialDuels = pre.home_totalAerialDuels
        self.home_totalCrosses = pre.home_totalCrosses
        self.home_totalDuels = pre.home_totalDuels
        self.home_totalFinalThirdPassesAgainst = pre.home_totalFinalThirdPassesAgainst
        self.home_totalGroundDuels = pre.home_totalGroundDuels
        self.home_totalLongBalls = pre.home_totalLongBalls
        self.home_totalOppositionHalfPasses = pre.home_totalOppositionHalfPasses
        self.home_totalOwnHalfPasses = pre.home_totalOwnHalfPasses
        self.home_totalPasses = pre.home_totalPasses
        self.home_totalPassesAgainst = pre.home_totalPassesAgainst
        self.home_yellowCards = pre.home_yellowCards
        self.home_yellowCardsAgainst = pre.home_yellowCardsAgainst
        self.home_yellowRedCards = pre.home_yellowRedCards
        self.away_accurateCrosses = pre.away_accurateCrosses
        self.away_accurateFinalThirdPassesAgainst = pre.away_accurateFinalThirdPassesAgainst
        self.away_accurateLongBalls = pre.away_accurateLongBalls
        self.away_accurateOppositionHalfPasses = pre.away_accurateOppositionHalfPasses
        self.away_accurateOppositionHalfPassesAgainst = pre.away_accurateOppositionHalfPassesAgainst
        self.away_accurateOwnHalfPasses = pre.away_accurateOwnHalfPasses
        self.away_accurateOwnHalfPassesAgainst = pre.away_accurateOwnHalfPassesAgainst
        self.away_accuratePasses = pre.away_accuratePasses
        self.away_accuratePassesAgainst = pre.away_accuratePassesAgainst
        self.away_aerialDuelsWon = pre.away_aerialDuelsWon
        self.away_assists = pre.away_assists
        self.away_averageBallPossession = pre.away_averageBallPossession
        self.away_avgRating = pre.away_avgRating
        self.away_bigChances = pre.away_bigChances
        self.away_bigChancesAgainst = pre.away_bigChancesAgainst
        self.away_bigChancesCreated = pre.away_bigChancesCreated
        self.away_bigChancesCreatedAgainst = pre.away_bigChancesCreatedAgainst
        self.away_bigChancesMissed = pre.away_bigChancesMissed
        self.away_bigChancesMissedAgainst = pre.away_bigChancesMissedAgainst
        self.away_cleanSheets = pre.away_cleanSheets
        self.away_clearances = pre.away_clearances
        self.away_clearancesAgainst = pre.away_clearancesAgainst
        self.away_clearancesOffLine = pre.away_clearancesOffLine
        self.away_corners = pre.away_corners
        self.away_cornersAgainst = pre.away_cornersAgainst
        self.away_crossesSuccessfulAgainst = pre.away_crossesSuccessfulAgainst
        self.away_crossesTotalAgainst = pre.away_crossesTotalAgainst
        self.away_dribbleAttempts = pre.away_dribbleAttempts
        self.away_dribbleAttemptsTotalAgainst = pre.away_dribbleAttemptsTotalAgainst
        self.away_dribbleAttemptsWonAgainst = pre.away_dribbleAttemptsWonAgainst
        self.away_duelsWon = pre.away_duelsWon
        self.away_errorsLeadingToGoal = pre.away_errorsLeadingToGoal
        self.away_errorsLeadingToGoalAgainst = pre.away_errorsLeadingToGoalAgainst
        self.away_errorsLeadingToShot = pre.away_errorsLeadingToShot
        self.away_errorsLeadingToShotAgainst = pre.away_errorsLeadingToShotAgainst
        self.away_fastBreakGoals = pre.away_fastBreakGoals
        self.away_fastBreakShots = pre.away_fastBreakShots
        self.away_fastBreaks = pre.away_fastBreaks
        self.away_fouls = pre.away_fouls
        self.away_freeKickGoals = pre.away_freeKickGoals
        self.away_freeKickShots = pre.away_freeKickShots
        self.away_goalsConceded = pre.away_goalsConceded
        self.away_goalsFromInsideTheBox = pre.away_goalsFromInsideTheBox
        self.away_goalsFromOutsideTheBox = pre.away_goalsFromOutsideTheBox
        self.away_goalsScored = pre.away_goalsScored
        self.away_groundDuelsWon = pre.away_groundDuelsWon
        self.away_headedGoals = pre.away_headedGoals
        self.away_hitWoodwork = pre.away_hitWoodwork
        self.away_hitWoodworkAgainst = pre.away_hitWoodworkAgainst
        self.away_interceptions = pre.away_interceptions
        self.away_interceptionsAgainst = pre.away_interceptionsAgainst
        self.away_keyPassesAgainst = pre.away_keyPassesAgainst
        self.away_lastManTackles = pre.away_lastManTackles
        self.away_leftFootGoals = pre.away_leftFootGoals
        self.away_longBallsSuccessfulAgainst = pre.away_longBallsSuccessfulAgainst
        self.away_longBallsTotalAgainst = pre.away_longBallsTotalAgainst
        self.away_matches = pre.away_matches
        self.away_offsides = pre.away_offsides
        self.away_offsidesAgainst = pre.away_offsidesAgainst
        self.away_oppositionHalfPassesTotalAgainst = pre.away_oppositionHalfPassesTotalAgainst
        self.away_ownGoals = pre.away_ownGoals
        self.away_ownHalfPassesTotalAgainst = pre.away_ownHalfPassesTotalAgainst
        self.away_penaltiesCommited = pre.away_penaltiesCommited
        self.away_penaltiesTaken = pre.away_penaltiesTaken
        self.away_penaltyGoals = pre.away_penaltyGoals
        self.away_penaltyGoalsConceded = pre.away_penaltyGoalsConceded
        self.away_possessionLost = pre.away_possessionLost
        self.away_redCards = pre.away_redCards
        self.away_redCardsAgainst = pre.away_redCardsAgainst
        self.away_rightFootGoals = pre.away_rightFootGoals
        self.away_saves = pre.away_saves
        self.away_shots = pre.away_shots
        self.away_shotsAgainst = pre.away_shotsAgainst
        self.away_shotsBlockedAgainst = pre.away_shotsBlockedAgainst
        self.away_shotsFromInsideTheBox = pre.away_shotsFromInsideTheBox
        self.away_shotsFromInsideTheBoxAgainst = pre.away_shotsFromInsideTheBoxAgainst
        self.away_shotsFromOutsideTheBox = pre.away_shotsFromOutsideTheBox
        self.away_shotsFromOutsideTheBoxAgainst = pre.away_shotsFromOutsideTheBoxAgainst
        self.away_shotsOffTarget = pre.away_shotsOffTarget
        self.away_shotsOffTargetAgainst = pre.away_shotsOffTargetAgainst
        self.away_shotsOnTarget = pre.away_shotsOnTarget
        self.away_shotsOnTargetAgainst = pre.away_shotsOnTargetAgainst
        self.away_successfulDribbles = pre.away_successfulDribbles
        self.away_tackles = pre.away_tackles
        self.away_tacklesAgainst = pre.away_tacklesAgainst
        self.away_totalAerialDuels = pre.away_totalAerialDuels
        self.away_totalCrosses = pre.away_totalCrosses
        self.away_totalDuels = pre.away_totalDuels
        self.away_totalFinalThirdPassesAgainst = pre.away_totalFinalThirdPassesAgainst
        self.away_totalGroundDuels = pre.away_totalGroundDuels
        self.away_totalLongBalls = pre.away_totalLongBalls
        self.away_totalOppositionHalfPasses = pre.away_totalOppositionHalfPasses
        self.away_totalOwnHalfPasses = pre.away_totalOwnHalfPasses
        self.away_totalPasses = pre.away_totalPasses
        self.away_totalPassesAgainst = pre.away_totalPassesAgainst
        self.away_yellowCards = pre.away_yellowCards
        self.away_yellowCardsAgainst = pre.away_yellowCardsAgainst
        self.away_yellowRedCards = pre.away_yellowRedCards
