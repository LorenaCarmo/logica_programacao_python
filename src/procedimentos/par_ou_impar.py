# programa diz se numero é par ou impar, usando procedimento

def verificar(n):
    if n % 2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} é ímpar!')

verificar(10)
verificar(5)
verificar(0)


'''
Pedindo um numero para o usuario:

def verificar(n):
    if n % 2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} é ímpar!')

        n = int(input('Digite um número inteiro: '))
verificar(n)
'''