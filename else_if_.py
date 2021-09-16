#para melhorar o codigo, podemos ultilizar o else_if de forma unida (ELIF)

pontuacao = int(input("Digite sua pontuacao"))

if pontuacao > 1000:
    print("Você ganhou 3gb de bônus")
elif pontuacao > 500:
    print("Você ganhou 1,5 gb de bônus")

elif pontuacao > 200:
    print("Você ganhou 500mg de bônus")

else:
    print("Você nao ganhou nada!")



