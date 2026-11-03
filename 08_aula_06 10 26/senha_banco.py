"""
Crie um sistema que peça ao usário para digitar uma senha para acessar sua conta bancára . Ele tem ** apenas 3 tentativas para acertar a senha, caso erre as 3 vezes , o sistema bloqueia a conta.

- A senha correta é: 1234;

- O usuário tem 3 tentativas para acertar a senha, caso erre as 3 vezes , o sistema bloqueia a conta.


"""
#váriaveis no escopo global
SENHA_CORRETA = "1234" # Constante que armazena a senha correta # SEMPRE MAISUCULO A CONSTANTE , PARA DIFERENCIAR DAS VARIAVEIS NO ESCOPO LOCAL
tentativas = 3 # Constante que armazena o número de tentativas , variaável contadora , pode ser i ou j , mas nesse caso é TENTATIVAS

#váriaveis no escopo local
while tentativas > 0:
    senha_digitada = input("Digite sua senha para acessar sua conta bancária: ")#variavel no escopo local
    if senha_digitada == SENHA_CORRETA:
        print("Acesso permitido! Bem-vindo à sua conta bancária.")
        break  # Sai do loop se a senha estiver correta
    else:
        tentativas -= 1  #tentativas = tentativas - 1  # Decrementa o número de tentativas restantes
        print(f"Senha incorreta. Você tem {tentativas} tentativa(s) restante(s)")

        #até aqui mostra senha correta ou incorreta , quebra while loop e decrementa tentativas , se tentativas for 0 , o while loop para de executar ao chegar  a zero

    if tentativas == 0:
        print("Conta bloqueada devido a tentativas excedidas!")
    
      