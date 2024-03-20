matriz = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
]

for linha in matriz:
    print(linha)

cidade1 = int(input("digite o número da primeira cidade: "))
cidade2 = int(input("digite o número da segunda cidade: "))
distancia = matriz[cidade1][cidade2]
print(f"a distância entre a cidade {cidade1} e a cidade {cidade2} é de {distancia} km.")

percurso = []
coordenadas = min(int(input("quantas coordenadas voce quer? ")), 6)
distanciaTotal = 0
for i in range(coordenadas):
    origem = int(input("informe a cidade de origem: "))
    destino = int(input("informe a cidade de destino: "))
    distanciaParcial = matriz[origem][destino]
    percurso.append((origem, destino))
    distanciaTotal += distanciaParcial

print(f"A distância total percorrida é de {distanciaTotal} km.")
