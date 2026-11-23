'''

Entendendo o código

- def operacao(n): define uma função que recebe um número inteiro.
- n % 2 == 0: verifica se o número é par.
- n ** 2: calcula o quadrado do número, caso seja par.
- n / 2: divide o número por 2, caso seja ímpar.
- return x: devolve o resultado da operação.
- range(1, 4): executa o laço com os valores 1, 2 e 3.
- s = s + operacao(c): acumula os resultados das chamadas da função.

'''

def operacao(n):
    if n % 2 == 0:
        x = n ** 2
    else:
        x = n / 2
    return x

s = 0

for c in range(1, 4):
    s = s + operacao(c)

print(s)

