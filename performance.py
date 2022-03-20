from dataclasses import dataclass


@dataclass()
class Performance:
    accurateCrosses: float = 0.0
    accurateFinalThirdPassesAgainst: float = 0.0
    accurateLongBalls: float = 0.0
    accurateOppositionHalfPasses: float = 0.0
    accurateOppositionHalfPassesAgainst: float = 0.0
    accurateOwnHalfPasses: float = 0.0
    accurateOwnHalfPassesAgainst: float = 0.0
    accuratePasses: float = 0.0
    accuratePassesAgainst: float = 0.0
    aerialDuelsWon: float = 0.0
    assists: float = 0.0
    averageBallPossession: float = 0.0
    avgRating: float = 0.0
    bigChances: float = 0.0
    bigChancesAgainst: float = 0.0
    bigChancesCreated: float = 0.0
    bigChancesCreatedAgainst: float = 0.0
    bigChancesMissed: float = 0.0
    bigChancesMissedAgainst: float = 0.0
    cleanSheets: float = 0.0
    clearances: float = 0.0
    clearancesAgainst: float = 0.0
    clearancesOffLine: float = 0.0
    corners: float = 0.0
    cornersAgainst: float = 0.0
    crossesSuccessfulAgainst: float = 0.0
    crossesTotalAgainst: float = 0.0
    dribbleAttempts: float = 0.0
    dribbleAttemptsTotalAgainst: float = 0.0
    dribbleAttemptsWonAgainst: float = 0.0
    duelsWon: float = 0.0
    errorsLeadingToGoal: float = 0.0
    errorsLeadingToGoalAgainst: float = 0.0
    errorsLeadingToShot: float = 0.0
    errorsLeadingToShotAgainst: float = 0.0
    fastBreakGoals: float = 0.0
    fastBreakShots: float = 0.0
    fastBreaks: float = 0.0
    fouls: float = 0.0
    freeKickGoals: float = 0.0
    freeKickShots: float = 0.0
    goalsConceded: float = 0.0
    goalsFromInsideTheBox: float = 0.0
    goalsFromOutsideTheBox: float = 0.0
    goalsScored: float = 0.0
    groundDuelsWon: float = 0.0
    headedGoals: float = 0.0
    hitWoodwork: float = 0.0
    hitWoodworkAgainst: float = 0.0
    interceptions: float = 0.0
    interceptionsAgainst: float = 0.0
    keyPassesAgainst: float = 0.0
    lastManTackles: float = 0.0
    leftFootGoals: float = 0.0
    longBallsSuccessfulAgainst: float = 0.0
    longBallsTotalAgainst: float = 0.0
    matches: float = 0.0
    offsides: float = 0.0
    offsidesAgainst: float = 0.0
    oppositionHalfPassesTotalAgainst: float = 0.0
    ownGoals: float = 0.0
    ownHalfPassesTotalAgainst: float = 0.0
    penaltiesCommited: float = 0.0
    penaltiesTaken: float = 0.0
    penaltyGoals: float = 0.0
    penaltyGoalsConceded: float = 0.0
    possessionLost: float = 0.0
    redCards: float = 0.0
    redCardsAgainst: float = 0.0
    rightFootGoals: float = 0.0
    saves: float = 0.0
    shots: float = 0.0
    shotsAgainst: float = 0.0
    shotsBlockedAgainst: float = 0.0
    shotsFromInsideTheBox: float = 0.0
    shotsFromInsideTheBoxAgainst: float = 0.0
    shotsFromOutsideTheBox: float = 0.0
    shotsFromOutsideTheBoxAgainst: float = 0.0
    shotsOffTarget: float = 0.0
    shotsOffTargetAgainst: float = 0.0
    shotsOnTarget: float = 0.0
    shotsOnTargetAgainst: float = 0.0
    successfulDribbles: float = 0.0
    tackles: float = 0.0
    tacklesAgainst: float = 0.0
    totalAerialDuels: float = 0.0
    totalCrosses: float = 0.0
    totalDuels: float = 0.0
    totalFinalThirdPassesAgainst: float = 0.0
    totalGroundDuels: float = 0.0
    totalLongBalls: float = 0.0
    totalOppositionHalfPasses: float = 0.0
    totalOwnHalfPasses: float = 0.0
    totalPasses: float = 0.0
    totalPassesAgainst: float = 0.0
    yellowCards: float = 0.0
    yellowCardsAgainst: float = 0.0
    yellowRedCards: float = 0.0

    def __init__(self, performance: dict = None):
        if performance is not None:
            self.accurateCrosses = performance['accurateCrosses']
            self.accurateFinalThirdPassesAgainst = performance['accurateFinalThirdPassesAgainst']
            self.accurateLongBalls = performance['accurateLongBalls']
            self.accurateOppositionHalfPasses = performance['accurateOppositionHalfPasses']
            self.accurateOppositionHalfPassesAgainst = performance['accurateOppositionHalfPassesAgainst']
            self.accurateOwnHalfPasses = performance['accurateOwnHalfPasses']
            self.accurateOwnHalfPassesAgainst = performance['accurateOwnHalfPassesAgainst']
            self.accuratePasses = performance['accuratePasses']
            self.accuratePassesAgainst = performance['accuratePassesAgainst']
            self.aerialDuelsWon = performance['aerialDuelsWon']
            self.assists = performance['assists']
            self.averageBallPossession = performance['averageBallPossession']
            self.avgRating = performance['avgRating']
            self.bigChances = performance['bigChances']
            self.bigChancesAgainst = performance['bigChancesAgainst']
            self.bigChancesCreated = performance['bigChancesCreated']
            self.bigChancesCreatedAgainst = performance['bigChancesCreatedAgainst']
            self.bigChancesMissed = performance['bigChancesMissed']
            self.bigChancesMissedAgainst = performance['bigChancesMissedAgainst']
            self.cleanSheets = performance['cleanSheets']
            self.clearances = performance['clearances']
            self.clearancesAgainst = performance['clearancesAgainst']
            self.clearancesOffLine = performance['clearancesOffLine']
            self.corners = performance['corners']
            self.cornersAgainst = performance['cornersAgainst']
            self.crossesSuccessfulAgainst = performance['crossesSuccessfulAgainst']
            self.crossesTotalAgainst = performance['crossesTotalAgainst']
            self.dribbleAttempts = performance['dribbleAttempts']
            self.dribbleAttemptsTotalAgainst = performance['dribbleAttemptsTotalAgainst']
            self.dribbleAttemptsWonAgainst = performance['dribbleAttemptsWonAgainst']
            self.duelsWon = performance['duelsWon']
            self.errorsLeadingToGoal = performance['errorsLeadingToGoal']
            self.errorsLeadingToGoalAgainst = performance['errorsLeadingToGoalAgainst']
            self.errorsLeadingToShot = performance['errorsLeadingToShot']
            self.errorsLeadingToShotAgainst = performance['errorsLeadingToShotAgainst']
            self.fastBreakGoals = performance['fastBreakGoals']
            self.fastBreakShots = performance['fastBreakShots']
            self.fastBreaks = performance['fastBreaks']
            self.fouls = performance['fouls']
            self.freeKickGoals = performance['freeKickGoals']
            self.freeKickShots = performance['freeKickShots']
            self.goalsConceded = performance['goalsConceded']
            self.goalsFromInsideTheBox = performance['goalsFromInsideTheBox']
            self.goalsFromOutsideTheBox = performance['goalsFromOutsideTheBox']
            self.goalsScored = performance['goalsScored']
            self.groundDuelsWon = performance['groundDuelsWon']
            self.headedGoals = performance['headedGoals']
            self.hitWoodwork = performance['hitWoodwork']
            self.hitWoodworkAgainst = performance['hitWoodworkAgainst']
            self.interceptions = performance['interceptions']
            self.interceptionsAgainst = performance['interceptionsAgainst']
            self.keyPassesAgainst = performance['keyPassesAgainst']
            self.lastManTackles = performance['lastManTackles']
            self.leftFootGoals = performance['leftFootGoals']
            self.longBallsSuccessfulAgainst = performance['longBallsSuccessfulAgainst']
            self.longBallsTotalAgainst = performance['longBallsTotalAgainst']
            self.matches = performance['matches']
            self.offsides = performance['offsides']
            self.offsidesAgainst = performance['offsidesAgainst']
            self.oppositionHalfPassesTotalAgainst = performance['oppositionHalfPassesTotalAgainst']
            self.ownGoals = performance['ownGoals']
            self.ownHalfPassesTotalAgainst = performance['ownHalfPassesTotalAgainst']
            self.penaltiesCommited = performance['penaltiesCommited']
            self.penaltiesTaken = performance['penaltiesTaken']
            self.penaltyGoals = performance['penaltyGoals']
            self.penaltyGoalsConceded = performance['penaltyGoalsConceded']
            self.possessionLost = performance['possessionLost']
            self.redCards = performance['redCards']
            self.redCardsAgainst = performance['redCardsAgainst']
            self.rightFootGoals = performance['rightFootGoals']
            self.saves = performance['saves']
            self.shots = performance['shots']
            self.shotsAgainst = performance['shotsAgainst']
            self.shotsBlockedAgainst = performance['shotsBlockedAgainst']
            self.shotsFromInsideTheBox = performance['shotsFromInsideTheBox']
            self.shotsFromInsideTheBoxAgainst = performance['shotsFromInsideTheBoxAgainst']
            self.shotsFromOutsideTheBox = performance['shotsFromOutsideTheBox']
            self.shotsFromOutsideTheBoxAgainst = performance['shotsFromOutsideTheBoxAgainst']
            self.shotsOffTarget = performance['shotsOffTarget']
            self.shotsOffTargetAgainst = performance['shotsOffTargetAgainst']
            self.shotsOnTarget = performance['shotsOnTarget']
            self.shotsOnTargetAgainst = performance['shotsOnTargetAgainst']
            self.successfulDribbles = performance['successfulDribbles']
            self.tackles = performance['tackles']
            self.tacklesAgainst = performance['tacklesAgainst']
            self.totalAerialDuels = performance['totalAerialDuels']
            self.totalCrosses = performance['totalCrosses']
            self.totalDuels = performance['totalDuels']
            self.totalFinalThirdPassesAgainst = performance['totalFinalThirdPassesAgainst']
            self.totalGroundDuels = performance['totalGroundDuels']
            self.totalLongBalls = performance['totalLongBalls']
            self.totalOppositionHalfPasses = performance['totalOppositionHalfPasses']
            self.totalOwnHalfPasses = performance['totalOwnHalfPasses']
            self.totalPasses = performance['totalPasses']
            self.totalPassesAgainst = performance['totalPassesAgainst']
            self.yellowCards = performance['yellowCards']
            self.yellowCardsAgainst = performance['yellowCardsAgainst']
            self.yellowRedCards = performance['yellowRedCards']