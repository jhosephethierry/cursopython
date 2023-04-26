def potencia(base,expoente):
    
    resultado = 1
    
    for i in range(expoente):
        
        resultado = resultado * base
   
    return resultado

a = potencia(4,2)
b = potencia(4,5)

print(a)
print(b)