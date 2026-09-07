# CRIE UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE EM METROS
# E CALCULE SUA ÁREA + A QTDE DE TINTA EM L A SER UTILIZADA PARA PINTURA
# CONSIDERE QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2m²

altura = float(input('Digite a altura da parede em metros: ').replace(',','.'))
larg = float(input('Agora digite a largura da parede em metros: ').replace(',','.'))
area = altura * larg
tinta = area / 2 
print(f'Para pintar uma parede de {altura}m x {larg}m, a quantidade de tinta necessária é: {tinta} litros.')