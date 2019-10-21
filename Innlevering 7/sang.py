class Sang:

# konstruktør
    def __init__(self,tittel, artist):
        self._tittel = str(tittel)
        self._artist = str(artist)

# funksjonsmetoder
    def spill(self):
        print("Spiller", self._tittel, "av", self._artist)


    def sjekkArtist(self, navn):
        if any(ord in navn
               for ord in self._artist.split() ):
            return True
        else:
            return False


    def sjekkTittel(self, tittel):
        if str(tittel).lower() == self._tittel.lower():
            return True
        else:
            return False


    def sjekkArtistogTittel(self, artist, tittel):
        if self.sjekkTittel(tittel) and self.sjekkArtist(artist):
            return True
        else:
            return False
