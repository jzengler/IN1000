'''
Scriptet tar for seg funksjoner for regneoperasjoner addisjon, subtraksjon, divisjon og konvertering fra tommer til cm.
Det demonstrerer også bruk av assert for å teste resultatet av funksjonene.
'''

# 1.
# funksjon for addisjon
def addisjon(a, b):
    return a + b

# skriv ut resultatet av addisjon
print("Sum", addisjon(2,3))

# 2.
#funksjon for subtraksjon
def subtraksjon(a, b):
    return a - b

#test subtraksjon med positive og negative heltall
assert subtraksjon(12, 3) == 9, "forventet 9, fikk " + str(subtraksjon(12,3))
assert subtraksjon(-12, -3) == -9, "forventet -9, fikk " + str(subtraksjon(-12,-3))
assert subtraksjon(12, -3) == 15, "forventet 15, fikk " + str(subtraksjon(12,-3))

#funksjon for divisjon
def divisjon(a, b):
    return a / b

# divisjon med positive og negative heltall
assert divisjon(25,5) == 5, "forventet 5 returnerte " + str(divisjon(25,5))
assert divisjon(-25,-5) == 5, "forventet 5 returnerte " + str(divisjon(-25,-5))
assert divisjon(25,-5) == -5, "forventet 5 returnerte " + str(divisjon(25,-5))

# 3.
#funksjon for å konvertere tommer til cm
def tommerTilCm(tommer):
    assert tommer > 0, "parameter maa være storre enn 0"

    return tommer * 2.54

assert tommerTilCm(4) == 10.16, "Forventet 10.16cm fikk " + str(tommerTilCm(4)) + "\""
print( str(tommerTilCm(2)) + "cm")

# 4.
# Prosedyre for å ta brukerinput og skrive ut resultatet av funksjonene over
def skrivBeregninger():

    # a.
    # ta to flyttall fra bruker
    print( "\nUtregninger:")
    a = float( input( "Skriv inn tall 1: ") )
    b = float( input( "Skriv inn tall 2: ") )

    # skriv ut resultatene
    print( "\nResultat av summering: ", addisjon(a,b) )
    print( "Resultat av subtraksjon: ", subtraksjon(a,b) )
    print( "Resultat av divisjon: ", divisjon(a,b) )

    # b.
    # ta input fra bruker for å kovertere tommer til cm
    print( "\nKonvertering fra tommer til cm:" )
    t = float( input( "Skriv inn ett tall: "))

    # skriv ut tommer konvertert til cm
    print ( "Resultat: ", tommerTilCm(t), "cm")


# kall prosedyren
skrivBeregninger()
