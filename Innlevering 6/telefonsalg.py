# importer urllib
import urllib.request


def innlesing(filnavn):

    # Opprett tom ordbok til salgstall for selgere
    salg = {}

    # Les fil fra lokal filbane
    with open(filnavn, "r") as salgsfil:

        # split hver linje på mellomrom og fjern newline
        # bruk navn som nøkkel og salgstall som verdi i ordbok
        for selger in salgsfil:
            s = selger.rstrip("\n").split(" ")
            salg[s[0]] = int(s[1])

    return salg
