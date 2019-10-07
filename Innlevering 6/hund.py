class Hund:

    # konstruktør for klassen Hund
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        #instansvariabel metthet
        self._metthet = 10

    # metode for å hente alder
    def hentAlder(self):

        return self._alder

    # metode for å hente vekt
    def hentVekt(self):

        return self._vekt

    # metode for å springe. reduserer metthet og vekt hvis metthet er mindre enn 5
    def spring(self):

        self._metthet -= 1

        if self._metthet < 5:
            self._vekt -= 1

    # metode for å spise. Øker metthet og vekt hvis metthet er større en 7
    def spis(self, mettet):

        self._metthet += mettet

        if self._metthet > 7:
            self._vekt += 1
