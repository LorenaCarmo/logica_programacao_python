n = int(input('Digite um número para ver sua tabuada: '))

print(f'{n} x 1 = {n * 1}')
print(f'{n} x 2 = {n * 2}')
print(f'{n} x 3 = {n * 3}')
print(f'{n} x 4 = {n * 4}')
print(f'{n} x 5 = {n * 5}')
print(f'{n} x 6 = {n * 6}')
print(f'{n} x 7 = {n * 7}')
print(f'{n} x 8 = {n * 8}')
print(f'{n} x 9 = {n * 9}')
print(f'{n} x 10 = {n * 10}')


# OUTRAS FORMAS:

# for i in range:

# n = int(input('Digite um número para ver sua tabuada: '))
# for i in range(1,11):
#     print(f'{n} x {i} = {n*1}')

# ------------------

# while:

# n = int(input('Digite um número: '))

# i = 1

# while i <= 10:
   # print(f'{n} x {i} = {n * i}')
    # i += 1

# ------------------

# lista:

# n = int(input('Digite um número: '))
# tabuada = [n * i for i in range(1, 11)]
# print(tabuada)