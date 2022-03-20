import csv

from btts import Btts
from over_goals import OverGoals
from preresult import PreResult
from winners import Winners


def get_non_saved_pre_result(pre_result: list) -> []:
    non_saved = []
    with open(file='persistence/pre_result.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in pre_result:
            if not (str(row.__dict__['id']) in ids):
                non_saved.append(row.__dict__)
    return non_saved


def save_pre_training(pre_result: list[PreResult]) -> int:
    non_saved = get_non_saved_pre_result(pre_result)
    fields = pre_result[0].__dict__.keys()
    with open(file='persistence/pre_result.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, [*fields])
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)
    return len(non_saved)


def get_non_saved_over_goals(over_goals: list) -> []:
    non_saved = []
    with open(file='persistence/over_goals.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in over_goals:
            if not (str(row.__dict__['id']) in ids):
                non_saved.append(row.__dict__)
    return non_saved


def save_over_goals(over_goals: list[OverGoals]) -> int:
    non_saved = get_non_saved_over_goals(over_goals)
    fields = over_goals[0].__dict__.keys()
    with open(file='persistence/over_goals.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, [*fields])
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)
    return len(non_saved)


def get_non_saved_btts(btts: list) -> []:
    non_saved = []
    with open(file='persistence/btts.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in btts:
            if not (str(row.__dict__['id']) in ids):
                non_saved.append(row.__dict__)
    return non_saved


def save_btts(btts: list[Btts]) -> int:
    non_saved = get_non_saved_pre_result(btts)
    fields = btts[0].__dict__.keys()
    with open(file='persistence/btts.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, [*fields])
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)
    return len(non_saved)


def get_non_saved_winner(winner: list) -> []:
    non_saved = []
    with open(file='persistence/pre_result.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in winner:
            if not (str(row.__dict__['id']) in ids):
                non_saved.append(row.__dict__)
    return non_saved


def save_winner(winner: list[Winners]) -> int:
    non_saved = get_non_saved_pre_result(winner)
    fields = winner[0].__dict__.keys()
    with open(file='persistence/winner.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, [*fields])
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)
    return len(non_saved)


def load_pre_result() -> list[PreResult]:
    lista: list[PreResult] = []
    with open(file='persistence/pre_result.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            awa = PreResult(**row)
            lista.append(awa)
    return [value for value in lista if value in get_non_saved_winner(lista) or
            value in get_non_saved_btts(lista) or value in get_non_saved_over_goals(lista)]