class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor_caneta(self):
        return self._cor
    
    @cor_caneta.setter
    def cor_caneta(self, valor):
        self._cor = valor
    


cn = Caneta('azul')

cn.cor_caneta = 'rosa'

print(cn.cor_caneta)