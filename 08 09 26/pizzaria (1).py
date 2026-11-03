# Variables and constants

#Perguntas a serem feitas ao cliente


# Pizza Little = 19,90
# Pizza Medium = 29,90
# Pizza BIG = 39,90


FRETE = 2

dia_semana = "sabado"

print(f"""

    ***********************************
    **** WELCOME YOUR BEST PLACE ******
    ***********************************
 """)
 
nome_cliente = input (f""" Informe seu nome :

 """)

pizza_sabor = input(f"""
            Sabores :
            1- To Frango com requeijão
            2- To Calabresa
            3- To Mussarela
            4- To Banana com Chocolate
""")

pizza_tamanho= input(f"""
            1- Little
            2- Medium
            3- BIG
""")

forma_entrega = input (f"""

            Escolha a froma de entrega:
            1- In Place
            2- To Delivery
""")

# Estrutura condicional para a promoção :

# Comprando qualquer tamanho e qualquer sabor no sabado , o refri é gratuito

# Comprando qualquer pizza de qualquer tamanho , no domingo , o frete e o refri são gratuitos


# Comprando uma pizza de clabresa , tamanho médio , em qualquer dia , o frete é grátis

# Promoções não são cumulativas


if dia_semana == "sabado": 
    print(f" Pedido Aceito ")
    print(f" TODAY Refri=Free")

elif dia_semana =="domingo"
    print(f" Pedido Aceito ")
    print(f" TODAY :  Frete and Refri = Free!")


elif pizza_sabor =="calabresa"and pizza_tamanho == " medium" :
     print(f" Pedido Aceito ")
     print(f"TODAY :  Frete = Free! ")


# print(f"""
# #     ***********************************
# #     ********* Resume Order ************
# #     ***********************************
# #         Name of client: {nome_cliente}
# #         Sabor da Pizza: {pizza_sabor}
# #         Tamanho da Pizza: {pizza_tamanho}
# #         Forma de Consumo: {forma_entrega}
# # """)

