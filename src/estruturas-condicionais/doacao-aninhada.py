frequencia = float(input('Digite a frequência (%): '))
nota = float(input('Digite a nota final: '))

if frequencia >= 75:
    if nota >= 7:
        print('Aprovado')
    else:
        print('Reprovado por nota')
else:
    print('Reprovado por falta')