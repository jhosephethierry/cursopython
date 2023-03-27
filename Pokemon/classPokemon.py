class Pokemon:

    def __init__(self, nome, especie, tipo, ataque, defesa, hp, poder):

        self._nome = nome
        self._especie = especie
        self._tipo = tipo
        self._ataque = int(ataque)
        self._defesa = int(defesa)
        self._hp = int(hp)
        self._poder = int(poder)

    def criarPokemon(self):
       
        self._nome = input('qual o nome do pokemon a ser criado? ')
       
        print(

        '''
        os tipos disponiveis são:
        1. Terra
        2. Água
        3. Ar
        4. Fogo

        ''' )

        self._tipo = input('escolha o tipo. ')
        
        if self._tipo == 1:
            self._tipo == Terra()
        elif self._tipo == 2:
            self._tipo == Agua()
        elif self._tipo == 3:
            self._tipo == Ar()
        elif self._tipo == 4:
            self._tipo == Fogo()
            



        self._tipo = [1: Terra(), 2: Agua(), 3: Ar(), 4: Fogo()]



class Terra(Pokemon):

    def __init__(self, nome, especie, tipo, ataque, defesa, hp, poder):
        super().__init__(self, nome, especie, tipo, ataque, defesa, hp, poder)

        if especie == 'Pedra':
            hp * 2 and poder == 'Avalanche'
        elif especie == 'Planta':
            hp * 3 and poder == 'Amarrar'

        self._tipo = 'Terra'


class Agua(Pokemon):

    def __init__(self, nome, especie, tipo, ataque, defesa, hp, poder):
        super().__init__(self, nome, especie, tipo, ataque, defesa, hp, poder)

        if especie == 'Gelo':
            hp * 2 and poder == 'Congelar'
        elif especie == 'Aquatico':
            hp * 3 and poder == 'Inundar'

        self._tipo = 'Agua'


class Ar(Pokemon):

    def __init__(self, nome, especie, tipo, ataque, defesa, hp, poder):
        super().__init__(self, nome, especie, tipo, ataque, defesa, hp, poder)

        if especie == 'Brisa':
            hp * 2 and poder == 'Ventania'
        elif especie == 'Furacão':
            hp * 3 and poder == 'Tornado'

        self._tipo = 'Ar'


class Fogo(Pokemon):

    def __init__(self, nome, especie, tipo, ataque, defesa, hp, poder):
        super().__init__(self, nome, especie, tipo, ataque, defesa, hp, poder)

        if especie == 'Fumaça':
            hp * 2 and poder == 'Cortina de Fumaça'
        elif especie == 'Plasma':
            hp * 3 and poder == 'Jato de Plasma'

        self._tipo = 'Fogo'


class Treinador:

    def __init__(self, nomeTreinador, pokemons):

        self._nomeTreinador = nomeTreinador
        self._pokemons = pokemons
