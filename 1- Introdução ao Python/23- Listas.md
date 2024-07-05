# Listas
As listas são um tipo de estrutura de dados em Python que permitem armazenar múltiplos valores em uma única variável. Elas são uma coleção ordenada e mutável, o que significa que os elementos dentro de uma lista mantêm a ordem e podem ser alterados após a criação da lista.

## Criando Listas
Você pode criar uma lista utilizando colchetes [] e separando os elementos por vírgulas.

### Exemplo 1: Lista Simples
```
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)
```
Saída esperada:
```
[1, 2, 3, 4, 5]
```

## Acessando Elementos da Lista
Os elementos de uma lista podem ser acessados por seu índice, que começa em 0.

### Exemplo 2: Acessando Elementos
```
print(minha_lista[0])  # Acessa o primeiro elemento
print(minha_lista[3])  # Acessa o quarto elemento
```

Saída esperada:
- 1
- 4

## Modificando Elementos da Lista
Você pode modificar um elemento de uma lista atribuindo um novo valor ao índice correspondente.

### Exemplo 3: Modificando Elementos
```
minha_lista[2] = 10
print(minha_lista)
```

Saída esperada:
- [1, 2, 10, 4, 5]

## Adicionando Elementos à Lista
Você pode adicionar elementos a uma lista usando os métodos append(), insert() e extend().

- append(): Adiciona um elemento ao final da lista.
- insert(): Adiciona um elemento em uma posição específica.
- extend(): Adiciona múltiplos elementos ao final da lista.

### Exemplo 4: Adicionando Elementos
```
minha_lista.append(6)
print(minha_lista)

# minha_lista.insert(posicao, valor)
# Se for atribuido um valor para a posição que é maior do que o valor da lista, o elemento é adicionado na última posição
minha_lista.insert(1, 1.5)
print(minha_lista)

minha_lista.extend([7, 8])
print(minha_lista)
```

Saída esperada:
- [1, 2, 10, 4, 5, 6]
- [1, 1.5, 2, 10, 4, 5, 6]
- [1, 1.5, 2, 10, 4, 5, 6, 7, 8]

## Removendo Elementos da Lista
Você pode remover elementos de uma lista usando os métodos remove(), pop(), e del.

- remove(): Remove a *primeira ocorrência* de um valor específico.
- pop(): Remove e retorna o elemento em uma posição específica (por padrão, o último). Caso queira definir uma posição específica o index deve ser informado: pop(x)
- del: Remove o elemento em uma posição específica.

### Exemplo 5: Removendo Elementos
```
minha_lista.remove(1.5)
print(minha_lista)

minha_lista.pop()
print(minha_lista)

del minha_lista[2]
print(minha_lista)
```

Saída esperada:
- [1, 2, 10, 4, 5, 6, 7, 8]
- [1, 2, 10, 4, 5, 6, 7]
- [1, 2, 4, 5, 6, 7]

## Operações com Listas
Listas em Python suportam várias operações e funções embutidas que facilitam a manipulação de dados.

### Exemplo 6: Operações Comuns
```
# Comprimento da lista
print(len(minha_lista))  # 6

# Concatenação de listas
nova_lista = minha_lista + [8, 9, 10]
print(nova_lista)

# Repetição de listas
repetida_lista = [1, 2, 3] * 3
print(repetida_lista)

# Verificação de existência
print(4 in minha_lista)  # True
print(100 in minha_lista)  # False
```

Saída esperada:
- 6
- [1, 2, 4, 5, 6, 7, 8, 9, 10]
- [1, 2, 3, 1, 2, 3, 1, 2, 3]
- True
- False

## Iterando Sobre Listas
Você pode iterar sobre os elementos de uma lista usando um laço for.

### Exemplo 7: Iteração
```
for elemento in minha_lista:
    print(elemento)
```

## Métodos Comuns de Listas
Aqui estão alguns métodos comuns disponíveis para listas em Python:

- append(x): Adiciona um item ao final da lista.
- extend([x, y, z]): Adiciona todos os itens de um iterável ao final da lista.
- insert(i, x): Insere um item em uma posição especificada.
- remove(x): Remove a primeira ocorrência de um item.
- pop([i]): Remove e retorna o item na posição especificada.
- clear(): Remove todos os itens da lista.
- index(x): Retorna o índice da *primeira ocorrência* de um item.
- count(x): Retorna o número de vezes que um item aparece na lista.
- sort(): Ordena os itens da lista.
- sort(reverse=True): Ordena os itens da lista em ordem decrescente. 
- sorted(nome_da_lista): Ordena os itens da lista sem alterar a lista original.
- sorted(nome_da_lista, reverse=True): Ordena os itens da lista em ordem decrescente sem alterar a lista original.
- reverse(): Inverte a ordem dos itens na lista.
- copy(): Retorna uma cópia da lista.

### Exemplo 8: Métodos de Lista
```
minha_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Ordenando a lista
minha_lista.sort()
print(minha_lista)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Revertendo a lista
minha_lista.reverse()
print(minha_lista)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Contando elementos
print(minha_lista.count(5))  # 2

# Índice de um elemento
print(minha_lista.index(4))  # 4
```

# Iterando listas

## Exemplo 1: Iteração Simples
Vamos iterar sobre cada elemento de uma lista e imprimir seu valor.
```
minha_lista = [10, 20, 30, 40, 50]

for elemento in minha_lista:
    print(elemento)
```
Saída esperada:
- 10
- 20
- 30
- 40
- 50

