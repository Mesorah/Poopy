from perfil import *

class Loja:
    def __init__(self, perfil):
        self.perfil = perfil
        self.lista_produtos = [
            {'numero_produto': 1, 'preco': 1500},

        ]


    def exibir_produtos(self):
        print('''
[1] Aumentar a energia || R$ 1500
''')
        

    def escolha_produto(self):
        self.exibir_produtos()

        escolha = input('Qual item você irá comprar? ')
        if not self.verifica_numero(escolha):
            print('ue')
        
        else:
            self.compra_produto(int(escolha))

    def compra_produto(self, produto):
        valor_produto = self.lista_produtos[produto - 1]['preco']

        if self.tem_saldo_suficiente(valor_produto):
            pass

        else:
            pass

    def tem_saldo_suficiente(self, valor):
        if self.perfil.dinheiro >= valor:
            self.perfil.dinheiro -= valor

            return True
        
        else:
            print('Valor insuficiente')

            return False
            

    """ Verifica se o que ele mandou é um número """
    def verifica_numero(self, numero):
        for caracter in numero:
            if not caracter.isnumeric():
                return False
            
        return True