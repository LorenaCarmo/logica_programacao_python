# Soma A e B e printa o resultado

n1 = int(input('Digite o primeiro valor para somar: '))
n2 = int(input('Digite o segundo valor para somar: '))

def soma(a, b):
    s = a + b
    return s

resultado = soma(n1,n2)

print(f'A soma dos números digitados é: {resultado}')