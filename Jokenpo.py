import random
import defs
defs.MenuInicial()
Lista = ['pedra', 'papel', 'tesoura']
while True:
    E = random.choice(Lista)
    OBJ = str(input('Escolha seu objeto: ')).strip().lower()
    if E == OBJ:
        print('=' * 30)
        print('           \033[36mEMPATE!\033[m \n  Os dois escolheram {}.'.format(E))
        print('=' * 30)
    elif E == 'pedra' and OBJ == 'tesoura':
        print('=' * 30)
        print('           \033[31mPERDEU!\033[m \n    Você escolheu {}. \n     Eu escolhi {}.'.format(OBJ, E))
        print('=' * 30)
    elif E == 'tesoura' and OBJ == 'pedra':
        print('=' * 30)
        print('           \033[32mPARABÉNS!\033[m \n     Você escolheu {}. \n     Eu escolhi {}.'.format(OBJ, E))
        print('=' * 30)
    elif E == 'papel' and OBJ == 'pedra':
        print('=' * 30)
        print('           \033[31mPERDEU!\033[m \n     Você escolheu {}. \n      Eu escolhi {}.'.format(OBJ, E))
        print('=' * 30)
    elif E == 'pedra' and OBJ == 'papel':
        print('=' * 30)
        print('          \033[32mPARABÉNS!\033[m \n    Você escolheu {}. \n     Eu escolhi {}.'.format(OBJ, E))
        print('=' * 30)
    elif E == 'tesoura' and OBJ == 'papel':
        print('=' * 30)
        print('           \033[31mPERDEU!\033[m \n     Você escolheu {}. \n     Eu escolhi {}.'.format(OBJ, E))
        print('=' * 30)
    elif E == 'papel' and OBJ == 'tesoura':
        print('=' * 30)
        print('          \033[32mPARABÉNS!\033[m \n    Você escolheu {} \n      Eu escolhi {}.'.format(OBJ, E))
        print('=' * 30)
    else:
        print('\033[4;30;41mObjeto inválido, tente novamente!\033[m')

    r = str(input('Deseja jogar mais uma vez?[S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
    while r != 'S':
        print('\033[4;30;41mDigite uma opção válida!\033[m')
        r = str(input('Deseja jogar mais uma vez?[S/N]: ')).strip().upper()[0]
        if r == 'N':
            break
    if r == 'N':
        break

