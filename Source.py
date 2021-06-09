#millor treballar amb define o algun sistema simular a l'enum de C++
from Server import *
from Client import *

class Source:

    def __init__(self, scheduler):
        # inicialitzar element de simulació
        self.entitatsCreades = 0
        self.state = "idle"
        self.scheduler = scheduler
    
    def crearConnexio(self, server):
        self.server = server

    def tractarEsdeveniment(self, event):
        if (event.tipus == 'SIMULATION START'):
            self.simulationStart(event)

        if (event.tipus == 'NEXT ARRIVAL'):
            self.processNextArrival()
        ...

    def simulationStart(self, event):
        nou_event = self.properaArribada(0)
        self.scheduler.afegirEsdeveniment(nou_event)


    def processNextArrival(self, event):
        # Cal crear l'entitat 
        entitat = self.crearEntitat(self)
        # Mirar si es pot transferir a on per toqui
        if (self.server.estat == "idle"):
            #transferir entitat (es pot fer amb un esdeveniment immediat o invocant a un métode de l'element)
            self.server.recullEntitat(event.time, entitat)
        else:
            #incrementar entitats perdudes en creació (si s'escau necessari)
            ...
        # Cal programar la següent arribada
        nouEvent = self.properaArribada(event.temps)
        self.scheduler.afegirEsdeveniment(nouEvent)

    def properaArribada(self, time):
        # cada quan generem una arribada (aleatorietat)
        tempsEntreArribades = 20
        # incrementem estadistics si s'escau
        self.entitatsCreades += 1
        self.state = "busy"
        # programació primera arribada
        return Event(self, 'NEXT ARRIVAL', time + tempsEntreArribades, Client)
         