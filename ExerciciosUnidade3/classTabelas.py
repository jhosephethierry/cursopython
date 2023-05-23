from classConexao import Conexao
import psycopg2

conexaoBanco = Conexao("Pomar", "localhost", "5432", "postgres", "postgres")

def criarTabelas():

    conexaoBanco.manipularBanco('''

    CREATE TABLE "Pomar"(
    
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Fruta" varchar(255) NOT NULL,
    "Peso" double precision NOT NULL default 0,
    "Estoque" int NOT NULL default 0,
    "Data Colheita" timestamp default CURRENT_TIMESTAMP(0)

    )
    
    ''')

criarTabelas()