# Exiba todos os números pares entre 1 e 1000 usando o for.

for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

# Outra forma
for i in range(2, 1001, 2):
    print(i)