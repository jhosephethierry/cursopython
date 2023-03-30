DicionarioPessoa = {
    
    "pNome": "Jhosephe",
    "sNome": "Thierry",
    "tNome": "Andrade",
    "qNome": "Cacau",
    "idade": 35
   
    }

print(len(DicionarioPessoa))

print(DicionarioPessoa)

DicionarioPessoa["pais"] = "Brasil"
print(DicionarioPessoa)

print(len(DicionarioPessoa))

DicionarioPessoa.pop("pais")
print(DicionarioPessoa)

DicionarioPessoa["pais"] = "Brasil"
print(DicionarioPessoa)

del DicionarioPessoa["pais"]
print(DicionarioPessoa)