import json

with open("BancoDados1/aula2/dep.json", 'r') as xyzJson:
    xyz = json.load(xyzJson)
    xyzFuncionarios = list(xyz['Funcionario'])
    xyzDepartamentos = list(xyz['Departamento'])


def ListaFuncionarios():

    print("")
    print("Estes sao os funcionarios da XYZ")
    print("")

    for i,Funcionarios in enumerate(xyzFuncionarios):
            
            print(f'{i}. Id - {Funcionarios["ID_Funcionario"]} | Nome - {Funcionarios["Nome_Funcionario"]} | Cpf - {Funcionarios["CPF_Funcionario"]} | Telefone - {Funcionarios["Fone_Funcionario"]} | Departamento - {Funcionarios["ID_Departamento"]}')
                  


def ListaDepartamentos():

    print("")
    print("Estes sao os departamentos da XYZ")
    print("")

    for Departamentos in xyzDepartamentos:
            
            print(f'Id - {Departamentos["ID_Departamento"]} | Nome - {Departamentos["Nome_Departamento"]} | Sigla - {Departamentos["Sig_Departamento"]}')



def ListaFuncionariosDepartamento():

    print("")
    print("Estes sao os vendedores da XYZ")
    print("")

    for i,Funcionarios in enumerate(xyzFuncionarios):

        if Funcionarios["ID_Departamento"] == "1":
            print(f'{i}. {Funcionarios["Nome_Funcionario"]}')

    print("")
    print("Estes sao os compradores da XYZ")
    print("")

    for i,Funcionarios in enumerate(xyzFuncionarios):

        if Funcionarios["ID_Departamento"] == "2":
            print(f'{i}. {Funcionarios["Nome_Funcionario"]}')

    print("")
                  
