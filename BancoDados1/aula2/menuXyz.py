import xyz

def menuXYZ():

    opcao = ""
    while(opcao != '5'):
        print("")
        print("Escolha uma opcao no menu.")
        print("")
        opcao = input("1. Ver lista de Funcionarios | 2. Ver Lista de Departamentos | 3. Ver Lista por Departamento | 4. Sair: ")
        
        if opcao == '1':
            
            xyz.ListaFuncionarios()
          
        elif opcao == '2':  

            xyz.ListaDepartamentos()
                             
        elif opcao == '3':

            xyz.ListaFuncionariosDepartamento()

        elif opcao == '4':
            print("Voce escolheu sair")
            break            
        else:
            print("Opção Inválida! Tente novamente.")

menuXYZ()