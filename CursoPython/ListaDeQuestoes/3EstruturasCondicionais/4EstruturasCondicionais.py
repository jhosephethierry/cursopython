# Escreva um programa que solicite ao usuário a idade e o sexo de uma pessoa e 
# imprima uma mensagem personalizada com base nas seguintes condições:
# Se a pessoa for do sexo feminino e tiver menos de 25 anos, imprima "Você é uma jovem mulher".
# Se a pessoa for do sexo feminino e tiver 25 anos ou mais, imprima "Você é uma mulher adulta".
# Se a pessoa for do sexo masculino e tiver menos de 25 anos, imprima "Você é um jovem homem".
# Se a pessoa for do sexo masculino e tiver 25 anos ou mais, imprima "Você é um homem adulto".

idade = int(input('Digite sua idade. '))
sexo = input(str('Digite seu sexo. '))

sexo = sexo.lower()

if sexo == 'feminino' and idade < 25:
    print('Você é uma mulher jovem.')
elif sexo == 'feminino' and idade > 25:
    print('Você é uma mulher adulta.')
elif sexo == 'masculino' and idade < 25:
    print('Você é um homem jovem.')
elif sexo == 'masculino' and idade > 25:
    print('Você é um homem adulto.')