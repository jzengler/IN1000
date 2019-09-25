

# 1.
mineOrd = []

# 2.
# funksjon som konkatenerer to strenger
def slaaSammen(a, b):
    return str(a)+str(b)


# 3.
# prosedyre for å skrive ut hvert element i en liste på en ny linje
def skrivUt(liste):
    for e in liste:
        print(e)

# 4.
#
valg = 0
while valg != "s":

    print("\ni: Konkatener to strenger")
    print("u: Skriv ut elementer i liste")
    print("s: Avslutt")
    valg = input("Skriv inn meny valg: ").lower()

    # a.
    if valg == "i":
        streng1 = input("\nSkriv inn den første strengen: ")
        streng2 = input("Skriv inn den andre strengen: ")
        mineOrd.append( slaaSammen(streng1, streng2) )

    # b.
    elif valg == "u":
        skrivUt(mineOrd)

    # c.
    elif valg == "s":
        exit()
