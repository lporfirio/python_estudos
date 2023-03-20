'''

Método 5Q's para montar um algorítimo:
Analíse criticamente o problema e descubra:
(tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais
até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?


'''


# Crie um programa que recebe um número e imprime seu fatorial.
'''
1. Quais são os dados de entrada necessários?
- número
2. O que devo fazer com estes dados?
- calcular o fatorial do número que for passado e o xibir na tela
3. Quais são as restrições deste problema?
- o número precisa ser positivo e inteiro
4. Qual é o resultado esperado?
- exibir na tela o fatorial do número
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
 fatorial = fatorial * numero
print(fatorial)

'''

numero = int(input('escolhe um número até 10'))
#numero = 5
fatorial = 1
if numero > 0:
 for number in range(1, numero + 1):
    fatorial = fatorial * number
print(fatorial)
