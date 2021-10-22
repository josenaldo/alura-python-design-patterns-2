from datetime import date
import pytest
from src.contrato import Contrato, Estado, Historico


class TestContrato:

    @pytest.fixture
    def data_do_contrato(self):
        return date.today()

    @pytest.fixture
    def cliente(self):
        return "João Grilo"

    @pytest.fixture
    def contrato_novo(self):
        return "NOVO"

    @pytest.fixture
    def contrato_em_andamento(self):
        return "EM ANDAMENTO"

    @pytest.fixture
    def contrato(self, data_do_contrato, cliente, contrato_novo):
        return Contrato(data_do_contrato, cliente, contrato_novo)

    @pytest.mark.parametrize("tipo_inicial, tipo_final",
                             [("NOVO", "EM ANDAMENTO"), ("EM ANDAMENTO", "ACERTADO"), ("ACERTADO", "CONCLUIDO")])
    def test_contrato_deve_avancar_de_estado(self, data_do_contrato, cliente, tipo_inicial, tipo_final):
        contrato = Contrato(data_do_contrato, cliente, tipo_inicial)
        contrato.avanca()
        assert contrato.tipo == tipo_final

    def test_contrato_deve_salvar_o_estado(self, contrato, data_do_contrato, cliente, contrato_novo):
        estado = contrato.salva_estado()

        assert estado.contrato.data == data_do_contrato
        assert estado.contrato.cliente == cliente
        assert estado.contrato.tipo == contrato_novo

    def test_contrato_deve_restaurar_um_estado(self, contrato, data_do_contrato, cliente, contrato_em_andamento):
        estado = Estado(Contrato(data_do_contrato, cliente, contrato_em_andamento))

        contrato.restaura_estado(estado)

        assert estado.contrato.data == data_do_contrato
        assert estado.contrato.cliente == cliente
        assert estado.contrato.tipo == contrato_em_andamento

    def test_historico_deve_armazenar_estados(self, contrato, contrato_em_andamento):
        historico = Historico()

        historico.adiciona_estado(contrato.salva_estado())
        contrato.avanca()
        historico.adiciona_estado(contrato.salva_estado())
        contrato.avanca()
        historico.adiciona_estado(contrato.salva_estado())

        assert len(historico) == 3

        estado = historico.obtem_estado(1)
        assert estado.contrato.tipo == contrato_em_andamento
