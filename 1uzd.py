def galvena_funkcija():
    try:
        with open("fails.txt", "r", encoding="utf-8") as aa:
            saturs=aa.read()
            print(saturs)
    except:
        pass
if __name__ == "__main__":
    galvena_funkcija()
    