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


def listar_focos(focos):
    if len(focos) == 0:
        print('Nenhum foco registrado.')
        return
    for foco in focos:

        print('-- FOCO ATIVO --')
        print(f'Latitude: {foco["latitude"]}')
        print(f'Longitude: {foco["longitude"]}')
        print(f'Intensidade: {foco["intensidade"]}')
        print(f'Vento: {foco["vento"]} km/h')
    
def simular_propagacao(focos):

     if len(focos) == 0:
        print('Nenhum foco registrado.')
        return

     for foco in focos:

        propagacao = foco['intensidade'] * foco['vento']

        print('-- SIMULAÇÃO --')
        print(f'Propagação estimada: {propagacao} metros')

        if propagacao > 150:
            print('RISCO ALTO!')
        else:
            print('RISCO MODERADO')

    
def gerar_relatorio(focos):
    total = len(focos)

    print('-- RELATÓRIO--')

    print(f'Total de focos: {total}')


def calcular_rota(focos):
    if len(focos) == 0:
        print('Nenhum foco registrado')
        return
    for foco in focos:

        propagacao = foco['intensidade'] * foco['vento']

        print('\n--- ROTA ---')

        if propagacao > 150:
            print('Rota principal bloqueada.')
            print('Nova rota segura ativada.')
        else:
            print('Rota segura liberada.')


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

    match escolha:

        case '0': 
            print('\nProjeto Agnelo é um sistema inteligente de apoio ao combate \n ' 
            'a incêndios florestais. O software registra focos ativos, \n ' 
            'simula a propagação do fogo com base na intensidade e vento, ' 
            'e auxilia brigadas na definição de rotas seguras.')
            print('O objetivo é reduzir riscos ambientais e operacionais.')

        case '1':
            registrar_foco(focos)
        case '2':
            listar_focos(focos)
        case '3':
            simular_propagacao(focos)
        case '4':
            calcular_rota(focos)
        case '5':
            gerar_relatorio(focos)
        case '6':
            break