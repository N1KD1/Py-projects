print("Індивідуальне завдання на обробку рядків двома способами. Варіaнт 3, Задача 1")
a = input('Введіть строку')
way = int(input("Виберіть спосіб "))
while True:
    if way == 1:                            ##спосіб перший через методи
        if a.find(":")!=-1:
            k=a.find(":")
            print(a[k+1::])
            print(len(a[k + 1::]))
        else:
            print("Символ \":\" відсутній!")
            print(a)
            print(len(a))
    elif way == 2:                          ##спосіб 2
        indx=0
        while indx!=len(a):
            if a[indx]==':':
                print(a[indx+1::])
                print(len(a[indx+1::]))
                break
            else: indx+=1
    else: print("Способу "+str(way)+" не існує!")
    break


