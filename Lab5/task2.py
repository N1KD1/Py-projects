def palindrome(a):
    if type(a)!= list:
        print("Функція приймає тільки списки!")
    else:
        b = []
        plndrm = 0
        for i in range(len(a)):
            b.append(a[i][::-1])
        for i in a:
            for ii in b:
                if i == ii:
                    plndrm+=1
                    break
        return plndrm # "...і визначає СКІЛЬКИ слів однаково читаються..."
print(palindrome("ooooooooo"))