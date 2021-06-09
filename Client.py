from Server import *


class Client:
    barber = None
    estat = None

    def __init__(self, id):
        self.barber = None
        self.estat = "Esperant"
