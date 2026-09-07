real = float(input('O valor do imposto é de 60% sobre o total da compra. Digite o valor total da compra em R$: '))
imposto = real * 60 / 100 # ou real * 0,6
total = imposto + real
print(f'O valor de imposto sobre a compra é de R${imposto}.')
print(f'O valor final da compra com imposto é de: R${total}')