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

velocidade = int(input('Velocidade que o veículo passou:')) 

if velocidade <= 80:
    print('não houve multa')
elif velocidade <= 90:
    print('multa leve')
elif velocidade <= 100:
    print('multa grave')
elif velocidade >= 101:
    print('multa gravíssima')

