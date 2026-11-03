sabores_caldo = ["Galinha", "Carne", "Peixe", "Legumes"]
print("Faça seu pedido 'sair' para encerrar):")
caldo = ""  # Aqui fica vazio para que o while loop seja executado # aqui ficará o caldorio

# Enquanto o caldoerente de "sair", continue pedindo , o while loop continuara até sendo executado

# Enquanto o while loop for verdadeiro, o código dentro do while loop será executado

# .capitalize() deixa a primeira letra maiúscula e o restante minúsculo

while caldo.capitalize() != "Sair":
    caldo = input("Qual sabor de caldo você deseja?: ").capitalize()  
    if caldo in sabores_caldo:
        print(f'{caldo} confirmado!')
    elif caldo.capitalize() == "Sair":
        print("Pedido encerrado.")
    else:
        print("Sabor indisponível, escolha outro sabor.")
