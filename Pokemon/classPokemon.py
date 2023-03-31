# Superclasse Pokemon
class Pokemon:

    def __init__(self,nome,tipo,ataque,defesa):

        self._nome = nome
        self._tipo = tipo
        
        if tipo == "Terra":
            self._tipo = PokemonTerra()
        elif tipo == "Agua":
            self._tipo = PokemonAgua()
        elif tipo == "Ar":
            self._tipo = PokemonAr()
        elif tipo == "Fogo":
            self._tipo = PokemonFogo()

        self._ataque = ataque
        self._defesa = defesa



# Subclasses Pokemon
class PokemonTerra(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa, pokemonOponente):
        super().__init__(nome, tipo, ataque, defesa)

        if pokemonOponente == PokemonTerra():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAgua():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAr():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonFogo():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10

class PokemonAgua(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa, pokemonOponente):
        super().__init__(nome, tipo, ataque, defesa)

        if pokemonOponente == PokemonTerra():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAgua():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAr():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonFogo():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        
class PokemonAr(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa, pokemonOponente):
        super().__init__(nome, tipo, ataque, defesa)

        if pokemonOponente == PokemonTerra():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAgua():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAr():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonFogo():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10

class PokemonFogo(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa, pokemonOponente):
        super().__init__(nome, tipo, ataque, defesa)

        if pokemonOponente == PokemonTerra():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAgua():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonAr():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == PokemonFogo():
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10



# Superclasse Treinador
class Treinador:

    def __init__(self,nome,timepokemon):
        
        self._nome = nome
        self._timepokemon = timepokemon



# Subclasses Treinador
class Jogador(Treinador):

    def __init__(self, nome, timepokemon):
        super().__init__(nome, timepokemon)

class Oponente(Treinador):

    def __init__(self, nome, timepokemon):
        super().__init__(nome, timepokemon)