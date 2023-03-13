# Escreva um programa que imprima todos os números ímpares entre 1 e 50.

lista = []

for i in range(50):
   
    if i / 2 % 1:
        
        lista.append(i)
        
print(lista)