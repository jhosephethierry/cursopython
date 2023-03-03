lista = [(2,5), (1,2), (4,4), (2,3), (2,1)]

novalista = []

for tupla in lista:
    
    novalista.append(tupla[::-1]) # reverte posição da tupla
    
novalista.sort()

lista.clear()

for tupla in novalista:
    
    lista.append(tupla[::-1])

print(lista)



