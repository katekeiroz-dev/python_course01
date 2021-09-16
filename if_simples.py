#desvio condicional
nome = input("Digite o nome do funcionario")
salario = float(input("Digite o salario do funcionario"))

if salario < 0: # o sinal de : em python significa que tudo que esta em depois do : pertence a determinado bloco
    salario = salario * -1
    print("O salario é negativo")


print("O salario do fucionario {} é {}".format(nome,salario))
