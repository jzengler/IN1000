# importer urllib
import urllib.request

# filnavn salgstall.txt
def innlesing(filnavn):

    # Opprett tom ordbok til salgstall for selgere
    salg = {}

    # Les fil fra lokal filbane
    with open(filnavn, "r") as salgsfil:

        # split hver linje på mellomrom og fjern newline
        # bruk navn som nøkkel og salgstall som verdi i ordbok
        for selger in salgsfil:
            s = selger.split()
            salg[s[0]] = int(s[1])

    return salg

# proseyre for å skrive ut månedens ansatte
def maanedensSalgsperson(salgsliste):

    # finn maks-verdi i ordboken og lagre nøkkelen i s
    s = max(salgsliste, key=salgsliste.get)

    # skriv ut månedens ansatte, s, og salgstallet fra ordboken salgsliste
    print("Maanedens ansatte er", s, "med", salgsliste[s], "salg")

# funksjon for totalt antall salg
def totaltAntallSalg(salgsliste):

    return sum( salgsliste.values() )

# funksjon for gjennomsnittssalg
def gjennomsnittSalg(salgsliste):

    return totaltAntallSalg(salgsliste) / len( salgsliste.keys() )


def hovedprogram():

    # filnavn
    filnavn = "salgstall.txt"
    # les inn fil til variabel salgsliste
    salgsliste = innlesing(filnavn)

    # kall for å skrive ut månedens salgsperson
    maanedensSalgsperson(salgsliste)

    # utskrift ved bruk av funksjonene for salg
    print("\nAktive selgere denne maaneden: ", len( salgsliste.keys() ) )
    print( "Totalt antall salg:", totaltAntallSalg(salgsliste) )
    print( "gjennomsnittlig antall salg per salgsperson:", gjennomsnittSalg(salgsliste) )

# kall hovedprogram
hovedprogram()
