import Funcoes as Func
import psycopg2

while True:

    try:
        print('''
        
    _________________________________

            Pomar da Fazenda 
    _________________________________

    Escolha uma opção no menu abaixo:

    [ 1 ] - Inserir Fruta
    [ 2 ] - Ver Pomar  
    [ 3 ] - Atualizar Pomar 
    [ 0 ] - Sair   
    
    __________________________________________________________________

        ''')   

        op = input("Digite uma das opções. ")
        print("")
        
        match op:

            case "1": 
                Func.inserirFruta()
            case "2":
                Func.verPomar()
            case "3":
                Func.atualizarPomar()
            case "4":
                print("Voltando ao menu principal...")
                break
                
                        
    except(Exception, psycopg2.Error) as error:
        print(error)