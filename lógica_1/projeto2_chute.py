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

import random
valor_aleatorio = random.randint(1, 10) 
acertou = False



while acertou == False:
  chute = int(input('chute um número de 1 a 10'))
  if chute > valor_aleatorio:
        print('chute um valor menor!')
  elif chute < valor_aleatorio:
        print('chute um valor manior!')
  elif chute == valor_aleatorio:
        print('parabéns! você acertou!')
        acertou = True
