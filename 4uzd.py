import json
import csv
ievadit=input("Ievadi faila nosaukumu ar paplašinājumu!:")
def nosacijumi():

    if "txt" in ievadit:
        try:
            with open(ievadit, "r", encoding="utf-8") as teksts:
                saturs=teksts.read()
                print(saturs)
        except FileNotFoundError:
            print("Datne nepastāv!")
    elif "json" in ievadit:
        try:
            with open(ievadit,"r", encoding="utf-8") as a:
                sat=json.load(a)
                print(sat)
        except FileNotFoundError:
            print("Datne nepastāv!")
        except SyntaxError:
            print("Nav pareiza sintakse!")
    else:
        try:
            with open(ievadit, "r", encoding="utf-8") as t:
                sa = t.read()
                print(sa)
        except FileNotFoundError:
            print("Datne netika atrasta!!!!")
if __name__=="__main__":
    nosacijumi()