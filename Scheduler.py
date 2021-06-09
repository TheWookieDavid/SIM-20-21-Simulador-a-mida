from Espera import *
from Server import *
from Source import *
from Event import *
from Client import*
from Resources import *

class Scheduler:

    currentTime = 0
    eventList = []
    tempsMigCua = 0

    
    def __init__(self):
        # creació dels objectes que composen el meu model
        self.cadires = Resources()
        self.source = Source(self)
        self.barber = Server(self, self.cadires)
        self.queue = Espera(self, self.cadires)
        self.barber2 = Server(self, self.cadires)
        self.barber3 = Server(self, self.cadires)
        
        self.simulationStart = Event(self, 'SIMULATION_START', 0, None)
        self.eventList.append(self.simulationStart)

    def run(self):
        #rellotge de simulacio a 0
        self.currentTime=0        
        #bucle de simulació (condició fi simulació llista buida)
        while self.eventList:
            #recuperem event simulacio
            event = self.eventList.pop(0)
            #actualitzem el rellotge de simulacio
            self.currentTime=event.time
            # deleguem l'acció a realitzar de l'esdeveniment a l'objecte que l'ha generat
            # també podríem delegar l'acció a un altre objecte
            self.tractarEsdeveniment(event)
        
        #recollida d'estadístics
        self.recollirEstadistics()

    def afegirEsdeveniment(self, event):
        #inserir esdeveniment de forma ordenada
        self.eventList.append(event)
        self.eventList.sort(key=lambda event: event.time)

    def tractarEsdeveniment(self, event):
        if event.type == "SIMULATION_START":
            # comunicar a tots els objectes que cal preparar-se
            self.source.tractarEsdeveniment(event)
            self.afegirEsdeveniment((Event(self, 'FI SIMULACIO', event.time + 720, None)))
            self.afegirEsdeveniment((Event(self, 'COMENÇA TORN', event.time, self.barber)))
            self.afegirEsdeveniment(Event(self, 'COMENÇA TORN', event.time + 180, self.barber2))
            self.afegirEsdeveniment(Event(self, 'COMENÇA TORN', event.time + 420, self.barber3))
        if event.type == "NEXT ARRIVAL":
            self.queue.tractarEsdeveniment(event)
            self.source.tractarEsdeveniment(event)
        if event.type == "ME CANSAO":
            self.calculaMitjana(event.entity)
            self.queue.tractarEsdeveniment(event)
        if event.type == "ACABEM DE TALLAR":
            event.entity.barber.tractarEsdeveniment(event)
        if event.type == "ACABA SERVEI":
            self.calculaMitjana(event.entity)
            event.entity.barber.tractarEsdeveniment(event)
        if event.type == "BARBER LLIURE":
            self.queue.tractarEsdeveniment(event)
        if event.type == "FI SIMULACIO":
            self.eventList.clear()

        if event.type == "COMENÇA TORN":
            event.entity.tractarEsdeveniment(event)

    def calculaMitjana(self, client):
        clientsTotals = self.queue.satisfets + self.queue.insatisfets
        tempsCua = client.tempsAtendre - client.tempsArribada
        if client.tempsAtendre != 0:
            self.tempsMigCua = (((self.tempsMigCua * clientsTotals) + tempsCua) / (clientsTotals + 1))
        else:
            self.tempsMigCua = (((self.tempsMigCua * clientsTotals) + 50) / (clientsTotals + 1))

    def recollirEstadistics(self):
        print("Entitats creades: {0}".format(self.source.entitatsCreades))
        print("Clients satisfets: {0}".format(self.queue.satisfets))
        print("Clients que han marxat després d'esperar 50min: {0}".format(self.queue.insatisfets))
        print("Clients que han marxat per que la sala d'espera era plena: {0}".format(self.queue.sinsillas))
        print("Temps mig que passa un client a la cua: {0}".format(self.tempsMigCua))

    def getBarberDsiponible(self):
        if self.barber.state == "En espera":
            return self.barber
        elif self.barber2.state == "En espera":
            return self.barber2
        elif self.barber3.state == "En espera":
            return self.barber3
        else : return None

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
