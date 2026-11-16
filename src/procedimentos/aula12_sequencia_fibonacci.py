'''
A sequência de Fibonacci começa com 0 e 1, e cada número seguinte é calculado pela soma dos dois números anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21...

d1 recebe o antigo valor de d2
d2 recebe o resultado da soma (d3)
    > fórmula: d1, d2 = d2, d1 + d2

'''

d1 = 0
d2 = 1

for i  in range(13):
    print(d1)
    d3 = d1 + d2
    d1 = d2
    d2 = d3
    print(d3)
