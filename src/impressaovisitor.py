from abc import ABCMeta, abstractmethod


class ExpressionVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visita_soma(self, soma):
        pass

    @abstractmethod
    def visita_subtracao(self, subtracao):
        pass

    @abstractmethod
    def visita_numero(self, numero):
        pass


class ImpressaoVisitor(ExpressionVisitor):

    def visita_soma(self, soma):
        print("(", end="")
        soma.expressao_esquerda.aceita(self)
        print(" + ", end="")
        soma.expressao_direita.aceita(self)
        print(")", end="")

    def visita_subtracao(self, subtracao):
        print("(", end="")
        subtracao.expressao_esquerda.aceita(self)
        print(" - ", end="")
        subtracao.expressao_direita.aceita(self)
        print(")", end="")

    def visita_numero(self, numero):
        print(numero.avalia(), end="")

class PrefixaVisitor(ExpressionVisitor):

    def visita_soma(self, soma):
        print("+", end="")
        print("(", end="")
        soma.expressao_esquerda.aceita(self)
        print(" , ", end="")
        soma.expressao_direita.aceita(self)
        print(")", end="")

    def visita_subtracao(self, subtracao):
        print("-", end="")
        print("(", end="")
        subtracao.expressao_esquerda.aceita(self)
        print(" , ", end="")
        subtracao.expressao_direita.aceita(self)
        print(")", end="")

    def visita_numero(self, numero):
        print(numero.avalia(), end="")