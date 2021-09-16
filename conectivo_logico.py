# uso do conectivo logico && (and)

valor_compra = float(input("Digite o valor da sua compra: "))
forma_pagamento = int(input("1 - Dinheiro / 2- cartao"))

if valor_compra > 100 and forma_pagamento==1:
    valor_compra = valor_compra * 0.9
    print("Voce tem direito a um desconto de 10%! ")

print("O valor a pagar é {}".format(valor_compra))
