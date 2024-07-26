# Geradores em Python
Geradores são uma forma especial de iteradores que permitem a criação de iteráveis de uma maneira mais eficiente e conveniente. Eles permitem a geração de valores sob demanda, ao invés de armazenar todos os valores na memória de uma vez. Isso é especialmente útil quando lidamos com grandes conjuntos de dados ou fluxos de dados infinitos.

## Como Funcionam os Geradores
Os geradores são criados usando uma função que utiliza a palavra-chave yield para retornar valores um por um, suspender a execução da função e lembrar do estado atual até que a função seja chamada novamente.

## Sintaxe Básica
```
def meu_gerador():
    yield valor1
    yield valor2
    yield valor3
```

## Exemplo Simples
```
def contador(maximo):
    contador = 1
    while contador <= maximo:
        yield contador
        contador += 1

# Usando o gerador
for numero in contador(5):
    print(numero)

# Saída
# 1
# 2
# 3
# 4
# 5
```

## Diferenças entre yield e return
- yield: Suspende a execução da função, salva seu estado e retorna um valor ao chamador. Quando a função é chamada novamente, ela retoma de onde parou.
- return: Encerra a execução da função e retorna um valor ao chamador.

## Vantagens dos Geradores
1. Eficiência de Memória: Os geradores produzem valores sob demanda, não armazenando todos os valores na memória de uma vez.
2. Lazy Evaluation: Os valores são calculados apenas quando necessários, evitando cálculos desnecessários.
3. Facilidade de Implementação: A criação de iteradores pode ser mais complexa; os geradores oferecem uma maneira simples de definir iteráveis.

## Exemplo de um Gerador com yield
### Gerador de Números Pares
```
def gerador_pares(limite):
    numero = 0
    while numero <= limite:
        yield numero
        numero += 2

# Usando o gerador
for par in gerador_pares(10):
    print(par)

# Saída
# 0
# 2
# 4
# 6
# 8
# 10
```

## Geradores vs. Funções Normais
Uma função normal retorna um valor e encerra sua execução. Um gerador, ao contrário, pode retornar múltiplos valores, um de cada vez, pausando sua execução entre cada retorno.

### Exemplo de Função Normal vs. Gerador
```
# Função normal que retorna uma lista de quadrados
def quadrados_normais(n):
    resultado = []
    for i in range(n):
        resultado.append(i ** 2)
    return resultado

print(quadrados_normais(5))

# Gerador que retorna quadrados
def quadrados_gerador(n):
    for i in range(n):
        yield i ** 2

for quadrado in quadrados_gerador(5):
    print(quadrado)

# Saída do gerador:
# 0
# 1
# 4
# 9
# 16
```

## Geradores com Expressões Geradoras
Python também oferece uma sintaxe concisa para criar geradores usando expressões geradoras, que são semelhantes às compreensões de lista, mas com parênteses ao invés de colchetes.

### Exemplo de Expressão Geradora
```
gerador = (x ** 2 for x in range(5))

for quadrado in gerador:
    print(quadrado)

# Saída:
# 0
# 1
# 4
# 9
# 16
```
