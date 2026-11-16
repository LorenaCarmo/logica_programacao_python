'''
PARÂMETROS E ARGUMENTOS

- Parâmetros (a, b): variáveis que recebem os valores na função
- Argumentos (x, y): valores enviados ao chamar a função
- A função recebe x=4 e y=8, soma 1 ao primeiro e 2 ao segundo
- As alterações acontecem apenas dentro da função
- Fora dela, x e y continuam com seus valores originais

Parâmetro: é a variável declarada na definição da função, preparada para receber um valor.
Argumento: é o valor enviado para a função no momento da chamada.
    > Resumindo: o parâmetro recebe dado; o argumento fornece dado.
'''

def soma(a, b):                         # a e b são PARÂMETROS
    a = a + 1
    b = b + 2
    print(f'A soma vale {a + b}')

x = 4                                    # x e y são ARGUMENTOS
y = 8

soma(x, y)
print(x, y)