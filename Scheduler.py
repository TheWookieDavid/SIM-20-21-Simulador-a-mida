from Espera import *
from Server import *
from Source import *
from Event import *


class Scheduler:

    currentTime = 0
    eventList = []
    ...
    
    def __init__(self):
        # creació dels objectes que composen el meu model
        self.source = Source(self)
        self.barber = Server(self)
        self.queue = Espera()
        self.barber2 = Server(self)
        self.barber3 = Server(self)

        self.source.crearConnexio(server)
        self.Server.crearConnexio(server2, queue)
        
        self.simulationStart=Event(self,'SIMULATION_START', 0,null))
        self.eventList.append(simulationStart)

    def run(self):
        #configurar el model per consola, arxiu de text...
        self.configurarModel()

        #rellotge de simulacio a 0
        self.currentTime=0        
        #bucle de simulació (condició fi simulació llista buida)
        while self.eventList:
            #recuperem event simulacio
            event=self.eventList.pop(0)
            #actualitzem el rellotge de simulacio
            self.currentTime=event.time
            # deleguem l'acció a realitzar de l'esdeveniment a l'objecte que l'ha generat
            # també podríem delegar l'acció a un altre objecte
            event.objecte.tractarEsdeveniment(event)
        
        #recollida d'estadístics
        self.recollirEstadistics()

    def afegirEsdeveniment(self,event):
        #inserir esdeveniment de forma ordenada
        self.eventList.append(event)

    def tractarEsdeveniment(self, event):
        if event.type == "SIMULATION_START":
            # comunicar a tots els objectes que cal preparar-se
        if event.type == "NEXT ARRIVAL":
            self.queue.tractarEsdeveniment(event)
        if event.type == "ME CANSAO":
            self.queue.tractarEsdeveniment(event)
        if event.type == "ACABEM DE TALLAR":

        if event.type == "ACABA SERVEI":


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