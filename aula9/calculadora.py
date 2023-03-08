def soma(numA,numB):
    
    soma = numA + numB
    
    return soma

def subtracao(numA,numB):
    
    subtracao = numA - numB
    
    return subtracao

def divisao(numA,numB):
    
    divisao = numA / numB
    
    return divisao

def multiplicacao(numA,numB):
    
    multiplicacao = numA * numB
    
    return multiplicacao

def main():


    num1 = int(input("digite o primeiro numero: "))
    operador = input("digite o operador: ")
    num2 = int(input("digite o segundo numero: "))
    
    if operador == "+":
        print(soma(num1,num2))
    elif operador == "-":
        print(subtracao(num1,num2))
    elif operador == "/":
        print(divisao(num1,num2))
    elif operador == "*":
        print(multiplicacao(num1,num2))
        
main()
    
    