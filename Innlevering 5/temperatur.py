'''
skriver ut gjennomsnittstemperatur fra fil med månedlige temperaturer
'''

# importer for å finne filsti til scriptet og behandle filbane
import sys
import os

# 1
# stien til temperatur.py plassering
pySti = os.path.dirname( sys.argv[0] )

# forutsetter at filen ligger i samme mappe som scriptet
filbane =  os.path.join( pySti, "temperatur.txt" )

# åpne filen og fjern new line for hver linje slik at temperaturene blir en liste
tempAar = [ float( linje.rstrip("\n") ) for linje in open( filbane , "r") ]

# 2
# funksjon gjennomsnitt
def gjennomsnitt(a):

    #return sum(a) / len(a)

    total = 0
    # loop it is
    for x in a:
        total += x

    return total / len(a)

print( "Gjennomsnittstemperatur:", gjennomsnitt(tempAar) )
