# programa que mostra se o número é negativo

contador = 0

while True:
    numero = float(input('Digite um número positivo ou negativo: '))
    
    if numero < 0:
        print('O número é negativo!')
        break
    elif numero > 0:
        print('O número é positivo!')
        break
    else:
        print('O número é zero!')
        break