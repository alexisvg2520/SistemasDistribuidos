from __future__ import print_function
from curses import keyname
from glob import escape
from re import T
import Pyro4

class Cliente(object):
    def __init__(self):
        self.bolsas = set()
        self.empresas = set()

    def start(self):
        print("Valor en el Mercado de las Empresas:\n", self.empresas)
        fuentes_mercado = {
            bolsa.name: bolsa.valor() for bolsa in self.bolsas
        }
        while True:
            a= input("Quiere seguir viendo? s/n")
            if a=='n':
                break
            for bolsa, fuente_valor in fuentes_mercado.items():
                valor = next(fuente_valor)  # obtiene un nuevo valor de la empresa de la bolsa
                empresa, value = valor
                if empresa in self.empresas:
                    print("{0}.{1}: {2}".format(bolsa, empresa, value))
                
                



def conectar_bolsa():
    # You can hardcode the stockmarket names for nasdaq and newyork, but it
    # is more flexible if we just look for every available stockmarket.
    bolsas = []
    with Pyro4.locateNS() as ns:
        for bolsa, bolsa_uri in ns.list(prefix="ecu.bolsa.").items():
            print("Bolsa en línea:", bolsa)
            bolsas.append(Pyro4.Proxy(bolsa_uri))
    if not bolsas:
        raise ValueError("La bolsa no se encuentra en línea! \nEspere hasta que vuelva abrir la Bolsa!")
    return bolsas

def menu():
    
	print("\n\nSelecciona una opción")
	print("\t1 - Bolsa por sus intereses")
	print("\t2 - Bolsa de UIO")
	print ("\t3 - Bolsa de GYE")
	print ("\t4 - Salir\n")

def main():
    cliente = Cliente()
    print("*****Bienvenido/a a la BOLSA DE VALORES******\n\n")
    cliente.bolsas = conectar_bolsa()
    while True:
        # Mostramos el menu
        menu()
        # solicituamos una opción al usuario
        opcionMenu = input("Inserta la opción: ")
   
        if opcionMenu=="1":

            print ("")
            input("Ha pulsado la opción 1...\nPulse una tecla para continuar\n")
            cliente.empresas = {"ADELCA", "NESTLE", "COCA-COLA", "La Favorita", "ROLAND"}
            cliente.start()
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
            cliente.empresas = {"La Favorita", "ROLAND", "FYBECA", "MARESA"}
            cliente.start()

        elif opcionMenu=="3":
            print ("")
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")
            cliente.empresas = {"ADELCA", "NESTLE", "COCA-COLA", "EL ROSADO","LA UNIVERSAL"}
            cliente.start()

        elif opcionMenu=="4":
            break

        else:

            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


if __name__ == "__main__":
    main()