# Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.

Lista = []

for numero in range(7):
    
        Lista.append(int(input('Digite um numero. ')))
    
print(f'O maior número da lista é {max(Lista)} e o menor é {min(Lista)}.')
