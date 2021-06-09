# millor treballar amb define o algun sistema simular a l'enum de C++
from Event import *
from Resources import *


class Server:

    def __init__(self, scheduler, cadires):
        # inicialitzar element de simulació
        self.entitatsTractades = 0
        self.state = "Fora del Treball"
        self.scheduler = scheduler
        self.entitatActiva = None
        self.cadires = cadires

    def recullEntitat(self, time, entitat):
        self.entitatsTractades += 1
        self.programarFinalServei(time, entitat)

    def tractarEsdeveniment(self, event):
        if (event.tipus == 'COMENÇA TORN'):
            self.desocupaBarber(self)

        elif event.type == "ACABEM DE TALLAR":
            if self.cadires.AgafarCadiraRentar() != -1:
                self.cadires.DeixarCadiraTallar()
                self.scheduler.tractarEsdeveniment(Event(self, "ACABA SERVEI", event.time + 10, event.entity))

        elif event.type == "ACABA SERVEI":
            self.state = "En espera"
            self.scheduler.tractarEsdeveniment(Event(self, "BARBER LLIURE", event.time, None))

    def ocupaBarber(self):
        self.state = "Treballant"

    def desocupaBarber(self):
        self.state = "En espera"
    ...
