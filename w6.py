def bigram(arg):
    str = arg
    restr= str.split()
    list = []
    mojiretu = ''.join(restr)
    for i in range(len(mojiretu)-1):
        list.append(mojiretu[i]+mojiretu[i+1])
    return list

def asset(arg1,arg2):

    x = bigram(arg1)
    y = bigram(arg2)
    x = list(set(x))
    y = list(set(y))
    xory = x
    xandy = []
    xminusy = []

    for i in x:
        if i in y:
            xandy.append(i)
        else:
            xminusy.append(i)

    xory.extend(y)
    xory = list(set(xory))

    print(xandy)
    print(xory)
    print(xminusy)
    if "se" in x:
        print("xに入っています")
    else:
        print("xに入っていません")

    if "se" in y:
        print("yに入っています")
    else:
        print("yに入っていません")


asset("paraparaparadise","pragraph")
