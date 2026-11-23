# este exercicio propoe que o usuario entre com um valor, e o programa conte ate esse valor, depois finaliza.

contador = 0
limite = int(input('Digite um valor limite para contagem: '))

while contador <= limite:
    print(contador)
    contador = contador + 1

print('A contagem chegou ao limite. Contador encerrado.')

# contador = 0                 → ponto de partida, igual pediu o exercício
# limite = int(input(...))     → guarda o número que o usuário digitou (convertido para int)
# while contador < limite:     → testa a condição antes de cada repetição
#     print(contador)          → mostra o valor atual do contador
#     contador = contador + 1  → incrementa, se aproximando do limite (evita loop infinito)