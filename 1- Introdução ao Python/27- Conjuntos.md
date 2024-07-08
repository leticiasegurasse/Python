# Conjuntos em Python
Os conjuntos (sets) são uma coleção de itens que são não ordenados e não indexados. Eles são definidos pela palavra-chave 'set' ou por '{}' e são particularmente úteis para armazenar itens únicos, evitando duplicatas automaticamente.

## Criando um Conjunto
Você pode criar um conjunto de várias maneiras:

### Exemplo 1: Usando '{}'
```
meu_conjunto = {1, 2, 3, 4}
print(meu_conjunto)  # Saida esperada: {1, 2, 3, 4}
```

### Exemplo 2: Usando set()
```
meu_conjunto = set([1, 2, 3, 4])
print(meu_conjunto)  # Saída esperada: {1, 2, 3, 4}
```

## Características dos Conjuntos
- Elementos Únicos: Todos os elementos em um conjunto são únicos.
- Não Ordenados: Conjuntos não mantêm a ordem dos elementos.
- Mutáveis: Conjuntos podem ter elementos adicionados ou removidos.

## Operações Básicas em Conjuntos
Adicionar Elementos
Você pode adicionar elementos a um conjunto usando o método 'add()'.
```
meu_conjunto = {1, 2, 3}
meu_conjunto.add(4)
print(meu_conjunto)  # Saída esperada: {1, 2, 3, 4}
```

## Remover Elementos
Você pode remover elementos usando 'remove()' ou 'discard()'. A diferença é que 'remove()' lança um erro se o elemento não estiver presente, enquanto 'discard()' não.
```
meu_conjunto = {1, 2, 3}
meu_conjunto.remove(2)
print(meu_conjunto)  # Saída esperada: {1, 3}

meu_conjunto.discard(3)
print(meu_conjunto)  # Saída esperada: {1}
```

## Verificar se um Elemento Existe
Você pode verificar a presença de um elemento em um conjunto usando o operador 'in'.
```
meu_conjunto = {1, 2, 3}
print(2 in meu_conjunto)  # True
print(5 in meu_conjunto)  # False
```

## Operações com Conjuntos
- União
A união de dois conjuntos contém todos os elementos de ambos os conjuntos. Use o operador '|' ou o método 'union()'.
```
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
# ou
uniao = conjunto1.union(conjunto2)

print(uniao)  # Saída esperada: {1, 2, 3, 4, 5}
```

## Interseção
A interseção de dois conjuntos contém apenas os elementos que estão presentes em ambos os conjuntos. Use o operador '&' ou o método 'intersection()'.
```
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

intersecao = conjunto1 & conjunto2
# ou
intersecao = conjunto1.intersection(conjunto2)

print(intersecao)  # Saída esperada: {3}
```

## Diferença
A diferença entre dois conjuntos contém os elementos que estão no primeiro conjunto, mas não no segundo. Use o operador '-' ou o método 'difference()'.
```
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

diferenca = conjunto1 - conjunto2
# ou
diferenca = conjunto1.difference(conjunto2)

print(diferenca)  # Saída esperada: {1, 2}
```

## Diferença Simétrica
A diferença simétrica contém elementos que estão em um dos conjuntos, mas não em ambos. Use o operador '^' ou o método 'symmetric_difference()'.
```
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

dif_simetrica = conjunto1 ^ conjunto2
# ou
dif_simetrica = conjunto1.symmetric_difference(conjunto2)

print(dif_simetrica)  # Saída esperada: {1, 2, 4, 5}
```

## Iterando sobre um Conjunto
Você pode iterar sobre os elementos de um conjunto usando um loop for.
```
meu_conjunto = {1, 2, 3, 4, 5}

for elemento in meu_conjunto:
    print(elemento)
```

## Conjuntos Imutáveis: 'frozenset'
'frozenset' é a versão imutável do 'set'. Uma vez criado, seus elementos não podem ser alterados.
```
meu_frozenset = frozenset([1, 2, 3, 4])
print(meu_frozenset)  # Saída esperada: frozenset({1, 2, 3, 4})
```
