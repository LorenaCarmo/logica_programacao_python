'''
Sem end=' ' 
    = resultado do print:
    1
    2
    3

Com end=' '
    = resultado do print:
    1 2 3

# Função que calcula e exibe o próximo número de Fibonacci
def proximo_fibonacci(a, b):
    c = a + b             # Soma os dois números anteriores
    print(c)              # Exibe o resultado
    a = b                 # O primeiro número recebe o valor do segundo
    b = c                 # O segundo número recebe o resultado da soma
    return a, b           # Devolve os dois valores atualizados


# Define os dois primeiros números da sequência
dado1 = 0
dado2 = 1

# Exibe os dois primeiros números
print(dado1, dado2)

# Repete 8 vezes para completar os 10 números da sequência
for c in range(3, 11):
    # Envia os valores à função e recebe os dois valores atualizados
    dado1, dado2 = proximo_fibonacci(dado1, dado2)
'''

def proximo_fibonacci(a, b):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    return a, b

dado1 = 0
dado2 = 1

print(dado1, dado2, end=' ')

for c in range(3, 11):
    dado1, dado2 = proximo_fibonacci(dado1, dado2)