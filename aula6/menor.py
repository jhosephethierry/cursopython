menor = 0

for i in range(5):

        numero = int(input("digite um inteiro: "))
    
        if menor == 0:
            menor = numero
    
        elif numero < menor:
            menor = numero
    
print("o menor número inserido foi ", menor)