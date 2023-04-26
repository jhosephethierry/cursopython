# Escreva um programa que solicite ao usuário a nota de um aluno em uma prova e imprima a mensagem 
# "Aprovado" se a nota for maior ou igual a 7, 
# "Reprovado" se a nota for menor que 5 e "Recuperação" se a nota estiver entre 5 e 7.

nomeAluno = input('Digite o nome do aluno. ')
nota = float(input('Digite a nota do aluno. '))

if nota >= 7:
    print(f'{nomeAluno} foi aprovado.')
elif nota <= 5:
    print(f'{nomeAluno} foi reprovado.')
elif nota > 5 and nota < 7:
    print(f'{nomeAluno} está em recuperação.')