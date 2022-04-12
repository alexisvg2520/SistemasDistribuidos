# Sistemas Distribuidos    Fecha: 07/04/2022 
# Práctica 1 : Ejercicio 1
# Tema: Sockets 
import socket
HOST=''
PORT=2113
#socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: 
    print("Esperando conexion")
    s.bind((HOST,PORT))
    # Recibe la conexión hasta 5 intentos
    s.listen(5)
    
    conn,addr=s.accept()
    with conn:
        print(f"Conectado al cliente {addr}")
        #Creación del bucle para recibir datos
        while True:
            data=conn.recv(1024)
            if not data:
                break
            else:
                print('[*] Datos recibidos: {}'.format(data.decode('utf-8')))
            conn.sendall(data)