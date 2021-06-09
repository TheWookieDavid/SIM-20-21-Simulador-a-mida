from Event import *
from Person import *


class Espera:

    def __init__(self, scheduler):
        self.ocupacio = 0
        self.scheduler = scheduler
        self.cua = []
        self.satisfets = 0
        self.insatisfets = 0
        self.sinsillas = 0

    def tractarEsdeveniment(self, event):
        if event.type == "NEXT ARRIVAL":
            if self.ocupacio < 4:
                self.ocupacio += 1
                self.scheduler.tractarEsdeveniment(Event(self, 'ME CANSAO', event.time + 50, event.entity))
                self.cua.append(event.entity)
                barber = self.scheduler.getBarberDsiponible()
                if self.ocupacio == 1 and barber is not None:
                    self.cua.pop(0)
                    barber.ocupaBarber()
                    #ocupa cadira
                    self.scheduler.tractarEsdeveniment(Event(self, "ACABEM DE TALLAR", event.time + 30, event.entity))
            else:
                print("Marxa un client per que la cua està plena")
                self.sinsillas += 1

        elif event.type == "ME CANSAO":
            if self.cua.count(event.entity) > 0:
                self.cua.remove(event.entity)
                print("Algú marxa insatisfet de la sala d'espera")
                self.insatisfets += 1
                self.ocupacio -= 1

        elif event.type == "ACABA SERVEI":
            self.satisfets += 1
            client = self.cua.pop(0)
            barber = self.scheduler.getBarberDsiponible()
            barber.ocupaBarber()
            #ocupa cadira
            self.scheduler.tractarEsdeveniment(Event(self, "ACABEM DE TALLAR", event.time + 30, client))





