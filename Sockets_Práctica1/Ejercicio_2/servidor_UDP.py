# Sistemas Distribuidos    Fecha: 07/04/2022 
# Práctica 1 : Ejercicio 2
# Tema: Sockets UDP
import socket
PORT=2113
#socket - creamos el socket en el cual servirá para la comunicación
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s: 
    print("Esperando conexion")
    #Declaración del socket con su HOST y Puerto
    s.bind(('',PORT))
    conn,addr=s.accept()
    with conn:
        print(f"Conectado al cliente {addr}")
        #Creación del bucle para recibir datos
        while True:
            data=conn.recv(1024)
            if not data:
                break
            else:
                #Imprime los datos recibidos del cliente
                print('[*] Datos recibidos: {}'.format(data.decode('utf-8')))
            conn.sendall(data)