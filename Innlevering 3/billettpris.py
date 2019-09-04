#Prosedyre som beregner billettpris basert på oppgitt alder

def beregn_pris():

    alder = int(input("Skriv inn alder"))

    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 60

    print("Billettpris for " + str(alder) + "år : " + str(billettpris) +"kr")


for i in range(0,4):
    beregn_pris()
