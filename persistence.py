import csv


def get_non_saved_pre_result(pre_result: list) -> []:
    non_saved = []
    with open(file='persistence/pre_result.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in pre_result:
            if not (str(row['id']) in ids):
                non_saved.append(row)
    return non_saved


def save_pre_training(fields: [], pre_result: list):
    non_saved = get_non_saved_pre_result(pre_result)
    with open(file='persistence/pre_result.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, fields)
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)


def get_non_saved_over_goals(over_goals: list) -> []:
    non_saved = []
    with open(file='persistence/over_goals.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in over_goals:
            if not (str(row['id']) in ids):
                non_saved.append(row)
    return non_saved


def save_over_goals(fields: [], over_goals: list):
    non_saved = get_non_saved_over_goals(over_goals)
    with open(file='persistence/over_goals.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, fields)
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)


def get_non_saved_btts(btts: list) -> []:
    non_saved = []
    with open(file='persistence/btts.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in btts:
            if not (str(row['id']) in ids):
                non_saved.append(row)
    return non_saved


def save_btts(fields: [], btts: list):
    non_saved = get_non_saved_pre_result(btts)
    with open(file='persistence/btts.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, fields)
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)


def get_non_saved_winner(winner: list) -> []:
    non_saved = []
    with open(file='persistence/pre_result.csv', mode='r', newline='') as file:
        writer = csv.DictReader(file)
        ids = [i['id'] for i in writer]
        for row in winner:
            if not (str(row['id']) in ids):
                non_saved.append(row)
    return non_saved


def save_winner(fields: [], winner: list):
    non_saved = get_non_saved_pre_result(winner)
    with open(file='persistence/winner.csv', mode='a+', newline='') as file:
        writer = csv.DictWriter(file, fields)
        if not file.tell():
            writer.writeheader()
        writer.writerows(non_saved)