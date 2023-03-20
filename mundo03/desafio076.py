'''
crie um programa que tenha uma TUPLA única com nomes de produtos e seus respectivos preços, na sequência.

no final, mostre uma listagem de preços organizando os dados em forma tabular.

'''

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    else:
        print(f' R${produtos[pos]:7.2f}')
print('-'*50)
    
    