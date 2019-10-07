# importer klassen Hund
from hund import Hund

def hovedprogram():

    # opprett objekt ipa fra klassen Hund
    ipa = Hund(2, 18)

    # kall metoden spring og skriv ut vekt
    ipa.spring()
    print( "Hunden veier", ipa.hentVekt(), "kg" )

    # kall metoden spring og skriv ut vekt
    ipa.spring()
    print( "Hunden veier", ipa.hentVekt(), "kg" )

    # kall metoden spis og skriv ut vekt
    ipa.spis(1)
    print( "Hunden veier", ipa.hentVekt(), "kg" )

    # kall metoden spring og skriv ut vekt
    ipa.spis(1)
    print( "Hunden veier", ipa.hentVekt(), "kg" )


hovedprogram()
