# Variáveis
Variáveis são usadas para armazenar informações que podem ser referenciadas e manipuladas ao longo do programa. Em Python, a declaração de variáveis é simples e direta, sem necessidade de especificar o tipo de dado que a variável irá armazenar.

## Exemplo:
### Declaração de variáveis
```
nome = "Maria"  # String
idade = 25      # Inteiro
altura = 1.68   # Float
is_estudante = True  # Booleano
```

## ---------------

## Tipos de Dados
Python possui vários tipos de dados integrados. Aqui estão alguns dos mais comuns:

1. Inteiros (int): Números inteiros, positivos ou negativos, sem parte decimal.
    ```
    idade = 25
    ```

2. Flutuantes (float): Números de ponto flutuante, ou seja, números com parte decimal.
    ```
    altura = 1.68
    ```

3. Strings (str): Sequência de caracteres, utilizada para representar texto.
    ```
    nome = "Maria"
    ```

4. Booleanos (bool): Valores lógicos que podem ser True (verdadeiro) ou False (falso).
    ```
    is_estudante = True
    ```

## ---------------

## Formatação de Strings
A formatação de strings pode tornar a saída de dados mais legível e organizada. Python oferece várias maneiras de formatar strings.
1. Concatenação de Strings:
    ```
    nome = "Carlos"
    idade = 30
    mensagem = "Meu nome é " + nome + " e eu tenho " + str(idade) + " anos."
    print(mensagem)
    ```

2. Método str.format():
    ```
    nome = "Carlos"
    idade = 30
    mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
    print(mensagem)
    ```

3. f-strings (Python 3.6+):
    ```
    nome = "Carlos"
    idade = 30
    mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
    print(mensagem)
    ```

## ---------------

# Sobreposição de Valores de Variáveis em Python
A sobreposição de valores de variáveis ocorre quando uma nova atribuição é feita a uma variável existente, substituindo o valor anterior com um novo valor. Em Python, isso é bastante direto devido à sua natureza dinâmica, onde variáveis não têm um tipo fixo e podem ser reassociadas a diferentes tipos de dados ao longo do programa.

## Exemplo de Sobreposição de Variáveis
Vamos observar um exemplo simples:
- Inicialmente, a variável 'x' é atribuída com um valor inteiro
    ```
    x = 10
    print(f"Valor inicial de x: {x}")
    ```

- Sobrescrevendo 'x' com um valor de ponto flutuante
    ```
    x = 5.75
    print(f"Valor de x após sobreposição com float: {x}")
    ```

- Sobrescrevendo 'x' com uma string
    ```
    x = "Olá, mundo!"
    print(f"Valor de x após sobreposição com string: {x}")
    ```

- Sobrescrevendo 'x' com um valor booleano
    ```
    x = True
    print(f"Valor de x após sobreposição com booleano: {x}")
    ```

Neste exemplo, a variável x é inicialmente atribuída com um valor inteiro, depois é sobrescrita com um valor flutuante, uma string e, finalmente, um valor booleano. Em cada etapa, o tipo de x muda para refletir o novo valor atribuído.

## Consequências da Sobreposição
A sobreposição de variáveis pode ser útil, mas também pode levar a confusões se não for bem administrada, especialmente em programas maiores ou mais complexos. Aqui estão alguns pontos a considerar:

- Facilidade de Uso: Permite modificar valores de variáveis conforme necessário ao longo do programa, tornando o código mais flexível.
- Leitura de Código: Pode tornar o código mais difícil de ler se a variável x for usada para armazenar diferentes tipos de dados ao longo do programa. É importante usar nomes de variáveis significativos e comentá-los adequadamente.
- Erros de Tipo: A sobreposição pode levar a erros de tipo se o programador não prestar atenção ao tipo atual da variável.


