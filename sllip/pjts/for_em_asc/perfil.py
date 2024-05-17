class Perfil:
    def __init__(self):
        self.nome = None
        self.sobrenome = None


    """
        Pede para o usuário colocar o nome do personagem
    """
    def nome_personagem(self):
        while True:
            self.nome = input('Nome: ')

            if self.verifica_string(self.nome):
                print('ok')
                break
            
            else:
                print('ue')


    """
        Pede para o usuário colocar o sobrenome do personagem
    """
    def sobrenome_personagem(self):
        while True:
            self.sobrenome = input('Sobrenome: ')

            if self.verifica_string(self.sobrenome):
                print('ok')
                break
            
            else:
                print('ue')

    """ Alterações de nome """
    @property
    def altera_nome(self):
        return self.nome
    
    @altera_nome.setter
    def altera_nome(self, novo_nome):
        if self.verifica_string(novo_nome):
            self.nome = novo_nome
            print('Nome alterado com sucesso!')
        else:
            print('O nome deve conter apenas letras.')

    @property
    def altera_sobrenome(self):
        return self.sobrenome
    
    @altera_sobrenome.setter
    def altera_sobrenome(self, novo_sobrenome):
        if self.verifica_string(novo_sobrenome):
            self.sobrenome = novo_sobrenome
            print('Sobrenome alterado com sucesso!')
        else:
            print('O sobrenome deve conter apenas letras.')

    """
        Verifica se a variável é uma string
    """
    def verifica_string(self, nome):
        for letra in nome:
            if not letra.isalpha():
                return False
            
        return True
    

    def exibir_perfil(self):
        print(f'''
Nome: {self.nome}
Sobrenome: {self.sobrenome}
''')