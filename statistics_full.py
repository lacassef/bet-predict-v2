from dataclasses import dataclass

from statistics import Statistics


@dataclass()
class StatisticsFull:
    goals: int
    possession: int
    totalShots: int
    shotsOnTarget: int
    blockedShots: int
    fouls: int
    yellowCard: int
    redCard: int
    bigChances: int
    bigChancesMissed: int
    shotsInsideTheBox: int
    shotsOutsideTheBox: int
    goalkeeperSaves: int
    offside: int
    totalPasses: int
    accuratePasses: int
    totalLongBalls: int
    accurateLongBalls: int
    totalCrosses: int
    accurateCrosses: int
    totalDribles: int
    accurateDribles: int
    duelsWon: int
    aerialDuelsWon: int
    tackles: int
    interceptions: int
    clearances: int
    cornerKicks: int
    goals_against: int
    possession_against: int
    totalShots_against: int
    shotsOnTarget_against: int
    blockedShots_against: int
    fouls_against: int
    yellowCard_against: int
    redCard_against: int
    bigChances_against: int
    bigChancesMissed_against: int
    shotsInsideTheBox_against: int
    shotsOutsideTheBox_against: int
    goalkeeperSaves_against: int
    offside_against: int
    totalPasses_against: int
    accuratePasses_against: int
    totalLongBalls_against: int
    accurateLongBalls_against: int
    totalCrosses_against: int
    accurateCrosses_against: int
    totalDribles_against: int
    accurateDribles_against: int
    duelsWon_against: int
    aerialDuelsWon_against: int
    tackles_against: int
    interceptions_against: int
    clearances_against: int
    cornerKicks_against: int

    def __init__(self, stat: Statistics, statAgainst: Statistics):
        self.goals = stat.goals
        self.goals_against = statAgainst.goals
        self.possession = stat.possession
        self.totalShots = stat.totalShots
        self.shotsOnTarget = stat.shotsOnTarget
        self.blockedShots = stat.blockedShots
        self.fouls = stat.fouls
        self.yellowCard = stat.yellowCard
        self.redCard = stat.redCard
        self.bigChances = stat.bigChances
        self.bigChancesMissed = stat.bigChancesMissed
        self.shotsInsideTheBox = stat.shotsInsideTheBox
        self.shotsOutsideTheBox = stat.shotsOutsideTheBox
        self.goalkeeperSaves = stat.goalkeeperSaves
        self.offside = stat.offside
        self.totalPasses = stat.totalPasses
        self.accuratePasses = stat.accuratePasses
        self.totalLongBalls = stat.totalLongBalls
        self.accurateLongBalls = stat.accurateLongBalls
        self.totalCrosses = stat.totalCrosses
        self.accurateCrosses = stat.accurateCrosses
        self.totalDribles = stat.totalDribles
        self.accurateDribles = stat.accurateDribles
        self.duelsWon = stat.duelsWon
        self.aerialDuelsWon = stat.aerialDuelsWon
        self.tackles = stat.tackles
        self.interceptions = stat.interceptions
        self.clearances = stat.clearances
        self.cornerKicks = stat.cornerKicks
        self.possession_against = statAgainst.possession
        self.totalShots_against = statAgainst.totalShots
        self.shotsOnTarget_against = statAgainst.shotsOnTarget
        self.blockedShots_against = statAgainst.blockedShots
        self.fouls_against = statAgainst.fouls
        self.yellowCard_against = statAgainst.yellowCard
        self.redCard_against = statAgainst.redCard
        self.bigChances_against = statAgainst.bigChances
        self.bigChancesMissed_against = statAgainst.bigChancesMissed
        self.shotsInsideTheBox_against = statAgainst.shotsInsideTheBox
        self.shotsOutsideTheBox_against = statAgainst.shotsOutsideTheBox
        self.goalkeeperSaves_against = statAgainst.goalkeeperSaves
        self.offside_against = statAgainst.offside
        self.totalPasses_against = statAgainst.totalPasses
        self.accuratePasses_against = statAgainst.accuratePasses
        self.totalLongBalls_against = statAgainst.totalLongBalls
        self.accurateLongBalls_against = statAgainst.accurateLongBalls
        self.totalCrosses_against = statAgainst.totalCrosses
        self.accurateCrosses_against = statAgainst.accurateCrosses
        self.totalDribles_against = statAgainst.totalDribles
        self.accurateDribles_against = statAgainst.accurateDribles
        self.duelsWon_against = statAgainst.duelsWon
        self.aerialDuelsWon_against = statAgainst.aerialDuelsWon
        self.tackles_against = statAgainst.tackles
        self.interceptions_against = statAgainst.interceptions
        self.clearances_against = statAgainst.clearances
        self.cornerKicks_against = statAgainst.cornerKicks
