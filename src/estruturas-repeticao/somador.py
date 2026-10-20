# programa que pede numeros para o usuario e soma eles no fim.

# acumulador
soma = 0 

# condiçao + repetição (while + true) & pausa (if + break)
while True:
    numero = float(input('Digite um número para somar: '))
    soma = soma + numero

    continuar = input('Deseja adicionar mais um número? (s/n): ').lower()

    if continuar == 'n':
        break

print(f'A soma dos números digitados é: {soma}')