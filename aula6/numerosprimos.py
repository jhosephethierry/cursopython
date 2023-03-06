

numero = int(input("digite um número inteiro: "))

contador = 0

for i in range(1,numero+1):
    
    if numero % i == 0:
        
        contador = contador + 1 
        
        print(contador, "-", i)
        
if contador <= 2:
    
    print(numero, "é primo")
    
else:
    
    print(numero, "não é primo")
    
    
numero = int(input("digite um número inteiro: "))

primo = True

for i in range(2, numero):
    
    if numero % i == 0:
        
        primo = False
        
if primo:
    
    print("é primo")
    
else:
    
    print("não é primo")
        