import random as rnd
import time as tm

dishes = ['Вареники', "Борщ", "Салат", "Суп овочевий", "Котлета", "Пюре", "Плов", "Рагу", "Спагеті", "Курка"]  # товари
rnd.shuffle(dishes)
price_weight_value = []
most_exp = []
el = []
shopper = {}
border = "//////////////////////"
ex1, ex2, ex3, ex4, ex5 = 1, 1, 1, 1, 1
p, m, k, money, sum_val, exp = 0, 0, 0, 0, 0, 0
print("Список страв:"
      "\n1.Згенерований"
      "\n2.Свій")
ex = int(input(">>>"))
if ex == 2:
    big_dict = {}
    while True:
        print('Будь ласка додайте нову страву за таким шаблоном: '
              'Назва страви Ціна Вага порції Кількість, 0 щоб закінчити')
        new_dish = input(">>>").split()
        if new_dish == ["0"]:
            ex = 1
            break
        if len(new_dish) == 4:
            if new_dish[1].isdigit() and new_dish[2].isdigit() and new_dish[
                3].isdigit():
                big_dict[new_dish[0]] = [int(x) for x in new_dish[1::]]
                print(f"Страву \"{new_dish[0]}\" додано до меню.\n{border}")
        else:
            print("Введені хибні дані! Спробуйте ще раз")
            new_dish = None
    dishes_dict = list(big_dict.keys())
elif ex == 1:
    for i in range(len(dishes)):  # створення рандомних значень ціни ваги та кількості в логічному обмеженні
        p = rnd.randint(10, 150)  # ціна
        m = rnd.choice(range(100, 500, 100))  # маса
        k = rnd.randint(1, 50)  # кількість
        temp = [p, m, k, ]
        price_weight_value.append(temp)
    big_dict = dict(zip(dishes, price_weight_value))  # саме словник
else:
    exit()
if len(big_dict) != 0:
    print(f"Ресторан \"{dishes[rnd.randint(0, len(dishes) - 1)]} і {dishes[rnd.randint(0, len(dishes) - 1)].lower()}\"")
