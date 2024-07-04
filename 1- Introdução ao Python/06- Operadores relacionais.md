# Operadores Relacionais em Python
Os operadores relacionais (ou operadores de comparação) são usados para comparar dois valores. O resultado da comparação é sempre um valor booleano (True ou False). Eles são fundamentais para a tomada de decisões em um programa, pois permitem comparar variáveis e valores.

Aqui estão os operadores relacionais disponíveis em Python:

1. Igualdade (==):
Verifica se os valores de dois operandos são iguais.
```
a = 5
b = 5
print(a == b)  # True
```

2. Diferença (!=):
Verifica se os valores de dois operandos são diferentes.
```
a = 5
b = 3
print(a != b)  # True
```

3. Maior que (>):
Verifica se o valor do operando à esquerda é maior que o valor do operando à direita.
```
a = 5
b = 3
print(a > b)  # True
```
4. Menor que (<):
Verifica se o valor do operando à esquerda é menor que o valor do operando à direita.
```
a = 3
b = 5
print(a < b)  # True
```

5. Maior ou igual a (>=):
Verifica se o valor do operando à esquerda é maior ou igual ao valor do operando à direita.
```
a = 5
b = 5
print(a >= b)  # True
```

6. Menor ou igual a (<=):
Verifica se o valor do operando à esquerda é menor ou igual ao valor do operando à direita.
```
a = 3
b = 5
print(a <= b)  # True
```

## Comparando Strings
Os operadores relacionais também podem ser usados para comparar strings, com base na ordem lexicográfica (alfabética).

## Exemplo:
```
str1 = "apple"
str2 = "banana"

print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 < str2)   # True, porque "apple" vem antes de "banana" na ordem alfabética
print(str1 > str2)   # False
```

# ---------------

# Diferença entre = e == 

1. Operador de Atribuição (=):
O operador = é usado para atribuir um valor a uma variável.
Ele coloca o valor do lado direito na variável do lado esquerdo.
## Exemplo de Atribuição (=)
```
# Atribuindo valores a variáveis
x = 5   # O valor 5 é atribuído à variável x
y = 10  # O valor 10 é atribuído à variável y
```
## Saída esperada:
```
x: 5, y: 10
```

2. Operador de Igualdade (==):
O operador == é usado para comparar dois valores.
Ele verifica se os valores dos operandos à esquerda e à direita são iguais e retorna um valor booleano (True ou False).
## Exemplo de Comparação de Igualdade (==)
```
a = 5
b = 5
c = 10

# Comparando se os valores de a e b são iguais
print(a == b)  # True, porque ambos são 5

# Comparando se os valores de a e c são iguais
print(a == c)  # False, porque 5 não é igual a 10
```
## Saída esperada:
```
True
False
```

## Exemplo: Comparando e Atribuindo
```
# Comparação e atribuição
x = 2 > 5
print(f"x = 2 > 5: {x}")  # False, porque 2 não é maior que 5

y = 10 == 10
print(f"y = 10 == 10: {y}")  # True, porque 10 é igual a 10

z = 3 != 3
print(f"z = 3 != 3: {z}")  # False, porque 3 é igual a 3, então não é diferente

a = 7 < 12
print(f"a = 7 < 12: {a}")  # True, porque 7 é menor que 12

b = 15 >= 15
print(f"b = 15 >= 15: {b}")  # True, porque 15 é igual a 15, então é maior ou igual

c = 5 <= 3
print(f"c = 5 <= 3: {c}")  # False, porque 5 não é menor ou igual a 3
```

