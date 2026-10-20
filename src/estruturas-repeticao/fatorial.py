# pergunta um numero pro usuario e faz o fatorial dele.

# logica:
# pergunta o numero para o usuario
# variavel que armazena resultados
# repete as multiplicaçoes até chegar 1
# mostra o resultado

# obs.: fatorial de 0 é sempre 1

continuar = 's'

while continuar == 's':
    numero = int(input('Digite um número maior ou igual a 1: '))
    fatorial = 1
        
    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1

    print(f'O fatorial do número digitado é: {fatorial}\n')

    continuar = input('Deseja continuar? (s/n): ').lower()

    if continuar == 's':
       print('Certo! Vamos fazer o fatorial de outro número.')
    elif continuar == 'n':
      print('Ok. Encerrando programa...')