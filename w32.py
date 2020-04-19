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
    for line in map:
        if line["pos"]=="動詞":
            print(line["base"])
extract_mecab()
