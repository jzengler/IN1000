'''
skriver ut gjennomsnittstemperatur fra fil med månedlige temperaturer
'''

# importer urllib
import urllib.request

# Url til fil med temperaturer
oblig_url = "https://www.uio.no/studier/emner/matnat/ifi/IN1000/h19/Obligatoriske-innleveringer/temperatur.txt"
# åpne url-filen med urllib
respons = urllib.request.urlopen(oblig_url)

# tom liste for å holde temperaturene
tempAar = []
# legg til hver temperatur som flyttal i listen
for linje in respons:
    tempAar.append( float(linje) )

# 2
# funksjon gjennomsnitt
def gjennomsnitt(a):

    # kortvarianten
    #return sum(a) / len(a)

    # startverdi for gjennomsnittsberegning
    total = 0
    # summer elementene i tempAar
    for x in a:
        total += x

    # returner summen av temperaturene delt på antallet oppføringer
    return total / len(a)

# Skriv gjennomsnittstemperaturen ved å kalle på funksjonen gjenomsnitt
print( "Gjennomsnittstemperatur:", gjennomsnitt(tempAar) )
