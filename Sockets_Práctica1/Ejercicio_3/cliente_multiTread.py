
#codigo del cliente decuado al ejercicio
#y btenido del siguiente sitio web https://recursospython.com/codigos-de-fuente/servidor-tcp-multi-hilo/

from socket import socket
# Conexion que se realiza para poder tener conexion con python3 y se importa la libreria socket
# el raw imput es una funcion mejorada para poder ingresar datos por consola
try:
    raw_input
except NameError:
    raw_input = input
    
#creacion de la funcion principal   
def main():
    #creacion de la conexion por medio del socket
    s = socket()
    s.connect(("172.17.37.141", 2113))
    # bucle infinito para la entrada de datos 
    while True:
        output_data = raw_input("> ")
        
        #creacion de excepcion en caso de que exista un error.
        if output_data:
    
            try:
                s.sendall(output_data)
            except TypeError:
                s.sendall(bytes(output_data, "utf-8"))
            
            # imprmir lo que el servidor reenvia como es tipo eco debe renviarse 
            #el mismo mensaje que se envia 
            input_data = s.recv(1024)
            if input_data:

                print(input_data.decode("utf-8") if
                      isinstance(input_data, bytes) else input_data)
if __name__ == "__main__":
    main()