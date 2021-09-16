pontuacao = int(input("Digite sua pontuacao"))

if pontuacao > 1000:
    print("Você ganhou 3gb de bônus")

else:
    if pontuacao > 500:
        print("Você ganhou 1,5gb de bônus")

    else:
        if pontuacao > 200:
            print("Você nao 500mb nada!")

        else:
            print("Você ganhou 1gb de bônus")




