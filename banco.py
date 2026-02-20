from conta import Conta as c
from excecoes import IncorrectPassword, BlockedAccount, Unlocked

class Banco:
    def __init__(self):
        self.contas_banco = []
    
    def criar_conta(self, titular, saldo, senha): #
        conta = c(titular, saldo, senha)
        account = self.find_account(titular)
        if account:
            return "USUARIO_EXISTE"
        else:
            self.contas_banco.append(conta)
    def find_account(self, titular):
        for c in self.contas_banco:
            if titular == c.take_titular():
                return c
        else:
            return None

    def deposity_bank(self, titular, valor): #
        account = self.find_account(titular)
        if account:       
            account.depositar(valor)
        
    def draft_permission(self, titular, value): #
        account = self.find_account(titular)
        if account:
            try:
                account.sacar(value)
            except ValueError:
                return "SALDO_INSUFICIENTE"    

    def permission_transfer(self, remetente, destino, value):
        remetente = self.find_account(remetente) 
        destino = self.find_account(destino)
        if remetente and destino:
            try:
                remetente.transferir(destino, value)
            except ValueError:
                return "SALDO_INSUFICIENTE "      

    def bank_verify_password(self, titular, senha):
        account = self.find_account(titular)
        if account:
            try:
                passe = account.verificar_senha(senha)
                if passe:
                    return "OK"
            except IncorrectPassword:
                return "SENHA_INCORRETA"
            except BlockedAccount:
                return "USUARIO_BLOQUEADO"
            except Unlocked:
                return "CONTA_DESBLOQUEADA"
        else:
            return "USUARIO_NAOEXISTE"