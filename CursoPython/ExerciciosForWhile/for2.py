nomes = ["jhosephe", "thierry", "andrade", "cacau"]

nomeEscolhido = input("escolha um nome. ").lower()

for r in nomes:

    print("inicio")

    input()

    print(". ", r.upper())
    print(". ", r.lower())
    print(". ", r.capitalize())
    print(". ", r.title())

    input()

    print("final")
    
    input()

    if r == nomeEscolhido:

        print("encontrei o nome escolhido.")

        break