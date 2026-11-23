# programa que faça o fatorial de um numero

def fat(numero):
    c = 1

  # for i in range(inicio, fim, passo)
    for i in range(1, numero + 1): # Se numero = 5 >>> for i in range(1, 6) >>> laço será de 1 até 5
        c = c * i
    return c

n = int(input('Digite um número: '))

resultado = fat(n)

print(f'O fatorial de {n}! é {fat}')