import socket 

target_host = '192.168.15.19'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send('Olá! Eu sou o cliente e estou me conectando ao servidor')

response = client.recv(4096)

print (response)