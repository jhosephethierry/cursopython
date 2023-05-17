contador = 0

while contador < 5:
   
    print(contador)
   
    contador = contador + 1

#CPF 

while True:

    cpf = int(input("digite seu cpf: "))

    if len(cpf) != 11:
        print("cpf inválido")

    else:
      
        break