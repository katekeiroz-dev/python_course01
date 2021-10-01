def somar (n1,n2):
    soma = n1 + n2
    print(soma)


#fora da funcao
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
somar(n1,n2)

#ou podemos passar o parametro direto na chamada da funcao, que o valor representara respectivamente a ordem
#criado na funcao em cima
#exemplo:
somar(23,25)