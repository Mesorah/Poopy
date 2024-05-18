from perfil import *
from trabalho import *
from loja import *
import bdd

class IniciarJogo:
    def __init__(self):
        self.personagem = Perfil()
        self.trabalho = EscolhaTrabalho()
        self.tra = Trabalho(self.personagem, self.trabalho)
        self.loja = Loja(self.personagem, self.tra)

    def iniciar_jogo(self):
        self.personagem.nome_personagem()
        self.personagem.sobrenome_personagem()

        while True:
            self.exibe_opcoes()

            acao = input('O que fazer? ')

            if not self.verifica_numero(acao) or int(acao) not in [1, 2, 3, 4, 5, 6]:
                print('Opção inválida!')
            
            else:
                self.escolha_opcoes(int(acao))

    def exibe_opcoes(self):
        print('''
    1- Escolher o trabalho
    2- Trabalhar
    3- Dormir
    4- Loja
    5- Exibir perfil
    ''') 
        
    def exibir_perfil(self):
        info_trabalhos = EscolhaTrabalho().trabalho
            

        print(f'''
Nome: {self.personagem.nome}
Sobrenome: {self.personagem.sobrenome}
Dinheiro: {self.personagem.dinheiro}
Trabalho atual: {info_trabalhos[EscolhaTrabalho().num_trabalho_atual]['nome_trabalho']}
Experiencia: {self.trabalho.experiencia}
Energia {self.tra.energia}
''')
    def escolha_opcoes(self, opcao):
        if opcao == 1:
            self.trabalho.escolha_trabalho()

        elif opcao == 2:
            self.tra.limpador_privado()

        elif opcao == 3:
            self.tra.descancar()

        elif opcao == 4:
            self.loja.escolha_produto()

        elif opcao == 5:
            self.exibir_perfil()

        elif opcao == 6:
            # Pegue os atributos do personagem
            tipo_perfis = TipoPerfis()
            nome = tipo_perfis.nome
            sobrenome = tipo_perfis.sobrenome
            dinheiro = tipo_perfis.dinheiro
            trabalho_atual = tipo_perfis.trabalho_atual
            experiencia = tipo_perfis.experiencia
            energia = tipo_perfis.energia

            # Envie os dados para o banco de dados
            print('fui enviado')
            bdd.enviar_dados_para_banco_de_dados()

            return
        
        else:
            print('opção inexistente')

    def verifica_numero(self, numero):
        return numero.isnumeric()
    


class TipoPerfis:
    def __init__(self):
        self.personagem = Perfil()
        self.trabalho = EscolhaTrabalho()
        self.tra = Trabalho(self.personagem, self.trabalho)
        self.loja = Loja(self.personagem, self.tra)

        info_trabalhos = EscolhaTrabalho().trabalho

        self.nome = self.personagem.nome
        self.sobrenome = self.personagem.sobrenome
        self.dinheiro = self.personagem.dinheiro
        self.trabalho_atual = info_trabalhos[self.trabalho.num_trabalho_atual]['nome_trabalho']
        self.experiencia = self.trabalho.experiencia
        self.energia = self.tra.energia


jogo = IniciarJogo()
jogo.iniciar_jogo()
