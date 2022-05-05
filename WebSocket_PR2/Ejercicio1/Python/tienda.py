#importar la clase warehouse
from warehouse import Warehouse
#importar la clase  cliente
from cliente import Cliente


nombre = input("Ingrese su nombre Pofavor : ")  

def instancia_nombre ():
    return nombre
   

while True :
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
        warehouse = Warehouse()
        name= Cliente (instancia_nombre())
        name.listar_articulos(warehouse)    
        
    if opcion =='2':
        warehouse = Warehouse()
        name= Cliente (instancia_nombre())
        name.visita(warehouse) 
 
 


  
