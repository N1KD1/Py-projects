while True:
    import math
    a=float(input('Введіть число а'))
    b=float(input('Введіть число b'))
    c = float(input('Введіть число c'))
    x1 = float(input('Введіть число x1'))
    x2 = float(input('Введіть число x2'))
    while x1 > x2:
        print("Неправильне значення х1 та х2")
        x1 = float(input('Введіть число x1'))
        x2 = float(input('Введіть число x2'))
    trace = x1
    dx = float(input('Введіть число delta x'))
    if a < 0 and c != 0:
        while trace <= x2:
            print("{:>5.3f}: {:.5f}".format(trace, a*trace**2 + b*trace+c))
            trace = trace + dx
    elif a > 0 and b == 0:
        while trace <= x2:
            print("{:>5.3f}: {:.5f}".format(trace, (-a)/(trace - c)))
            trace = trace + dx
    else:
            while trace <= x2:
                print("{:>5.3f}: {:.5f}".format(trace, a * (trace - c)))
                trace = trace + dx
    




