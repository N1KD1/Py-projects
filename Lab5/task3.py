def rev(a):
    b = a
    if len(a) == 1:
        return a
    else:
        return a[-1] + " "+ rev(b[0:len(b)-1])

print(rev(input(">>>")))