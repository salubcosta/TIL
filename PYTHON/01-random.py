from random import randint

number = randint(0, 100)

print('##10 chances##')

qtd = 0
while 1 == 1:
    choice = int(input('Chute um número (0 a 100): '))
    qtd += 1
    if(number == choice):
        print('Acertou!')
        break
    else:
        if qtd == 10:
            print('Game over!')
            break
        tip = 'Tente um número maior' if choice < number else 'Tente um número menor'
        print('Errou!', tip)