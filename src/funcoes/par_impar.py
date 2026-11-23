# verifique se um numero é par ou impar

'''
Algoritmo:

- Função
- Condição dentro da funçao 
- Chamada da função
- Solicitar um dado de entrada
- Retornar msg com o resultado
'''

def par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'


n1 = int(input('Digite um número: '))

print(f'O número {numero} é um valor {par_impar(numero)}.')

# outra forma:
# print(par_impar(n1))

'''
Outras formas de entradas de dados: 

print(par_impar(10))
print(par_impar(33))
print(par_impar(12))
print(par_impar(25))
'''