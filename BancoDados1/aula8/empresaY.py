import psycopg2


# def criarTabelaFuncionario():

    
#     sql = ('''

#     CREATE TABLE "Funcionarios"(

#     "Func_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     "Func_nome" varchar(255),
#     "Func_cpf" char(11) UNIQUE NOT NULL,
#     "Func_salario" money,
#     "Dept_id"  int,
#     CONSTRAINT fk_departamento
#     FOREIGN KEY ("Dept_id")
#     REFERENCES "Departamentos"("Dept_id")

#     )

#     ''')
    
#     return sql


# def criarTabelaDepartamento():

    
#     sql = ('''

#     CREATE TABLE "Departamentos"(

#     "Dept_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     "Dept_nome" varchar(255)

#     )

#     ''')
    
#     return sql


# try:


#     conn = psycopg2.connect(dbname = "EmpresaY", host = "localhost", port = "5432", user = "postgres", password = "postgres")

#     cursor = conn.cursor()

#     cursor.execute(criarTabelaDepartamento())

#     conn.commit()

#     cursor.execute(criarTabelaFuncionario())

#     conn.commit()

#     print("Conectado")

#     conn.close()

#     print("Desconectado")


# except(Exception, psycopg2.Error) as error:


#     print("Ocorreu um erro,", error)