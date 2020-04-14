def join(arg,arg2):
    len1 = len(arg)
    len2 = len(arg2)
    count = 0
    restr = ''

    if len1 > len2:
        while count < len2:
            restr = restr + arg[count]
            restr = restr + arg2[count]
            count = count + 1
        count = len2
        while count < len1:
            restr = restr + arg[count]
            count = count + 1
    elif len1 < len2:
        while count < len1:
            restr = restr + arg[count]
            restr = restr + arg2[count]
            count = count + 1
        count = len1
        while count < len2:
            restr = restr + arg2[count]
            count = count + 1
    else:
        while count < len1:
            restr = restr + arg[count]
            restr = restr + arg2[count]
            count = count + 1
    print(restr)

join("パトカー","タクシー")
