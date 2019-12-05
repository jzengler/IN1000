# importer klassen Motorsykkel fra motorsykkel.py
from motorsykkel import Motorsykkel

def hovedprogram():

    # opprett objekter av klassen Motorsykkel
    kawasaki = Motorsykkel("Kawasaki", "FW1234", 12000)
    honda = Motorsykkel("Honda", "FT1414", 6000)
    ducati = Motorsykkel("Ducati", "LY1337", 2500)

    # kall metoden skrivUt til objektene
    kawasaki.skrivUt()
    honda.skrivUt()
    ducati.skrivUt()

    # øk kilometerstand på objektet Ducati
    ducati.kjor(10)

    # hent kilometerstand fra objektet Ducati
    print("Ny kilometerstand:", ducati.hentKilometerstand() )

# kall hovedprogram
hovedprogram()
