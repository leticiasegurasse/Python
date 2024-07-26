# Funções Lambda em Python
As funções lambda, também conhecidas como funções anônimas, são funções simples e pequenas que são definidas sem um nome. Elas são criadas usando a palavra-chave lambda e podem ter qualquer número de argumentos, mas apenas uma expressão. A expressão é avaliada e retornada quando a função é chamada.

## Sintaxe
A sintaxe de uma função lambda é:
```
lambda argumentos: expressão
```
- argumentos: Uma lista de argumentos separados por vírgulas.
- expressão: Uma única expressão que é avaliada e retornada.

## Exemplo Simples
Aqui está um exemplo de uma função lambda que soma dois números:
```
soma = lambda x, y: x + y
resultado = soma(2, 3)
print(resultado)  # Saída: 5
```

## Comparação com Funções Definidas com def
As funções lambda são geralmente usadas para operações simples e rápidas, onde a definição completa de uma função com 'def' seria desnecessária ou excessiva.

### Função com 'def'
```
def soma(x, y):
    return x + y

resultado = soma(2, 3)
print(resultado)  # Saída: 5
```

### Função Lambda
```
soma = lambda x, y: x + y
resultado = soma(2, 3)
print(resultado)  # Saída: 5
```

## Usos Comuns de Funções Lambda
As funções lambda são frequentemente usadas em conjunto com outras funções, como 'map()', 'filter()', e 'sorted()', que aceitam funções como argumentos.

### Exemplo com 'map()'
A função 'map()' aplica uma função a todos os itens em uma lista (ou outro iterável).
```
numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x ** 2, numeros)
print(list(quadrados))  # Saída: [1, 4, 9, 16, 25]
```

## Exemplo com 'filter()'
A função 'filter()' cria uma lista de elementos para os quais uma função retorna True.
```
numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4]
```

## Exemplo com 'sorted()'
A função 'sorted()' retorna uma nova lista ordenada a partir dos elementos de qualquer iterável.
```
pares = [(1, 3), (4, 1), (5, 2), (2, 4)]
ordenado = sorted(pares, key=lambda x: x[1])
print(ordenado)  # Saída: [(4, 1), (5, 2), (1, 3), (2, 4)]
```

## Limitações das Funções Lambda
As funções lambda têm algumas limitações:
- Expressão Única: Elas podem conter apenas uma expressão e não podem incluir várias instruções ou comandos.
- Legibilidade: Funções complexas ou longas são difíceis de ler e entender quando escritas como funções lambda.
- Sem Nome: Elas são anônimas, o que significa que não possuem um nome, tornando a depuração mais difícil.

## Quando Usar Funções Lambda
- Simples e Curto: Quando a função é pequena e simples.
- Uso Único: Quando a função é usada apenas uma vez ou em um contexto específico.
- Operações Temporárias: Quando se deseja passar uma pequena função como argumento para outra função, como map(), filter(), ou sorted().