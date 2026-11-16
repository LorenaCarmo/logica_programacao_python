def operacao(n):
    if n % 2 == 0:
        x = n ** 2
    else:
        x = n / 2
    return x

# variavel acumuladora que começa em 0    
s = 0

# range(inicio, fim) (1,4) (1,2,3)
for c in range(1, 4):
    s = s + operacao(c) # o valor de c é passado para o parâmetro n quando a função é chamada.

print(s)