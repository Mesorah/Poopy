from perfil import Perfil

class Trabalho:
    def __init__(self):
        pass

    def exibir_trabalho(self, trabalhos):
        print("Trabalhos disponíveis:")
        for trabalho in trabalhos:
            print(f"[{trabalho['id_trabalho']}] {trabalho['nome_trabalho']} || Experiência necessária: {trabalho['experiencia']}")

    def escolher_trabalho(self, trabalhos, experiencia):
        while True:
            escolha = input('Qual trabalho você irá escolher? ')
            if self.verifica_numero(escolha) and int(escolha) in [1] and self.verifica_experiencia(trabalhos[int(escolha) - 1]['experiencia']):
                print('ok')
                print(trabalhos[int(escolha) - 1]['experiencia'], '################')
                break

            else:
                print('ue')

    def escolha_trabalho(self, experiencia):
        trabalho = [
            {'id_trabalho': 1, 'nome_trabalho': 'Limpador de privada', 'experiencia': 0},

        ]

        expericia_jogador = experiencia


        self.exibir_trabalho(trabalho)

        self.escolher_trabalho(trabalho)


    def verifica_experiencia(self, experiencia):
        if Perfil().experiencia >= experiencia:
            return True
        
        print('Experiência insuficente')
        return False

    
    def verifica_numero(self, numero):
        for caracter in numero:
            if not caracter.isnumeric():
                return False
            
        return True