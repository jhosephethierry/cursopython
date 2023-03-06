def listaintervalo(lista,limiteinferior,limitesuperior):

    novalista = []
    
    for n in lista:
        
        if n >= limiteinferior and n <= limitesuperior:
            
            novalista.append(n)
        
    return novalista
            
listanumero = []
        
listanumero = [2,5,7,7,8,13,15,16,80]
       
listanumero.sort()

listanovanumero = listaintervalo(listanumero,7,40)

print(listanovanumero)

