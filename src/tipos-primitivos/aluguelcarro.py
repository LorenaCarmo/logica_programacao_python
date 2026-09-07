# Escreva um programa que pergunte a quantidade de Km percorridos por um 
# carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
# R$0,15 por Km rodado.

km_rodado = int(input('Digite a quantidade de km rodados: '))
qtde_dia = int(input('Por quantos dias usou o carro? '))
pagamento = (qtde_dia * 60) + (km_rodado * 0.15)

print(f'O valor a ser pago na locadora é de: R${pagamento:.2f}.')