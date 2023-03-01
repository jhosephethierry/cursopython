Lista = [int(input("digite um numero: ")), 7, 2, 3, 14]
    
print(max(Lista)) # resolução simples

maior = Lista[0]


for numero in Lista:
    
    if numero > maior:
    
        maior = numero

print(maior)
