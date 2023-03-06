a = int(input("digite um numero inteiro a: "))

b = int(input("digite um numero inteiro b: "))

c = a+b or a*b

if a == b:
    c = a + b
    print(f"A soma de a e b é {c}")
else:
    c = a*b
    print(f"A multiplicação de a b é {c}")