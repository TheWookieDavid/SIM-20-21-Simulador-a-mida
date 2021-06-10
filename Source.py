#millor treballar amb define o algun sistema simular a l'enum de C++
from Server import *
from Client import *

class Source:

    def __init__(self, scheduler):
        # inicialitzar element de simulació
        self.entitatsCreades = 0
        self.scheduler = scheduler

    def tractarEsdeveniment(self, event):
        if (event.type == 'SIMULATION_START'):
            self.simulationStart(event)

        elif (event.type == 'NEXT ARRIVAL'):
            self.processNextArrival(event)

    def simulationStart(self, event):
        nou_event = self.properaArribada(event.time - 20)
        self.scheduler.afegirEsdeveniment(nou_event)


    def processNextArrival(self, event):
        nou_event = self.properaArribada(event.time)
        self.scheduler.afegirEsdeveniment(nou_event)

    def properaArribada(self, time):
        # cada quan generem una arribada
        tempsEntreArribades = 20
        # incrementem estadistics si s'escau
        self.entitatsCreades += 1
        # creem client i programació primera arribada
        client = Client(time + tempsEntreArribades)
        return Event(self, 'NEXT ARRIVAL', time + tempsEntreArribades, client)
         