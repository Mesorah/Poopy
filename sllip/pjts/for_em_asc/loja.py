from perfil import *
from time import sleep

class Loja:
    def __init__(self, perfil, trabalho):
        self.perfil = perfil
        self.trabalho = trabalho
        self.lista_produtos = [
            {'numero_produto': 1, 'preco': 1500, 'quantia': 15},

        ]


    """ Exibe todos os produtos da loja """
    def exibir_produtos(self):
        print('''
[1] Aumentar a energia em +15 || R$ 1500
''')


    """ Escolhe qual produte irá comprar """
    def escolha_produto(self):
        self.exibir_produtos()

        escolha = input('Qual item você irá comprar? ')
        if not self.verifica_numero(escolha):
            print('ERROR')

        elif int(escolha) not in [1]:
            print('opção inexistente')
            
            return
        
        else:
            self.compra_produto(int(escolha))


    """ Pega o preço e evenvia para o tem_saldo_suficiente """
    def compra_produto(self, produto):
        valor_produto = self.lista_produtos[produto - 1]['preco']
        produto = self.lista_produtos[produto - 1]

        if self.tem_saldo_suficiente(valor_produto):
            self.efetuar_compra(produto)

        else:
            pass

    
    """ Verifica se a pessoa tem saldo para comprar o produto escolhido """
    def tem_saldo_suficiente(self, valor):
        if self.perfil.dinheiro >= valor:
            self.perfil.dinheiro -= valor

            return True
        
        else:
            print('Valor insuficiente')

            return False
            

    """ Efetua/entrega a compra ao usuário """
    def efetuar_compra(self, produto):
        print('Compra efetuada com sucesso!')
        sleep(0.3)

        if produto['numero_produto'] == 1:
            self.trabalho.maximo_energia += 15
            print('+15 de energia!')


    """ Verifica se o que ele mandou é um número """
    def verifica_numero(self, numero):
        for caracter in numero:
            if not caracter.isnumeric():
                return False

        return True