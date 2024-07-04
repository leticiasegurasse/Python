# Estrutura de Repetição for em Python
A estrutura de repetição for em Python é usada para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou qualquer outro objeto iterável. A sintaxe básica do laço for é:
```
for elemento in sequencia:
    # bloco de código a ser repetido
```

## Uso Básico do for com range()
A função range() é utilizada para gerar uma sequência de números. É frequentemente usada em laços for para iterar sobre uma sequência de números. A função pode ser chamada de várias maneiras, dependendo de quantos argumentos você fornece.

### Sintaxe Básica
```
range(stop)
range(start, stop, step)
```

1. range(stop)
Quando range() é chamado com um argumento, ele gera uma sequência de números de 0 até stop - 1.

### Exemplo 1: Contando de 0 a 4
```
for i in range(5):
    print(i)
```
Saída esperada:
- 0
- 1
- 2
- 3
- 4

Neste exemplo, range(5) gera a sequência de números de 0 a 4.

2. range(start, stop)
Quando range() é chamado com dois argumentos, ele gera uma sequência de números de start até stop - 1.

### Exemplo 2: Dois Argumentos
```
for i in range(2, 7):
    print(i)
```
Saída esperada:
- 2
- 3
- 4
- 5
- 6
Aqui, range(2, 7) gera a sequência de números de 2 a 6.

3. range(start, stop, step)
Quando range() é chamado com três argumentos, ele gera uma sequência de números de start até stop - 1, com um incremento (ou decremento) de step.

### Exemplo 3: Três Argumentos
```
for i in range(1, 10, 2):
    print(i)
```
Saída esperada:
- 1
- 3
- 5
- 7
- 9
Neste exemplo, range(1, 10, 2) gera a sequência de números de 1 a 9, com um incremento de 2.

### Exemplo 4: Decremento com range()
```
for i in range(10, 0, -1):
    print(i)
```
Saída esperada:
- 10
- 9
- 8
- 7
- 6
- 5
- 4
- 3
- 2
- 1
Aqui, range(10, 0, -1) gera a sequência de números de 10 a 1, com um decremento de 1.

## Controle de Fluxo com break e continue
Você pode usar break para interromper o loop antecipadamente e continue para pular o restante do código no loop atual e ir para a próxima iteração.

### Exemplo 5: Uso de 'break'
```
for i in range(10):
    if i == 5:
        break  # Interrompe o loop quando i for igual a 5
    print(i)
```
Saída esperada:
- 0
- 1
- 2
- 3
- 4
Neste exemplo, o loop é interrompido quando 'i' é igual a 5, então o número 5 e os seguintes não são impressos.

### Exemplo 6: Uso de 'continue'
```
for i in range(10):
    if i % 2 == 0:
        continue  # Pula para a próxima iteração se i for par
    print(i)
```
Saída esperada:
- 1
- 3
- 5
- 7
- 9
Aqui, o loop 'for' pula a impressão dos números pares usando 'continue'.

### Exemplo 7: Iterando sobre uma String
```
palavra = "Python"

for letra in palavra:
    print(letra)
```
Saída esperada:
- P
- y
- t
- h
- o
- n

### Exemplo Prático: Tabuada de Multiplicação
Você pode usar um loop for para gerar uma tabuada de multiplicação para um número específico.
```
numero = 7

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```
Saída esperada:
- 7 x 1 = 7
- 7 x 2 = 14
- 7 x 3 = 21
- 7 x 4 = 28
- 7 x 5 = 35
- 7 x 6 = 42
- 7 x 7 = 49
- 7 x 8 = 56
- 7 x 9 = 63
- 7 x 10 = 70
Neste exemplo, o loop 'for' itera de 1 a 10, multiplicando o numero (7) por cada valor de 'i' e imprimindo o resultado.

