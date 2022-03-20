import time
from datetime import datetime


def get_today_timestamp() -> int:
    return round(time.time() * 1000)


def get_date_timestamp(day: int, month: int, year: int) -> int:
    return round(datetime(year=year, month=month, day=day, hour=12, minute=30).timestamp() * 1000)
