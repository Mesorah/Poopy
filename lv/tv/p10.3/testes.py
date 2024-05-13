from cliente import Cliente
from conta import Conta
from banco import Banco

joao = Cliente('joao', 1234)
maria = Cliente('Maria Silva', 1213)
contaJM = Conta([joao, maria], 100)
tatu = Banco('Tatú')
tatu.abre_conta(contaJM)
tatu.lista_contas()