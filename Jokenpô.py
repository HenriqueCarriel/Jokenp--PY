import random
import time
pc_opc = random.randint(1, 3)
pedra = 1
papel = 2
tesoura = 3

print('----------------------------------------------------------------------------------')
print('Vamos jogar jokenpô!')
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Valendo!!!")
time.sleep(1)

jogador = (int(input('\nEscolha uma opção [1] [2] [3]: ')))

print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Pô')
time.sleep(1)

if jogador == 1 and pc_opc == 2:
    print('\nVocê jogou pedra e o computador jogou papel')
    print('Você perdeu! Tente novamente')
elif jogador == 2 and pc_opc == 1:
    print('\nVocê jogou papel e computador jogou pedra')
    print('Você ganhou! Parabéns')
elif jogador == 3 and pc_opc == 1:
    print('\nVocê jogou tesoura e o computador jogou pedra')
    print('Você perdeu! Tente novamente')
elif jogador == 1 and pc_opc == 3:
    print('\nVocê jogou pedra e o computador jogou tesoura')
    print('Você ganhou! Parabéns')
elif jogador == 2 and pc_opc == 3:
    print('\nVocê jogou papel e o computador jogou tesoura')
    print('Você perdeu! Tente novamente')
elif jogador == 3 and pc_opc == 2:
    print('\nVocê jogou tesoura e o computador jogou papel')
    print('Você ganhou! Parabéns')
else:
    print('Deu empate! Vamos mais uma')
print('----------------------------------------------------------------------------------')