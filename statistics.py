from dataclasses import dataclass

from schedule import Schedule


@dataclass()
class Statistics:
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

    def __init__(self, match: Schedule, stat: list, home: bool):
        for s in stat:
            if s['name'] == 'ALL':
                if home:
                    stats = s['home']
                    self.goals = match.home_score
                else:
                    stats = s['away']
                    self.goals = match.away_score
                self.possession = stats['possession']
                self.totalShots = stats['totalShots']
                self.shotsOnTarget = stats['shotsOnTarget']
                self.blockedShots = stats['blockedShots']
                self.fouls = stats['fouls']
                self.yellowCard = stats['yellowCard']
                self.redCard = stats['redCard']
                self.bigChances = stats['bigChances']
                self.bigChancesMissed = stats['bigChancesMissed']
                self.shotsInsideTheBox = stats['shotsInsideTheBox']
                self.shotsOutsideTheBox = stats['shotsOutsideTheBox']
                self.goalkeeperSaves = stats['goalkeeperSaves']
                self.offside = stats['offside']
                self.totalPasses = stats['totalPasses']
                self.accuratePasses = stats['accuratePasses']
                self.totalLongBalls = stats['totalLongBalls']
                self.accurateLongBalls = stats['accurateLongBalls']
                self.totalCrosses = stats['totalCrosses']
                self.accurateCrosses = stats['accurateCrosses']
                self.totalDribles = stats['totalDribles']
                self.accurateDribles = stats['accurateDribles']
                self.duelsWon = stats['duelsWon']
                self.aerialDuelsWon = stats['aerialDuelsWon']
                self.tackles = stats['tackles']
                self.interceptions = stats['interceptions']
                self.clearances = stats['clearances']
                self.cornerKicks = stats['cornerKicks']
                break

