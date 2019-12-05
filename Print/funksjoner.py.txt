'''
1. Funksjon som tar to heltall som parameter og returnerer summen
2,3. Funksjon som returnerer antallet forekomster av en bokstav i en streng
'''
# 1
# funksjon adder med to parameter tall1 og tall2
def adder( tall1, tall2):

    # returner summen av heltallene tall1 og tall2
    return int(tall1) + int(tall2)


# kall funksjonen og skriv ut resultatet 5
print( "Summen er",adder(2,3) )

# kall funksjonen og skriv ut resultatet 19
print( "Summen er", adder(10,9) )




# 2,3

# Funksjon som returnerer forekomster av en bokstav i en streng
def tellForekomst(minTekst, minBokstav):

    # initialiser variabelen forekomst med 0 før løkken
    forekomst = 0

    # sjekk om den valgte bokstaven er den samme for hver karakter i tekstrengen
    for karakter in minTekst:
        # hvis sann inkrementer antall forekomster
        if karakter == minBokstav:
            forekomst += 1

    #skriv ut antallet forekomster av bokstaven i tekststrengen
    return "Bokstaven " + minBokstav + " forekommer " + str(forekomst) + " gang(er) i teksten: \n" + minTekst

# Ta en tekstreng som input
minTekst = input("Skriv inn en streng: ")
# ta en bokstav som input
minBokstav = input("Skriv inn en bokstav: ")
# skriv ut resultatet av funksjonen tellForekomst med bokstav og streng som parameter
print( tellForekomst(minTekst, minBokstav) )
