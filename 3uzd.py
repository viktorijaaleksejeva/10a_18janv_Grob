def funkcijaa():
    try:
        with open("fails3.txt", "r", encoding="utf-8") as dati:
            saturs=dati.read()
            for i, rinda in enumerate(saturs):
                if i==2:
                    print(rinda)
                return rinda

            

    except:
        pass
if __name__=="__main__":
    funkcijaa()