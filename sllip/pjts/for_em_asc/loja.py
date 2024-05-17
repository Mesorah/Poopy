class Loja:
    def __init__(self):
        self.lista_produtos = [
            {'numero_produto': 1, 'preco': 1500},

        ]


    def exibir_produtos(self):
        print('''
[1] Aumentar a energia || R$ 1500
''')
        

    def escolha_produto(self):
        escolha = input('Qual item você irá comprar? ')
        if not self.verifica_numero(escolha):
            print('ue')
        
        else:
            self.compra_produto(int(escolha))

    def compra_produto(self, produto):
        numero_produto = self.lista_produtos[produto]['preco']

        if ...

    def tem_saldo_suficiente(self): ...


    """ Verifica se o que ele mandou é um número """
    def verifica_numero(self, numero):
        for caracter in numero:
            if not caracter.isnumeric():
                return False
            
        return True