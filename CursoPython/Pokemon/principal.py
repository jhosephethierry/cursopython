import classPokemon

treinador = classPokemon.Treinador()

def menuTreinador():

    opcao = ""
    while(opcao != '7'):
        print("Escolha uma opcao no menu.")
        opcao = input("1. Criar Treinador | 2. Criar Pokemon | 3. Mostrar Time | 4. Mostrar Mundo Pokemon | 5. Capturar Pokemons | 6. Batalhar | 7. Sair : ")
        
        if opcao == '1':
            print("Vamos criar o treinador")
            print("")
            treinador.criarTreinador()                     
            print(f"{treinador._nome} criado")
            print("")
          
        elif opcao == '2':            
            print("Vamos criar o pokemon")
            print("")
            treinador.criarPokemon()
            print("")
                             
        elif opcao == '3':
            print(f"{treinador._nome}, esse e seu time pokemon")
            print("")
            treinador.mostrarTimePokemon()
            print("")

        elif opcao == '4':
            print("Esse e o mundo pokemon")
            print("")
            treinador.mostrarMundoPokemon()
            print("") 

        elif opcao == '5':
            print("Vamos capturar pokemons")
            print("")
            treinador.capturarPokemon()
            print("")

        elif opcao == '6':
            print("Vamos batalhar")
            print("")
            treinador.mostrarTimePokemon()
            print("") 

        elif opcao == '7':
            print("Voce escolheu sair")
            break            
        else:
            print("Opção Inválida! Tente novamente.")

menuTreinador()
            










    