def listaintervalo(lista,limiteinferior,limitesuperior):

    novalista = []
    
    for n in lista:
        
        if n >= limiteinferior and n <= limitesuperior:
            
            novalista.append(n)
        
    return novalista
            
listanumero = [10,20,30,40,50,60,70,80,90,100]

listanumero.sort()

listanovanumero = listaintervalo(listanumero,50,100)

print(listanovanumero)

