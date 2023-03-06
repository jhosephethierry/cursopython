

codigo = input("digite o codigo do produto: ")

quantidade = int(input("digite a quantidade: "))



if codigo == "100":
    nome = "Cachorro quente" 
    preco = 1.10
elif codigo == "101":
    nome = "Bauru simples" 
    preco = 1.30
elif codigo == "102":
    nome = "Bauru com ovo" 
    preco = 1.50
elif codigo == "103":
    nome = "Hamburguer" 
    preco = 1.10
elif codigo == "104":
    nome = "Cheeseburguer" 
    preco = 1.30
elif codigo == "105":
    nome = "Refrigerante" 
    preco = 1.00



valortotal = preco * quantidade

print(f"você comprou {quantidade} {nome} e o valor total é R$ {valortotal}")

