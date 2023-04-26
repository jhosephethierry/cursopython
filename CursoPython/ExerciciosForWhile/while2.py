nomes = ["jhosephe", "thierry", "andrade", "cacau"]

nomeEscolhido = input("escolha um nome. ").lower()
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

    if r == nomeEscolhido:

        print("encontrei o nome escolhido.")

        break

    indice += 1