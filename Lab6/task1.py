example = {"one":1,"two":2,"three":3}
while True:
    a = input("Введіть ключ\n>>>")
    try:
        print(example[a])
    except KeyError:
        a = "Написано неправильний ключ!"
        print(a)