nomes = ["jhosephe", "thierry", "andrade", "cacau"]

tamanhoListaNomes = len(nomes)
indice = 0

while indice < tamanhoListaNomes:

    r = nomes[indice]

    print("inicio")

    print(". ", r.upper())
    print(". ", r.lower())
    print(". ", r.capitalize())
    print(". ", r.title())

    print("final")

    indice += 1
    
    input()