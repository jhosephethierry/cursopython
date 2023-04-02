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
        self._timepokemon = []



    def criarTreinador(self):

        self._nome = input("Escreva o nome do treinador. ")



    def criarPokemon(self):

        def criar():

            self._nomePokemon = []
            self._pokemonCriado = ()
        
            self._nomePokemon = input("Escolha o nome do seu pokemon. ")

            print("O tipo do seu pokemon pode ser.")
            print("1. Terra | 2. Agua | 3.Ar | 4. Fogo")

            self._tipoPokemon = input("Escolha o tipo. ")
            match self._tipoPokemon:
                case "1":
                    self._tipoPokemon = "Terra"
                case "2":
                    self._tipoPokemon = "Agua"
                case "3":
                    self._tipoPokemon = "Ar"
                case "4":
                    self._tipoPokemon = "Fogo"

            self._ataque = int(input("Escolha um valor de poder de ataque. "))
            self._defesa = int(input("Agora escolha o valor para o poder de defesa. "))

            print(f"{self._nome}, voce criou o pokemon {self._nomePokemon} do tipo {self._tipoPokemon} com poder de ataque {self._ataque} e {self._defesa} de defesa.")

            adicionar = input("Vamos adicionar ao seu time? s ou n?  ")
            if adicionar == "s":

                def adicionarAoTime():

                    self._pokemonCriado = [{self._nomePokemon}, {self._tipoPokemon}, {self._ataque}, {self._defesa}]
                    self._timepokemon.append(self._pokemonCriado)
                    print(f"{self._nomePokemon} foi adicionado ao seu time.")

                adicionarAoTime()
                
            elif adicionar == "n":
                
                print(f"{self._nomePokemon} foi descartado.")
   
            continuar = input("quer continuar criando pokemons? ")
            while continuar == "s":
                criar()
                if continuar == "n":
                    print("voce escolheu parar.")
                break

        criar()


    def mostrarTimePokemon(self):
            

            for i in range(len(self._timepokemon)):
                print(f"{i+1}. {self._pokemonCriado[i]}")



# Subclasses Treinador
class Jogador(Treinador):

    def __init__(self):
        super().__init__()

class Oponente(Treinador):

    def __init__(self):
        super().__init__()


