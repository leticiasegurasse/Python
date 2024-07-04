# Estrutura de Repetição while
A estrutura de repetição while permite executar um bloco de código repetidamente enquanto uma condição especificada for verdadeira. É útil quando não sabemos antecipadamente quantas vezes o bloco de código deve ser executado. A condição é avaliada antes de cada iteração, e se for True, o bloco de código é executado. Se for False, o loop termina.

## Sintaxe do while
```
while condição:
    # bloco de código a ser repetido
```

## Exemplos de Uso
### Exemplo 1: Contagem Ascendente
```
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # O mesmo que contador = contador + 1
```
Neste exemplo, o loop while continua a executar enquanto contador for menor ou igual a 5. O valor de contador é incrementado em 1 a cada iteração, e o loop imprime o valor atual de contador.

Saída esperada:
- Contador: 1
- Contador: 2
- Contador: 3
- Contador: 4
- Contador: 5

### Exemplo 2: Entrada do Usuário
```
senha = ""

while senha != "segredo":
    senha = input("Digite a senha: ")

print("Senha correta!")
```
Aqui, o loop while continua a solicitar a senha até que o usuário digite "segredo". Quando a condição senha != "segredo" se torna False, o loop termina e imprime "Senha correta!".

### Exemplo 3: Soma de Números Positivos
```
soma = 0
numero = 1

while numero != 0:
    soma += numero
    numero = int(input("Digite um número (-1 para parar de somar): "))

print(f"A soma dos números digitados é: {soma - 1}")
```
Neste exemplo, o loop while continua a solicitar números ao usuário e adiciona-os à variável soma até que o usuário digite -1. Quando -1 é digitado, o loop termina e a soma total é exibida.

## Controle de Fluxo com break e continue
- break: Interrompe o loop imediatamente, independentemente da condição.
- continue: Pula o restante do código no loop atual e vai para a próxima iteração.
### Exemplo 4: Uso de 'break'
```
contador = 1

while contador <= 10:
    if contador == 5:
        break  # Interrompe o loop quando contador for igual a 5
    print(f"Contador: {contador}")
    contador += 1
```
Saída esperada:
- Contador: 1
- Contador: 2
- Contador: 3
- Contador: 4

### Exemplo 5: Uso de 'continue'
```
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Pula para a próxima iteração se o número for par
    print(f"Contador: {contador}")
```
Saída esperada:
- Contador: 1
- Contador: 3
- Contador: 5
- Contador: 7
- Contador: 9

## Exemplo Prático: Jogo de Adivinhação
```
numero_secreto = int(input("Digite um número de 1 a 100: "))
tentativas = 0

print("Tente adivinhar o número secreto entre 1 e 100!")

while True:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1

    if chute < numero_secreto:
        print("Muito baixo!")
    elif chute > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break
```
Neste exemplo, o loop while continua indefinidamente até que o usuário adivinhe o número secreto. Quando o palpite está correto, o loop é interrompido com break.

# ---------------

# Exercício Tabuada:
Receba um número inteiro do usuário e mostre a tabuada de multiplicação desse número (até x10).
