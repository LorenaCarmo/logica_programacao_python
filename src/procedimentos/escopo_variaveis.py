N1 = 5          # fora de qualquer def → escopo GLOBAL
N2 = 3

def Rotina(A, B):
    X = A       # dentro do def → escopo LOCAL
    Y = B
    print(N1, N2, A, B, X, Y)   # aqui as 6 aparecem

Rotina(N1, N2)
print(N1, N2)   # aqui só N1 e N2 aparecem