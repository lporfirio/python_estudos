# Laços de repetição + Listas
print('carregando')
print('carregando')
print('carregando')

for palavra in range(1, 4):
    print('carregando')

'''
for item in coleção:
    expressão    
'''

for item in range(1, 21):
    print(item)
for item in range(1, 20, 2):
    print(item)

nomes = ['luke', 'peter', 'liam', 'john', 'serge']
for nome in nomes:
    print(nome)


print('')
# imprima os valores de 1 a N

numero = int(input('Escolha um número positivo: '))
numero2 = 5
valor_inicial = 1

for number in range(valor_inicial, numero + 1):  # range é uma função
    print(number)
