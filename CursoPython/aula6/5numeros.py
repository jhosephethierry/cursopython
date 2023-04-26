
for i in range(5):
        numero = int(input("insira um número: "))

        if i == 0:
            menor = numero
        else:
            if numero < menor:
                menor = numero

print(f"o menor numero é {menor}")

