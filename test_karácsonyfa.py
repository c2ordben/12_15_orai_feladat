magassag = int(input("Add meg a karácsonyfa magasságát: "))

for i in range(1, magassag + 1):
    szokoz = magassag - i
    csillag = 2 * i - 1
    print(" " * szokoz + "*" * csillag)
