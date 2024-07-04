# Receba um número inteiro do usuário e mostre a tabuada de multiplicação desse número (até x10).

num = int(input("Digite um número: "))

contador = 0

while contador <= 10:
    print(f"{contador} x {num} = {num * contador}")
    contador += 1

