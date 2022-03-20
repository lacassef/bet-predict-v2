from dataclasses import dataclass


@dataclass()
class Schedule:
    id: int
    home: str
    away: str
    home_id: int
    away_id: int
    home_score: int
    away_score: int
    date: str
    time: str
    status: int
    tournament: int
    season: int
    custom_id: str

    def __init__(self, dic: dict):
        self.id = dic['id']
        self.home = dic['home']['shortName']
        self.away = dic['away']['shortName']
        self.home_id = dic['home']['id']
        self.away_id = dic['away']['id']
        self.home_score = dic['home']['score']
        self.away_score = dic['away']['score']
        self.date = dic['date']
        self.time = dic['time']
        self.status = dic['status']
        self.tournament = dic['tournament']['id']
        self.season = dic['tournament']['season']
        self.custom_id = dic['customId']

    def home_win(self) -> bool:
        return self.home_score > self.away_score

    def away_win(self) -> bool:
        return self.home_score < self.away_score

    def draw(self) -> bool:
        return self.home_score == self.away_score

    def both_scored(self) -> bool:
        return self.home_score > 0 and self.away_score > 0

    def over_two_goals_scored(self) -> bool:
        return self.home_score + self.away_score > 2
