# programa que soma dois numeros usando procedimento

def somar(a, b):        # a e b = PARÂMETROS (as vagas)
    resultado = a + b
    print(f'{a} + {b} = {resultado}')
    
x = 5
y = 10

somar(x, y)             # x e y = ARGUMENTOS (o que você entrega)
somar(10, 15)           # 10 e 15 também são argumentos
somar(60, 30)

'''
Outro exemplo
def somar(a, b):        # a e b = PARÂMETROS (as vagas)
    print(a + b)

x = 4
y = 7
somar(x, y)             # x e y = ARGUMENTOS (o que você entrega)
somar(2, 3)             # 2 e 3 também são argumentos
'''