# Receba uma temperatura em Farenheit e exiba em gruas Celsius.
# c = 5/9 * (f - 32)

temp_farenheit = float(input("Digite uma temperatura em Farenheit: "))

temp_celsius = (5/9) * (temp_farenheit - 32)

print(f"A temperatura em graus Celsius é {temp_celsius}ºC")