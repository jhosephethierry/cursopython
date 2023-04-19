import psycopg2


def criarTabelaFuncionario():

    
    sql = ('''

    CREATE TABLE "Funcionários"(

    "Id_Funcionário" serial,
    "Nome_Funcionário" varchar (255) NOT NULL,
    "Salário_Funcionário" money DEFAULT 0,
    "Cargo_Funcionário" varchar (255) NOT NULL DEFAULT 'vazio',
    "Id_Departamento" integer  DEFAULT 1,

    PRIMARY KEY ("Id_Funcionário")

    )

    ''')
    
    return sql


def criarTabelaDepartamento():

    
    sql = ('''

    CREATE TABLE "Departamentos"(

    "Id_Departamento" serial,
    "Nome_Departamento" varchar (255) NOT NULL,
    
    PRIMARY KEY ("Id_Departamento")

    )

    ''')
    
    return sql


try:


    conn = psycopg2.connect(dbname = "EmpresaXyz", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()

    cursor.execute(criarTabelaFuncionario())

    conn.commit()

    cursor.execute(criarTabelaDepartamento())

    conn.commit()

    print("Conectado")

    conn.close()

    print("Desconectado")


except(Exception, psycopg2.Error) as error:


    print("Ocorreu um erro,", error)

