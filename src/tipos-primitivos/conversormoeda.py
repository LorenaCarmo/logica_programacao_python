# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO TEM NA CARTEIRA
# E CONVERTA ESSE VALOR EM DOLAR 

# recebendo dados em reais
real = float(input('Digite a quantidade em reais que você possui: '))

# declarando valor do dolar
cotacao = 5.50

# calculo
conversao_real = real / cotacao

# saida dos dados 
print(f'R${real:.2f} equivalem a: US${conversao_real:.2f} de dólares.')