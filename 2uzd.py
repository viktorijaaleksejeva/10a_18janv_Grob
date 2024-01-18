import csv 
def funkcija():
    try:
        with open("fails2.csv", "r", encoding="utf-8") as bb:
            saturs = csv.reader(bb)
            print(saturs)
            
    except:
        pass
if __name__=="__main__":
    funkcija()