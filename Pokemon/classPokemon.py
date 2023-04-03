import json

# Superclasse Pokemon
class Pokemon:

    def __init__(self,nomePokemon,tipoPokemon,ataque,defesa):

        self._nomePokemon = nomePokemon
        self._tipoPokemon = tipoPokemon
        self._ataque = ataque
        self._defesa = defesa
    
    def gerarDicionario(self):
        
        pokeDicionario = {"Nome":self._nomePokemon, "Tipo": self._tipoPokemon, "Ataque": self._ataque, "Defesa": self._defesa}
        return pokeDicionario
    
    def batalhar(self,oponente):
        
        ataqueAtual = 0
        defesaAtual = 0
        
        if oponente._tipoPokemon == "Terra":
            ataqueAtual = self._ataque 
            defesaAtual = self._defesa
        elif oponente._tipoPokemon == "Agua":
            ataqueAtual = self._ataque * 0.5
            self._defesa = self._defesa * 0.5
        elif oponente._tipoPokemon == "Ar":
            self._ataque = self._ataque * 0.5
            self._defesa = self._defesa * 2
        elif oponente._tipoPokemon == "Fogo":
            self._ataque = self._ataque * 2
            self._defesa = self._defesa * 0.5

        if ataqueAtual+defesaAtual > oponente._ataque + oponente._defesa:
            print("Eu ganho")



