# Dicionários em Python
Os dicionários são estruturas de dados em Python que armazenam pares de chave-valor. São mutáveis, o que significa que podem ser modificados após a criação, e não permitem chaves duplicadas. Os dicionários são particularmente úteis quando você precisa associar dados (valores) a chaves únicas de uma maneira que permite acesso rápido.

## Criando um Dicionário
Você pode criar um dicionário usando chaves ({}) e especificando os pares de chave-valor dentro dessas chaves.

### Exemplo 1: Dicionário Simples
```
meu_dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

print(meu_dicionario)  # Saída = {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}
```

## Acessando Valores
Para acessar o valor associado a uma chave específica, você usa a notação de colchetes ('[]').

### Exemplo 2: Acessando Valores
```
nome = meu_dicionario["nome"]
idade = meu_dicionario["idade"]

print(nome)   # Alice
print(idade)  # 25
```

## Adicionando e Modificando Valores
Você pode adicionar novos pares de chave-valor ou modificar valores existentes atribuindo um valor a uma chave específica.

### Exemplo 3: Adicionando e Modificando Valores
```
meu_dicionario["profissao"] = "Engenheira"
meu_dicionario["idade"] = 26

print(meu_dicionario)  # Saida = {'nome': 'Alice', 'idade': 26, 'cidade': 'São Paulo', 'profissao': 'Engenheira'}

```

## Removendo Itens
Você pode remover itens de um dicionário usando o método 'pop()', que remove o item com a chave especificada e retorna seu valor, ou usando a palavra-chave 'del'.

### Exemplo 4: Removendo Itens
```
profissao = meu_dicionario.pop("profissao")
print(profissao)        # Engenheira
print(meu_dicionario)   # {'nome': 'Alice', 'idade': 26, 'cidade': 'São Paulo'}

del meu_dicionario["idade"]
print(meu_dicionario)   # {'nome': 'Alice', 'cidade': 'São Paulo'}
```

## Iterando sobre Dicionários
Você pode iterar sobre as chaves, valores ou pares chave-valor de um dicionário usando loops for.

### Exemplo 5: Iterando sobre Chaves, Valores e Pares Chave-Valor
```
# Iterando sobre as chaves
for chave in meu_dicionario:
    print(chave)

    # Saida
    # nome
    # cidade

# Iterando sobre os valores
for valor in meu_dicionario.values():
    print(valor)

    # Saida
    # Alice
    # São Paulo

# Iterando sobre os pares chave-valor
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
    
    # Saida
    # nome: Alice
    # cidade: São Paulo
```

## Métodos Úteis de Dicionários
Python fornece vários métodos úteis para trabalhar com dicionários.

### Exemplo 6: Métodos Comuns de Dicionários
```
# Obtendo todas as chaves
chaves = meu_dicionario.keys()
print(chaves)  # dict_keys(['nome', 'cidade'])

# Obtendo todos os valores
valores = meu_dicionario.values()
print(valores)  # dict_values(['Alice', 'São Paulo'])

# Obtendo todos os pares chave-valor
itens = meu_dicionario.items()
print(itens)  # dict_items([('nome', 'Alice'), ('cidade', 'São Paulo')])

# Verificando se uma chave está no dicionário
existe = "nome" in meu_dicionario
print(existe)  # True

# Usando o método get para acessar valores com uma chave padrão
cidade = meu_dicionario.get("cidade", "Desconhecida")  # se a chave não existir no dicionário ele retorna "Desconhecida"
print(cidade)  # São Paulo
```

## Dicionários Aninhados
Dicionários podem conter outros dicionários como valores, permitindo a criação de estruturas de dados aninhadas.

### Exemplo 7: Dicionário Aninhado
```
estudantes = {
    "Alice": {
        "idade": 25,
        "cidade": "São Paulo",
        "curso": "Engenharia"
    },
    "Bob": {
        "idade": 23,
        "cidade": "Rio de Janeiro",
        "curso": "Medicina"
    }
}

print(estudantes)
```
Saída esperada:
```
{
    'Alice': {'idade': 25, 'cidade': 'São Paulo', 'curso': 'Engenharia'},
    'Bob': {'idade': 23, 'cidade': 'Rio de Janeiro', 'curso': 'Medicina'}
}
```
