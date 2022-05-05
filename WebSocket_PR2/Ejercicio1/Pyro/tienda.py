#importar la clase warehouse
from warehouse import Warehouse
#importar la clase  cliente
from cliente import Cliente
#Importar la libreria para utilizar pyro
import Pyro4

# consumo del servidor de nombres
tienda = Pyro4.Proxy("PYRONAME:almacen.1")    # use name server object lookup uri shortcut


nombre = input("Ingrese su nombre Pofavor : ")  
#funcion para guardar el nombre
def instancia_nombre ():
    return nombre
   
#Menu iterativo para el cliente con cbucle infinito
while True :
    #menu de opciones
    print(" ")
    print("***********COMPUTRONIX********************")  
    print("Digite la Opcion deseada:")
    print("1.-Listar Productos Disponibles ")
    print("2.-Agregar un articulo y dejar un articulo ")
    print("3.-Salir")
    opcion = input("Digite la Opcion:")
    if opcion == '3':
        break
    if opcion =='1':
        #instancias a las clases
        warehouse = Warehouse()
        name= Cliente (instancia_nombre())
        name.listar_articulos(warehouse)    
        
    if opcion =='2':
        #instancias a las clases
        warehouse = Warehouse()
        name= Cliente (instancia_nombre())
        name.visita(warehouse) 
 
 


  
