def contaletras(palavra,letra):
    
    contador = 0
    
    for l in palavra:
        if l.lower() == letra.lower():
            contador += 1
            
    return contador

pal = input("digite o texto: ")
let = input("digite uma letra do texto digitada: ")

contagem = contaletras(pal,let)

print(f"a letra {let} aparece {contagem} vezes na palavra {pal}")
