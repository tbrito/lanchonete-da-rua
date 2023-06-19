from domain.entities.cliente import Cliente

class ClienteService:

    def obter_clientes():
        # Lógica para obter clientes do domínio. Mock:
        clientes = [Cliente("Joao", "12345678901", "1234567890"),
                    Cliente("Maria", "98765432109", "0987654321")]
        return clientes

    def criar_cliente(cliente_data):
        # Lógica para persistir o cliente no domínio
        ...

    def obter_cliente_por_id(cliente_id):
        # Lógica para obter um cliente pelo ID do domínio
        ...

    def atualizar_cliente(cliente_id, cliente_data):
        # Lógica para atualizar um cliente no domínio
        ...

    def deletar_cliente(cliente_id):
        # Lógica para deletar um cliente do domínio
        ...