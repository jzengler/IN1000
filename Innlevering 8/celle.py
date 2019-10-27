class Celle:

    # Konstruktør
    def __init__(self):

        # false = "død", true = "levende"​
        self._status = False

    # Endre status
    def settDoed(self):
        self._status = False


    def settLevende(self):
        self._status = True


    # Hente status
    def erLevende(self):

        return self._status


    def hentStatusTegn(self):
        
        if self._status == True:
            return "O"
        else:
            return "."
