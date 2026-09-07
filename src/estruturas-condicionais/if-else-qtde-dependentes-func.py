func = input('Digite o nome do funcionário: ')
sal = float(input('Digite o salário do funcionário: ').replace(',','.'))
dep = int(input('Digite a quantidade de dependentes: '))

if dep == 0:
    aumento = sal * 0.08    
elif dep == 1:
    aumento = sal * 0.10
elif dep == 2:
    aumento = sal * 0.12
else:
    aumento = sal * 0.14

final = sal + aumento
print(f'O aumento do salário com {dep} dependentes, é de: R$ {aumento:.2f}')
print(f'O novo salário de {func} é: R$ {final}')
