pizzas = 0
faturamento = 0
maior_venda = 0
menor_venda = 0
acima_50 = 0

# while True:
#     valor = float(input("Valor da Pizza Vendida (ou 0 para encerrar)R$: "))
#     if valor == 0:
#         break
#     if valor < 0:
#         print("🚨Valor inválido. Digite um valor positivo ou 0 para encerrar.")
#         continue
#     pizzas += 1
#     faturamento += valor
#     if valor > maior_venda: # na primeira venda ela será a maior venda
#         maior_venda = valor
#     if pizzas == 1 or valor < menor_venda: # na primeira venda ela será a menor venda
#         menor_venda = valor
#     if valor > 50:
#         acima_50 += 1
# print(f"Esse foi o último valor da variavel pizzas no while: {pizzas}")
# print(f"ideem ^^ Faturamento total^no while: R$ {faturamento:.2f}")
# print(f"ideem ^^ esse é p valor da variavel^no(existe somente no while): R$ {valor}")

if pizzas == 0:
    print("Nenhuma venda registrada hoje.")
else:
    ticket_medio = faturamento / pizzas
    print(f"Total de pizzas vendidas: {pizzas}")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")
    print(f"Maior venda: R$ {maior_venda:.2f}")
    print(f"Menor venda: R$ {menor_venda:.2f}")
    print(f"Pizzas vendidas acima de R$ 50,00: {acima_50}")

# #and = ambos true = true
# #or = um ou outro true = true

#     #verificar se é positivo ou não ( então digitar valor correto) ou zero ( e então encerrar o sistema e não contabilizar como valor de pizza )