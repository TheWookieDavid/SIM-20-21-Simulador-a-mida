class Person:
    # creació d'una entitat "Persona"
    def __init__(self, temps):
        self.tempsTotal = temps
        self.state = "null"
        self.tempsArribada = None
        self.tempsForaCua = None
        self.tempsEnLaCua = 0

    def canviarEstat(self, nomEstat):
        self.state = nomEstat

    def canviarTemps(self, nouTemps):
        self.tempsTotal = nouTemps

    def getTemps(self):
        return self.tempsTotal

    def setTempsArribada(self, t):
        self.tempsArribada = t

    def getTempsArribada(self):
        return self.tempsArribada

    def setTempsCua(self, timeOutOfWaiting):
        self.tempsForaCua = timeOutOfWaiting
        self.tempsEnLaCua = timeOutOfWaiting - self.tempsArribada

    def getTempsEsperatCua(self):
        return self.tempsEnLaCua

    def getTempsTotalEnBarberia(self):
        return self.tempsEnLaCua + 40