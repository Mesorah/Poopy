from perfil import Perfil

class EscolhaTrabalho:
    def __init__(self):
        self.experiencia = 0

    
    """ Exibe todos os trabalhos """
    def exibir_trabalho(self, trabalhos):
        print("Trabalhos disponíveis:")
        for trabalho in trabalhos:
            print(f"[{trabalho['id_trabalho']}] {trabalho['nome_trabalho']} || Experiência necessária: {trabalho['experiencia']}")


    """ Pergunta qual trabalho, e puxa para a função de verificar """
    def escolher_trabalho(self, trabalhos):
        while True:
            escolha = input('Qual trabalho você irá escolher? ')
            if self.verifica_numero(escolha) and int(escolha) in [1] and self.verifica_experiencia(trabalhos[int(escolha) - 1]['experiencia']):
                print('ok')
                break

            else:
                print('ue')

    """ Chamas as outras funções, e tem a lista de dicionário dos trabalhos """
    def escolha_trabalho(self):
        trabalho = [
            {'id_trabalho': 1, 'nome_trabalho': 'Limpador de privada', 'salario': 1000, 'experiencia': 0},

        ]

        self.exibir_trabalho(trabalho)

        self.escolher_trabalho(trabalho)


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
    def __init__(self):
        self.energia = 100

    def exemplo_trabalho(self, msg):
        from time import sleep

        print(f'{msg}')
        sleep(3)
        print('Almoçando...')
        sleep(3)
        print('Pegando o salário com o chefe...')
        sleep(3)
        print(f'+ R${self.salario_trabalho}')
        self.dinheiro += EscolhaTrabalho().escolha_trabalho.trabalho

        self.experiencia(self.salario_trabalho)
        print(f'+ {self.salario_trabalho / 220} EXP')

        self.menos_energia(self.salario_trabalho) 

    def comecar_trabalho(self):
        pass
    