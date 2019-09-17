import socket

class Client:
    
    def __init__(self):
        HOST = 'localhost'

        PORT = 80

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        dest = (HOST, PORT)

        self.client.connect(dest)

    def enviarMensagem(self, msg):
        self.client.sendall(msg.encode('utf-8'))
        response = self.client.recv(4096)
        return response
            

    def closeConnection():
        client.close()