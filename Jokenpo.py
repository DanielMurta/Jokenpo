import random
from time import sleep
print('INICIANDO O JOGO...')
sleep(2)
print('='*15)
print('    JOKENPO')
print('='*15)
Lista = ['pedra', 'papel', 'tesoura']
E = random.choice(Lista)
OBJ = str(input('Escolha seu objeto: ')).strip().lower()
if E == OBJ:
    print('=' * 15)
    print('   \033[4;34mEMPATE!!!\033[m \nOs dois escolheram {}.'.format(E))
    print('=' * 15)
elif E == 'pedra' and OBJ == 'tesoura':
    print('=' * 15)
    print('   \033[4;31mPERDEU!!!\033[m \nVocê escolheu {}. \nEu escolhi {}.'.format(OBJ, E))
    print('=' * 15)
elif E == 'tesoura' and OBJ == 'pedra':
    print('=' * 15)
    print('   \033[4;32mPARABÉNS!!!\033[m \nVocê escolheu {}. \nEu escolhi {}.'.format(OBJ, E))
    print('=' * 15)
elif E == 'papel' and OBJ == 'pedra':
    print('=' * 15)
    print('   \033[4;31mPERDEU!!!\033[m \nVocê escolheu {}. \nEu escolhi {}.'.format(OBJ, E))
    print('=' * 15)
elif E == 'pedra' and OBJ == 'papel':
    print('=' * 15)
    print('   \033[4;32mPARABÉNS!!!\033[m \nVocê escolheu {}. \nEu escolhi {}.'.format(OBJ, E))
    print('=' * 15)
elif E == 'tesoura' and OBJ == 'papel':
    print('=' * 15)
    print('   \033[4;31mPERDEU!!!\033[m \nVocê escolheu {}. \nEu escolhi {}.'.format(OBJ, E))
    print('=' * 15)
elif E == 'papel' and OBJ == 'tesoura':
    print('=' * 15)
    print('   \033[4;32mPARABÉNS!!!\033[m \nVocê escolheu {} \nEu escolhi {}.'.format(OBJ, E))
    print('=' * 15)
else:
    print('\033[4;30;41mObjeto inválido, tente novamente!\033[m')