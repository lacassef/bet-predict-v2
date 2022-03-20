import requests

import utils
from performance import Performance
from schedule import Schedule


def get_today_matches() -> list[Schedule]:
    req = requests.get(f'http://localhost:8081/api/matches/schedules/{utils.get_today_timestamp()}')
    today: list[Schedule] = []
    for i in req.json():
        today.append(Schedule(i))
    return today


def get_matches_from_date(year, month, day) -> list[Schedule]:
    req = requests.get(f'http://localhost:8081/api/matches/schedules/{utils.get_date_timestamp(day, month, year)}')
    today: list[Schedule] = []
    for i in req.json():
        today.append(Schedule(i))
    return today


def get_match(mId: int) -> Schedule:
    req = requests.get(f'http://localhost:8081/api/matches/{mId}')
    return Schedule(req.json())


def get_performance(team: int, season: int, tournament: int) -> Performance:
    req = requests.get(f'http://localhost:8081/api/team/{team}/{tournament}/{season}/statistics')
    return Performance(req.json())


def get_head_to_head(cId: str) -> list[Schedule]:
    req = requests.get(f'http://localhost:8081/api/matches/{cId}/h2h')
    today: list[Schedule] = []
    for i in req.json():
        today.append(Schedule(i))
    return today


def get_last_matches(tId: int) -> list[Schedule]:
    req = requests.get(f'http://localhost:8081/api/team/{tId}/last')
    today: list[Schedule] = []
    for i in req.json():
        today.append(Schedule(i))
    return today