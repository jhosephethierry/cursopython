# Escreva um programa que leia o nome e a idade de uma pessoa e imprima uma mensagem personalizada com base na idade. 
# Se a idade for menor que 18 anos, imprima "Você é menor de idade". 
# Se a idade estiver entre 18 e 65 anos, imprima "Você é adulto". 
# Caso contrário, imprima "Você é idoso".

Nome = input('Digite seu nome. ')
Idade = int(input('Digite sua idade. '))

    
if Idade < 18:
    print(f'Olá {Nome}, você tem {Idade} ano(s). Portanto é menor de idade.') 
elif Idade >= 18 and Idade <= 65:
    print(f'Olá {Nome}, você tem {Idade} ano(s). Portanto é adulto.') 
elif Idade > 65:
    print(f'Olá {Nome}, você tem {Idade} ano(s). Portanto é idoso.') 