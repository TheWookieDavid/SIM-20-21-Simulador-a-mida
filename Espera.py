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
                barber = self.scheduler.getBarberDsiponible()
                if self.ocupacio == 0 and barber is not None:
                    event.entity.estat = "Ates"
                    barber.ocupaBarber()
                    event.entity.barber = barber
                    event.entity.atendreClient(event.time)
                    #ocupa cadira
                    if self.cadires.AgafarCadiraRentar() != -1:
                        self.scheduler.afegirEsdeveniment(Event(self, "ACABEM DE TALLAR", event.time + 30, event.entity))
                else:
                    self.ocupacio += 1
                    self.scheduler.afegirEsdeveniment(Event(self, 'ME CANSAO', event.time + 50, event.entity))
                    self.cua.append(event.entity)
            else:
                self.sinsillas += 1

        elif event.type == "ME CANSAO":
            if self.cua.count(event.entity) > 0:
                self.cua.remove(event.entity)
                self.insatisfets += 1
                self.ocupacio -= 1

        elif event.type == "BARBER LLIURE":
            self.satisfets += 1
            if len(self.cua) > 0:
                client = self.cua.pop(0)
                barber = self.scheduler.getBarberDsiponible()
                self.cadires.DeixarCadiraRentar()
                barber.ocupaBarber()
                client.barber = barber
                client.atendreClient(event.time)
                self.scheduler.afegirEsdeveniment(Event(self, "ACABEM DE TALLAR", event.time + 30, client))








