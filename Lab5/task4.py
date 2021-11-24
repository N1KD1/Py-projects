def xn(x,n):
    if n < 0:
        print("Значення n приймає тільки натуральні числа!")
        return x
    elif n == 1:
        return x
    return x * xn(x, n-1)
print(xn(int(input("Число \n>>>")),int(input("Степінь \n>>>"))))