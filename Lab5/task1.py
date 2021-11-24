 # варіант 3
def all(a, b):
    def first(a, b):
        return b + 2*a*b + 1
    def second(a, b):
        return a + 2*b*a + 1
    def third(a, b):
       return (abs(a - b))**0.5
    if first(a, b) == 0 or second(a, b) == 0:
        print("Розв'язку немає")
    else:
        return 5*a/first(a, b) + 2*(5*b/second(a, b)) - third(a , b)
while True:
    print("Введіть 2 довільні числа a i b:")
    a = input(">>>").split()
    print(all(int(a[0]),int(a[1])))
