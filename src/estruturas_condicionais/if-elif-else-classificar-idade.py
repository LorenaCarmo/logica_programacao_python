# criança, adulto ou idoso? 

idade = int(input("Digite a sua idade: "))

if idade < 12:
    print('Você é uma criança')
elif idade < 18:
    print('Você é um adolescente')
elif idade < 60:
    print('Você é um adulto(a)')
else:
    print('Você é um idoso(a)')