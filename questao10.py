'''10 - Faça um programa para determinar a próxima jogada em um Jogo da Velha. Assumir que o tab_do_exemplo é
representado por uma matriz de 3 x 3, onde cada posição representa uma das casas do tabuleiro. A matriz
pode conter os seguintes valores -1, 0, 1 representando respectivamente uma casa contendo uma peça minha
(-1), uma casa vazia do tabuleiro (0), e uma casa contendo uma peça do meu oponente (1).'''


def proxima_jogada(tab_de_vei):

    for i in range(3):
        # linhas
        if tab_de_vei[i][0] == tab_de_vei[i][1] == -1 and tab_de_vei[i][2] == 0:
            return i, 2
        elif tab_de_vei[i][1] == tab_de_vei[i][2] == -1 and tab_de_vei[i][0] == 0:
            return i, 0
        elif tab_de_vei[i][0] == tab_de_vei[i][2] == -1 and tab_de_vei[i][1] == 0:
            return i, 1
        
        # colunas
        if tab_de_vei[0][i] == tab_de_vei[1][i] == -1 and tab_de_vei[2][i] == 0:
            return 2, i
        elif tab_de_vei[1][i] == tab_de_vei[2][i] == -1 and tab_de_vei[0][i] == 0:
            return 0, i
        elif tab_de_vei[0][i] == tab_de_vei[2][i] == -1 and tab_de_vei[1][i] == 0:
            return 1, i
        
    # diag principal
    if tab_de_vei[0][0] == tab_de_vei[1][1] == -1 and tab_de_vei[2][2] == 0:
        return 2, 2
    elif tab_de_vei[1][1] == tab_de_vei[2][2] == -1 and tab_de_vei[0][0] == 0:
        return 0, 0
    elif tab_de_vei[0][0] == tab_de_vei[2][2] == -1 and tab_de_vei[1][1] == 0:
        return 1, 1
    
    #diag secundária
    if tab_de_vei[0][2] == tab_de_vei[1][1] == -1 and tab_de_vei[2][0] == 0:
        return 2, 0
    elif tab_de_vei[1][1] == tab_de_vei[2][0] == -1 and tab_de_vei[0][2] == 0:
        return 0, 2
    elif tab_de_vei[0][2] == tab_de_vei[2][0] == -1 and tab_de_vei[1][1] == 0:
        return 1, 1
    
    for i in range(3):
        for j in range(3):
            if tab_de_vei[i][j] == 0:
                return i, j
    
    return print("Todas as casas já estão preenchidas")


def imprimir_tabuleiro(tab_de_vei):
    for linha in tab_de_vei:
        print(" ".join(map(str, linha)))

tab_de_vei = [

    [-1, 1, 1],
    [-1, -1, 0],
    [ 0, 1, 0]
]

print("Tabuleiro game of veio:")
imprimir_tabuleiro(tab_de_vei)

'''trecho opcional 64 a 74'''
def possiveis_jogadas(tab_de_vei):
    jogadas = []
    for i in range(3):
        for j in range(3):
            if tab_de_vei[i][j] == 0:
                jogadas.append((i, j))
    return jogadas

print("\nPossíveis jogadas:")
print(possiveis_jogadas(tab_de_vei))

proximo_movimento = proxima_jogada(tab_de_vei)
if proximo_movimento:
    print("\n Próxima jogada:", proximo_movimento)
else:
    print("\n O jogo está cheio. Jogo empatado.")