n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('O resultado da soma é {}, o produto é {}, a divisão é {:.3f}, a divisão inteira é {} e a potência é {:.0f}.'.format (s, m, d, di, e))


# end=' ' (faz não quebrar a linha)
# print('O resultado da soma é {}, o produto é {} e a divisão é {:.3f}'.format (s, m, d), end=' ')
# print('O resultado da divisão inteira é {} e a potência é {}'.format (di, e))
# VIRA:
# print('O resultado da soma é {}, o produto é {} e a divisão é {:.3f}'.format (s, m, d))
# print('O resultado da divisão inteira é {} e a potência é {}'.format (di, e))