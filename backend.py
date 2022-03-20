import requests

import utils
from performance import Performance
from schedule import Schedule
from statistics import Statistics


def get_today_matches() -> list:
    req = requests.get(f'http://localhost:8081/api/matches/schedules/{utils.get_today_timestamp()}')
    return req.json()


def get_matches_from_date(year, month, day) -> list:
    req = requests.get(f'http://localhost:8081/api/matches/schedules/{utils.get_date_timestamp(day, month, year)}')
    return req.json()


def get_match(mId: int) -> Schedule:
    req = requests.get(f'http://localhost:8081/api/matches/{mId}')
    return Schedule(req.json())


def get_performance(team: int, season: int, tournament: int) -> Performance:
    req = requests.get(f'http://localhost:8081/api/team/{team}/{tournament}/{season}/statistics')
    return Performance(req.json())


def get_statistics(mId: int, home: bool, match: Schedule) -> Statistics:
    req = requests.get(f'http://localhost:8081/api/matches/{mId}/statistics')
    return Statistics(match, req.json(), home)


def get_head_to_head(cId: str) -> list:
    req = requests.get(f'http://localhost:8081/api/matches/{cId}/h2h')
    return req.json()