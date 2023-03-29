nomes = ["jhosephe", "thierry", "andrade", "cacau"]

nomeEscolhido = input("escolha um nome. ").lower()

for r in nomes:

    if r != nomeEscolhido:

        print("o nome escolhido se encontra fora dessa posicao.")

        continue

    print("inicio")

    print(". ", r.upper())
    print(". ", r.lower())
    print(". ", r.capitalize())
    print(". ", r.title())

    print("final")

    if r == nomeEscolhido:

        print("encontrei o nome escolhido.")

        break