import json
import re

def read_json():
    with open('jawiki-country.json','r',encoding="utf-8") as f:
    # with open('egi.json','r',encoding="utf-8") as f:
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
            # print(i)
            # ここががテンプレートを取り出せる場所
            bef = re.search(r'[^|].+=', i)
            aft = re.search(r' =.+', i)

            if bef != None and aft != None:
                # print(bef)
                # print(aft)
                key = bef.group().replace("=","").replace(" ","")
                value = aft.group().replace("=","").replace(" ","")
                # print(key)
                # print(value)
                dict[key] = value
        # # matchは文の先頭から検索searchは文の最初に見つかった場所から
        # m = re.search(r'[a-zA-Z]([a-zA-Z]|\s|_|,)+\.(jpg|png|svg)', i)
        # if m != None:
        #     print(m.group())
    print(dict)

get_temp()