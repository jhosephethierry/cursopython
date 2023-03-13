# Escreva um programa que solicite ao usuário a nota de um aluno em uma prova e imprima 
# a mensagem "Aprovado" se a nota for maior ou igual a 7, "Reprovado" 
# se a nota for menor que 5 e "Recuperação" se a nota estiver entre 5 e 7.

nomeAluno = input('Digite o nome do aluno. ')

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

somaNotas = nota1 + nota2 + nota3

media = somaNotas/3

print(f"A média do aluno é {media}")

if media >= 7:
    print(f"{nomeAluno} foi aprovado.")
elif media <= 5:
    print(f"{nomeAluno} foi reprovado.")
elif media > 5 and media < 7:
    print(f"{nomeAluno} está em recuperação.")