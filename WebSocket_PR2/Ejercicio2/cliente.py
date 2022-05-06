from __future__ import print_function
import Pyro4
import keyboard

class Cliente(object):
    #Definición del constructor Cliente el cual entrará a la bolsa
    def __init__(self):
        self.bolsas = set()
        self.empresas = set()

    #Construcción de la función que imprime los valores aleatorios de 
    # cada empresa en la bolsa respectiva
    def start(self):
        print("Valor en el Mercado de las Empresas:\n", self.empresas)
        fuentes_mercado = {
            bolsa.name: bolsa.valor() for bolsa in self.bolsas
        }
        #Creación de un bucle infinito si no se presiona la tecla ESC sale de la ejecución
        while not (keyboard.is_pressed('esc')):
            for bolsa, fuente_valor in fuentes_mercado.items():
                valor = next(fuente_valor)  # obtiene un nuevo valor de la empresa de la bolsa
                empresa, value = valor
                if empresa in self.empresas:
                    print("{0}.{1}: {2}".format(bolsa, empresa, value))
                

#Función que nos permitirá conectarnos a la bolsa de acuerdo a un nombre proporcionado
#el cual ya se encuentra codificado la URI respectiva
def conectar_bolsa():
    #Creamos un array en el cual se guardarán las bolsas en línea
    bolsas = []
    with Pyro4.locateNS() as ns:
        for bolsa, bolsa_uri in ns.list(prefix="ecu.bolsa.").items():
            print("Bolsa en línea:", bolsa)
            bolsas.append(Pyro4.Proxy(bolsa_uri))
    if not bolsas:
        raise ValueError("La bolsa no se encuentra en línea! \nEspere hasta que vuelva abrir la Bolsa!")
    return bolsas

#Creación del Menú
def menu():
	print("\nBOLSA DE VALORES\n\nSelecciona una opción")
	print("\t1 - Bolsa por sus intereses")
	print("\t2 - Bolsa de UIO")
	print ("\t3 - Bolsa de GYE")
	print ("\t4 - Salir\n")

def main():
    #Instanciamos el objeto cliente
    cliente = Cliente()
    print("\n\n******Bienvenido/a al Programa de BOLSA DE VALORES******\n\n")
    cliente.bolsas = conectar_bolsa()
    while True:
        # Mostramos el menu
        menu()
        # solicitamos una opción al usuario
        opcionMenu = input("Inserta la opción: ")
   
        if opcionMenu=="1":
            print ("")
            input("Ha pulsado la opción 1...\n\n****Para salir de la ejecución presione ESC repetidamente***\n\nPulse una tecla para continuar\n")
            #Instanciamos las empresas a ver dentro de la bolsa - preferencia
            cliente.empresas = {"ADELCA", "NESTLE", "La Favorita", "ROLAND"}
            cliente.start()
        
        elif opcionMenu=="2":
            print ("")
            input("Ha pulsado la opción 2...\n\n****Para salir de la ejecución presione ESC repetidamente***\n\nPulse una tecla para continuar\n")
            #Instanciamos las empresas a ver dentro de la bolsa - UIO
            cliente.empresas = {"La Favorita", "ROLAND", "FYBECA", "MARESA"}
            cliente.start()

        elif opcionMenu=="3":
            print ("")
            input("Ha pulsado la opción 3...\n\n****Para salir de la ejecución presione ESC repetidamente***\n\nPulse una tecla para continuar\n")
            #Instanciamos las empresas a ver dentro de la bolsa - GYE
            cliente.empresas = {"ADELCA", "NESTLE", "COCA-COLA", "EL ROSADO","LA UNIVERSAL"}
            cliente.start()
        
        elif opcionMenu=="4":
            break
        
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


if __name__ == "__main__":
    main()