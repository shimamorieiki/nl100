import json

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

def get_section():
    text = read_json().split("\n")
    for i in text:
        if "======" in i:
            i = i.replace("======","")
            print("    "+i+":レベル4")
        elif "=====" in i:
            i = i.replace("=====","")
            print("   "+i+":レベル3")
        elif "====" in i:
            i = i.replace("====","")
            print("  "+i+":レベル2")
        elif "===" in i:
            i = i.replace("===","")
            print(" "+i+":レベル1")
        elif "==" in i:
            i = i.replace("==","")
            print(""+i+":レベル0")

get_section()
