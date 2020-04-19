import sys
import MeCab

def read_text():
    m = MeCab.Tagger("-Ochasen")
    with open('neko.txt.mecab','w',encoding="utf-8") as fw:
        with open('neko.txt','r',encoding="utf-8") as fr:
            line = fr.readline()
            while line:
                fw.write(m.parse(line))
                line = fr.readline()


def read_mecab():
    keitaiso = {}
    with open('neko.txt.mecab','r',encoding="utf-8") as f:
        line = f.readline()
        while line:
            linelist = line.split()
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
            line = f.readline()
            print(keitaiso)

read_mecab()
