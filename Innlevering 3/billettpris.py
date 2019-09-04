#Prosedyre som beregner billettpris basert på oppgitt alder

def beregn_pris():

    alder = int(input("Skriv inn alder(år): "))

    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 60

    print("Billettpris for oppgitt alder (" + str(alder) + ") : " + str(billettpris) + "kr")


for i in range(0,4):
    beregn_pris()


# Input blir forsøkt konvertert til heltall uten validering av input.
# Hvis bruker oppgir noe annet enn heltall for alder stopper programmet.
