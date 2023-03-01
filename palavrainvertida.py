palavra = input("digite uma palavra: ")

print(palavra [::-1])

palavrainvertida = ""

for i in range(len(palavra)):
    
    palavrainvertida = palavrainvertida + palavra[len(palavra)-1-i]
    
    print(palavrainvertida)