from spillebrett import Spillebrett


def main():

    print("Oppgi dimensjoner på spillebrettet")
    kolonner = int( input("Antall kolonner: ") )
    rader = int( input("Antall rader: ") )

    nyttSpill = Spillebrett(rader,kolonner)
    nyttSpill.tegnBrett()
    #naboer = nyttSpill.finnNabo(1,0)


    while( input("Trykk [q] for aa avslutte\nTrykk [enter] for aa fortsette\n").lower() != "q" ):
        nyttSpill.oppdatering()
        nyttSpill.tegnBrett()

main()
