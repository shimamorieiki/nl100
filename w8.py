def cipher(arg):
    str = arg
    restr = ''
    for i in str:
        if i.isalpha():
            restr = restr + chr(219-ord(i))
        else:
            restr = restr + i
    print(restr)
    
cipher("a63ge643bcde fg")
