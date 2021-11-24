import random as rnd
inpt = input("Введіть десять чисел через пробіл, або залиште пустим").split(" ")
if inpt == ['']:
    inpt.clear()
    for i in range(rnd.randint(2,20)):
        inpt.insert(i,rnd.randint(1, 100))
        intinpt = inpt
intinpt = [int(x) for x in inpt]
print(intinpt)
intinpt.pop(int(input("Введіть індекс елементу, який ви хочете вилучити через метод \"pop\"")))
print(intinpt)