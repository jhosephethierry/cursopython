import psycopg2

class Conexao:
    def __init__(self, banco, host, port, user, senha):

        self._banco = banco
        self._host = host
        self._port = port
        self._user = user
        self._senha = senha
    
    def consultarBanco(self,sql):

        conn = psycopg2.connect(dbname=self._banco, host=self._host, port=self._port, user=self._user,password=self._senha )
        cursor = conn.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado


    def manipularBanco(self,sql):

        conn = psycopg2.connect(dbname=self._banco, host=self._host, port=self._port, user=self._user,password=self._senha )
        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

        cursor.close()
        conn.close()



def criarTabelaFuncionario():

    sql = '''
    CREATE TABLE "Funcionários"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Salário" money NOT NULL default 0,
    "Id_Dept" int NOT NULL default 1,
    CONSTRAINT fk_departamento
        FOREIGN KEY("Id_Dept")
        REFERENCES "Departamentos"("Id")
        ON DELETE NO ACTION
        ON UPDATE NO ACTION


    )
    
    '''
    return sql

def criarTabelaDepartamento():

    sql = '''
    CREATE TABLE "Departamentos"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL

    )
    
    '''
    return sql

conexaoBanco = Conexao("Empresa Exemplo","localhost","5432","postgres","postgres")

while True:

    try:
        print("Cadastro de Funcionário")
        nomeFunc = input("Digite o nome do Funcionário: ")
        salarioFunc = input("Digite o salário do Funcionário: ")
        idDept = input("Digite o departamento: ")

        conexaoBanco.manipularBanco(f'''
        INSERT INTO "Funcionários"
        VALUES(default, '{nomeFunc}', '{salarioFunc}', '{idDept}' )
        
        ''')

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)