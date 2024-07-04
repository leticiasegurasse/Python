# Receba F para feminino e M para masculino e exiba o sexo da pessoa.

sexo = input("Digite 'F' para feminino ou 'M' para masculino: ")

if sexo == "F" or sexo == "f":
    print("Você é do sexo FEMININO")
elif sexo == "M" or sexo == "m":
    print("Você é do sexo MASCULINO")
else:
    print("Opção inválida")