def ngram(arg):
    str = arg
    restr= str.split()
    list = []
    for i in range(len(restr)-1):
        list.append(restr[i]+" "+restr[i+1])
    print(list)
    list = []
    mojiretu = ''.join(restr)
    for i in range(len(mojiretu)-1):
        list.append(mojiretu[i]+mojiretu[i+1])
    print(list)
    
ngram("I am an NLPer")
