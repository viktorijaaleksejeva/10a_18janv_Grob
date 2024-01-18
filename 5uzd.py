ievade=str(input("Ievadi savu vārdu!:"))
def galvena_funkcija():
    try:
        with open("failsa.txt","w", encoding="utf-8") as b:
            b.write(ievade)
            if ievade in "failsa.txt":
                print("Ir izveidots fails, un tajā ir ierakstīts Tavs vārds!")
    except SyntaxError:
        print("Nav pareiza sintakse!")
if __name__ == "__main__":
    galvena_funkcija()