DicionarioNumeros = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

dicionarionumerosB = {r for r in DicionarioNumeros}
print(dicionarionumerosB)

dicionarionumerosB = {r: r ** 2 for r in DicionarioNumeros}
print(dicionarionumerosB)

dicionarionumerosB = {r: r ** 2 for r in DicionarioNumeros if r % 2 == 0}
print(dicionarionumerosB)

dicionarionumerosB = {r: r ** 3 for r in DicionarioNumeros}
print(dicionarionumerosB)

dicionarionumerosB = {r: r ** 3 for r in DicionarioNumeros if r % 2 == 0}
print(dicionarionumerosB)