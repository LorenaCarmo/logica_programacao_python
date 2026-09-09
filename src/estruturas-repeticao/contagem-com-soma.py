# o programa começa em 0, pede o usuario para digitar 10 numeros e no fim soma eles 

contador = 0
soma = 0

while contador < 10:
    numero  = int(input(f'Digite o número {contador + 1}: '))
    soma += numero
    contador += 1

print(f'A soma de todos os números é: {soma}.')
