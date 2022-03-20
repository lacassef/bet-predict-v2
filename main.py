import utils

if __name__ == '__main__':
    print('Aguarde...')
    # print('sleeping')
    # time.sleep(2*60*60+45*60)
    # print('continues')
    utils.update_pre_result()
    utils.update_results()
    while True:
        print('Escolha a sua operação (zero para sair):')
        try:
            ok = int(
                input('1 -> Avaliar os modelos\n2 -> Obter predições de hoje\n3 -> Obter predições de outra data\n'))
        except:
            continue
        if ok == 0:
            break
        elif ok == 2:
            pass
        elif ok == 1:
            pass
        elif ok == 3:
            pass
