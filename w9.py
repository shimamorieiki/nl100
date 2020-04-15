import random as ran

def Typoglycemia(arg):
    str = arg
    strlist = str.split()
    retlist = []
    for i in strlist:
        if len(i)>4:
            chr = []
            for j in i:
                chr.append(j)
            f = chr.pop(0)
            e = chr.pop(-1)
            ran.shuffle(chr)
            # print(f)
            # print(e)
            # print(chr)
            restr = f + ''.join(chr) + e
            retlist.append(restr)
        else:
            retlist.append(i)

    return ' '.join(retlist)


print(Typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
