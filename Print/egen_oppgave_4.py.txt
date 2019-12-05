'''
Lag et program som lar brukeren administrere biler og registreringsnummer.
Brukeren skal kunne legge til, slette eller skrive ut en oversikt.
Bruk løkker og lister for å løse oppgaven
'''
# Liste til å holde registreringsnummer, bilmerke, modell og farge
# kan skrives/fra fil hvis det skal lagres mellom ekskeveringer av programmet
regNummer = []

# funksjon for å legge til bil i listen
def leggTilBil():

    # lokal variabel for å holde brukerinput
    bil = []
    # legg til RegNr, merke, modell og farge
    bil.append( input("Skriv inn registreringsnummer: ").upper() )
    bil.append( input("Skriv inn bilmerke: ").title() )
    bil.append( input("Skriv inn bilmodell: ").upper() )
    bil.append( input("Skriv inn farge: ").lower() )

    # returner hele listen
    return bil

# funskjon for å slette bil fra liste
def slettBil(regNummer):
    # be bruker om registreringsnummer på bilen hen ønsker å slette
    slettReg = input("Skriv inn registreringsnummer på bilen du vil slette:  ").upper()

    # løkke for for å sjekke om regnummer finnes i de nøstede listene
    for bil in regNummer:
        # hvis regnr finnes slett listen for den bilen
        if slettReg in bil:
            regNummer.remove(bil)
            print(bil[1], "med registreringsnummer", slettReg, "ble slettet!")

    # returner den oppdaterte listen
    return regNummer

# prosedyre for å skrive ut en oversikt over biler
def printOversikt(regNummer):

    # løkke som skriver ut hver bil med kjennetegn
    for bil in regNummer:
        print("RegNr:", bil[0], "er en", bil[3], bil[1], bil[2])

# prosedyre for å printe meny og kalle andre funksjoner
def meny(regNummer):

    # skriv ut meny til bruker
    print("\n1: Legg til bil")
    print("2: Slett bil")
    print("3: Skriv ut oversikt")
    print("9: Avslutt program\n")
    # lagre brukerens menyvalg
    valg = int(input("Skriv inn menyvalg: \n"))

    # kall funksjon iht brukerens valg
    # lagrer resultatet av funksjonen i samme liste som funksjonens parameter
    if valg == 1:
        regNummer.append( leggTilBil() )
    elif valg == 2:
        regNummer = slettBil(regNummer)
    elif valg == 3:
        printOversikt(regNummer)
    elif valg == 9:
        exit()
    else:
        print("Ugyldig menyvalg!")


# løkke for å kalle meny-prosedyren frem til brukeren avslutter programmet gjennom menyvalg 9
while True:
        meny(regNummer)
