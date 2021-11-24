from random import *
rand = open("numbers.txt", "w+")
for i in range(randint(1,100)):
    rand.write(f"{randint(-300, 300)}\n")
rand.close()
rand=open("numbers.txt",'r')
rand.seek(0)
x=0
numbers = rand.readlines()
for i in numbers:
    ii=int(i)/2
    if round(int(i)/2) !=ii:
        x+=1
rand.close()
rand=open("numbers.txt",'a',encoding='utf8')
rand.write(f"Непарних чисел: {x}")