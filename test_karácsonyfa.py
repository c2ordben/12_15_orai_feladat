def karacsonyfa(magassag: int):
    for i in range(1, magassag + 1):
        szokoz = magassag - i
        csillag = 2 * i - 1
        print(" " * szokoz + "*" * csillag)


if __name__ == "__main__":
    magassag = int(input("Add meg a karácsonyfa magasságát: "))
    karacsonyfa(magassag)
