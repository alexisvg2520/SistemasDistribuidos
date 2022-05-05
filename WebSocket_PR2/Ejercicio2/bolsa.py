from __future__ import print_function
import random
import Pyro4
import time


@Pyro4.expose
class Bolsa(object):
    #Definición del contructor de la BOLSA
    def __init__(self, nombreBolsa, empresa):
        self._name = nombreBolsa
        self._empresa = empresa

    #Operación para la generación de valores aleatorios para cada
    def valor(self):
        while True:
            emp = random.choice(self.empresa)
            yield emp, round(random.uniform(5, 150), 2)
            time.sleep(random.random()/2.0)

    @property
    def name(self):
        return self._name

    @property
    def empresa(self):
        return self._empresa


if __name__ == "__main__":
    quito = Bolsa("UIO", ["La Favorita", "ROLAND", "FYBECA", "MARESA"])
    guayaquil = Bolsa("GYE", ["ADELCA", "NESTLE", "COCA-COLA", "EL ROSADO","LA UNIVERSAL"])
    
    #Ingreso al servidor a través del demonio de Pyro4
    with Pyro4.Daemon() as daemon:
        quito_uri = daemon.register(quito)
        guayaquil_uri = daemon.register(guayaquil)
        with Pyro4.locateNS() as ns:
            ns.register("ecu.bolsa.quito", quito_uri)
            ns.register("ecu.bolsa.guayaquil", guayaquil_uri)
        print("Bolsas en línea...")
        daemon.requestLoop()