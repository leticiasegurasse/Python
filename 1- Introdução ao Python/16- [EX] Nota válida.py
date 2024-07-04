# Escreva um programa que receba notas de um aluno (0 - 10), caso a nota digitada esteja fora desse intervalo peça para o professor digitar novamente.

nota = int(input("Digite a nota do aluno (0 - 10): "))

while nota > 10 or nota < 0:
    nota = int(input("Valor inválido. Digite novamente (0 - 10): "))

print(f"Nota do aluno armazenada com sucesso: {nota}")


# Outra resolução
while True:
    nota_aluno = int(input("Digite a nota do aluno (0 - 10): "))
    if nota_aluno >= 0 and nota_aluno <= 10:
        print(f"Nota do aluno armazenada com sucesso: {nota}")
        break

    print("Nota Inválida")
    