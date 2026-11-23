# programa pede um numero para o usuario e mostra a tabuada dele até 10
# se usar input dentro do while fica: exemplo n 5 = 5 * 1 = 5 (fim) um por um
# se usar input fora do while fica: exemplo n 5 = 5 * 1, 5 * 2, 5 * 3... (fim) todos de uma vez

numero = int(input('Digite um número: '))
contador = 0 # começa calculo no 0

while contador <= 10:
    print(f'{numero} * {contador} = {numero * contador}')
    contador += 1