'''
Para I <- 1 até 5 faça
    Escreva("Digite o nome: ")
    Leia(N)
    Escreva("Digite o peso de ", N, ": ")
    Leia(P)
    Se (P > Mai) então
        MAI <- P
        Pesado <- N
    FimSe
    LimpaTela
    Escreva("DETECTOR DE PESADO")
    Escreva("Maior Peso até agora: ", Mai, "Kg")
FimPara
'''

'''
1. def → criar o procedimento que MOSTRA a mensagem (recebe o maior)
2. maior = 0 (campeão inicial)
3. for (5 voltas):
      ler o peso
      se peso > maior → atualizar maior
      chamar o procedimento
'''

maior = 0

def mostre_o_maior():
    for i in range(5):
    peso = float(input('Digite um peso: '))
    if peso > maior:
        print( f'O maior peso até agora é: {maior} kg!')
    
print(mostre_o_maior)



def mostrar_maior(maior):
    print(f'O maior peso até agora é: {maior} kg!')

maior = 0
for i in range(5):
    peso = float(input('Digite um peso: '))
    if peso > maior:
        maior = peso
    mostrar_maior(maior)