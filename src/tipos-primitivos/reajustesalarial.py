# Faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: ').replace(',','.'))
aumento = salario * (15/100)
novo_salario = salario + aumento

print(f'O seu novo salário será: {novo_salario:.2f}')