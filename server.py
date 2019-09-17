
import socket

HOST = 'localhost'

PORT = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

server.bind(orig)

server.listen(1)

print("Escutando %s:%d \n" %(HOST, PORT))

while True:
    con, cliente = server.accept()
    print('Conectado por ', cliente)

    while True:
        msg = con.recv(1024)
        if not(msg): break
        print("Mensagem enviada via cliente: ", msg)
        con.sendall(msg)


    print('Finalizando conexao do cliente', cliente)
    con.close()