def listalimites():

    lista  = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    limiteinferior = int(input("digite o limite inferior: "))
    limitesuperior = int(input("digite o limite superior: "))
    intervalo = limiteinferior[0::] and limitesuperior[::0]

listalimites()