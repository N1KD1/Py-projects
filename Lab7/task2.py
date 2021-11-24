text = open("text.txt", "r+" )
lines =[]
for i in text.readlines():
    lines.append(str(i))
text.close()
text = open("text.txt", "w")
for i in lines:
    templine = i
    symbols = 0
    for ii in i:
        if ii !=" " and ii!="\n":
            symbols+=1
    text.write(f"{symbols}{i}")
