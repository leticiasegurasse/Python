# Estrutura de Decisão
Estruturas de decisão permitem que seu programa tome diferentes caminhos com base em certas condições. Python oferece várias formas de implementar estruturas de decisão, as principais sendo if, elif e else.

1. Estrutura if
A estrutura if é usada para executar um bloco de código se uma condição for verdadeira.
```
x = 10

if x > 5:
    print("x é maior que 5")
```
Neste exemplo, a mensagem "x é maior que 5" será exibida porque a condição x > 5 é verdadeira.

2. Estrutura if-else
A estrutura if-else permite executar um bloco de código se a condição for verdadeira e outro bloco se a condição for falsa.
```
x = 3

if x > 5:
    print("x é maior que 5")
else:
    print("x não é maior que 5")
```
Neste caso, a mensagem "x não é maior que 5" será exibida porque a condição x > 5 é falsa.

3. Estrutura if-elif-else
A estrutura if-elif-else permite verificar múltiplas condições. O elif (abreviação de "else if") é usado para verificar condições adicionais se as anteriores forem falsas.
```
x = 7

if x > 10:
    print("x é maior que 10")
elif x > 5:
    print("x é maior que 5 mas menor ou igual a 10")
else:
    print("x é 5 ou menor")
```
Neste exemplo, a mensagem "x é maior que 5 mas menor ou igual a 10" será exibida porque x é 7, e a condição x > 5 é verdadeira.

## Exemplos Práticos
### Exemplo 1: Verificação de Paridade
```
numero = 8

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")
```
Neste exemplo, a mensagem "8 é par" será exibida porque a condição numero % 2 == 0 é verdadeira.

### Exemplo 2: Classificação por Idade
```
idade = 17

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```
Neste caso, a mensagem "Menor de idade" será exibida porque a condição idade >= 18 é falsa.

### Exemplo 3: Avaliação de Notas
```
nota = 85

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
```
Aqui, a mensagem "B" será exibida porque nota é 85, e a condição nota >= 80 é verdadeira.

## Uso de Operadores Lógicos em Estruturas de Decisão
Você pode combinar condições usando operadores lógicos (and, or, not) nas estruturas de decisão.

### Exemplo 4: Verificação de Intervalos
```
x = 15

if x > 10 and x < 20:
    print("x está entre 10 e 20")
else:
    print("x não está entre 10 e 20")
```
Neste caso, a mensagem "x está entre 10 e 20" será exibida porque ambas as condições x > 10 e x < 20 são verdadeiras.

## Aninhamento de Estruturas de Decisão
Você pode aninhar estruturas de decisão, colocando uma estrutura if dentro de outra.

### Exemplo 5: Aninhamento
```
x = 25

if x > 10:
    if x < 20:
        print("x está entre 10 e 20")
    else:
        print("x é maior que 20")
else:
    print("x é 10 ou menor")
```
Neste exemplo, a mensagem "x é maior que 20" será exibida porque a condição x > 10 é verdadeira e x < 20 é falsa.

# ---------------

# Exercício

## Exercício Aprovado/Reprovado:
Receba 4 notas de um aluno e exiba se ele foi APROVADO (nota maior ou igual a 6), se ele ficou de RECUPERAÇÃO (nota maior ou igual a 4) ou se ele foi REPROVADO (nota menor que 4).

## Exercício Maior Número:
Receba 3 números inteiros diferentes e exiba o maior deles.

## Exercício Número Positivo ou Negativo:
Receba um número e exiba se ele é positivo ou negativo.

## Exercício Masculino ou Feminino:
Receba F para feminino e M para masculino e exiba o sexo da pessoa.