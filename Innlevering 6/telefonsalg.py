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

def maanedensSalgsperson(salgsliste):

    s = max(salgsliste, key=salgsliste.get)

    print("Maanedens ansatte er", s, "med", salgsliste[s], "salg")


def totaltAntallSalg(salgsliste):

    return sum( salgsliste.values() )


def gjennomsnittSalg(salgsliste):

    return totaltAntallSalg(salgsliste) / len( salgsliste.keys() )

def hovedprogram():

    filnavn = "salgstall.txt"
    salgsliste = innlesing(filnavn)

    maanedensSalgsperson(salgsliste)

    print("\nAktive selgere denne maaneden: ", len( salgsliste.keys() ) )
    print( "Totalt antall salg:", totaltAntallSalg(salgsliste) )
    print( "gjennomsnittlig antall salg per salgsperson:", gjennomsnittSalg(salgsliste) )

hovedprogram()
