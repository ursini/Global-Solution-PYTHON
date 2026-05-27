focos = []

def registrar_foco(focos):

    try:
        latitude = float(input('Digite a latitude: '))
        longitude = float(input('Digite a longitude: '))

        while True:
            intensidade = int(input('Digite a intensidade do fogo (1-10): '))

            if intensidade < 1 or intensidade > 10:
                print('Erro: intensidade deve estar entre 1 e 10!')
            else:
                break

        vento = int(input('Digite a velocidade do vento: '))

        foco = {
            'latitude': latitude,
            'longitude': longitude,
            'intensidade': intensidade,
            'vento': vento
        }

        focos.append(foco)

        print('Foco registrado com sucesso!')

    except ValueError:
        print('Erro: digite apenas números válidos.')
while True:
    print('--MENU--')

    print('0 - Sobre o projeto')
    print('1 - Registrar foco de incêndio')
    print('2 - Ver focos ativos')
    print('3 - Simular propagação')
    print('4 - Calcular rota segura')
    print('5 - Relatório operacional')
    print('6 - Sair')

    escolha = input('Qual o requisito: \n(1/2/3/4/5/6): ') 