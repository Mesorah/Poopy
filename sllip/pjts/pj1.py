class Cadastro:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def verifica_cadastro(self):
        if isinstance(self.nome, str) and isinstance(self.sobrenome, str):
            pass

        else:
            raise TypeError('nome e sobrenome devem ser strings')
    
    @property
    def altera_nome(self):
        return self.nome
    
    @altera_nome.setter
    def altera_nome(self, valor):
        self.nome = valor

    @property
    def altera_sobrenome(self):
        return self.sobrenome
    
    @altera_sobrenome.setter
    def altera_sobrenome(self, valor):
        self.sobrenome = valor

class Banco:
    def __init__(self, nome, sobrenome, saldo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'; Nome: {self.nome!r}, Sobrenome: {self.sobrenome!r}'
        return f'{class_name}{attrs}'

    def atualiza_dados(self):
        pass

    def ver_saldo(self):
        print(self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        
        else:
            print('saldo insuficiente')
    

if __name__ == '__main__':
    cadatro = Cadastro('ga', 'ro')
    cadatro.verifica_cadastro()

    conta_banco = Banco(cadatro.nome, cadatro.sobrenome, 450)
    conta_banco.ver_saldo()

    cadatro.altera_nome = 'gabriel'
    cadatro.altera_sobrenome = 'aguiar'
    print(conta_banco)
    
