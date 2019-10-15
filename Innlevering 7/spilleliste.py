from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn


    def lesFraFil(self, filnavn):
        with open(filnavn, "r") as spilleliste:
            for spor in spilleliste:
                sang = spor.strip("\r\n").split(";")
                self._sanger.append( Sang(tittel=sang[0], artist=sang[1]) )


    def leggTilSang(self, nySang):
        self._sanger.append(nySang)


    def fjernSang(self, sang):
        self._sanger.remove(sang)


    def spillSang(self, sang):
        sang.spill()


    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()


    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang

    def hentArtistUtvalg(self, artistnavn):
        artistUtvalg = []

        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                artistUtvalg.append(sang)

        return artistUtvalg
