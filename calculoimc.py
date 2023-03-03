def calculoimc(peso, altura):
    
    imc = peso / altura ** 2
    
    print(imc)
    
calculoimc(peso = float(input("digite seu peso ")), altura = float(input("digite sua altura: ")))