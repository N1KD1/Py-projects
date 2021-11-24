class InapproriateDictError(Exception):
    pass
def toomanydicts(*slovari):
    keys=[]
    items=[]
    for i in slovari:
        try:
            keys+=list(i.keys())
            items+=list(i.values())
        except AttributeError as e:
            raise InapproriateDictError("Wrong element")
    return keys,items
print(toomanydicts({"eafaple":1, "somafaey":0},{"1":999},{"oshi":10,"hi":0,"teo":"0-7"}))
print(toomanydicts("something that not dict"))