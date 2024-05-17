class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self.ferramenta
    
    ferramenta.setter
    def ferramenta(self, valor):
        self.ferramenta = valor



class Ferramenta:
    def __init__(self, nome):
        self.nome = nome

    def falar_ferramenta(self):
        print(f'A {self.nome} está escrevendo')

    def opa(self):
        print('opa')


escritor = Escritor('Gabriel')
ferramenta = Ferramenta('Bic')

escritor.ferramenta = ferramenta

ferramenta.falar_ferramenta()
escritor.ferramenta.falar_ferramenta()
escritor.ferramenta.opa()
