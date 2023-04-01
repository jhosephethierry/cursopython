# Superclasse Pokemon
class Pokemon:

    def __init__(self,nomePokemon,tipoPokemon,ataque,defesa):

        self._nomePokemon = nomePokemon
        self._tipoPokemon = tipoPokemon
        self._ataque = ataque
        self._defesa = defesa



# Subclasses Pokemon
class PokemonTerra(Pokemon):

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa,pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

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

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa,pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

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

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa,pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

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

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa,pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

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

    def criarPokemon(self):

        print("Crie seu pokemon")
        self._nomePokemon = input("Escolha o nome do seu pokemon. ")

        print("O tipo do seu pokemon pode ser.")
        print(" 1. Terra | 2. Agua | 3.Ar | 4. Fogo")
        self._tipoPokemon = input("Escolha o tipo. ")
        match self._tipoPokemon:
            case "1":
                self._tipo = PokemonTerra()
            case "2":
                self._tipo = PokemonAgua()
            case "3":
                self._tipo = PokemonAr()
            case "4":
                self._tipo = PokemonFogo()

        self._ataque = input(int("Escolha um valor de poder de ataque. "))
        self._defesa = input(int("Agora escolha o valor para o poder de defesa. "))

        print(f"{self._nome}, voce criou o pokemon {self._nomePokemon} do tipo {self._tipoPokemon} com poder de ataque {self._ataque} e {self._defesa} de defesa.")

    def mostrarTimePokemon(self):






# Subclasses Treinador
class Jogador(Treinador):

    def __init__(self, nome, timepokemon):
        super().__init__(nome, timepokemon)

class Oponente(Treinador):

    def __init__(self, nome, timepokemon):
        super().__init__(nome, timepokemon)