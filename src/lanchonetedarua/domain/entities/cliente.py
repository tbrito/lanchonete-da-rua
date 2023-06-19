class Cliente(Entity):
    def __init__(self, id, nome, cpf):
        super().__init__(id)
        self.nome = nome
        self.cpf = cpf