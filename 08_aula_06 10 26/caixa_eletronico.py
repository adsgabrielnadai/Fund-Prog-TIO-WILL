"""
Crie um sistema que simule um caixa eletrônico. O usuário pode sacar até o saldo disponivel acabe ou até que o usuário decida encerrar a operação. O sistema deve informar o saldo atual após cada saque e permitir que o usuário continue sacando até que o saldo seja insuficiente ou que ele decida 'encerrar' a operação.
- O saldo inicial é de R$ 500,00;
- Peça ao usuário digitar um valor para saque
- O usuário pode sacar qualquer valor, desde que seja menor ou igual ao saldo disponível e o informar o saldo
- Se o usuário digitar um valor maior que o saldo disponível, informe que o saldo é insuficiente e peça para digitar outro valor
- O usuário pode encerrar a operação digitando 'encerrar'
"""

# Variáveis no escopo global ^^^^^^^^^^^^^^^^^^^^^^n

    saldo= 500.00  # Constante que armazena o saldo inicial # irá continusr sté que o saldo seja False ( saldo insuficiente ) ou que o usuário decida encerrar a operação

    while saldo > 0:
            print(f'\n Saldo disponível: R$ {saldo:.2f}') #n\quebra linha
            saque = input("Digite o valor que deseja sacar ou 'encerrar' para finalizar a operação: ")

            if saque.lower() == 'encerrar':
                print("Operação encerrada pelo usuário.")
                break  # Sai do loop se o usuário decidir encerrar a operação
            
            saque = float(saque)  # Converte o valor digitado para float
            if saque > saldo:
                print("Saldo insuficiente. Por favor, digite um valor menor ou igual ao saldo disponível.")
            else:
                saldo -= saque
                print(f'Saque realizado com sucesso. Novo saldo: R$ {saldo:.2f}')