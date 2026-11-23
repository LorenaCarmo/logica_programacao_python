# exercicio que proproe trocar o numero e acrescer +1 ate que chegue em um limite pre definido

mao = 0

while mao <= 10:
    print('Troca', mao)
    mao = mao + 1

print('O limite 10 foi atingido, laço encerrado!') 


# Explicando a logica:
# mao = 0                → ponto de partida ("mão <- 0")
# while mao < 10:        → testa a condição antes de cada repetição
# print('Troca:', mao)   → executa a "ação" do laço
# mao = mao + 1          → incrementa +1 (sem essa linha, entra em loop infinito)

# estrutura utilizada: WHILE
# while: testa a condição, executa o bloco, testa de novo, executa de novo... até a condição virar falsa.

# para cazer contagem reversa, basta trocar o sinal de comparação e iniciar a variável com o valor máximo, decrementando -1 a cada repetição.