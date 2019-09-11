import socket

import threading

bind_ip = '192.168.15.19'

bind_port = 80

# Socket AF_INET define ipv4 e SOCK_STREAM determina que estamos trabalhando com TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

# Ouve 5 conexões simultaneas
server.listen(5)
print ('[*] Escutando %s:%d \n' %(bind_ip, bind_port))

def handle_client(client_socket):
    request =  client_socket.recv(1024)
    print('[*] Recebido: %s' %request)
    print('\n-----------------\n')
    client_socket.send('Mensagem destinada ao cliente : %s \n' %addr[0])
    client_socket.send('\n ACK! \nRecebido pelo servidor!\n')
    client_socket.close()

while True:
    client, addr = server.accept()
    print('[*] Conexao aceita de: %s %d' %(addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client, ))
    client_handler.start()

