import time
from datetime import datetime

import backend
import persistence
from btts import Btts
from over_goals import OverGoals
from preresult import PreResult
from schedule import Schedule
from winners import Winners


def get_today_timestamp() -> int:
    return round(time.time() * 1000)


def get_date_timestamp(day: int, month: int, year: int) -> int:
    return round(datetime(year=year, month=month, day=day).timestamp() * 1000)



def get_pre_result(matchw: Schedule) -> PreResult:
    match = backend.get_match(matchw.id)
    home_performance = backend.get_performance(team=match.home_id, season=match.season, tournament=match.tournament)
    away_performance = backend.get_performance(team=match.away_id, season=match.season, tournament=match.tournament)
    return PreResult(id = match.id, home = home_performance, away = away_performance)


def update_pre_result():
    today = backend.get_today_matches()
    lista = []
    for m in today:
        if m.status == 0:
            # try:
            lista.append(get_pre_result(m))
            # except Exception as err:
            #     print(f'Saltando jogo: {m.home} vs {m.away}...')
            #     print(err)
    # try:
    persistence.save_pre_training(lista)
    # except Exception as err:
    #     print('Erro ao salvar jogos de pre-treino!!')
    #     print(err)
    # else:
    #     print(f'Adicionados {n} novos jogos!!')


def update_results():
    non_results = persistence.load_pre_result()
    winners = []
    btts = []
    over = []
    for n in non_results:
        m = backend.get_match(n.id)
        if m.status == 100 or m.status == 120 or m.status == 110:
            winners.append(Winners(m, n))
            btts.append(Btts(m, n))
            over.append(OverGoals(m, n))
    try:
        ii = persistence.save_winner(winners)
    except Exception as err:
        print('Erro ao salvar resultado do jogo!!')
        print(err)
    else:
        print(f'Foram salvos {ii} resultados de jogos!!')
    try:
        ii = persistence.save_btts(btts)
    except Exception as err:
        print('Erro ao salvar ambas marcam no jogo!!')
        print(err)
    else:
        print(f'Foram salvos {ii} resultados de ambas marcam no jogos!!')
    try:
        ii = persistence.save_over_goals(over)
    except Exception as err:
        print('Erro ao salvar resultado de mais/menos 2.5 golos no jogo!!')
        print(err)
    else:
        print(f'Foram salvos {ii} resultados de mais/menos 2.5 golos no jogo!!')
