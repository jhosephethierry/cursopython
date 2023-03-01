palavraA = input("digite uma palavra: ")

palavraB = input("digite uma palavra: ")

string = list(palavraA), list(palavraB) 

print(string)

palavraAinicial = palavraA[0:2] # primeira e segunda letra

palavraBinicial = palavraB[0:2] # primeira e segunda letra

palavraAfinal = palavraA[2::] # caracteres após a segunda letra

palavraBfinal = palavraB[2::] # caracteres após a segunda letra

print(f"{palavraBinicial}{palavraAfinal} {palavraAinicial}{palavraBfinal}")
