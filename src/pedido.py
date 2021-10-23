from datetime import date
from abc import ABCMeta, abstractmethod


class Pedido(object):
    """Classe que representa um pedido"""
    
    def __init__(self, cliente, valor):
        """Construtor de Pedido"""
        self.__cliente = cliente
        self.__valor  = valor
        self.__status = "NOVO"
        self.__data_finalizacao = None

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao

    def paga(self):
        self.__status = "PAGO"

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = "ENTREGUE"


class Comando(metaclass=ABCMeta):
    """Classe que representa um comando"""

    @abstractmethod
    def executa(self):
        pass


class ConcluiPedido(Comando):
    """Classe que representa um comando para finalizar um pedido"""

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()


class PagaPedido(Comando):
    """Classe que representa um comando para pagar um pedido"""

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


class FilaDeTrabalho:
    """Classe que representa uma fila de trabalho"""
    def __init__(self):
        """Construtor de FilaDeTrabalho"""
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


if __name__ == '__main__':
    pedido1 = Pedido("Flávio", 200)
    pedido2 = Pedido("Almeida", 400)

    fila_de_trabalho = FilaDeTrabalho()

    comando1 = ConcluiPedido(pedido1)
    comando2 = ConcluiPedido(pedido1)
    comando3 = ConcluiPedido(pedido2)

    fila_de_trabalho.adiciona(comando1)
    fila_de_trabalho.adiciona(comando2)
    fila_de_trabalho.adiciona(comando3)

    fila_de_trabalho.processa()


