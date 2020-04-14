def pi():
    str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    strlist = str.split()
    numlist = []
    for i in strlist:
        rei = i.replace(",","").replace(".","")
        num = len(rei)
        numlist.append(num)
    print(numlist)
    
pi()
