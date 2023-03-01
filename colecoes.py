Lista = [1,2,3,4]
Tupla = (1,2,3,4)
Dicionario = {"P":1,"S":2,"T":3,"R":4}

print(type(Lista))
print(type(Tupla))
print(type(Dicionario))

print(len(Lista))
print(len(Tupla))
print(len(Dicionario))

print(Lista[0])
print(Tupla[0])
print(Dicionario["P"])

Aluno = ["Thierry" , 35 , 1.83]
print(Aluno[0], Aluno[1], Aluno[2])
print(f"{Aluno[0]}, tem {Aluno[1]} anos e {Aluno[2]} de altura")

Aluno = ["Jhosephe" , "Thierry", "Andrade"]
Aluno.append("Cacau") # adiciona elemento no final da lista APPEND
print(Aluno) # imprime lista
print(Aluno[1]) # imprime conteúdo do indice posição 2

Aluno = ["Jhosephe" , "Andrade" , "Cacau"]
Aluno.insert(1,"Thierry") # adiciona elemento na posição 2 da lista INSERT
print(Aluno) # imprime lista
print(Aluno[1]) # imprime conteúdo do indice posição 2

Aluno = ["Jhosephe" , "Thierry", "Andrade", "Cacau"]
Aluno.remove("Cacau") # remove elemento no final da lista REMOVE
print(Aluno) # imprime lista
print(Aluno[1]) # imprime conteúdo do indice posição 2

Aluno = ["Jhosephe" , "Thierry", "Andrade", "Cacau"]
Aluno.pop(3) # remove elemento na posição 4 da lista POP
print(Aluno) # imprime lista
print(Aluno[1]) # imprime conteúdo do indice posição 2