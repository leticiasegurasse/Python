# Faça um programa que o usuário possa cadastrar n pessoas, armazenando seu nome, idade e altura

pessoas = []

while True:
    opcao = int(input("Digite 1 para cadastrar uma pessoa ou 0 para sair: "))

    if opcao == 0:
        print("Programa finalizado!")
        break
    elif opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))

        pessoas.append(
            {"nome": nome, 
            "idade": idade, 
            "altura": altura})
    else:
        print("Opção inválida")

print(pessoas)