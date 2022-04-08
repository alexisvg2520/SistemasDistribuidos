"""
Grupo N1
CLIENTE SOCKET TCP/IP

"""
#creacion del cliente 
#importar la libreria socket

import socket
#declarar las variables
HOST="172.17.36.51"
PORT=2113
#establecer la conexion
with  socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s :
   #REALIZAR LA CONEXION
    s.connect((HOST,PORT))
    #LECTURA DE DATOS DEL SERVIDOR
    s.sendall(b'Enviando un mensaje con eco al servidor UDP  ')
    data=s.recv(1024)

print(f" Conexion exitosa al servidor UPD  Se recibio \n {data!r}")