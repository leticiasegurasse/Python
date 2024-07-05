# Receba 10 valores e exiba a soma de todos eles.

lista = [int(input("Digite um número: ")) for i in range(1, 11)]

soma = 0
for i in lista:
    soma += i

print(soma)


# ou usar a função sum
print(sum(lista))
