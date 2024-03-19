matriz = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]

n = len(matriz)
soma_referencia = sum(matriz[0])

e_quadrado_magico = True

for i in range(n):
    if sum(matriz[i]) != soma_referencia or sum(matriz[j][i] for j in range(n)) != soma_referencia:
        e_quadrado_magico = False
        break

if sum(matriz[i][i] for i in range(n)) != soma_referencia:
    e_quadrado_magico = False

if sum(matriz[i][n - 1 - i] for i in range(n)) != soma_referencia:
    e_quadrado_magico = False

if e_quadrado_magico:
    print("A matriz é um quadrado mágico.")
else:
    print("A matriz não é um quadrado mágico.")