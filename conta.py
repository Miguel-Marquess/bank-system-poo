from excecoes import BlockedAccount, IncorrectPassword, Unlocked
from datetime import datetime
import time
class Conta:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.saldo = saldo
        self.minha_senha = senha
        self.conta_bloqueada = False
        self.tentativas = 0
        self.timeout = 0
        self.time_bloqueio = 0

    def take_titular(self):
        return self.titular

    def depositar(self,valor): #
        self.saldo+=valor
      
    def sacar(self, valor): #
            if valor <= self.saldo:
                self.saldo-= valor
            else:
                raise ValueError
            
    def transferir(self, destino, valor): #
            if valor <= self.saldo:
                self.saldo -= valor
                destino.depositar(valor)
            else:
                raise ValueError

    def verificar_senha(self, senha):
        if senha == self.minha_senha and not self.conta_bloqueada:
            return True
        elif senha != self.minha_senha and not self.conta_bloqueada:
            self.tentativas +=1
            if self.tentativas == 3:
                self.bloquear()
            else:
                raise IncorrectPassword
        else:
            self.desbloquear()
            raise Unlocked

    def bloquear(self):
        self.conta_bloqueada = True
        self.tentativas=0
        self.timeout = time.time() + 30
        raise BlockedAccount
        
    def desbloquear(self):
        if self.timeout <= time.time():
            self.conta_bloqueada = False
            self.timeout = 0
            raise Unlocked
        else:
            raise BlockedAccount
            
    def blocked_information(self):
        return self.conta_bloqueada
    
    def __str__(self):
        return f"Titular: {self.titular}\nSaldo: R${self.saldo:,.2f}"