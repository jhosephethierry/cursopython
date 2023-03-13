# Escreva um programa que solicite ao usuário um número e imprima a tabuada desse número até o valor 10.

numeroinformado = int(input('Digite um número. '))

for i in range(1,11):
       
        calculo = i * numeroinformado
       
        print(f"{i}. {numeroinformado} x {i} = {calculo}")