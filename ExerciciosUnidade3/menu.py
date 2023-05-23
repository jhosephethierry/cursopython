import funcoes as func
import psycopg2

while True:

    try:
        print('''
        
    ______________________________________________________________________________

    Pomar da Fazenda 
    ______________________________________________________________________________

    Escolha uma opção no menu abaixo.

    [ 1 ] - Inserir Fruta
    [ 2 ] - Ver Pomar  
    [ 3 ] - Atualizar Pomar 
    [ 0 ] - Sair   
    
    ______________________________________________________________________________

        ''')   
    
        op = input("Digite uma das opções. ")
        print("")
        
        match op:

            case "1": 
                func.inserirFruta()
            case "2":
                func.verPomar()
            case "3":
                func.atualizarPomar()
            case "4":
                print("Voltando ao menu principal...")
                break
                
                        
    except(Exception, psycopg2.Error) as error:
        print(error)