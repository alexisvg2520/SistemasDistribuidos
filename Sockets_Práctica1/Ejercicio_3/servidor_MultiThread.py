# Sistemas Distribuidos    Fecha: 07/04/2022 
# Práctica 1 : Ejercicio 3
# Tema: Sockets Multihilo

from socket import socket, error
from threading import Thread
class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """
    
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        self.conn = conn
        self.addr = addr
    
    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    self.conn.send(input_data)
def main():
    s = socket()
    
    # Escuchar peticiones en el puerto 2113.
    s.bind(('', 2113))
    s.listen(0)
    
    while True:
        print('\nEsperando Conexion...')
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)

if __name__ == "__main__":
    main()