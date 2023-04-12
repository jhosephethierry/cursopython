import json

with open("BancoDados1/aula2/dep.json", 'r') as xyzJson:
    xyz = json.load(xyzJson)
    xyzFuncionarios = list(xyz['Funcionario'])
    xyzDepartamentos = list(xyz['Departamento'])


def ListaFuncionarios():

    print("")
    print("Estes sao os funcionarios da XYZ")
    print("")

    for Funcionarios in xyzFuncionarios:
            
            print(f'Id - {Funcionarios["ID_Funcionario"]} | Nome - {Funcionarios["Nome_Funcionario"]} | Cpf - {Funcionarios["CPF_Funcionario"]} | Telefone - {Funcionarios["Fone_Funcionario"]} | Departamento - {Funcionarios["ID_Departamento"]}')
                  
ListaFuncionarios()

def ListaDepartamentos():

    print("")
    print("Estes sao os departamentos da XYZ")
    print("")

    for Departamentos in xyzDepartamentos:
            
            print(f'Id - {Departamentos["ID_Departamento"]} | Nome - {Departamentos["Nome_Departamento"]} | Sigla - {Departamentos["Sig_Departamento"]}')

ListaDepartamentos()