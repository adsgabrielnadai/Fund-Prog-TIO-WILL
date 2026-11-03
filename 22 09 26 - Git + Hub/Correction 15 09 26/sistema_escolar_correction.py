# Entrada de dados

#ANALISES DOS DADOS E DAS CONDIÇÕES
# 
# Verifica se o aluno é maior de idade
# Verifica se a nota do aluno é maior ou igual a 9
# Verifica se a frequência do aluno é maior ou igual a 75%
# Verifica se o aluno é aprovado ou reprovado com base nas condições acima
# Se não , será reprovado 

idade = int(input("idade do aluno: "))
nota = float(input("nota do aluno: "))
frequencia = float(input("frequencia do aluno: "))

# Condições de aprovação e exibindo mensagens de acordo com a idade, nota e frequência do aluno

if idade <= 18:
    print("Matrícula Negada . Aluno menor de idade")

elif nota >= 9:
    print("Matrícula Aprovada automaticamente")

elif idade >= 18 and nota >= 6 and frequencia >= 75:
    print("Matrícula Aprovada")
else:
    print("Matrícula Negada")

