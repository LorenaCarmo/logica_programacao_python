# o programa pergunta um numero para o usuario, e tambem o numero para o salto. Progama conta ate o limite com salto.

contador = 0
limite = int(input('Digite até qual número você quer contar: '))
salto = int(input('Digite qual será o salto: '))

while contador <= limite:
    print(contador)
    contador = contador + salto

print('O programa chegou ao fim.')