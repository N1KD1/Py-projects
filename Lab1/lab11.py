import math
a=int(input('число а'))
b=int(input('число b'))
c = int(input('число c'))
x1 = int(input('число x1'))
x2 = int(input('число x2'))
deltax=int(input("крок"))
x=x1
if x1<0 and x2<0 and c!=0:
    while x<=x2:
        print(x+";", -(a)*x-c)
        x=x+deltax
elif x1>0 and x2>0 and c==0:
    if b!=0:
        while x<=x2:
            print(x +";", (x-a)/-b)
            x=x+deltax
    else:
        print("розвязків немає")
else:
    if (c-a)!=0:
        while x<=x2:
            print(x+";", (b*x)/(c-a))
            x=x+deltax

