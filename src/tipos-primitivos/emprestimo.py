print('Seja bem-vindo ao Banco L. \nO valor de juros para empréstimo é de 20%.')

emprestimo = float(input('Digite o valor do empréstimo que deseja: ').replace(',','.'))
parcelamento = float(input('Em quantas vezes deseja parcelar? '))
juros = emprestimo * 0.2
totaljuros = juros + emprestimo
parcela = totaljuros / parcelamento
print(f'O valor final do seu empréstimo será R${totaljuros:.2f}. \nO valor da parcela será {parcelamento} vezes de R${parcela:.2f}')