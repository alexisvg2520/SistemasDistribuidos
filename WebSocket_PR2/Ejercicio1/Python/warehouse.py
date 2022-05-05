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