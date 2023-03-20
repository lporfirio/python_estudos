# Coleções (listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
# Lista
precos = [20,50,200]
#          0, 1, 2
print(precos[0])
print(precos.index(200)) # para procurar o indice do valor
# Lista pode ter vários tipos
diversidades = [15,'jhonatan', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])

# Laçoes em iteráveis
for preco in precos:
    print(preco)

# Exemplo 5 - Some os valores

idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
    print(total)
print(total)