# Mostre a tabuada completa de todos os números entre 1 e 10.

for i in range(1, 11):
    print(f"---------- Tabuada do número {i} ----------")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")