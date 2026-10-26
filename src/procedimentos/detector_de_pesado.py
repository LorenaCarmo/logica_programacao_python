'''
algoritmo:
cria uma lista vazia
passa um laço de x vezes pedindo o input e guarda ela na lista
coloca os pesos em ordem na lista
pega o peso em questao (maior)
mostra o maior

procedimento: serve para quando voce tem uma rotina que se repete. Daí, não precisa deixar o código imenso repetindo aquele bloco, declara ele uma vez, e dps chama ele para repetir.
'''

pesos = []
for i in range(5): # laço / loop
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
pesos.sort()
print('===================================')
print(f'O maior peso digitado foi: {pesos[-1]} kg!')
print('===================================')