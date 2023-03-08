def Negativo(numero):
    
    if numero < 0:
   
        return numero
    
def Positivo(numero):
    
    if numero >= 0:
   
        return numero
    
def main():
    
    numeroinformado = int(input("digite o primeiro numero: "))
    
    if numeroinformado == Negativo(numeroinformado):
        print("N") 
    elif numeroinformado == Positivo(numeroinformado):
        print("P") 

main()
    
