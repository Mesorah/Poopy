class Conta:
    def __init__(self, cliente, numero, saldo=0):
        self. cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.transacoes = []

    def deposito(self, valor):
        self.saldo += valor

        self.transacoes.append(['Depósito: ', valor])

        return self.saldo

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

            self.transacoes.append(['Saque: ', valor])

            return self.saldo
        
        return'Saldo insuficiente'

    def resumo(self):
        print(f'N: {self.numero}  Saldo: {self.saldo}')

    def extrato(self):
        print('Extratos')

        for valores in self.transacoes:
            print(valores[0], valores[1])

if __name__ == '__main__':
    p1 = Conta('ga', 1, 300)
    print(p1.deposito(400))
    p1.resumo()
    print(p1.saque(200))
    p1.saque(1000)
    p1.resumo()
    p1.extrato()