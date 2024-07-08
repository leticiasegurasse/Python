# Funções em Python
Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a tornar o código mais modular, legível e fácil de manter. Em Python, as funções são definidas usando a palavra-chave 'def', seguidas pelo nome da função, parênteses e dois pontos. O corpo da função é indentado abaixo da definição.

## Definindo uma Função
A sintaxe básica para definir uma função é:
```
def nome_da_funcao(parametros):
    # Corpo da função
    # Instruções
    return valor_de_retorno
```
- 'nome_da_funcao': O nome da função que será usado para chamá-la.
- 'parametros': (Opcional) Uma lista de parâmetros que a função pode aceitar.
- 'return': (Opcional) A instrução 'return' especifica o valor que a função retorna. Se omitida, a função retorna 'None'.

## Exemplos
### Exemplo 1: Função Sem Parâmetros e Sem Retorno
```
def saudacao():
    print("Olá, mundo!")

# Chamando a função
saudacao()  # Saída esperada: Olá, mundo!
```

### Exemplo 2: Função com Parâmetros
```
def saudacao(nome):
    print(f"Olá, {nome}!")

# Chamando a função com um argumento
saudacao("Alice")  # Saída esperada: Olá, Alice!
```

### Exemplo 3: Função com Retorno
```
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado em uma variável
resultado = soma(3, 5)
print(resultado)  # Saída esperada: 8
```

## Parâmetros Padrão
Você pode definir valores padrão para os parâmetros. Se nenhum argumento for passado para esses parâmetros, os valores padrão serão usados.
```
def saudacao(nome="Mundo"):
    print(f"Olá, {nome}!")

# Chamando a função sem argumentos
saudacao()  # Saída esperada: Olá, Mundo!

# Chamando a função com um argumento
saudacao("Bob")  # Saída esperada: Olá, Bob!
```

## Parâmetros Nomeados
Ao chamar uma função, você pode especificar os parâmetros pelo nome, tornando o código mais legível.
```
def soma(a, b):
    return a + b

# Chamando a função com parâmetros nomeados
resultado = soma(b=5, a=3)
print(resultado)  # Saída esperada: 8
```

## Parâmetros Arbitrários
Você pode definir funções que aceitam um número arbitrário de argumentos usando '*args' para uma lista de argumentos posicional e '**kwargs' para um dicionário de argumentos nomeados.

### Exemplo 1: Usando '*args'
```
def soma(*args):
    return sum(args)

# Chamando a função com múltiplos argumentos
resultado = soma(1, 2, 3, 4)
print(resultado)  # Saída esperada: 10
```

### Exemplo 2: Usando **kwargs
```
def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função com múltiplos argumentos nomeados
exibir_informacoes(nome="Alice", idade=25, cidade="São Paulo")
```
Saída esperada:
```
nome: Alice
idade: 25
cidade: São Paulo
```
