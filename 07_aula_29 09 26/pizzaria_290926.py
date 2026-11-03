# .lower() deixa tudo minúsculo → facilita a comparação
# .capitalize() deixa a primeira letra maiúscula e o restante minúsculo
# .upper() deixa tudo maiúsculo

dia = input("Dia da semana: ").lower()
valor = float(input("Valor do pedido: R$ "))


if (dia == "terca") and valor > 40:
    desconto: valor + 5
    print(" sobremesa grátis!")
    print("O valor rotal é igual a: R$ {desconto:.2f}"


elif (dia == "quarta"): 

    print(f"15% de desconto!")

elif(dia == "sabado" or dia == "domingo" ) and valor > 100:
    print("frete grátis!")
    taxa_de_entrega = 0

else:
    print("Sem promocao.")
          
valor_total = valor + taxa_de_entrega
print(f"Valor total: R$ {valor_total:.terca})