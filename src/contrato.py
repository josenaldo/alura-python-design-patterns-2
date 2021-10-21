class Contrato:

    def __init__(self, data, cliente, tipo):
        self.data = data
        self.cliente = cliente
        self.tipo = tipo

    def __eq__(self, other):
        return self.data == other.data and self.cliente == other.cliente and self.tipo == other.tipo

    def __repr__(self):
        return f"Contrato(data='{self.data}', cliente='{self.cliente}', tipo='{self.tipo}')"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        self.__cliente = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    def avanca(self):
        if self.tipo == "NOVO":
            self.tipo = "EM ANDAMENTO"
        elif self.tipo == "EM ANDAMENTO":
            self.tipo = "ACERTADO"
        elif self.tipo == "ACERTADO":
            self.tipo = "CONCLUIDO"

    def salva_estado(self):
        contrato = Contrato(self.data, self.cliente, self.tipo)
        return Estado(contrato)

    def restaura_estado(self, estado):
        self.data = estado.contrato.data
        self.cliente = estado.contrato.cliente
        self.tipo = estado.contrato.tipo


class Estado:
    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato


class Historico:

    def __init__(self,):
        self.__estados_salvos = []

    def __len__(self):
        return len(self.__estados_salvos)

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)
