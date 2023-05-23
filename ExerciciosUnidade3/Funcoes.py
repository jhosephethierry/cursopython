from classPomar import Pomar

import psycopg2


def consultarBanco(sql):

    conn = psycopg2.connect(dbname = "Pomar", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()

    return resultado
    
def manipularBanco(sql):
        
    conn = psycopg2.connect(dbname = "Pomar", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()

    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()



def verPomar():

    pomar = consultarBanco('''

    SELECT * FROM "Pomar"
    ORDER BY "Id" ASC

    ''')

    if pomar:

        print('''
        
    ______________________________________________________________________________

    Pomar da Fazenda 
    ______________________________________________________________________________

    Estas são as frutas do seu pomar.

    [ Id ]  | Fruta     | Peso      | Estoque       | Data Última Colheita 
    ______________________________________________________________________________

        ''')   

        for fruta in pomar:
            print(f" [ {fruta[0]} ] | {fruta[1]}    | {fruta[2]}    | {fruta[3]}    |{fruta[4]}")
        
        print("")

        breakpoint

        input("Enter para continuar. ")

    else:
        
        print("Seu Pomar está vario.")

        breakpoint

    print("")



def inserirFruta():


    
    nomeFruta = input("Digite o nome da fruta. ")
    pesoFruta = input("Digite o peso. ")
    quantidadeColhida = input("Digite a quantidade colhida. ")

    fruta = Pomar(None, (nomeFruta), float(pesoFruta), int(quantidadeColhida), )

    manipularBanco(fruta.sqlInserirFruta())

    #print(f"Compra de {pedido._quantidade} de {produto._nome} de {produto._sabor} por R$ {pedido._valorTotal} foi cadastrada com sucesso!")

    print("Nova inserida com sucesso!")


    op = input("Quer continuar inserindo frutas? s ou n? ")
    
    match op:

        case "s":
            inserirFruta()
        case "n":
            print("Saindo!")
            breakpoint
        case _:
            print("Digite uma opção válida.")
            print("")   

    
    op = input("Quer visualizar seu Pomar? s ou n? ")
    
    match op:

        case "s":
            verPomar()
        case "n":
            print("Saindo!")
            print("")
            breakpoint
        case _:
            print("Digite uma opção válida.")
            print("")

    breakpoint
