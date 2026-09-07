# Escreva um programa que converta uma temperatura digitando em graus Celsius 
# e converta para graus Fahrenheit.

graus = float(input('Qual a temperatura atual em graus? '))
temperatura = graus * 1.8 + 32
print(f'Está fazendo {temperatura:.1f} graus fahrenheit.')