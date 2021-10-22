from abc import ABCMeta


class Expressao(ABCMeta):

    @staticmethod
    def avalia(self):
        pass


class Subtracao(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        """Construtor de Subtracao """
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()


class Soma(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        """Construtor de Adicao """
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()


class Numero(Expressao):
    """Classe que representa um número"""

    def __init__(self, numero):
        """Construtor de Numero"""
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == '__main__':
    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Soma(Numero(5), Numero(2))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    resultado = expressao_conta.avalia()

    print(f"Resultado: {resultado}")
