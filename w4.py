def en():
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    en_dict = {}
    strlist = str.split()
    count = 0
    while count < len(strlist):
        if count == 0 or count == 4 or count == 5 or count == 6 or count == 7 or count == 8 or count == 14 or count == 15 or count == 18:
            en = strlist[count]
            enK = en[0]
            en_dict[enK]  = count + 1
        else:
            en = strlist[count]
            enK = en[0] + en[1]
            en_dict[enK]  = count + 1
        count = count + 1
    print(en_dict)
#
# test_dict_1['YEAR']  = '2010'
# test_dict_1['MONTH'] = '1'
# test_dict_1['DAY']   = '20'
#
# print(test_dict_1)

en()
