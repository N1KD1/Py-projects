import random as rnd
a=input("Введіть десять чисел через пробіл, або залиште пустим").split(" ")
if a==['']:
    a=[0]*10
    for i in range(9):
        a[i]=rnd.randint(1, 100)
elif len(a)!=10:
    print("Введіть ще раз")
    a = input("Введіть десять чисел через пробіл").split(" ")
a_int = [int(x) for x in a]
print(a)
print(sum(a_int[0:5])-sum(a_int[5:10]))


