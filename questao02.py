def main():
    vetor = []
    for i in range(8):
        valor = int(input(f"Digite o valor para a posição do vetor {i}: "))
        vetor.append(valor)
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))
    
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        print("Posições inválidas! Digite um valor que esteja dentro do número de posições do vetor. ")
    else:
        soma = vetor[x] + vetor[y]
        print(f"A soma dos valores nas posições {x} e {y} é: {soma}")
        
main()
