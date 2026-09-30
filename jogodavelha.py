def interface():
    print(f'''
       1   2   3
    1 [{tabuleiro[0][0]}] [{tabuleiro[0][1]}] [{tabuleiro[0][2]}]
    2 [{tabuleiro[1][0]}] [{tabuleiro[1][1]}] [{tabuleiro[1][2]}]
    3 [{tabuleiro[2][0]}] [{tabuleiro[2][1]}] [{tabuleiro[2][2]}]
    ''')

def validarVitoria(rodada):
    global parar

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == rodada or \
    tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == rodada or \
    tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == rodada or \
    tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == rodada or \
    tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == rodada or \
    tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == rodada or \
    tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == rodada or \
    tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == rodada:
        
        interface()   
        print(f'==== {rodada} VENCEU! ===='.center(20))
        parar = True
        
tabuleiro = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

parar = False

rodada = 'X'

jogadas = 0

while parar == False:

    print(f'=> {rodada} jogando!')


    interface()

    while True:
        try:
            linha = int(input('Insira a linha: '))
            coluna = int(input('Insira a coluna: '))

            if (linha not in [1,2,3]) or (coluna not in [1,2,3]):
                print('=> Linha ou coluna inválida!')
                continue

            l = linha - 1
            c = coluna - 1

            if tabuleiro[l][c] != ' ':
                print('=> Posição já ocupada!')
                continue

            break

        except:
            print('=> ERRO!')



    tabuleiro[l][c] = rodada
    jogadas += 1

    validarVitoria(rodada)

    if parar == False and jogadas == 9:
        interface()
        print('==== EMPATE ===='.center(20))

        
    rodada = 'O' if rodada == 'X' else 'X'


print('\nPrograma Encerrado.\n')

