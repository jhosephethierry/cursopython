nomes = ["jhosephe", "thierry", "andrade", "cacau"]

nomeEscolhido = input("escolha um nome. ").lower()
tamanhoListaNomes = len(nomes)
indice = 0

while indice < tamanhoListaNomes:

    r = nomes[indice]
    indice += 1

    if r != nomeEscolhido:
         print("ainda estou procurando o nome escolhido.")

    print("_" * 72)

    print(". ", r.upper())
    print(". ", r.lower())
    print(". ", r.capitalize())
    print(". ", r.title())

    if r == nomeEscolhido:
        print("encontrei o nome escolhido.")

        break

    