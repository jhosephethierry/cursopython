from Controle.classConexao import Conexao
import psycopg2

conexaoBanco = Conexao("Abc","localhost","5432","postgres","postgres")

try:

    conexaoBanco.manipularBanco('''

    CREATE TABLE "Cliente"(

    "Id_Cliente" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome_Cliente" varchar(255) NOT NULL

    )

    ''')

    conexaoBanco.manipularBanco('''

    CREATE TABLE "Produto"(

    "Id_Produto" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome_Produto" varchar(255),
    "Preço_Produto" money DEFAULT 0,
    "Estoque_Produto" int

    )

    ''')

except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)

