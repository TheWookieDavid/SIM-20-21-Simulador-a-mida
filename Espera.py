from Event import *
from Person import *
from Resources import *
from Client import *


class Espera:

    def __init__(self, scheduler, cadires):
        self.ocupacio = 0
        self.scheduler = scheduler
        self.cua = []
        self.satisfets = 0
        self.insatisfets = 0
        self.sinsillas = 0
        self.cadires = cadires

    def tractarEsdeveniment(self, event):
        if event.type == "NEXT ARRIVAL":
            if self.ocupacio < 4:
                self.ocupacio += 1
                self.scheduler.tractarEsdeveniment(Event(self, 'ME CANSAO', event.time + 50, event.entity))
                barber = self.scheduler.getBarberDsiponible()
                if self.ocupacio == 1 and barber is not None:
                    event.entity.estat = "Ates"
                    self.cua.pop(0)
                    barber.ocupaBarber()
                    event.entity.barber = barber
                    #ocupa cadira
                    if self.cadires.AgafarCadiraRentar() != -1:
                        self.scheduler.tractarEsdeveniment(Event(self, "ACABEM DE TALLAR", event.time + 30, event.entity))
            else:
                print("Marxa un client per que la cua està plena")
                self.sinsillas += 1

        elif event.type == "ME CANSAO":
            if event.entity.estat == "Esperant":
                #self.cua.remove(event.entity)
                print("Algú marxa insatisfet de la sala d'espera")
                self.insatisfets += 1
                self.ocupacio -= 1

        elif event.type == "BARBER LLIURE":
            self.satisfets += 1
            client = self.cua.pop(0)
            barber = self.scheduler.getBarberDsiponible()
            client.barber = barber
            self.cadires.DeixarCadiraRentar()
            barber.ocupaBarber()
            self.scheduler.tractarEsdeveniment(Event(self, "ACABEM DE TALLAR", event.time + 30, client))








