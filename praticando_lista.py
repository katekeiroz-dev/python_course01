# sistema de notas de alunos, e verificacao da media da turma

nota = []

opcao = -1
while opcao != 4:
    print('Digite: \n 1 - informar nota do aluno \n 2 - Exibir notas dos alunos \n 3 - Calcular média da sala \n 4 - '
          'Sair do programa')
    opcao = int(input('Escolha sua opção: '))
    if opcao == 1:
        nota.append(float(input('Digite a nota:')))
    elif opcao == 2:
        for x in nota:
            print(x)
    elif opcao == 3:
        print(sum(nota)/len(nota))
