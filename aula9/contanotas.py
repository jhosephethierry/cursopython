numero = int(input("digite o valor do saque: "))

cem = int(numero / 100)
numero = numero % 100

cinquenta = int(numero/50)
numero = numero % 50

vinte = int(numero/20)
numero = numero % 20

dez = int(numero/10)
numero = numero % 10

cinco = int(numero/5)
numero = numero % 5

dois = int(numero/2)
numero = numero % 2

um = numero

def main():
    
    if cem > 0:
        print('Notas R$100,00 = ',cem)
    if cinquenta > 0:
        print('Notas R$ 50,00 = ',cinquenta)
    if vinte > 0:
        print('Notas R$ 20,00 = ',vinte)
    if dez > 0:
        print('Notas R$ 10,00 = ',dez)
    if cinco > 0:
        print('Notas R$ 5,00 = ',cinco)
    if dois > 0:
        print('Notas R$ 2,00 = ',dois)
    if um > 0:
        print('Notas R$ 1,00 = ',um)
    
main()