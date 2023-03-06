quantidade = 0
    
for i in range(5):
        numero = int(input("insira um número: "))
        
        if numero >=10 and numero <=50:
            quantidade = quantidade + 1
    
print(f"A quantidade de números dentro do intervalo é ,{quantidade}")