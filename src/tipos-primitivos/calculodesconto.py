# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.

preco = float(input('Digite o valor do produto: ').replace(',','.'))
desconto = preco * 5/100
produto = preco - desconto

print(f'O valor final do produto é: R${produto:.2f}.')