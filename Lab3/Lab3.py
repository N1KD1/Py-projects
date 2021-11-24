import random
import random as rnd
import time
bank = rnd.randint(1, 300)
ply = 0
bot = 0
crd = rnd.randint(1,300)
while True:
    if bank<=0:
        if crd-(-bank)==0:
            print("Игра окончена: Вы погрязли в долгах")
            break
        else:
            print('Ваш счет:{}'.format(bank))
            print("Кредитный лимит:{}".format(crd-(-bank)))
    else:
        print('Ваш счет:{}'.format(bank))
    deed = int(input('Ваша ставка '))
    if bank>0:
        while deed<0 or deed>bank:
            print('Ставка неверна!')
            deed = int(input('Ваша ставка '))
    else:
        while deed>crd or deed>crd+bank:
            print('Ставка неверна!')
            deed = int(input('Ваша ставка '))
    print('Бросаем кости...')
    for i in range(3):
        time.sleep(0.5)
        print('.')
    bot=random.randint(1,12)
    ply=random.randint(1,12)
    print("Счет бота:{}".format(bot))
    time.sleep(1.3)
    print("Ваш счет:{}".format(ply))
    time.sleep(0.7)
    if bot>ply:
        print('Вы проиграли!')
        bank -=deed
    elif bot<ply:
        print('Вы выиграли!')
        if bank ==0 or bank<=0:
            bank += deed//2
            crd -= crd//rnd.randint(1, 15)
        else:
            bank += deed
    else:
        print('Ничья!')
    time.sleep(0.7)
