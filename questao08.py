#função para corrigir as provas 
def corrigir_prova(gabarito, respostas_aluno):
    nota = 0
    for i in range(len(gabarito)):
        if gabarito[i] == respostas_aluno[i]:
            nota += 1
    return nota

#função para calcular as medias 
def calcular_media(notas):
    return sum(notas) / len(notas)

#função principal (main)
def main():
    gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
    notas = []

    for aluno in range(1, 4):
        matricula = int(input(f"Digite a matrícula do aluno {aluno}: "))
        respostas_aluno = []
        for i in range(1, 11):
            resposta = input(f"Digite a resposta do aluno {aluno} para a questão {i}: ")
            respostas_aluno.append(resposta.lower())

        nota_aluno = corrigir_prova(gabarito, respostas_aluno)
        notas.append(nota_aluno)
        print(f"Matrícula do aluno: {matricula}")
        print(f"Respostas do aluno: {respostas_aluno}")
        print(f"Nota do aluno: {nota_aluno}")
        print()

    media = calcular_media(notas)
    percentual_aprovacao = len([nota for nota in notas if nota >= 7]) / len(notas) * 100

    print(f"Média da turma: {media}")
    print(f"Percentual de aprovação: {percentual_aprovacao}%")

#chamando função main
main()
