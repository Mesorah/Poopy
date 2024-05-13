class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone



if __name__ == '__main__':
    cliente = Cliente('ga', '23')
    print(cliente.nome)
    print(cliente.telefone)
