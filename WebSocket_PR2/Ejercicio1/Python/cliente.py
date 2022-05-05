#Define la clase para los clientes
class Cliente(object):
    #constructor de la clase que recive el nombre
    def __init__(self, name):
        self.name = name
    
    #funcion para mostrar las funciones
    def visita(self, warehouse):
        print("Hola {0}!".format(self.name))
        self.deposita(warehouse)
        self.retira(warehouse)
        print("Gracias, vuelva pronto!")

    #Funcion para dejar un articulo
    def deposita(self, warehouse):
        print("El almacén tiene disponible: ", warehouse.list_contenido())
        item = input("Digite el artículo que va a dejar: ").strip()
        if item:
            warehouse.guardar(self.name, item)

    #funcion para retirar un articulo
    def retira(self, warehouse):
        print("El almacén tiene disponible: ", warehouse.list_contenido())
        item = input("Digite el artículo a comprar: ").strip()
        if item:
            warehouse.eliminar(self.name, item)
        print("El almacén tiene disponible: ", warehouse.list_contenido())
    
    #funcion para mostrar los articulos de la tienda        
    def listar_articulos(self, warehouse):
        print("El almacén tiene disponible: ", warehouse.list_contenido())