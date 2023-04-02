import classPokemon
import random

jogador = classPokemon.Jogador()
oponente = classPokemon.Oponente()

def menuJogador():
    opcao = ""
    while(opcao != '4'):
        print("Escolha uma opcao no menu.")
        opcao = input("1. Criar Treinador | 2. Criar Pokemon | 3. Mostrar Time | 4. Sair : ")
        
        if opcao == '1':
            print("Vamos criar o treinador")
            jogador.criarTreinador()                     
            print(f"{jogador._nome} criado")
          
        elif opcao == '2':            
            print("Vamos criar o pokemon")
            jogador.criarPokemon()
                             
        elif opcao == '3':
            print("Esse e o time pokemon")
            jogador.mostrarTimePokemon() 

        elif opcao == '4':
            print("Voce escolheu sair")
            break            
        else:
            print("Opção Inválida! Tente novamente.")

menuJogador()
            









    