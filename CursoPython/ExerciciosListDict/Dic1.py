DicionarioPessoa = {
    
    "pNome": "Jhosephe",
    "sNome": "Thierry",
    "tNome": "Andrade",
    "qNome": "Cacau",
    "idade": 35
   
    }

print(DicionarioPessoa)

r = DicionarioPessoa["pNome"]
print(r)

r = DicionarioPessoa.get("pNome")
print(r)

DicionarioPessoa["idade"] = 36
print(DicionarioPessoa)