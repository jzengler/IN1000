from random import randint
from celle import Celle


class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjon = 0
        self._rutenett = []

        # opprett spillebrett
        for x in range(kolonner):
            self._rutenett.append([])

            for y in range(rader):

                self._rutenett[x].append( Celle() )

        # generer spillebrett
            self._generer()


    def tegnBrett(self):
        print("### The Game of Life ###\n")

        for kolonne in self._rutenett:
            for celle in kolonne:
                print( "|" + celle.hentStatusTegn(), end="")
            print("|")

    def oppdatering(self):
        pass



    def finnAntallLevende(self):
        pass



    def _generer(self):
        for kolonne in self._rutenett:
            for celle in kolonne:
                seed = randint(0,2)

                if seed == 0:
                    celle.settLevende()
                else:
                    celle.settDoed()


    def finnNabo(self, rad, kolonne):
        pass
