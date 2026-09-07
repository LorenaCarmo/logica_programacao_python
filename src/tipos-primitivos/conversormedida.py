# CRIE UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS 

v1 = float(input('Digite um valor em metros para a conversão: ').replace(',','.'))
cm = v1 * 100
mm = v1 * 1000
print(f'{v1} metros é equivalente a {cm} centímetros, e {mm} milímetros.')
