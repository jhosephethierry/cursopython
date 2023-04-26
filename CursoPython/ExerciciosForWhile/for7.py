print("_" * 72)

for x in range(1,11):
    for y in range(1,11):
        if y == 10:
            print(f"|{x * y: > 6d} |")
        else:
            print(f"|{x * y: > 6d}", end= "")

print("_" * 72)