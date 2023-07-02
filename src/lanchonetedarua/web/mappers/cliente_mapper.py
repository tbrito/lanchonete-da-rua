from web.resources.clientes.output.ObterClientesOutput import ObterClientesOutput
from domain.entities.cliente import Cliente

class ClienteMapper:

    @staticmethod
    def cliente_dominio_para_resposta(cliente_dominio : Cliente):
        return ObterClientesOutput(cliente_dominio.id, cliente_dominio.nome, cliente_dominio.cpf.valor, cliente_dominio.telefone, cliente_dominio.created_at)

