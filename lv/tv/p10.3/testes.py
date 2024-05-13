from cliente import Cliente
from conta import Conta

joao = Cliente('joao', 1234)
conta1 = Conta([joao], 1, 300)

print(conta1.deposito(300))
print(conta1.saque(4000))