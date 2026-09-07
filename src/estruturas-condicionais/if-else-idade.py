# PROGRAMA QUE DESCOBRE A IDADE POR ANO NASC E ANO ATUAL

anoatual = int(input('Digite o ano atual: '))
anonasc = int(input('Digite o ano em que você nasceu: '))
idade = anoatual - anonasc

if idade >= 18:
    print(f'Sua idade é {idade}. Você já é maior de idade.')
else:
        print(f'Sua idade é {idade}.Você ainda não é maior de idade.')