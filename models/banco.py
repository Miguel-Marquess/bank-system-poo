from models.conta import Conta as c
from models.excecoes import UserExist, UserNotExist

class Banco:
    def __init__(self):
        self.contas_banco = []
    
    def criar_conta(self, titular, saldo, senha): #
        for c in self.contas_banco:
            if c.titular == titular:
                raise UserExist
        else:        
            conta = c(titular, saldo, senha)
            self.contas_banco.append(conta)
        
    def pegar_conta(self, titular):
        for c in self.contas_banco:
            if titular == c.titular:
                return c
        else:
            raise UserNotExist

    def deposito(self, titular, valor, senha): #
        self.pegar_conta(titular).depositar(valor, senha)
        
    def permissao_saque(self, titular, value, senha): #
        self.pegar_conta(titular).sacar(value, senha)
    
    def transferencia(self, remetente, destino, value, senha):
        self.pegar_conta(remetente).transferir(self.pegar_conta(destino), value, senha)
            
    def timeout(self, nome):
        return int(self.pegar_conta(nome).timeout)
    