# Subclasses Pokemon
class PokemonTerra(Pokemon):

    def __init__(self, nomePokemon, tipoPokemon, ataque, defesa, ):
        super().__init__(nomePokemon, tipoPokemon, ataque, defesa)

        self._tipoPokemon = "Terra"

        

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
        
        self._nome = ""
        self._timepokemon = []
        self._pokemonCriado = {"Nome":"", "Tipo":"", "Ataque": 0, "Defesa":0}
        self._mundopokemon = []



    def criarTreinador(self):

        self._nome = input("Escreva o nome do treinador. ")



    def criarPokemon(self):

        self._pokemonCriado["Nome"] = input("Escolha o nome do seu pokemon. ")

        print("")
        print("Estes sao os tipos disponiveis 1. Terra | 2. Agua | 3.Ar | 4. Fogo")

        escolhaTipo = input("Escolha o tipo. ")
        
        self._pokemonCriado["Ataque"] = int(input("Escolha um valor de poder de ataque. "))
        self._pokemonCriado["Defesa"] = int(input("Agora escolha o valor para o poder de defesa. "))

        match escolhaTipo:
            case "1":
                self._pokemonCriado["Tipo"] = "Terra"
                novoPokemon = PokemonTerra(self._pokemonCriado['Nome'],self._pokemonCriado['Tipo'],self._pokemonCriado['Ataque'],self._pokemonCriado['Defesa'],None)
            case "2":
                self._pokemonCriado["Tipo"] = "Agua"
                novoPokemon = PokemonAgua(self._pokemonCriado['Nome'],self._pokemonCriado['Tipo'],self._pokemonCriado['Ataque'],self._pokemonCriado['Defesa'],None)
            case "3":
                self._pokemonCriado["Tipo"] = "Ar"
                novoPokemon = PokemonAr(self._pokemonCriado['Nome'],self._pokemonCriado['Tipo'],self._pokemonCriado['Ataque'],self._pokemonCriado['Defesa'],None)
            case "4":
                self._pokemonCriado["Tipo"] = "Fogo"
                novoPokemon = PokemonFogo(self._pokemonCriado['Nome'],self._pokemonCriado['Tipo'],self._pokemonCriado['Ataque'],self._pokemonCriado['Defesa'],None)
            case _:
                novoPokemon = Pokemon(self._pokemonCriado['Nome'],self._pokemonCriado['Tipo'],self._pokemonCriado['Ataque'],self._pokemonCriado['Defesa'],None)

        print("")
        print(f"{self._nome}, voce criou o pokemon {self._pokemonCriado['Nome']} do tipo {self._pokemonCriado['Tipo']} com poder de ataque {self._pokemonCriado['Ataque']} e {self._pokemonCriado['Defesa']} de defesa.")

        print("")
        adicionar = input("Vamos adicionar ao seu time? s ou n?  ")
        if adicionar == "s":

            
            self._timepokemon.append(novoPokemon)

            print("")
            print(f"{novoPokemon._nomePokemon} foi adicionado ao seu time.")

            with open("Pokemon/timePokemon.json", 'r') as timePokemonJson:
                timeJson = json.load(timePokemonJson)

                timeJson.append(novoPokemon.gerarDicionario())

            with open("Pokemon/timePokemon.json", 'w') as timePokemonJson:
                
                json.dump(timeJson, timePokemonJson, indent=2)

            with open("Pokemon/mundoPokemon.json", 'r') as mundoPokemonJson:
                mundoJson = json.load(mundoPokemonJson)
                    
                mundoJson.append(novoPokemon.gerarDicionario())

            with open("Pokemon/mundoPokemon.json", 'w') as mundoPokemonJson:

                

                json.dump(mundoJson, mundoPokemonJson, indent=2)

            
            
        elif adicionar == "n":

            self._mundopokemon.append(novoPokemon)
            
            print(f"{novoPokemon._nomePokemon} foi descartado do seu time, mas foi adicionado ao mundo pokemon.")

            with open("Pokemon/mundoPokemon.json", 'r') as mundoPokemonJson:
                mundoJson = json.load(mundoPokemonJson)
                    
                mundoJson.append(novoPokemon.gerarDicionario())

            with open("Pokemon/mundoPokemon.json", 'w') as mundoPokemonJson:

                

                json.dump(mundoJson, mundoPokemonJson, indent=2)

            

        continuar = input("quer continuar criando pokemons? ")
        while continuar == "s":
            self.criarPokemon()
            if continuar == "n":
                print("voce escolheu parar.")
            break

        


    def mostrarTimePokemon(self):
        
        def carregarTimePokemonJson():

            with open("Pokemon/timePokemon.json", 'r') as timePokemonJson:
                timepokemon = json.load(timePokemonJson)
                
                return timepokemon
        
        carregarTimePokemonJson()

        def mostrarTimePokemon():
                
                timepokemon = carregarTimePokemonJson()

                print("Esse e seu time pokemon")

                for pokemons in timepokemon:

                    print(f'{pokemons["Nome"]} | {pokemons["Tipo"]} | {pokemons["Ataque"]} | {pokemons["Defesa"]}')
                
                print("")

        mostrarTimePokemon()

    def mostrarMundoPokemon(self):

        def carregarMundoPokemonJson():

            with open("Pokemon/mundoPokemon.json", 'r') as mundoPokemonJson:
                mundopokemon = json.load(mundoPokemonJson)
                
                return mundopokemon
        
        carregarMundoPokemonJson()

        def mostrarMundoPokemon():
                
                listamundopokemon = carregarMundoPokemonJson()

                print("Esse e o mundo pokemon")

                for pokemons in listamundopokemon:

                    print(f'{pokemons["Nome"]} | {pokemons["Tipo"]} | {pokemons["Ataque"]} | {pokemons["Defesa"]}')
                
                print("")

        mostrarMundoPokemon()
    
    def capturarPokemon(self):
            
        with open("Pokemon/mundoPokemon.json", 'r') as mundoPokemonJson:
            mundopokemon = json.load(mundoPokemonJson)
            
   
        

        print("Esse e o mundo pokemon")

        for pokemons in mundopokemon:

            print(f'{pokemons["Nome"]} | {pokemons["Tipo"]} | {pokemons["Ataque"]} | {pokemons["Defesa"]}')
                
        print("")        

            

        pokemonAcapturar = input("Escreva o nome do pokemon que voce quer capturar. ")

        print(f"Voce escolheu {pokemonAcapturar}.")

        pokemonEscolhido = pokemonAcapturar

        for pokemonSelvagem in mundopokemon:

            if pokemonEscolhido == pokemonSelvagem["Nome"]:

                adicionar = input("Vamos adicionar ao seu time? s ou n?  ")
                if adicionar == "s":

                    

                    match pokemonSelvagem["Tipo"]:
                        case "Terra":
                            novoPokemon = PokemonTerra(pokemonSelvagem['Nome'],pokemonSelvagem['Tipo'],pokemonSelvagem['Ataque'],pokemonSelvagem['Defesa'],None)
                        case "Agua":
                            
                            novoPokemon = PokemonAgua(pokemonSelvagem['Nome'],pokemonSelvagem['Tipo'],pokemonSelvagem['Ataque'],pokemonSelvagem['Defesa'],None)
                        case "Ar":
                            
                            novoPokemon = PokemonAr(pokemonSelvagem['Nome'],pokemonSelvagem['Tipo'],pokemonSelvagem['Ataque'],pokemonSelvagem['Defesa'],None)
                        case "Fogo":
                            
                            novoPokemon = PokemonFogo(pokemonSelvagem['Nome'],pokemonSelvagem['Tipo'],pokemonSelvagem['Ataque'],pokemonSelvagem['Defesa'],None)


                    self._timepokemon.append(novoPokemon)

                    print("")
                    print(f"{novoPokemon._nomePokemon} foi adicionado ao seu time.")
            
                

                    with open("Pokemon/timePokemon.json", 'r') as timePokemonJson:
                        timeJson = json.load(timePokemonJson)

                        timeJson.append(novoPokemon.gerarDicionario())

                    with open("Pokemon/timePokemon.json", 'w') as timePokemonJson:
                
                        json.dump(timeJson, timePokemonJson, indent=2)

                    break

                    

                    
            
                elif adicionar == "n":    
                    print(f"{pokemonEscolhido} foi descartado.")
                
                    break

        
                               

# Subclasses Treinador
class Jogador(Treinador):

    def __init__(self):
        super().__init__()

class Oponente(Treinador):

    def __init__(self):
        super().__init__()
    


# self._pokemonCriado = [f"{self._nomePokemon} | Tipo {self._tipoPokemon} | Ataque {self._ataque} | Defesa {self._defesa}"]