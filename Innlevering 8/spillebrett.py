from random import randint
from celle import Celle
from os import system,name


class Spillebrett:

    ### konstruktør
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjon = 0
        self._rutenett = []

        # opprett spillebrett
        for y in range(rader):
            self._rutenett.append([])

            for x in range(kolonner):
                self._rutenett[y].append( Celle() )

        # generer spillebrett
        self._generer()



    ### tegn spillebrettet i terminalvinduet
    def tegnBrett(self):
        # "scroller" terminalvinduet
        #print('\x1b[2J')
        system('cls' if name == 'nt' else 'clear')

        #skriver ut spillebrettet
        print("### The Game of Life ###\n")

        for rad in self._rutenett:
            for celle in rad:
                print( "|" + celle.hentStatusTegn(), end="")
            print("|")

        print("Generasjon:", self._generasjon)
        print("Antall levende celler:", self.finnAntallLevende())


    ### oppdaterer cellestatus og generasjonsnummer
    def oppdatering(self):
        nyeLevende = []
        nyeDoede = []

        # finn neste status for alle celler
        for y in range(0, self._rader):
            for x in range(0, self._kolonner):

                # lagre minneadresse til celle for lesbarhet
                celle = self._rutenett[y][x]

                # teller for levende naboer
                lever = 0

                # tell alle levende naboer
                for nabo in self.finnNabo(y,x):
                    if nabo.erLevende():
                        lever += 1

                # cellen er allerede i live
                if celle.erLevende():

                    if lever > 3 or lever < 2:
                        nyeDoede.append(celle)
                    elif lever in [2,3]:
                        nyeLevende.append(celle)

                # cellen er dø fra før
                else:
                    if lever == 3:
                        nyeLevende.append(celle)

        # oppdater statusen til alle celler
        for celle in nyeLevende:
            celle.settLevende()

        for celle in nyeDoede:
            celle.settDoed()

        # inkrementer generasjon
        self._generasjon += 1


    ### returner antall levende celler
    def finnAntallLevende(self):
        antallLevende = 0

        for rad in self._rutenett:
            for celle in rad:
                if celle.erLevende():
                    antallLevende += 1

        return antallLevende


    ### sett tilfeldig cellestatus
    def _generer(self):

        for rad in self._rutenett:
            for celle in rad:
                tilfeldig = randint(0,2)

                # 33% sannsynlighet for levende
                if tilfeldig == 0:
                    celle.settLevende()
                else:
                    celle.settDoed()

    ### returner alle naboer
    def finnNabo(self, rad, kolonne):

        naboer = []

        # iterer gjennoom hver nabo fra venstre over til høyre nedenfor
        # antall naboer begrenses av spillebrettets ytterkanter
        for y in range(max(0, rad - 1), min(rad + 2, self._rader) ):
            for x in range( max(0, kolonne - 1), min(kolonne + 2, self._kolonner) ):

                # utelater seg selv i listen over naboer
                if self._rutenett[y][x] != self._rutenett[rad][kolonne]:
                    naboer.append(self._rutenett[y][x])

        return naboer
