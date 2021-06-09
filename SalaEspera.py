import queue

from ServerTallar import *
from Event import *
from Person import *


class SalaEspera:
    cuaSala: queue
    cadiresOcupades: int
    clientsMarxat: int
    tempsEsperatTotal: int
    clientsTemp: int

    def __init__(self, scheduler):
        # inicialitzar element de simulació
        self.entitatsTractades = 0
        self.clientsMarxat = 0
        self.cadiresOcupades = 0
        self.tempsEsperatTotal = 0
        self.state = "Sala no plena"
        self.scheduler = scheduler
        self.entitatActiva = None
        self.cuaSala = queue.Queue()
        self.source = None
        self.serverCadiresTallar = None
        self.clientsTemp = 0

    def crearConnexio(self, source, serverTallar):
        self.source = source
        self.serverCadiresTallar = serverTallar

    def recullEntitat(self, event):
        self.tractarEsdeveniment(event)

    def tractarEsdeveniment(self, event):

        if event.type == 'Arribada client':
            self.entitatsTractades += 1
            if self.state == "Sala no plena":
                event.entity.setTempsArribada(event.time)
                event.entity.canviarTemps(0)
                if self.cadiresOcupades == 0 and self.serverCadiresTallar.get_state() != 'busy':
                    event.entity.setTempsCua(event.time)
                    self.serverCadiresTallar.recullEntitat(event.time, event.entity)
                else:
                    event.entity.state = "Esperant en la cua"
                    eventNou = Event(self, "Temporitzador espera", event.time + 50, event.entity)
                    self.cadiresOcupades += 1
                    self.cuaSala.put(event.entity)
                    print("Cua sala: " + str(self.cuaSala.qsize()) + " persones")  # nomes per debugar
                    self.scheduler.afegirEsdeveniment(eventNou)
                    if self.cadiresOcupades == 4:
                        self.state = "Sala plena"

            else:
                print("Client marxa (cua plena)")
                self.clientsMarxat += 1

        if (event.type == 'Temporitzador espera') and (event.entity.state == "Esperant en la cua"):
            self.cuaSala.get()
            self.cadiresOcupades -= 1
            self.state = "Sala no plena"
            self.clientsTemp += 1
            self.tempsEsperatTotal += 50
            print("Client marxa (molt temps esperat)")

        if (event.type in (["Treballador lliure", "Arriba treballador"])) and (self.cadiresOcupades >= 1) and (self.serverCadiresTallar.get_state() != 'busy'):
            p = self.cuaSala.get()
            p.canviarEstat("Sent ates")
            self.cadiresOcupades -= 1
            self.state = "Sala no plena"
            p.setTempsCua(event.time)
            self.tempsEsperatTotal += p.getTempsEsperatCua()
            self.serverCadiresTallar.recullEntitat(event.time, p)


    def simulationStart(self, event):
        self.entitatsTractades = 0
        self.cadiresOcupades = 0
        self.clientsMarxat = 0
        self.state = "Sala no plena"
        self.entitatActiva = None
        self.cuaSala = queue.Queue()

    # FUNCIONS QUE US PODRIEN RESULTAR UTILS

    def salaBuida(self):
        return self.cadiresOcupades == 0

    def getNombreClients(self):
        return self.cadiresOcupades

    def treureClient(self):
        self.cadiresOcupades -= 1
        return self.cuaSala.get()

    def salaPlena(self):
        return self.cadiresOcupades == 4

    def getTempsEsperat(self):
        return self.tempsEsperatTotal

    def getClientsMarxat(self):
        return self.clientsMarxat

    def getClientsCansatsEsperar(self):
        return self.clientsTemp

    def getState(self):
        return self.state

    def changeState(self, new):
        self.state = new

    # def programarFinalServei(self, time, entitat):
    # que triguem a fer un servei (aleatorietat)
    # tempsServei = 720
    # incrementem estadistics si s'escau
    # self.entitatsTractades = self.entitatsTractades + 1
    # self.state = "Peace"
    # programació final servei
    # return Event(self, 'END_SERVICE', time + tempsServei, entitat)

    # def processarFiServei(self, event):
    # Registrar estadístics
    # self.entitatsTractades = self.entitatsTractades + 1
    # Mirar si es pot transferir a on per toqui
    # if (server.state == "idle"):
    # transferir entitat (es pot fer amb un esdeveniment immediat o invocant a un métode de l'element)
    # server.recullEntitat(event.time, event.entitat)
    # else:
    # if (queue.state == "idle"):
    # queue.recullEntitat(event.time, event.entitat)
    # ...
    # self.state = idle
