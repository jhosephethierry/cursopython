def gorjeta(valordaconta):
    
    gorjeta = (valordaconta / 100) * 10
    
    print(f"a gorjeta é R$ {gorjeta}")
    
gorjeta(valordaconta = float(input("digite o valor da conta: ")))



# alternativa RETURN

def calculagorjeta(valorconta):
    
    gorjeta = float(valorconta) * 0.1
    
    return gorjeta

conta = input("digite o valor da conta: ")
gorjetaconta = calculagorjeta(conta)
totalconta = float(conta) + gorjetaconta

print("o valor da gorjeta é R$ ", gorjetaconta)
print("o valor total da conta é R$", totalconta)