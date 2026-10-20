# usuario digita um numero e o programa mostra se ele é um nº primo

# usuario digita um numero
# programa testa (a partir de 2) se existe algum divisor que deixa resto 0
# se encontrar algum divisor que deixa resto 0 → não é primo
# se não encontrar nenhum divisor que deixa resto 0 → é primo
# imprime resultado do calculo dizendo se é ou não um número primo

n = int(input('Digite um número: '))

if n <= 1:
    print('Este não é um número primo.')
else:
    primo = True

    for i in range(2, n): # testa a partir do 2 até o n (digitado pelo usuario) se tem divisor que resta 0.
        if n % i == 0:
            primo = False
            break
    if primo:
        print('Este é um número primo!')
    else: 
        print('Este não é um número primo!')
