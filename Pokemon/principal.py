import classPokemon

jogador = classPokemon.Jogador()
oponente = classPokemon.Oponente()

def menuJogador():

    op = input("Escolha")
    match op:
        case "1":
            jogador.criarTreinador()
        case "2":
            jogador.criarPokemon()
        case "3":
            jogador.mostrarTimePokemon()

menuJogador()
            










    