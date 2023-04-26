itens = [3,56,33,77,88,11,333,"j",None]    

somaItens = 0
quantidadeItens = 0

for r in itens:
    
    if type(r) != int and type(r) != float:

        continue

    somaItens += r
    quantidadeItens += 1

media = somaItens / quantidadeItens

print("a media é", media)