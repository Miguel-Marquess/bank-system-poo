from models.excecoes import BlockedAccount, IncorrectPassword, SaldoInsuficiente
import time

class Conta:
    def __init__(self, titular, saldo, senha):
        self._titular = titular
        self.saldo = saldo
        self.minha_senha = senha
        self.conta_bloqueada = False
        self.tentativas = 0
        self._timeout = 0

    @property
    def titular(self):
        return self._titular

    def depositar(self,valor, senha): #
        if self.verificar_senha(senha):
            self.saldo+=valor
      
    def sacar(self, valor, senha): #
        if self.verificar_senha(senha):
            if valor <= self.saldo:
                self.saldo-= valor
            else:
                raise SaldoInsuficiente
            
    def transferir(self, destino, valor, senha): #
        if self.verificar_senha(senha):
            if valor <= self.saldo:
                self.saldo -= valor
                destino.depositar(valor, senha)
            else:
                raise SaldoInsuficiente
            
    def verificar_senha(self, senha):
        if self.conta_bloqueada:
            self.desbloquear()
        if senha == self.minha_senha:
            return True
        else:
            self.tentativas +=1
            if self.tentativas == 3:
                self.bloquear()
            else:
                raise IncorrectPassword
        
    def bloquear(self):
        self.conta_bloqueada = True
        self.tentativas=0
        self._timeout = time.time() + 30
        raise BlockedAccount
        
    def desbloquear(self):
        if self._timeout > time.time():
            raise BlockedAccount
        else:
            self.conta_bloqueada = False
            self._timeout = 0
            self._tentativas = 0

    def __str__(self):
        return f"Titular: {self.titular}\nSaldo: R${self.saldo:,.2f}"
    
    @property
    def timeout(self):
        return self._timeout - time.time()