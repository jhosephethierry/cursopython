class Pokemon:

    def __init__(self,nome,elemento,fAataque,fDefesa):
        
        self.nome = nome
        self.elemento = elemento
        self.fAtaque = fAataque
        self.fDefesa = fDefesa

pokemon1 = Pokemon('Charmander','fogo',700,700)
pokemon2 = Pokemon('Meotwo','Telepata',1300,1100)

print(f'Este pokemon é o {pokemon1.nome}, seu tipo é {pokemon1.elemento}, sua força de ataque é {pokemon1.fAtaque} e a defesa é {pokemon1.fDefesa}.')
print(f'Este pokemon é o {pokemon2.nome}, seu tipo é {pokemon2.elemento}, sua força de ataque é {pokemon2.fAtaque} e a defesa é {pokemon2.fDefesa}.')

print(pokemon1.nome)
print(pokemon2.nome)

pokemonSelecionado = input('Selecione seu pokemon. ')

if pokemonSelecionado == pokemon1.nome:
    print(f'Você escolheu {pokemon1.nome}.')

elif pokemonSelecionado == pokemon2.nome:
    print(f'Você escolheu {pokemon2.nome}.')



