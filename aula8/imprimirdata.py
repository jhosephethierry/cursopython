def imprimirdata(data):
    
    listadata = data.split("/")
    
    
    if int(listadata[0]) <= 0 or int(listadata[0]) > 31:
        print("dia invalido")
    elif int(listadata[1]) <= 0 or int(listadata[1]) > 12:
        print("mes invalido")
    elif not listadata[2].isnumeric():
        print("o ano deve ser um número inteiro")
    else:
        match int(listadata[1]):
           
            case 1:
                mes = "janeiro"
            case 2:
                mes = "fevereiro"
            case 3:
                mes = "março"
            case 4:
                mes = "abril"
            case 5:
                mes = "maio"
            case 6:
                mes = "junho"
            case 7:
                mes = "julho"
            case 8:
                mes = "agosto"
            case 9:
                mes = "setembro"
            case 10:
                mes = "outubro"
            case 11:
                mes = "novembro"
            case 12:
                mes = "dezembro"
        
        return f"{listadata[0]} de {mes} de {listadata[2]}"
    
    return None

diamesano = input("digite uma data: ")
print (imprimirdata(diamesano))