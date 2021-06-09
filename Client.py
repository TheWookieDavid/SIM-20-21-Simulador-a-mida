from Server import *


class Client:
    barber = None
    estat = None
    tempsArribada = None
    tempsAtendre = 0

    def __init__(self, time):
        self.estat = "Esperant"
        self.tempsArribada = time

    def atendreClient(self, time):
        self.tempsAtendre = time