## Exemplo 2: Iteração com Índices
Às vezes, pode ser útil iterar sobre a lista com acesso aos índices dos elementos. Podemos fazer isso utilizando a função 'range()' combinada com 'len()'.
```
minha_lista = [10, 20, 30, 40, 50]

for i in range(len(minha_lista)):
    print(f"Índice {i} tem valor {minha_lista[i]}")
```
Saída esperada:
- Índice 0 tem valor 10
- Índice 1 tem valor 20
- Índice 2 tem valor 30
- Índice 3 tem valor 40
- Índice 4 tem valor 50

## Exemplo 3: Iteração com 'enumerate'
O método 'enumerate' facilita a iteração ao fornecer tanto o índice quanto o valor do elemento.
```
minha_lista = [10, 20, 30, 40, 50]

for i, valor in enumerate(minha_lista):
    print(f"Índice {i} tem valor {valor}")
```
Saída esperada:
- Índice 0 tem valor 10
- Índice 1 tem valor 20
- Índice 2 tem valor 30
- Índice 3 tem valor 40
- Índice 4 tem valor 50

## Exemplo 4: Iteração com Condicionais
Podemos iterar sobre uma lista e aplicar condicionais para filtrar ou modificar os dados.
```
minha_lista = [10, 15, 20, 25, 30]

lista_par = []
lista_impar = []

for elemento in minha_lista:
    if elemento % 2 == 0:
        print(f"{elemento} é par")
        lista_par.append(elemento)
    else:
        print(f"{elemento} é ímpar")
        lista_impar.append(elemento)


print(f"Lista Par: {lista_par}")
print(f"Lista Impar: {lista_impar}")
```
Saída esperada:
- 10 é par
- 15 é ímpar
- 20 é par
- 25 é ímpar
- 30 é par
- Lista Par: [10, 20, 30]
- Lista Impar: [15, 25]

# ---------------

# Listas de Lista
Uma lista de listas, comumente conhecida como matriz, é uma estrutura de dados bidimensional que pode ser usada para representar tabelas, grades ou matrizes matemáticas. Cada elemento da lista principal é, por sua vez, uma lista que pode conter múltiplos elementos.

### Inteirando uma lista de listas com tamanhos diferentes
```
idades[[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15, 16, 17]]

for i in range(0, len(idades)):
    for j in range(0, len(idades[i])):
        print(idades[i][j])
```

## Criando uma Matriz
Você pode criar uma matriz em Python usando listas aninhadas.

### Exemplo 1: Criando uma Matriz
```
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
```
Saída esperada:
- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## Acessando Elementos de uma Matriz
Para acessar elementos de uma matriz, você pode usar dois índices: o primeiro para a linha e o segundo para a coluna.

### Exemplo 2: Acessando Elementos
```
print(matriz[0][0])  # Acessa o elemento na primeira linha, primeira coluna (1)
print(matriz[1][2])  # Acessa o elemento na segunda linha, terceira coluna (6)
print(matriz[2][1])  # Acessa o elemento na terceira linha, segunda coluna (8)
```

## Iterando Sobre uma Matriz
Você pode usar laços for aninhados para iterar sobre todos os elementos de uma matriz.

### Exemplo 3: Iterando Sobre uma Matriz
```for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
```

Saída esperada:
- 1 2 3 
- 4 5 6 
- 7 8 9 

## Modificando Elementos de uma Matriz
Para modificar elementos, você pode acessar o elemento desejado usando índices e atribuir um novo valor.

### Exemplo 4: Modificando Elementos
```
matriz[0][1] = 10
matriz[2][0] = 14

for linha in matriz:
    print(linha)
```

Saída esperada:
- [1, 10, 3]
- [4, 5, 6]
- [14, 8, 9]

## Adicionando e Removendo Linhas ou Colunas
Você pode adicionar novas linhas ou colunas à matriz usando operações de lista.

### Exemplo 5: Adicionando e Removendo Linhas
```
# Adicionando uma nova linha
matriz.append([10, 11, 12])
print(matriz)

# Removendo uma linha
del matriz[1]
print(matriz)
```
Saída esperada:
- [[1, 10, 3], [4, 5, 6], [14, 8, 9], [10, 11, 12]]
- [[1, 10, 3], [14, 8, 9], [10, 11, 12]]

### Exemplo 6: Adicionando e Removendo Colunas
Adicionar ou remover colunas é um pouco mais complicado, pois envolve iterar sobre cada linha.
```
# Adicionando uma nova coluna
for linha in matriz:
    linha.append(0)

print(matriz)

# Removendo uma coluna
for linha in matriz:
    del linha[1]

print(matriz)
```
Saída esperada:
- [[1, 10, 3, 0], [14, 8, 9, 0], [10, 11, 12, 0]]
- [[1, 3, 0], [14, 9, 0], [10, 12, 0]]

### Exemplo 7: Transposta de uma Matriz
A transposta de uma matriz é obtida trocando suas linhas por colunas.
```
transposta = []
for i in range(len(matriz[0])):
    nova_linha = []
    for linha in matriz:
        nova_linha.append(linha[i])
    transposta.append(nova_linha)

for linha in transposta:
    print(linha)
```
Saída esperada:
- [1, 14, 10]
- [3, 9, 12]
- [0, 0, 0]

# ----------------

# Exercício Soma
Receba 10 valores e exiba a soma de todos eles.