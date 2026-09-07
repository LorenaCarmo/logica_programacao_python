# faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as infos dele

a = (input('Digite algo: '))

print('O tipo primitivo que você digitou é: ', type(a))
print('É um número?', a.isnumeric())
print('Só tem espaços?', a.isspace())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('É maiúsculo?', a.isupper())
print('É minúsculo?', a.islower())
print('É capitalizado??', a.istitle())

# utilizamos o type para descobrir o tipo
# input sempre retorna str
# capitalizado é maiusculo seguido de minusculos