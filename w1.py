def cut(arg):
    count = 0
    str1 = ""
    str2 = ""
    while count<len(arg):
        if count % 2 == 0:
            str1 = str1 + arg[count]
        else:
            str2 = str2 + arg[count]
        count = count + 1
    print(str1)
    print(str2)

cut("パタトクカシーー")
