listanumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
listanumerosB = [r for r in listanumeros if r % 2 == 0]
print(listanumerosB)

listanumerosB = [r ** 2 for r in listanumeros]
print(listanumerosB)

listanumerosB = [r ** 2 for r in listanumeros if r % 2 == 0]
print(listanumerosB)

listanumerosB = [r for r in listanumeros if r % 2 != 0]
print(listanumerosB)

listanumerosB = [r ** 3 for r in listanumeros]
print(listanumerosB)

listanumerosB = [r ** 3 for r in listanumeros if r % 2 == 1]
print(listanumerosB)

