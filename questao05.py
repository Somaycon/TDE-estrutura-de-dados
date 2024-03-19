import random

def gerar_cartela():
    numeros = list(range(100))  
    random.shuffle(numeros)  
    cartela = [numeros[i:i+5] for i in range(0, 25, 5)] 

    return cartela

def exibir_cartela(cartela):
    for linha in cartela:
        print(' '.join(f"{n:02}" for n in linha))

cartela_bingo = gerar_cartela()
exibir_cartela(cartela_bingo)
