# Operadores Aritméticos em Python
Os operadores aritméticos são usados para realizar operações matemáticas comuns, como adição, subtração, multiplicação e divisão. Python suporta uma variedade de operadores aritméticos. Vamos ver cada um deles em detalhes:

1. Adição (+):
Soma dois números.
```
a = 5
b = 3
resultado = a + b
print(f"A soma de {a} e {b} é {resultado}")  # Saída: A soma de 5 e 3 é 8
```

2. Subtração (-):
Subtrai o segundo número do primeiro.
```
a = 5
b = 3
resultado = a - b
print(f"A subtração de {b} de {a} é {resultado}")  # Saída: A subtração de 3 de 5 é 2
```

3. Multiplicação (*):
Multiplica dois números.
```
a = 5
b = 3
resultado = a * b
print(f"A multiplicação de {a} e {b} é {resultado}")  # Saída: A multiplicação de 5 e 3 é 15
```

4. Divisão (/):
Divide o primeiro número pelo segundo. A divisão em Python 3 sempre resulta em um float.
```
a = 5
b = 3
resultado = a / b
print(f"A divisão de {a} por {b} é {resultado}")  # Saída: A divisão de 5 por 3 é 1.6666666666666667
```

5. Divisão Inteira (//):
Divide o primeiro número pelo segundo e retorna apenas a parte inteira do quociente.
```
a = 5
b = 3
resultado = a // b
print(f"A divisão inteira de {a} por {b} é {resultado}")  # Saída: A divisão inteira de 5 por 3 é 1
```

6. Módulo (%):
Retorna o resto da divisão do primeiro número pelo segundo.
```
a = 5
b = 3
resultado = a % b
print(f"O resto da divisão de {a} por {b} é {resultado}")  # Saída: O resto da divisão de 5 por 3 é 2
```

7. Exponenciação (**):
Eleva o primeiro número à potência do segundo número.
```
a = 5
b = 3
resultado = a ** b
print(f"{a} elevado a {b} é {resultado}")  # Saída: 5 elevado a 3 é 125
```

## Exemplos Combinados
Vamos ver um exemplo que combina vários operadores aritméticos:
```
a = 10
b = 4

# Adição
soma = a + b
print(f"Soma: {a} + {b} = {soma}")

# Subtração
subtracao = a - b
print(f"Subtração: {a} - {b} = {subtracao}")

# Multiplicação
multiplicacao = a * b
print(f"Multiplicação: {a} * {b} = {multiplicacao}")

# Divisão
divisao = a / b
print(f"Divisão: {a} / {b} = {divisao}")

# Divisão Inteira
divisao_inteira = a // b
print(f"Divisão Inteira: {a} // {b} = {divisao_inteira}")

# Módulo
modulo = a % b
print(f"Módulo: {a} % {b} = {modulo}")

# Exponenciação
exponenciacao = a ** b
print(f"Exponenciação: {a} ** {b} = {exponenciacao}")
```

## Precedência de Operadores
A precedência dos operadores determina a ordem em que as operações são realizadas. Em Python, a ordem de precedência (do mais alto para o mais baixo) é a seguinte:

1. Exponenciação (**)
2. Sinais positivos e negativos unários (+, -)
3. Multiplicação, Divisão, Divisão Inteira e Módulo (*, /, //, %)
4. Adição e Subtração (+, -)
Você pode usar parênteses () para alterar a ordem de avaliação:
```
resultado = (2 + 3) * 4  # Parênteses alteram a precedência
print(f"Resultado com parênteses: {resultado}")  # Saída: Resultado com parênteses: 20

resultado = 2 + 3 * 4  # Sem parênteses, multiplicação ocorre primeiro
print(f"Resultado sem parênteses: {resultado}")  # Saída: Resultado sem parênteses: 14
```
