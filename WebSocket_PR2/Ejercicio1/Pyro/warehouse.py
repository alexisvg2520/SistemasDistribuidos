#Libreria para implentar pyro
import Pyro4

#decoradores propios de pyro
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

#clase generica del almacen
class Warehouse(object):
    def __init__(self):
        self.contenido = ["hp", "dell", "usb", "laptop", "ssd"]

    #funcion para mostrar articulos
    def list_contenido(self):
        return self.contenido
    
    # eliminar un articulo
    def eliminar(self, name, item):
        self.contenido.remove(item)
        print("{0} compró el artículo{1}.".format(name, item))
    
    # agregar un nuevo articulo
    def guardar(self, name, item):
        self.contenido.append(item)
        print("{0} dejó el artículo {1}.".format(name, item))
        
#funcion que se ejecuta para el servidor de nombres        
def main():
    daemon = Pyro4.Daemon()                # Hacer un proceso en pyro
    ns = Pyro4.locateNS()                  # Encontrar el nombre del servidor de nombres 
    uri = daemon.register(Warehouse)   # registar la clase como un objeto de pyro
    ns.register("almacen.1", uri)   # registar el objeto con un nombre en el servidor de nombres

    print("LISTO")
    daemon.requestLoop()  


#Ejucion del main 
if __name__=="__main__":
    main()