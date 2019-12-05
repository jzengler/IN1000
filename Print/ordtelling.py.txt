'''
scriptet inneholder to funksjoner som returnerer antallbokstaver i et ord
og antall forekomster av et ord i en setning.
Tar setning som brukerinput
skriver ut antall ord i setningen, forekomster av ord og antall bokstaver i hvert ord.
'''

# funksjon som returnerer antall bokstaver i et ord
def antallBokstaver(ord):
    return len(ord)

# funksjon som returnerer antall ord i setning som en ordbok
def antallOrd(setning):
    # splitter strengen i en liste av ord i minuskler
    ordListe = setning.lower().split()
    # tom ordbok for å holde ord:antall
    ordTelling = {}

    # løkke for å telle forekomster av ordet i listen med ord
    for nokkel in ordListe:
        ordTelling[nokkel] = ordListe.count(nokkel)
    # returnerer ordboken fra funksjonen
    return ordTelling


# Tar brukerinput
minSetning = input("Skriv inn en setning: ")

# lagre resultatet av funksjonen
forekomst = antallOrd(minSetning)

# skriv ut antall ord i setningen
print("Det er", len(minSetning.split()), "ord i setningen")
# løkke for å skrive ut forekomst og antall bokstaver for nøkkel i variabelen forekomst
for ord in forekomst:
    print("Ordet '" + ord + "'\tforekommer", forekomst[ord], " ganger, og har", antallBokstaver(ord), "bokstaver" )
