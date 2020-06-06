from random import randint

number = randint(0, 10)

while 1 == 1:
    choice = int(input('Chute um número (0a10): '))

    if(number == choice):
        print('Acertou!')
        break
    else:
        print('Errou!')