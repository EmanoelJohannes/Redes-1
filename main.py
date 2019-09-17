import socket
from tkinter import *


from client import Client

client = Client()


class Application:
    

    def __init__(self, master=None):
        self.response = ""

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()  

        self.titulo = Label(self.primeiroContainer, text="Comunicação via TCP!")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.descricao = Label(self.primeiroContainer, text="A mensagem será destinada ao servidor!")
        self.descricao["font"] = self.fontePadrao
        self.descricao.pack()

        self.clientLabel = Label(self.segundoContainer, text = "Mensagem:", font = self.fontePadrao)
        self.clientLabel.pack(side=LEFT)

        self.mensagem = Entry(self.segundoContainer)
        self.mensagem["width"] = 30
        self.mensagem["font"] = self.fontePadrao
        self.mensagem.pack(side=LEFT)

        self.enviar = Button(self.terceiroContainer)
        self.enviar["text"] = "Enviar"
        self.enviar["font"] = ("Calibri", "8")
        self.enviar["width"] = 12
        self.enviar["command"] = self.enviarMensagem
        self.enviar.pack()

        self.mensagemLabel = Label(self.terceiroContainer, text= "Mensage vinda do servidor, logo abaixo ", font = self.fontePadrao)
        self.mensagemLabel.pack()

        self.mensagemLabel = Label(self.quartoContainer, text= self.response, font = self.fontePadrao)
        self.mensagemLabel.pack() 

    def enviarMensagem(self):
        mensagem = self.mensagem.get()
        if mensagem != 'Sair':
            self.response = client.enviarMensagem(mensagem)
            self.mensagemLabel.configure(text = self.response)
        else:    
            client.closeConnection()
        print(mensagem)


root = Tk()
Application(root)
root.mainloop()
