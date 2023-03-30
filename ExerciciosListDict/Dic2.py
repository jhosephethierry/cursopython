DicionarioPessoa = {
    
    "pNome": "Jhosephe",
    "sNome": "Thierry",
    "tNome": "Andrade",
    "qNome": "Cacau",
    "idade": 35
   
    }

for r in DicionarioPessoa:
    print(r) # imprime chaves

for r in DicionarioPessoa:
    print(DicionarioPessoa[r]) # imprime conteudo das chaves

for r in DicionarioPessoa.keys():
    print(r) # imprime chaves

for r in DicionarioPessoa.values():
    print(r) # imprime chaves

for r1,r2 in DicionarioPessoa.items():
    print(r1,"-",r2) # imprime chaves e valores atribuindo-os a dois recipientes

