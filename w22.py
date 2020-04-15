import json

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

def get_category():
    text = read_json().split("\n")
    for i in text:
        if "[[Category:" in i:
            i = i.replace("[[Category:","").replace("]]","").replace("|*","")
            print(i)


get_category()
