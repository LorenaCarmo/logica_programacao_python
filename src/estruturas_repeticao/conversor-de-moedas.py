# Faça a conversao de moedas 4x

cotacao_dolar = 5.00 
contador = 0
soma_total = 0

while contador < 4:
    valor_real = float(input('Digite um valor em real para ser convertido em dólar: ').replace(',','.'))
    cotacao = valor_real / cotacao_dolar
    print(f'O valor convertido para dólar é: {cotacao:.2f}')

    contador += 1
    soma_total += valor_real

print(f'A soma dos valores em dólares é: {soma_total}')
