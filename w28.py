import json
import re

def read_json():
    # with open('jawiki-country.json','r',encoding="utf-8") as f:
    with open('egi.json','r',encoding="utf-8") as f:
        line = f.readline()

        while line:
            json_data = json.loads(line)
            if json_data["title"] == "イギリス":
                break
            line = f.readline()

    return json_data["text"]

def get_temp():
    flag = 0
    dict = {}
    text = read_json().split("\n")

    for i in text:
        if "{{基礎情報" in i:
            flag = 1
        if flag == 1 and i == "}}":
            flag = 0
            break
        elif "{{基礎情報" not in i and flag == 1:
            # ここががテンプレートを取り出せる場所
            valcutbrakets = re.search(r'<.*>', i)
            if valcutbrakets != None:
                i = re.sub(r'<.*>','',i)

            bef = re.search(r'[^\|]*=', i)
            aft = re.search(r'=.+', i)

            if bef != None and aft != None:

                key = bef.group().replace("=","").replace(" ","")
                value = aft.group().replace("=","").replace(" ","").replace("'","")

                valcutlink = re.search(r'\[\[.+', value)
                if valcutlink != None:
                    # print(valcutlink.group())
                    if "|" in valcutlink.group():
                        a = re.sub(r'.*\[\[.+\|','',valcutlink.group())
                        value = re.sub(r'\]\].*','',a)
                    else:
                        a = re.sub(r'.*\[\[','',valcutlink.group())
                        value = re.sub(r'\]\].*','',a)

                valcutlink = re.search(r'\[\[.+', value)
                if valcutlink != None:
                    # print(valcutlink.group())
                    if "|" in valcutlink.group():
                        a = re.sub(r'.*\[\[.+\|','',valcutlink.group())
                        value = re.sub(r'\]\].*','',a)
                    else:
                        a = re.sub(r'.*\[\[','',valcutlink.group())
                        value = re.sub(r'\]\].*','',a)

                valcutbraces = re.search(r'\{\{.+', value)
                if valcutbraces != None:
                    if "|" in valcutbraces.group():
                        a = re.sub(r'.*\{\{.+\|','',valcutbraces.group())
                        value = re.sub(r'\}\}.*','',a)
                    else:
                        a = re.sub(r'.*\{\{.+\|','',valcutbraces.group())
                        value = re.sub(r'\}\}.*','',a)
                        
                dict[key] = value

    print(dict)

get_temp()
