import json

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
            self._ataque = self._ataque 
            self._defesa = self._defesa
        elif pokemonOponente == "Agua":
            self._ataque = self._ataque * 0.5
            self._defesa = self._defesa * 0.5
        elif pokemonOponente == "Ar":
            self._ataque = self._ataque * 0.5
            self._defesa = self._defesa * 2
        elif pokemonOponente == "Fogo":
            self._ataque = self._ataque * 2
            self._defesa = self._defesa * 0.5

class PokemonAgua(Pokemon):

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa, pokemonOponente):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

        self._tipoPokemon = "Agua"
        
        if pokemonOponente == "Terra":
            self._ataque = self._ataque * 0.10
            self._defesa = self._defesa * 0.10
        elif pokemonOponente == "Agua":
            self._ataque = self._ataque 
            self._defesa = self._defesa
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
            self._ataque = self._ataque 
            self._defesa = self._defesa
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
            self._ataque = self._ataque
            self._defesa = self._defesa



# Superclasse Treinador
class Treinador:

    def __init__(self):
        
        self._nome = []
        self._timepokemon = []
        self._pokemonCriado = []



    def criarTreinador(self):

        self._nome = input("Escreva o nome do treinador. ")



    def criarPokemon(self):

        def criar():

            self._nomePokemon = []
            self._nomePokemon = input("Escolha o nome do seu pokemon. ")

            print("")
            print("Estes sao os tipos disponiveis 1. Terra | 2. Agua | 3.Ar | 4. Fogo")

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

            print("")
            print(f"{self._nome}, voce criou o pokemon {self._nomePokemon} do tipo {self._tipoPokemon} com poder de ataque {self._ataque} e {self._defesa} de defesa.")

            self._pokemonCriado = {"Nome": [self._nomePokemon], "Tipo": [self._tipoPokemon], "Ataque": [self._ataque], "Defesa": [self._defesa]}
            print("")
            adicionar = input("Vamos adicionar ao seu time? s ou n?  ")
            if adicionar == "s":

                def adicionarAoTime():

                    self._timepokemon.append(self._pokemonCriado)

                    print("")
                    print(f"{self._nomePokemon} foi adicionado ao seu time.")

                    def adicionarAoTimeJson():

                        with open("Pokemon/timePokemon.json", 'w') as timePokemonJson:
                            
                            json.dump(self._timepokemon, timePokemonJson, indent=2)

                    adicionarAoTimeJson()

                    def adicionarAoMundo():

                        with open("Pokemon/mundoPokemon.json", 'w') as mundoPokemonJson:
                            
                            json.dump(self._timepokemon, mundoPokemonJson, indent=2)

                    adicionarAoMundo()

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
        
        for r in range(len(self._timepokemon)):
            print(f"{r+1}. {self._timepokemon[r]}")

    def mostrarMundoPokemon(self):

        with open("Pokemon/mundoPokemon.json", 'r') as mundoPokemonJson:
            mundopokemon = json.load(mundoPokemonJson)
            for r in range(len(mundopokemon)):
                print(f"{r+1}. {mundopokemon[r]}")

        return mundopokemon
    
    def capturarPokemon(self):

        with open("Pokemon/mundoPokemon.json", 'r') as mundoPokemonJson:
            mundopokemon = json.load(mundoPokemonJson)
            print("Esse e o mundo pokemon")
            print(mundopokemon)

        pokemonCapturado = input("Escreva o nome do pokemon que voce quer capturar. ")

        if pokemonCapturado == "":
            print("Opção Inválida! Tente novamente.")

        for pokemonCapturado in mundopokemon:

            print(f"Voce escolheu {pokemonCapturado}.")
            adicionar = input("Vamos adicionar ao seu time? s ou n?  ")
            if adicionar == "s":

                def adicionarAoTime():

                    self._timepokemon.append(pokemonCapturado)

                    print("")
                    print(f"{pokemonCapturado} foi adicionado ao seu time.")

                def adicionarAoTimeJson():

                    with open("Pokemon/timePokemon.json", 'w') as timePokemonJson:
                        json.dump(self._timepokemon, timePokemonJson, indent=2)

                adicionarAoTimeJson()
            
            

        if adicionar == "n":    
            print(f"{pokemonCapturado} foi descartado.")

        



        adicionarAoTime()
                
            

        

          

# Subclasses Treinador
class Jogador(Treinador):

    def __init__(self):
        super().__init__()

class Oponente(Treinador):

    def __init__(self):
        super().__init__()
    


# self._pokemonCriado = [f"{self._nomePokemon} | Tipo {self._tipoPokemon} | Ataque {self._ataque} | Defesa {self._defesa}"]