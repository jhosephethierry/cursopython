import classPokemon


treinador = classPokemon.Treinador()
jogador = classPokemon.Jogador()
oponente = classPokemon.Oponente()

def menuInicial():

    opcao = ""
    while(opcao != '3'):
        print("Escolha o modo de entrada")
        opcao = input("1. Modo Jogador | 2. Modo Oponente | 3. Sair : ")
        
        if opcao == '1':
            print("Voce esta no modo Jogador")
            print("")
            menuJogador()         

        elif opcao == '2':
            print("Voce esta no modo Oponente")
            print("")
            menuOponente()     

        elif opcao == '3':
            print("Voce escolheu sair")
            break            
        else:
            print("Opção Inválida! Tente novamente.")          
            

def menuJogador():

    opcao = ""
    while(opcao != '5'):
        print("Escolha uma opcao no menu.")
        opcao = input("1. Criar Treinador | 2. Criar Pokemon | 3. Mostrar Time | 4. Mostrar Mundo Pokemon | 5. Sair : ")
        
        if opcao == '1':
            print("Vamos criar o treinador")
            print("")
            jogador.criarTreinador()                     
            print(f"{jogador._nome} criado")
            print("")
          
        elif opcao == '2':            
            print("Vamos criar o pokemon")
            print("")
            jogador.criarPokemon()
            print("")
                             
        elif opcao == '3':
            print("Esse e o time pokemon")
            print("")
            jogador.mostrarTimePokemon()
            print("")

        elif opcao == '4':
            print("Esse e o mundo pokemon")
            print("")
            jogador.mostrarMundoPokemon()
            print("") 

        elif opcao == '5':
            print("Voce escolheu sair")
            break            
        else:
            print("Opção Inválida! Tente novamente.")

menuJogador()
            
def menuOponente():

    opcao = ""
    while(opcao != '3'):
        print("Escolha uma opcao no menu.")
        opcao = input("1. Criar Oponente | 2. Mostrar Mundo Pokemon | 3. Sair : ")
        
        if opcao == '1':
            print("Vamos criar o oponente")
            print("")
            oponente.criarTreinador()                     
            print(f"{oponente._nome} criado")
            print("")

        elif opcao == '2':
            print("Esse e o mundo pokemon")
            print("")
            oponente.mostrarMundoPokemon()
            print("") 

        elif opcao == '3':
            print("Voce escolheu sair")
            break            
        else:
            print("Opção Inválida! Tente novamente.")

menuOponente()









    