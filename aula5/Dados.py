dados = {"Nome":'John',"Último Nome":'James',"idade":'20',"Curso":'Matemática',"Endereço":'Avenida A'}

print(dados.items())

print(dados["Nome"])
print(dados["Último Nome"])
print(dados["Idade"])
print(dados["Curso"])
print(dados["Endereço"])

del (dados["Curso"])

dados["Último Nome"] = 'Lopes'

print(dados.items())

print(dados["Endereço"])

dadosB = dados.copy()

dadosB["Nome"] = 'Maria'
dadosB["Idade"] = '22'

print(dadosB.items())
