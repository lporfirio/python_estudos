# Condicionais
# if, elif e else
'''
E ae lucas, vamos sair hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''

trabalho_terminado = False
if trabalho_terminado == True:
    print('Opa! Bora sair!!')
else:
    print('Não posso sair agora')

'''
Ei, você consegue me ajudar a colocar as caixas lá fora hoje a tarde?
Se eu estiver livre, sim. Se não, pede para o meu irmão te ajudar.
'''

estou_livre = True
if estou_livre == True:
    print('OK, posso ajudar sim!')
else:
    print('Peça ao meu irmão para te ajudar.')

'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for a sua terceira vez chegando atrasado, sim. 
Caso contrário, irá tomar uma suspensão.
'''

numero_de_atraso = 1
if numero_de_atraso >= 3:
    print('você está suspenso')
elif numero_de_atraso == 1:
    print('pode entrar, porém caso atrase mais duas vezes, irá ser suspenso')
elif numero_de_atraso == 2:
    print('pode entrar, porém cao atrase mais uma vez, irá ser suspenso')
else:
    print('pode entrar')

print(' ')

primeiro_valor = input('digite o primeiro valor')
segundo_valor = input('digite o segundo valor')

if primeiro_valor > segundo_valor:
    print('o primeiro valor é maior')
else:
    print('o segundo valor é maior')
