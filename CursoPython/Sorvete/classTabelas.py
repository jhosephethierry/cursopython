from classConexao import Conexao
import psycopg2

conexaoBanco = Conexao("Sorvete", "localhost", "5432", "postgres", "postgres")

def criarTabelas():

    conexaoBanco.manipularBanco('''

    CREATE TABLE "Clientes"(
    
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL
    
    )
    
    ''')

    conexaoBanco.manipularBanco('''

    CREATE TABLE "Produtos"(
    
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Peso" varchar(255) NOT NULL,
    "Preço" numeric(2) NOT NULL default 0,
    "Estoque" int NOT NULL default 0
    
    )
    
    ''')

    conexaoBanco.manipularBanco('''

    CREATE TABLE "Pedidos"(
    
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Id_Cliente" int,
    "Id_Produto" int,
    "Quantidade" int NOT NULL default 1,
    "Valor Total" numeric(2) NOT NULL,
    "Horário" timestamp default CURRENT_TIMESTAMP(0),
    CONSTRAINT fk_cliente
        FOREIGN KEY("Id_Cliente")
        REFERENCES "Clientes"("Id")
        ,
    CONSTRAINT fk_produto
        FOREIGN KEY("Id_Produto")
        REFERENCES "Produtos"("Id")

    )
    
    ''')

    print("Tabelas cadastradas!")

criarTabelas()