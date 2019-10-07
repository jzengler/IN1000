
# definer klassen Motorsykkel
class Motorsykkel:

    # konstruktør for klassen Motorsykkel
    def __init__(self, merke, regNummer, kmStand):
        self._merke = merke
        self._regNummer = regNummer
        self._kmStand = kmStand

    # metode for å øke kilometerstand
    def kjor(self, km):
        self._kmStand += km

    # metode for å hente kilometerstand
    def hentKilometerstand(self):
        return self._kmStand

    # metode for å skrive ut informasjon om objektet
    def skrivUt(self):

        print("\n" + self._merke)
        print(self._regNummer)
        print(self._kmStand)
