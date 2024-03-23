def calcular_pontuacao(respostas_dos_alunos, gabarito):
    pontuacoes = []
    for respostas in respostas_dos_alunos:
        pontuacao = sum(1 for resp_aluno, resp_gabarito in zip(respostas, gabarito) if resp_aluno == resp_gabarito)
        pontuacoes.append(pontuacao)
    return pontuacoes

gabarito = input("Digite o gabarito (sem espaço e sem vírgula): ").lower()

respostas_dos_alunos = []
for i in range(5):
    respostas = input(f"Digite as respostas do aluno {i+1} (sem espaço e sem virgula): ").lower()
    respostas_dos_alunos.append(respostas)

if len(gabarito) != 10:
    print("Erro: O gabarito deve conter 10 respostas.")
else:
    pontuacoes = calcular_pontuacao(respostas_dos_alunos, gabarito)

    for i, pontuacao in enumerate(pontuacoes):
        print(f"Aluno {i+1}: Pontuação = {pontuacao}")
        