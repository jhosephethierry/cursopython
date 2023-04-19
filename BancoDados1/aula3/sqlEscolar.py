import psycopg2

try:


    conn = psycopg2.connect(dbname = "Escolar", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()

    print("Conectado")


except(Exception, psycopg2.Error) as error:


    print("Ocorreu um erro,", error)

    
cursor.execute('''

DROP TABLE IF EXISTS "Alunos";

CREATE TABLE "Alunos"(

"NroMatricula" serial,
"Nome" varchar (255) NOT NULL,
"Cpf" varchar (11) NOT NULL,
"Endereço" varchar (255) DEFAULT 'vazio',
"Telefone" varchar (11) DEFAULT 'vazio',
"Ano Nascimento" integer,
PRIMARY KEY ("NroMatricula")

)

''')

conn.commit()

cursor.execute('''

INSERT INTO "Alunos"

VALUES(DEFAULT, 'José', '11111111111', DEFAULT, DEFAULT, 2020)

''')

conn.commit()

cursor.execute('''SELECT * FROM "Alunos"''')

# print(cursor.fetchall())

for aluno in cursor.fetchall():
    print(f"{aluno[0]} - {aluno[1]}")

conn.close()