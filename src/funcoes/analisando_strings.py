'''

len() e .length():              tamanho de uma string.
.upper() e .lower():            transformação de texto.
find() e indexOf():             localização de caracteres.
ord() e chr():                  conversão entre caracteres e códigos.
range() com passo negativo:     repetição decrescente.

'''

nome = input('Digite seu nome: ')

print(f'Total de letras do seu nome: {len(nome)}')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'A primeira letra do seu nome é {nome[0]}')
print(f'A última letra do seu nome é {nome[-1]}')
print(f'Seu nome tem a letra A na posição {nome.upper().find("A") + 1}')
print(f'O código da letra A é {ord("A")}')
print(f'A letra do código 65 é {chr(65)}')

# Percorre o nome de trás para frente, começando pela quantidade de caracteres,
# parando antes de 0 e diminuindo 1 a cada repetição.
for c in range(len(nome), 0, -1):

    # Converte o nome para maiúsculas e acessa a letra correspondente à posição c - 1.
    print(nome.upper()[c - 1], end='')