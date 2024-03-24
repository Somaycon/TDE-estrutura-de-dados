matriz = [
    [25, 28, 39],
    [98, 27, 99],
    [98, 11, 22]
]

# Função para ler as colunas da matriz
def ler_colunas(matriz):
    colunas = len(matriz)
    for j in range(colunas):
        coluna = []
        for i in range(len(matriz)):
            coluna.append(matriz[i][j])
        print("Coluna", j+1, ":", coluna)
        print("soma da coluna ",j+1,"e", sum(coluna))

# Chamando a função para ler as colunas
ler_colunas(matriz)

