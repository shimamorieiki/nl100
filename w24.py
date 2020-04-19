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

def get_media():

    text = read_json().split("\n")
    for i in text:
        # matchは文の先頭から検索searchは文の最初に見つかった場所から
        m = re.search(r'[a-zA-Z]([a-zA-Z]|\s|_|,)+\.(jpg|png|svg)', i)
        if m != None:
            print(m.group())

get_media()
