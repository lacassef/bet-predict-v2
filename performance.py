from dataclasses import dataclass


@dataclass()
class Performance:
    accurateCrosses: float
    accurateFinalThirdPassesAgainst: float
    accurateLongBalls: float
    accurateOppositionHalfPasses: float
    accurateOppositionHalfPassesAgainst: float
    accurateOwnHalfPasses: float
    accurateOwnHalfPassesAgainst: float
    accuratePasses: float
    accuratePassesAgainst: float
    aerialDuelsWon: float
    assists: float
    averageBallPossession: float
    avgRating: float
    bigChances: float
    bigChancesAgainst: float
    bigChancesCreated: float
    bigChancesCreatedAgainst: float
    bigChancesMissed: float
    bigChancesMissedAgainst: float
    cleanSheets: float
    clearances: float
    clearancesAgainst: float
    clearancesOffLine: float
    corners: float
    cornersAgainst: float
    crossesSuccessfulAgainst: float
    crossesTotalAgainst: float
    dribbleAttempts: float
    dribbleAttemptsTotalAgainst: float
    dribbleAttemptsWonAgainst: float
    duelsWon: float
    errorsLeadingToGoal: float
    errorsLeadingToGoalAgainst: float
    errorsLeadingToShot: float
    errorsLeadingToShotAgainst: float
    fastBreakGoals: float
    fastBreakShots: float
    fastBreaks: float
    fouls: float
    freeKickGoals: float
    freeKickShots: float
    goalsConceded: float
    goalsFromInsideTheBox: float
    goalsFromOutsideTheBox: float
    goalsScored: float
    groundDuelsWon: float
    headedGoals: float
    hitWoodwork: float
    hitWoodworkAgainst: float
    interceptions: float
    interceptionsAgainst: float
    keyPassesAgainst: float
    lastManTackles: float
    leftFootGoals: float
    longBallsSuccessfulAgainst: float
    longBallsTotalAgainst: float
    matches: float
    offsides: float
    offsidesAgainst: float
    oppositionHalfPassesTotalAgainst: float
    ownGoals: float
    ownHalfPassesTotalAgainst: float
    penaltiesCommited: float
    penaltiesTaken: float
    penaltyGoals: float
    penaltyGoalsConceded: float
    possessionLost: float
    redCards: float
    redCardsAgainst: float
    rightFootGoals: float
    saves: float
    shots: float
    shotsAgainst: float
    shotsBlockedAgainst: float
    shotsFromInsideTheBox: float
    shotsFromInsideTheBoxAgainst: float
    shotsFromOutsideTheBox: float
    shotsFromOutsideTheBoxAgainst: float
    shotsOffTarget: float
    shotsOffTargetAgainst: float
    shotsOnTarget: float
    shotsOnTargetAgainst: float
    successfulDribbles: float
    tackles: float
    tacklesAgainst: float
    totalAerialDuels: float
    totalCrosses: float
    totalDuels: float
    totalFinalThirdPassesAgainst: float
    totalGroundDuels: float
    totalLongBalls: float
    totalOppositionHalfPasses: float
    totalOwnHalfPasses: float
    totalPasses: float
    totalPassesAgainst: float
    yellowCards: float
    yellowCardsAgainst: float
    yellowRedCards: float

    def __init__(self, performance: dict):
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