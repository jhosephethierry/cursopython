# Escreva um programa que solicite ao usuário um número e imprima se ele é positivo, negativo ou zero.

numeroinformado = int(input('Digite um número. '))
    
if numeroinformado > 0:
    print(f'{numeroinformado} é positivo.') 
elif numeroinformado == 0:
    print('O número informado é zero.')
else:
    print(f'{numeroinformado} é negativo.') 