print("\x1B[3mВведіть відповідну цифру для виклика меню:\x1B[0m")
while ex != 0:
    my_prod = list(shopper.keys())
    ex1, ex2, ex3, ex4, ex5 = 1, 1, 1, 1, 1
    print("Головне меню"
          f"\n{border}"
          "\n1.Страви"
          "\n2.Кошик"
          "\n0.Вихід"
          f"\n{border}")
    ex = int(input(">>>"))
    while ex2 != 0:
        ex1, ex2, ex3, ex4, ex5 = 1, 1, 1, 1, 1
        if ex == 1:
            dishes_dict = list(big_dict.keys())
            print(border)
            sum_val = 0
            most_exp.clear()
            el.clear()
            for i in range(len(big_dict)):
                if big_dict[dishes_dict[i]][2] == 0:
                    print(
                        f"{i + 1}.{dishes_dict[i]}: НЕМА В НАЯВНОСТІ")
                else:
                    print(
                        f"{i + 1}.{dishes_dict[i]}: {big_dict[dishes_dict[i]][0]} грн; "
                        f"{big_dict[dishes_dict[i]][1]} г; {big_dict[dishes_dict[i]][2]} шт.", )
                sum_val += big_dict[dishes_dict[i]][2]  # завдання про кількість страв
                most_exp.append(big_dict[dishes_dict[i]][0])
            if len(big_dict) != 0:
                ex5 = max(most_exp)
                for i in range(len(most_exp)):
                    if most_exp[i] == ex5:
                        el.append(i)
                print("Найдорожчі страва:")
                for i in el:
                    print(f"{dishes_dict[i]} : {big_dict[dishes_dict[i]][0]} грн")
                print(f"Загальна кількість страв {sum_val}")
            print(f'{border}'
                  '\n1.Додати страву(-ви) у замовлення'
                  '\n2.Редагувати меню страв'  # не зробив
                  '\n0.Вихід у головне меню'
                  f'\n{border}')
            ex2 = int(input(">>>"))
            if ex2 == 1:
                print("Щоб додати страву у кошик введіть її номер або 0 щоб повернутися до переліку")
                ex1 = int(input(">>>"))
                if ex1 > len(dishes_dict) or ex < 0:
                    print("Введено невірний номер!")
                    ex1 = 0
                while ex1 != 0:
                    if big_dict[dishes_dict[ex1 - 1]][2] == 0:
                        print(f"Страва {dishes_dict[int(ex1 - 1)]} на жаль зараз відсутня.")
                        break
                    val = int(input(
                        f"Яку кількість {dishes_dict[int(ex1 - 1)]} бажаєте додати?"))
                    if big_dict[dishes_dict[ex1 - 1]][2] < val:
                        print(
                            f"Введена невірна кількість!"
                            f" У замовлення було додано {big_dict[dishes_dict[ex1 - 1]][2]}шт.")
                        val = big_dict[dishes_dict[ex1 - 1]][2]
                    big_dict[dishes_dict[ex1 - 1]][2] -= val
                    if shopper.get(dishes_dict[ex1 - 1]) is not None:
                        shopper[dishes_dict[ex1 - 1]] += val
                    else:
                        shopper[dishes_dict[ex1 - 1]] = val  # їжа=[кількість порцій куплених]
                    my_prod = list(shopper.keys())
                    print(f"Страву {dishes_dict[ex1 - 1]} в кількості {val}шт. додано до вашого кошика."
                          f"\n{border}"
                          f"\n1. Продовжити покупку"
                          f"\n0. Повернутися у головне меню")
                    ex2 = int(input(">>>"))
                    if ex2 == 1:
                        ex1 = 0
                    else:
                        break
            if ex2 == 2:
                while ex3 != "0":
                    print(border)
                    dishes_dict = list(big_dict.keys())
                    for i in range(len(big_dict)):
                        print(
                            f"{i + 1}.{dishes_dict[i]}:{big_dict[dishes_dict[i]][0]} грн; "
                            f"{big_dict[dishes_dict[i]][1]} г; {big_dict[dishes_dict[i]][2]} шт.")
                    print(border +
                          "\nВведіть номер страви, яку бажаєте змінити,\"+\" щоб додати нову страву,\"0\" "
                          "щоб повернутися")
                    ex3 = input(">>>")
                    if ex3 != '+':
                        while ex3 != '0':
                            ex3 = int(ex3)
                            print(f"\nСтрава \"{dishes_dict[ex3 - 1]}\""
                                  f"\nЩо бажаєте зробити?\n{border}"
                                  f"\n1.Видалити"
                                  f"\n2.Змінити назву"
                                  f"\n3.Змінити ціну({big_dict[dishes_dict[ex3 - 1]][0]} грн)"
                                  f"\n4.Змінити вагу({big_dict[dishes_dict[ex3 - 1]][1]}г)"
                                  f"\n5.Змінити кількість({big_dict[dishes_dict[ex3 - 1]][2]}шт.)"
                                  f"\n0.Повернутися"
                                  f"\n{border}")
                            ex4 = int(input(">>>"))
                            if ex4 == 1:
                                print(f"{border}\nСтраву \"{dishes_dict[ex3 - 1]}\" успішно видалено!")
                                del big_dict[dishes_dict[ex3 - 1]]
                                del dishes_dict[ex3 - 1]
                                tm.sleep(0.5)
                                break
                            elif ex4 == 3:
                                print(f'{border}\nВведіть нове значення:')
                                big_dict[dishes_dict[ex3 - 1]][0] = (int(input(">>>")))
                            elif ex4 == 4:
                                print(f'{border}\nВведіть нове значення:')
                                big_dict[dishes_dict[ex3 - 1]][1] = (int(input(">>>")))
                            elif ex4 == 5:
                                print(f'{border}\nВведіть нове значення:')
                                big_dict[dishes_dict[ex3 - 1]][2] = (int(input(">>>")))
                            elif ex4 == 2:
                                all_dishes = list(big_dict.items())
                                print(f"{border}\nВведіть нову назву")
                                ex4 = input(">>>")
                                new_dish = (ex4, big_dict[dishes_dict[ex3 - 1]])
                                if ex3 - 1 != 0:
                                    new_dict = all_dishes[0:ex3 - 1]
                                    new_dict.append(new_dish)
                                    new_dict += all_dishes[ex3 - 1::]
                                else:
                                    new_dict = [new_dish]
                                    new_dict += all_dishes[ex3 - 1::]
                                big_dict.clear()
                                big_dict = dict(new_dict)
                                dishes_dict = list(big_dict.keys())
                            else:
                                break
                    elif ex3 == '0':
                        break
                    else:
                        while ex4 != 0:
                            print('Будь ласка додайте нову страву за таким шаблоном: '
                                  'Назва страви Ціна Вага порції Кількість, 0 щоб закінчити')
                            new_dish = input(">>>").split()
                            if new_dish == ["0"]:
                                ex4 = 1
                                ex3 = "0"
                                break
                            if len(new_dish) == 4:
                                if isinstance(new_dish[0], str) and new_dish[1].isdigit() and new_dish[2].isdigit() and \
                                        new_dish[3].isdigit():
                                    big_dict[new_dish[0]] = [int(x) for x in new_dish[1::]]
                                    print(f"Страву \"{new_dish[0]}\" додано до меню.\n{border}")
                            else:
                                print("Введені хибні дані! Спробуйте ще раз")
                                new_dish = None
        if ex == 2:
            while ex2 != 0:
                sum_money = 0
                print("Ваш кошик замовлень:")
                for i in range(len(shopper)):
                    print(f"{i + 1}.{my_prod[i]}: {shopper[my_prod[i]]}шт. {big_dict[my_prod[i]][0]} грн за 1; "
                          f"{shopper[my_prod[i]] * big_dict[my_prod[i]][0]} грн за {shopper[my_prod[i]]}шт.")
                    sum_money += shopper[my_prod[i]] * big_dict[my_prod[i]][0]
                if len(shopper) == 0:
                    print(f"{border}"
                          f"\nЗараз ваш кошик порожній. "
                          f"Додайте будь який товар зі списку щоб побачити його тут та оплатити\n{border}")
                    ex2 = 0
                    break
                if ex2 == 0:
                    break
                else:
                    print(f"{border}"
                          f"\nТоварів на суму {sum_money}грн"
                          f"\n{border}"
                          f"\n1. Оплатити"
                          f"\n2. Змінити список товарів"
                          f"\n0. Вийти в головне меню")
                    ex3 = int(input(">>>"))
                    if ex3 == 0:
                        ex = 1
                        ex2 = 0
                        break
                    while ex3 != 0:
                        if ex3 == 1:
                            ex4 = int(input(f"Оплатити товар на суму {sum_money}\n1.Так\n2.Ні?\n>>>"))
                            if ex4 == 1:
                                print("Проведення транзакції...")
                                for i in range(3):
                                    tm.sleep(0.7)
                                    print(".")
                                print("Успіх! Дякуємо за покупку! Гарного дня!")
                                ex = 0
                                break
                            else:
                                break
                        elif ex3 == 2:
                            print("Що бажаєте змінити?"
                                  "\n1.Видалити елемент"
                                  "\n2.Змінити кількість"
                                  "\n0.Повернутися")
                        else:
                            ex2 = 0
                            ex = 1
                            break
                        ex4 = int(input(">>>"))
                        while ex4 != 0:
                            if ex4 == 1:
                                print("Який елемент бажаєте видалити?")
                                ex4 = int(input(">>>"))
                                if ex4 - 1 > len(my_prod) or ex4 - 1 < 0:
                                    print("Введено невірний номер!")
                                    break
                                if ex4 == 0:
                                    break
                                print(f"{shopper[my_prod[ex4 - 1]]} {my_prod[ex4 - 1]} було успішно видалено з вашого кошика\n{border}")
                                del shopper[my_prod[ex4 - 1]]
                                break
                            elif ex4 == 2:
                                print("Кількість якого продукту бажаєте змінити?")
                                ex4 = int(input(">>>"))
                                if ex4 == 0:
                                    break
                                if ex4 -1 > len(my_prod) or ex4 - 1 < 0:
                                    print("Введено невірний номер!")
                                    break
                                print(f"Яку кількість {my_prod[ex4 - 1]} бажаєте встановити? (На даний момент на складі є "
                                      f"{big_dict[my_prod[ex4 - 1]][2]}шт.)")
                                ex5 = int(input(">>>"))
                                if ex5 == 0:
                                    break
                                elif ex5 > shopper[my_prod[ex4 - 1]]:  # ex5 > big_dict[my_prod[ex4 - 1]][2]
                                    if big_dict[my_prod[ex4 - 1]][2] - ex5 >= 0:
                                        big_dict[my_prod[ex4 - 1]][2] += shopper[my_prod[ex4 - 1]] - ex5
                                        shopper[my_prod[ex4 - 1]] = ex5
                                        print(
                                            f"Кількість {my_prod[ex4 - 1]} успішно змінено на {shopper[my_prod[ex4 - 1]]}")
                                        ex3 = 0
                                        break
                                    else:
                                        print("Введена неправильна кількість!")
                                    break
                                else:
                                    big_dict[my_prod[ex4 - 1]][2] += shopper[my_prod[ex4 - 1]] - ex5
                                    shopper[my_prod[ex4 - 1]] = ex5
                                    print(f"Кількість {my_prod[ex4 - 1]} успішно змінено на {shopper[my_prod[ex4 - 1]]}")
                                break
                            else:
                                ex3 = 0
                                ex4 = 0
                                break
                        if ex3 ==0 or ex4 ==0:
                            break

                break
        if ex == 0:
            print("До побачення! Гарного дня!")
            break
