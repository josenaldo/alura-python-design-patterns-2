from abc import ABCMeta, abstractmethod

from src.impressaovisitor import ImpressaoVisitor, PrefixaVisitor


class Expressao(metaclass=ABCMeta):

    @abstractmethod
    def avalia(self):
        pass

    @abstractmethod
    def aceita(self, visitor):
        pass


class Subtracao(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        """Construtor de Subtracao """
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

    def aceita(self, visitor):
        return visitor.visita_subtracao(self)


class Soma(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        """Construtor de Adicao """
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()

    def aceita(self, visitor):
        return visitor.visita_soma(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita


class Numero(Expressao):
    """Classe que representa um número"""

    def __init__(self, numero):
        """Construtor de Numero"""
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        return visitor.visita_numero(self)


if __name__ == '__main__':
    exp_esquerda = Soma(Numero(10), Numero(20))
    exp_direita = Subtracao(Numero(7), Numero(2))
    exp_conta = Subtracao(exp_esquerda, exp_direita)
    resultado = exp_conta.avalia()

    impressao = ImpressaoVisitor()
    exp_conta.aceita(impressao)

    print(f" = {resultado}")

    prefixa = PrefixaVisitor()
    exp_conta.aceita(prefixa)