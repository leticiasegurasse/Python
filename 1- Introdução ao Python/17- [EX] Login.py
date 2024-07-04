# Defina um usuário e senha e depois tente "logar" verificando se o login e senha são válidos

USUARIO = "leticia"
SENHA = "senha123"

while True:
    logar_usuario = input("Digite seu usuário: ")
    logar_senha = input("Digite sua senha: ")

    if logar_usuario == USUARIO and logar_senha == SENHA:
        print("Login feito com sucesso!")
        break
        
    print("Usuário ou senha inválido! Tente novamente.")
    

