'''
scriptet demonstrerer bruk av løkker og nøstede lister
Det tas brukerinput for å lagre fem steder, klesplagg og avreisedatoer i separate lister
Disse tre listene lagres i en nøstet liste, reiseplan
Deretter tas det brukerinput for å velge element i den nøstede listen reiseplan
'''

#INIT
# oppretter liste for steder
steder = []
# oppretter liste for klesplagg
klesplagg = []
# oppretter liste for avreisedatoer
avreisedatoer = []
# oppretter liste for reiseplan
reiseplan = []

# løkke for å legge til inntil 5 destinasjoner, klessplagg og avreisedatoer
for i in range(0,5):
    # legger til sted
    steder.append( input("Legg til reisemål " + str(i + 1) + " av 5: ").title() )

for i in range(0,5):
    # legger til klessplagg
    klesplagg.append( input("Legg til klesplagg " + str(i + 1) + " av 5: ").lower() )

for i in range(0,5):
    #legg til avreisedato
    avreisedatoer.append( input("Legg til avreisedato [dd.mm.yy] " + str(i + 1) + " av 5: "))

# lager en nøstet liste av steder, klesplagg, avreisedatoer
reiseplan = [steder], [klesplagg], [avreisedatoer]

# skriver ut hver liste i reiseplan
for liste in reiseplan:
    print(liste)

# Ta input fra bruker for å bestemme liste og element, hhv i1 og i2
i1 = int( input("Hvilken liste vil du lese? Skriv inn indeks [0-" + str( len(reiseplan) - 1 ) + "]: ") )
i2 = int( input("Hvilket element vil du lese? Skriv inn indeks [0-" + str( len(steder) - 1) + "]: ") )

# hvis i1 og i2 er gyldige indekser
if i1 in range(0, len(reiseplan)) and i2 in range(0, len(steder)):
    print(reiseplan[i1][i2])

# hvis ikke go bruker tilbakemelding
else:
    print("Ugyldig input!")
