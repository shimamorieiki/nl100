import json

def read_json():
    with open('jawiki-country.json','r',encoding="utf-8") as f:
        line = f.readline()

        while line:
            json_data = json.loads(line)
            if json_data["title"] == "イギリス":
                print(json_data["text"])
                break
            line = f.readline()


read_json()
