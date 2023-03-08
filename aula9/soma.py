def soma(numA,numB,numC):
    
    soma = numA + numB + numC
    
    return soma


def main():
    
    n1 = int(input("digite o primeiro número: "))
    n2 = int(input("digite o segundo número: ")) 
    n3 = int(input("digite o terceiro número: "))
   
    print(f"{n1} + {n2} + {n3} = {soma(n1,n2,n3)}")
    
main()