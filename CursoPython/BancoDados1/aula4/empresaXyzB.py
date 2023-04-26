import psycopg2

try:


    conn = psycopg2.connect(dbname = "EmpresaXyz", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()

    print("Conectado.")


except(Exception, psycopg2.Error) as error:
    

    print("Ocorreu um erro,", error)

