numero = int(input('Digite um numero'))

if numero % 2 == 0:
    print('O número digitado é par!')
else:
    print('O número digitado é ímpar!')


# explicação da logica: 
# % módulo (mostra o resto da divisao)
# == (sinal de igualdade x == y?)
# Se o resto for 0, significa que o número é divisível por 2 → é par.
# Se o resto for 1, sobrou alguma coisa → é ímpar.