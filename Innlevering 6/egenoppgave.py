'''
Skriv en klasse Person med en konstruktør som tar imot navn og alder.
I tillegg skal konstruktøren ha en tom liste hobbyer.
Skriv en metode leggTilHobby som tar imot en tekststreng og legger den til i hobbyer-listen.
Skriv også en metode skrivHobbyer.
Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUtsom i tillegg til å skrive ut navn og alder kaller på metoden skrivHobbyer.
La brukeren skrive inn navn og alder, og lag et Person-objekt med informasjonen du får.
Deretter skal brukeren ved hjelp av en løkke få legge til så mange hobbyer de vil.
Når brukeren ikke lenger ønsker å oppgi hobbyer skal statistikk om brukeren skrives ut.
'''

# klasse definisjon
class Person:

    # konstrutør med instansvariabler
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    # metode for å legge til hobby
    def leggTilHobby(self, hobby):

        self._hobbyer.append(hobby)

    # metode for å skrive ut hobbyer
    def skrivHobbyer(self):

        print( ",".join(self._hobbyer) )

    # metode for å skrive ut informasjon om objektet
    def skrivUtsom(self):

        print( self._navn, "er", self._alder, "år gammel")
        print( "Hobbyene til", self._navn, "er:" )
        self.skrivHobbyer()

# definisjon av hovedprogram
def hovedprogram():

    # ta navn og alder fra brukerinput
    navn = input( "Skriv inn navn: " ).title()
    alder = int( input( "Skriv inn alder: " ) )

    # opprett objekt av klassen Person
    person = Person(navn, alder)

    # løkke-variabel for fortsette while
    leggTil = "ja"

    # while-løkke for å legge til hobby
    while leggTil == "ja":

        # ta hobby fra brukerinput
        hobby = input( "\nSkriv inn en hobby: " ).title()
        # kall instansmetode for å legge til hobby
        person.leggTilHobby(hobby)

        # spør om bruker vil legge til enda en hoobby
        leggTil = input( "\nVil du legge til en hobby? [ja] " ).lower()

    # skriv ut informasjon om objekt når bruker er ferdig
    person.skrivUtsom()

# kall hovedprogram
hovedprogram()
