# o programa começa em 0, pede o usuario para digitar 10 numeros e no fim soma eles 

contador = 0
soma = 0
maior = None
menor = None

while contador < 5:
    numero  = int(input(f'Digite o número {contador + 1}: '))
    soma += numero #soma += numero  é o mesmo que   soma = soma + numero
    contador += 1 # tambem poderia ser contador = contador + 1

    # if maior is None or numero > numero → na primeira volta do loop, maior ainda é None, então essa condição é verdadeira e maior vira o primeiro número digitado. Nas voltas seguintes, só atualiza se o número novo for realmente maior.
    # Se ainda não tenho um maior definido, ou se o número atual é maior que o maior de agora, então esse número vira o novo maior.
    if maior is None or numero > maior:
        # quando tiver o maior numero detectado, a variavel mario guarda o numero
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print(f'A soma de todos os números é: {soma}.')
print(f'O maior número digitado é: {maior}.')
print(f'O menor número digitado é: {menor}.')