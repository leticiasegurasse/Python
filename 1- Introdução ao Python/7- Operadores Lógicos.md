# Operadores Lógicos
Os operadores lógicos são usados para combinar expressões booleanas. Python oferece três operadores lógicos principais: and, or e not. Eles permitem construir expressões lógicas mais complexas a partir de expressões simples.

1. Operador 'and'
O operador and retorna True se ambas as expressões forem verdadeiras. Caso contrário, retorna False.
```
# Exemplo de uso do operador 'and'
a = True
b = False

resultado = a and b
print(f"{a} and {b} = {resultado}")  # Saída: False, porque b é False

# Exemplo prático
idade = 25
possui_carteira = True

pode_dirigir = (idade >= 18) and possui_carteira
print(f"Pode dirigir: {pode_dirigir}")  # Saída: True, porque ambas as condições são verdadeiras
```

2. Operador 'or'
O operador or retorna True se pelo menos uma das expressões for verdadeira. Retorna False apenas se ambas as expressões forem falsas.
```
# Exemplo de uso do operador 'or'
a = True
b = False

resultado = a or b
print(f"{a} or {b} = {resultado}")  # Saída: True, porque a é True

# Exemplo prático
tem_experiencia = False
tem_diploma = True

pode_concorrer_vaga = tem_experiencia or tem_diploma
print(f"Pode concorrer à vaga: {pode_concorrer_vaga}")  # Saída: True, porque tem_diploma é True
```

3. Operador 'not'
O operador not inverte o valor lógico de uma expressão. Se a expressão for verdadeira, not a torna falsa, e vice-versa.
```
# Exemplo de uso do operador 'not'
a = True

resultado = not a
print(f"not {a} = {resultado}")  # Saída: False, porque 'not True' é False

# Exemplo prático
esta_chovendo = False

nao_vai_sair = not esta_chovendo
print(f"Não vai sair: {nao_vai_sair}")  # Saída: True, porque não está chovendo
```

## Exemplo Combinado
Você pode combinar operadores lógicos para formar expressões complexas.
```
# Exemplo combinado de operadores lógicos
idade = 20
possui_carteira = True
esta_sob_efeito_alcool = False

# Pode dirigir se tiver carteira e não estiver sob efeito de álcool
pode_dirigir = (idade >= 18) and possui_carteira and not esta_sob_efeito_alcool
print(f"Pode dirigir: {pode_dirigir}")  # Saída: True, porque todas as condições são verdadeiras
```

## Precedência de Operadores Lógicos
A precedência dos operadores lógicos determina a ordem em que as expressões são avaliadas:

1. not: Tem a maior precedência.
2. and: Tem a segunda maior precedência.
3. or: Tem a menor precedência.

### Exemplo com precedência:
```
# Precedência de operadores lógicos
a = True
b = False
c = True

# 'not' é avaliado primeiro, depois 'and', e por fim 'or'
resultado = a or b and not c
print(f"{a} or {b} and not {c} = {resultado}")  # Saída: True, porque 'not c' é False, e 'b and False' é False, então 'a or False' é True
```

Para evitar confusão e garantir a clareza, é uma boa prática usar parênteses para agrupar expressões e definir explicitamente a ordem de avaliação:
```
# Usando parênteses para definir a ordem de avaliação
resultado = (a or b) and (not c)
print(f"({a} or {b}) and (not {c}) = {resultado}")  # Saída: False, porque 'a or b' é True, e 'not c' é False, então 'True and False' é False
```
