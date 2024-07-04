# Receba 4 notas de um aluno e exiba se ele foi APROVADO (nota maior ou igual a 6), se ele ficou de RECUPERAÇÃO (nota maior ou igual a 4) ou se ele foi REPROVADO (nota menor que 4).

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print("APROVADO")
elif media >= 4:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")

print(f"Sua média: {media}")
