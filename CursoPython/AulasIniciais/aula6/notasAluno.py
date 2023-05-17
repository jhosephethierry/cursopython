nomeAluno = input("Digite o nome do aluno: ")

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
    