def funkcijaa():
    try:
        with open("fails3.txt", "r", encoding="utf-8") as dati:
            i=0
            saturs=dati.readlines("\n")

    except:
        pass
if __name__=="__main__":
    funkcijaa()