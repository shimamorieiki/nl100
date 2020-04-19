import sys
import MeCab

def read_mecab():
    list = []
    with open('neko.txt.mecab','r',encoding="utf-8") as f:
        line = f.readline()
        while line:
            linelist = line.split()
            keitaiso = {}
            if len(linelist)>=3:
                if "-" in linelist[3]:
                    pos = linelist[3].split("-")
                    keitaiso["pos"] = pos[0]
                    keitaiso["pos1"] = pos[1]
                else:
                    keitaiso["pos"] = linelist[3]
                    keitaiso["pos1"] = ""

                keitaiso["surface"] = linelist[0]
                keitaiso["base"] = linelist[2]
                list.append(keitaiso)
            line = f.readline()

    return list

def extract_mecab():
    map = read_mecab()
    resultstr = ""
    flag = 3
    for line in map:
        # flag = 0 名詞
        # flag = 1 名詞 + 助詞の「の」
        # flag = 2 AのB
        # flag = 3 直前まで何もない

        if line["pos"]=="名詞" and flag == 3:
            flag = 0 #突然名詞が来た
            resultstr = line["base"]
        elif flag == 3:
            pass #何もない
        elif line["pos"]=="名詞" and flag == 1:
            flag = 0#AのB
            resultstr = resultstr + line["surface"]
            print(resultstr)
            resultstr = line["surface"]
        elif line["pos"]!="名詞" and flag == 1:
            flag = 3 #AのCなのでだめ
        elif line["pos"]=="助詞" and line["base"]=="の" and flag == 0:
            resultstr = resultstr + "の"
            flag = 1
        elif line["pos"]!="助詞" and flag == 0:
            flag = 3

extract_mecab()
