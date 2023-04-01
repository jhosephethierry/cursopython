# Superclasse Pokemon
class Pokemon:

    def __init__(self,nomePokemon,tipoPokemon,ataque,defesa):

        self._nomePokemon = nomePokemon
        self._tipoPokemon = tipoPokemon
        self._ataque = ataque
        self._defesa = defesa



# Subclasses Pokemon
class PokemonTerra(Pokemon):

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa, pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

        self._tipoPokemon = "Terra"

        if pokemonOponente == "Terra":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Agua":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Ar":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Fogo":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10

class PokemonAgua(Pokemon):

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa, pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

        self._tipoPokemon = "Agua"
        
        if pokemonOponente == "Terra":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Agua":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Ar":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Fogo":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        
class PokemonAr(Pokemon):

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa, pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

        self._tipoPokemon = "Ar"

        if pokemonOponente == "Terra":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Agua":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Ar":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Fogo":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10

class PokemonFogo(Pokemon):

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa, pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

        self._tipoPokemon = "Fogo"

        if pokemonOponente == "Terra":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Agua":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Ar":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Fogo":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10



# Superclasse Treinador
class Treinador:

    def __init__(self):
        
        self._nome = []
        self._nomePokemon = []
        self._timepokemon = []

    def criarTreinador(self):
        
        self._nome = input("Escreva seu nome. ")
        print(f"Ola {self._nome}.")

    def criarPokemon(self):

        self._pokemonCriado = ()

        print("Crie seu pokemon")
        self._nomePokemon = input("Escolha o nome do seu pokemon. ")

        print("O tipo do seu pokemon pode ser.")
        print(" 1. Terra | 2. Agua | 3.Ar | 4. Fogo")
        self._tipoPokemon = input("Escolha o tipo. ")
        match self._tipoPokemon:
            case "1":
                self._tipo = "Terra"
            case "2":
                self._tipo = "Agua"
            case "3":
                self._tipo = "Ar"
            case "4":
                self._tipo = "Fogo"

        self._ataque = int(input("Escolha um valor de poder de ataque. "))
        self._defesa = int(input("Agora escolha o valor para o poder de defesa. "))

        print(f"{self._nome}, voce criou o pokemon {self._nomePokemon} do tipo {self._tipo} com poder de ataque {self._ataque} e {self._defesa} de defesa.")

        

    def adicionarAoTime(self):

        self._pokemonCriado = [self._nome, self._tipoPokemon, self._ataque, self._defesa]
        
        self._timepokemon.append(self._pokemonCriado)
        print(f"{self._nomePokemon} foi adicionado ao seu time.")

    def mostrarTimePokemon(self):

        print("Seu time pokemon e.")
        for i in range(len(self._timepokemon)):
                print(f"{i+1}. {self._timepokemon[i]}")


# Subclasses Treinador
class Jogador(Treinador):

    def __init__(self, nome, timepokemon):
        super().__init__(nome, timepokemon)

class Oponente(Treinador):

    def __init__(self, nome, timepokemon):
        super().__init__(nome, timepokemon)



Thierry = Treinador()
Thierry.criarTreinador()
Thierry.criarPokemon()
Thierry.adicionarAoTime()
Thierry.mostrarTimePokemon()