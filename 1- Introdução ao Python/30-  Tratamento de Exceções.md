# Tratamento de Exceções em Python
Exceções são erros que ocorrem durante a execução de um programa. O tratamento de exceções é o processo de responder a esses erros de maneira controlada, sem que o programa falhe de forma abrupta. Python fornece um mecanismo robusto para lidar com exceções usando os blocos 'try', 'except', 'else' e 'finally'.

## Estrutura Básica
A estrutura básica para o tratamento de exceções em Python é:
```
try:
    # Código que pode causar uma exceção
    pass
except TipoDeExcecao:
    # Código que será executado se ocorrer uma exceção
    pass
else:
    # Código que será executado se nenhuma exceção ocorrer
    pass
finally:
    # Código que será executado sempre, independentemente de exceções
    pass
```

- try: Contém o código que pode gerar uma exceção.
- except: Contém o código que será executado se uma exceção for lançada no bloco try.
- else: (Opcional) Contém o código que será executado se nenhuma exceção ocorrer.
- finally: (Opcional) Contém o código que será executado sempre, independentemente de uma exceção ter sido lançada ou não.

### Exemplo Simples
### Exemplo 1: Divisão por Zero
```
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
else:
    print("Divisão realizada com sucesso.")
finally:
    print("Bloco finally executado.")
```
Saída esperada:
```
Erro: divisão por zero não é permitida.
Bloco finally executado.
```

### Exemplo 2: Conversão de Tipo
```
try:
    numero = int("abc")
except ValueError:
    print("Erro: não é possível converter a string para um número inteiro.")
else:
    print("Conversão realizada com sucesso.")
finally:
    print("Bloco finally executado.")
```
Saída esperada:
```
Erro: não é possível converter a string para um número inteiro.
Bloco finally executado.
```

### Capturando Múltiplas Exceções
Você pode capturar múltiplas exceções usando tuplas ou múltiplos blocos 'except'.
```
try:
    resultado = 10 / 0
except (ZeroDivisionError, ValueError):
    print("Erro: uma divisão por zero ou um valor inválido ocorreu.")
```

### Acessando Detalhes da Exceção
Você pode acessar os detalhes da exceção capturada usando a palavra-chave 'as'.
```
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")
```
Saída esperada:
```
Erro: division by zero
```

### Levantando Exceções
Você pode levantar exceções manualmente usando a palavra-chave 'raise'.
```
def verifica_idade(idade):
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
    return "Idade válida."

try:
    verifica_idade(15)
except ValueError as e:
    print(f"Erro: {e}")  # Saída esperada: Erro: Idade deve ser maior ou igual a 18.
```

### Criando Exceções Personalizadas
Você pode criar suas próprias exceções personalizadas derivando da classe 'Exception'.
```
class MinhaExcecao(Exception):
    pass

def verifica_condicao(condicao):
    if not condicao:
        raise MinhaExcecao("A condição não foi satisfeita.")
    return "Condição satisfeita."

try:
    verifica_condicao(False)
except MinhaExcecao as e:
    print(f"Erro: {e}")  # Saída esperada: Erro: A condição não foi satisfeita.
```

## 'assert'
O comando 'assert' é utilizado para realizar verificações no código, permitindo que você verifique se uma condição é verdadeira durante a execução. Se a condição for falsa, uma exceção 'AssertionError' será levantada. Ele é útil para debugging e testes, ajudando a garantir que seu programa se comporte conforme esperado.

## Sintaxe
A sintaxe básica do 'assert' é:
```
assert condição, mensagem_opcional
```

- condição: Uma expressão que deve ser avaliada como True para que o programa continue executando normalmente.
- mensagem_opcional: Uma mensagem opcional que será exibida se a condição for False.

## Como Funciona
Quando o comando assert é encontrado, o Python avalia a condição:

- Se a condição for True, o programa continua a execução normalmente.
- Se a condição for False, uma exceção AssertionError é levantada e, se fornecida, a mensagem opcional é exibida.

## Exemplos de Uso
Exemplo 1: Sem Mensagem
```
def divide(a, b):
    assert b != 0  # Verifica se b não é zero
    return a / b

# Teste
resultado = divide(10, 2)
print(resultado)  # Saída: 5.0

# Isso irá gerar um AssertionError
resultado = divide(10, 0)  # AssertionError
```

Exemplo 2: Com Mensagem
```
def divide(a, b):
    assert b != 0, "Divisor não pode ser zero."  # Verifica se b não é zero
    return a / b

# Teste
resultado = divide(10, 2)
print(resultado)  # Saída: 5.0

# Isso irá gerar um AssertionError com a mensagem "Divisor não pode ser zero."
resultado = divide(10, 0)  # AssertionError: Divisor não pode ser zero.
```

