# input() sempre devolve texto → converta para número


distancia = int(input("Digite a distância em km: "))


if distancia <= 5:
    print("Pedido Aceito e Taxa de RS 5")

elif distancia <= 10: 
    print("Pedido Aceito e Taxa de RS 10")

else : 
    print("Pedido Negado por estar Fora dos Limites de Entrega")



