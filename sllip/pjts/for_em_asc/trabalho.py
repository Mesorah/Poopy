from perfil import Perfil
from time import sleep

class EscolhaTrabalho:
    def __init__(self):
        self.experiencia = 0
        self.num_trabalho_atual = 0
        self.trabalho = [
            {'id_trabalho': 1, 'nome_trabalho': 'Limpador de privada', 'salario': 1000, 'experiencia': 0},
            {'id_trabalho': 2, 'nome_trabalho': 'Faxineiro', 'salario': 2500, 'experiencia': 0},

        ]
    
    """ Exibe todos os trabalhos """
    def exibir_trabalho(self, trabalhos):
        print("Trabalhos disponíveis:")
        for trabalho in trabalhos:
            print(f"[{trabalho['id_trabalho']}] {trabalho['nome_trabalho']} || Experiência necessária: {trabalho['experiencia']}")


    """ Pergunta qual trabalho, e puxa para a função de verificar """
    def escolher_trabalho(self, trabalhos):
        while True:
            escolha = input('Qual trabalho você irá escolher? ')
            # print(trabalhos[int(escolha) - 1], '############$$$$$$$$$$$$$$$$$$@')
            if self.verifica_numero(escolha) and int(escolha) in [1, 2] and self.verifica_experiencia(trabalhos[int(escolha) - 1]['experiencia']):
                # self.num_trabalho_atual = trabalhos[int(escolha) - 1] ######
                self.num_trabalho_atual = int(escolha) - 1 
                print('ok')
                break

            else:
                print('ue')

    """ Chamas as outras funções, e tem a lista de dicionário dos trabalhos """
    def escolha_trabalho(self):

        self.exibir_trabalho(self.trabalho)

        self.escolher_trabalho(self.trabalho)


    """ Verifica a expericia que o jogador tem no perfil.py """
    def verifica_experiencia(self, experiencia):
        if self.experiencia >= experiencia:
            return True
        
        print('Experiência insuficente')
        return False

    """ Verifica se o que ele mandou é um número """
    def verifica_numero(self, numero):
        for caracter in numero:
            if not caracter.isnumeric():
                return False
            
        return True
    
    

class Trabalho:
    def __init__(self, perfil, escolha_trabalho):
        self.perfil = perfil
        self.escolha_trabalho = escolha_trabalho
        self.energia = 100
        self.maximo_energia = 100


    """ Verifica se a energia é maior ou igual a 51 """
    def verifica_energia(self):
        if self.energia >= 51:
            return True
        
        return False
    

    """ Serve para recuperar a energia no máximo """
    def descancar(self):
        print('descansando...')
        sleep(0.4)

        self.energia = self.maximo_energia

        print('energia recuperada!')
        sleep(0.1)


    """ Remover a energia """
    def remove_energia_trabalho(self):
        self.energia -= 50


    """ Um exemplo para seguir em todos os trabalhos, removendo energia, adicionando salario e experiência """
    def exemplo_trabalho(self, msg):
        if not self.verifica_energia():
            print('energia insuficiente')
            return

        else:
            print(f'{msg}')
            sleep(0.4)
            print('Almoçando...')
            sleep(0.4)
            print('Pegando o salário com o chefe...')
            sleep(0.4)

            ###############################################

            ### ver melhor, talver colocar como self.escolhatrabalho.... ###

            ###############################################

            info_trabalhos = self.escolha_trabalho.trabalho
            salario_trabalho_atual = info_trabalhos[self.escolha_trabalho.num_trabalho_atual]['salario']
            print(salario_trabalho_atual, '##############################################################')

            print(f'+ R${salario_trabalho_atual}')

            self.perfil.dinheiro += salario_trabalho_atual

            experiencia_adicional = int(round(salario_trabalho_atual / 220, 0))
            self.escolha_trabalho.experiencia += experiencia_adicional

            print(f'+ Exp{self.escolha_trabalho.experiencia}')

            self.remove_energia_trabalho()

            print(f'- 50 de energia, Total de energia: {self.energia}')


    """ Emprego para substituar a mensagem no exemplo_trabalho """
    def limpador_privada(self):
        self.exemplo_trabalho('Limpando a privada...')

    def faxineiro(self):
        self.exemplo_trabalho('Limpando a parede...')
    