Exemplo 3: Verificando Tipos
```
def soma_numeros(a, b):
    assert isinstance(a, (int, float)), "a deve ser int ou float"
    assert isinstance(b, (int, float)), "b deve ser int ou float"
    return a + b

# Teste
resultado = soma_numeros(10, 5)
print(resultado)  # Saída: 15

# Isso irá gerar um AssertionError com a mensagem "a deve ser int ou float"
resultado = soma_numeros("10", 5)  # AssertionError: a deve ser int ou float
```



Em Python, existem várias exceções integradas que são classificadas em diferentes tipos com base no tipo de erro que representam. Aqui está uma visão geral das exceções mais comuns:

### Exceções Básicas
- Exception: Classe base para todas as exceções embutidas, exceto para o 'SystemExit', 'KeyboardInterrupt' e 'GeneratorExit'.

### Exceções Comuns
- ArithmeticError: Classe base para erros numéricos.
    - OverflowError: Ocorre quando um cálculo excede o limite permitido.
    - ZeroDivisionError: Ocorre quando um número é dividido por zero.
    - FloatingPointError: Ocorre quando uma operação de ponto flutuante falha.

- AssertionError: Ocorre quando uma afirmação assert falha.

- AttributeError: Ocorre quando um atributo de um objeto não é encontrado.

- BufferError: Ocorre quando uma operação em um buffer falha.

- EOFError: Ocorre quando a função input() atinge o fim de um arquivo sem ler qualquer dado.

- ImportError: Ocorre quando uma importação falha.
    - ModuleNotFoundError: Subclasse de ImportError, ocorre quando um módulo não é encontrado.

- LookupError: Classe base para erros de pesquisa.
    - IndexError: Ocorre quando um índice de sequência está fora do intervalo.
    - KeyError: Ocorre quando uma chave de dicionário não é encontrada.

- MemoryError: Ocorre quando uma operação de memória falha.

- NameError: Ocorre quando uma variável local ou global não é encontrada.
    - UnboundLocalError: Subclasse de NameError, ocorre quando uma variável local é referenciada antes de ser atribuída.

- OSError: Classe base para falhas de sistema.
    - BlockingIOError: Ocorre quando uma operação de E/S bloqueada é detectada.
    - ChildProcessError: Ocorre quando uma operação no processo filho falha.
    - ConnectionError: Classe base para erros de conexão.
        - BrokenPipeError: Ocorre quando uma tentativa de escrita em um pipe quebrado.
        - ConnectionAbortedError: Ocorre quando uma conexão é abortada.
        - ConnectionRefusedError: Ocorre quando uma conexão é recusada.
        - ConnectionResetError: Ocorre quando uma conexão é redefinida.
    - FileExistsError: Ocorre quando uma operação de arquivo falha porque o arquivo já existe.
    - FileNotFoundError: Ocorre quando uma operação de arquivo falha porque o arquivo não foi encontrado.
    - InterruptedError: Ocorre quando uma operação de sistema é interrompida.
    - IsADirectoryError: Ocorre quando uma operação de arquivo falha porque o caminho é um diretório.
    - NotADirectoryError: Ocorre quando uma operação de diretório falha porque o caminho não é um diretório.
    - PermissionError: Ocorre quando uma operação falha devido a permissões insuficientes.
    - ProcessLookupError: Ocorre quando uma operação falha porque o processo não foi encontrado.
    - TimeoutError: Ocorre quando uma operação de sistema expira.

- ReferenceError: Ocorre quando uma referência fraca é usada de forma incorreta.

- RuntimeError: Classe base para erros que não se encaixam em outras categorias.
    - NotImplementedError: Ocorre quando uma operação não é implementada.
    - RecursionError: Ocorre quando o limite de recursão é excedido.

- StopIteration: Ocorre quando a função next() é chamada em um iterador que não possui mais itens.

- StopAsyncIteration: Ocorre quando a função __anext__() de um iterador assíncrono não possui mais itens.

- SyntaxError: Ocorre quando a análise do código fonte falha.
    - IndentationError: Ocorre quando a indentação não é correta.
    - TabError: Ocorre quando a mistura de tabulações e espaços na indentação é incorreta.

- SystemError: Ocorre quando um erro interno no interpretador é detectado, mas a situação não é grave o suficiente para gerar uma SystemExit.

- TypeError: Ocorre quando uma operação ou função é aplicada a um objeto de tipo inapropriado.

- ValueError: Ocorre quando uma operação ou função recebe um argumento com o tipo certo, mas valor inapropriado.

- UnicodeError: Classe base para erros relacionados a codificação/decodificação Unicode.
    - UnicodeEncodeError: Ocorre quando uma codificação Unicode falha.
    - UnicodeDecodeError: Ocorre quando uma decodificação Unicode falha.
    - UnicodeTranslateError: Ocorre quando uma tradução Unicode falha.
