# Python3
# Scriptet tar brukerinput navn og bosted og skriver ut en konkatenert strengen
# Gjøres 3 ganger

def navnOgBosted():
    # Lagrer brukerinput i variabelen navn
    navn = input("Skriv inn navn: ")

    # Lagrer brukerinput i variabelen sted
    bosted = input("Hvor kommer du fra? ")

    # Skriver ut en konkatenert streng med innholdet fra variablene navn og bosted
    print("Hei, " + navn + "! Du er fra " + bosted + "\n")

# Kaller navnogbosted 3 ganger
for _ in range(3):
	navnOgBosted()