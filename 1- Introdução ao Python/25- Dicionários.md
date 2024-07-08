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

## Dicionários Contendo Outras Estruturas de Dados
### Exemplo 1: Dicionários com Listas como Valores
```
# Dicionário onde os valores são listas
estudantes_notas = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Carol": [92, 95, 93]
}

# Acessando notas de um estudante
notas_alice = estudantes_notas["Alice"]
primeira_nota_alice = estudantes_notas["Alice"][0]
print(notas_alice)  # [85, 90, 88]
print(primeira_nota_alice)  # 85

# Adicionando uma nova nota para Bob
estudantes_notas["Bob"].append(85)
print(estudantes_notas["Bob"])  # [78, 82, 80, 85]
```

### Exemplo 2: Dicionários com Tuplas como Chaves
```
# Dicionário onde as chaves são tuplas
localizacoes = {
    (40.7128, -74.0060): "Nova York",
    (34.0522, -118.2437): "Los Angeles",
    (51.5074, -0.1278): "Londres"
}

# Acessando uma localização pelo par de coordenadas
cidade = localizacoes[(40.7128, -74.0060)]
print(cidade)  # Nova York
```

## Estruturas de Dados Contendo Dicionários
### Exemplo 3: Lista de Dicionários
```
# Lista de dicionários, cada um representando um estudante
estudantes = [
    {"nome": "Alice", "idade": 25, "curso": "Engenharia"},
    {"nome": "Bob", "idade": 23, "curso": "Medicina"},
    {"nome": "Carol", "idade": 22, "curso": "Arquitetura"}
]

# Acessando informações do primeiro estudante
primeiro_estudante = estudantes[0]
print(primeiro_estudante)  # {'nome': 'Alice', 'idade': 25, 'curso': 'Engenharia'}

# Acessando o curso do segundo estudante
curso_bob = estudantes[1]["curso"]
print(curso_bob)  # Medicina
```

### Exemplo 4: Tupla de Dicionários
```
# Tupla de dicionários
dados_tupla = (
    {"nome": "Alice", "idade": 25},
    {"nome": "Bob", "idade": 23},
    {"nome": "Carol", "idade": 22}
)

# Acessando informações do terceiro elemento
terceiro_elemento = dados_tupla[2]
print(terceiro_elemento)  # {'nome': 'Carol', 'idade': 22}

# Acessando a idade do primeiro elemento
idade_alice = dados_tupla[0]["idade"]
print(idade_alice)  # 25
```

## Usando o Método update em Dicionários Python
O método update é utilizado para atualizar um dicionário com elementos de outro dicionário ou de uma sequência de pares chave-valor. Ele adiciona novas chaves e valores ao dicionário original e, se houver chaves duplicadas, os valores são substituídos pelos novos.

### Sintaxe
```
dicionario.update(outro_dicionario)
```

- outro_dicionario: Pode ser um dicionário ou uma sequência de pares chave-valor (como uma lista de tuplas).

## Exemplos
### Exemplo 1: Atualizando um Dicionário com Outro Dicionário
```
dicionario1 = {"nome": "Alice", "idade": 25}
dicionario2 = {"cidade": "São Paulo", "idade": 26}

dicionario1.update(dicionario2)
print(dicionario1)  # Saída esperada: {'nome': 'Alice', 'idade': 26, 'cidade': 'São Paulo'}
```
Neste exemplo, o valor da chave "idade" foi substituído pelo valor do segundo dicionário (26), e a nova chave "cidade" foi adicionada ao dicionário original.

### Exemplo 2: Atualizando um Dicionário com uma Sequência de Pares Chave-Valor
```
dicionario = {"nome": "Bob", "curso": "Medicina"}

# Sequência de pares chave-valor
novos_valores = [("idade", 23), ("cidade", "Rio de Janeiro")]

dicionario.update(novos_valores)
print(dicionario)  # Saída esperada: {'nome': 'Bob', 'curso': 'Medicina', 'idade': 23, 'cidade': 'Rio de Janeiro'}
```

## Misturando Diferentes Formas de Atualização
Você pode combinar todas as formas mencionadas acima ao usar o método 'update'.
```
dicionario = {"nome": "Dave", "idade": 30}

# Outro dicionário
dicionario_update1 = {"cidade": "Curitiba"}

# Sequência de pares chave-valor
dicionario_update2 = [("profissao", "Engenheiro")]

# Atualizando com diferentes formas
dicionario.update(dicionario_update1)
dicionario.update(dicionario_update2)
dicionario.update(email="dave@example.com")

print(dicionario)  # Saída esperada: {'nome': 'Dave', 'idade': 30, 'cidade': 'Curitiba', 'profissao': 'Engenheiro', 'email': 'dave@example.com'}
```

## Iterar sobre as chaves e valores
Para iterar sobre as chaves e valores em um dicionário Python, você pode usar o método 'items()' do dicionário juntamente com um loop 'for'. O método 'items()' retorna uma visão de pares (chave, valor) que podem ser facilmente iterados. Aqui estão alguns exemplos de como fazer isso:

### Iterando Apenas sobre Chaves
Para iterar apenas sobre as chaves do dicionário, você pode usar um loop for diretamente no dicionário ou utilizar o método keys().
```
meu_dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

# Iterando diretamente sobre as chaves
for chave in meu_dicionario:
    print(chave)

# Iterando usando o método keys()
for chave in meu_dicionario.keys():
    print(chave)
```

### Iterando Apenas sobre Valores
Para iterar apenas sobre os valores do dicionário, use o método 'values()'.
```
meu_dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

for valor in meu_dicionario.values():
    print(valor)
```

### Iterando sobre Chaves e Valores
Para iterar sobre pares chave-valor, use o método 'items()'.
```
meu_dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

for chave, valor in meu_dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")
```

### Exemplo 1: Iterando sobre um Dicionário Aninhado
Dicionários aninhados (dicionários dentro de dicionários) também podem ser iterados.
```
dados_pessoas = {
    "Alice": {"idade": 25, "cidade": "São Paulo"},
    "Bob": {"idade": 23, "cidade": "Rio de Janeiro"},
    "Carol": {"idade": 22, "cidade": "Brasília"}
}

# Iterando sobre o dicionário aninhado
for nome, dados in dados_pessoas.items():
    print(f"Nome: {nome}")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")
```

# ---------------

## Exercício cadastro pessoa
Faça um programa que o usuário possa cadastrar n pessoas, armazenando seu nome, idade e altura
