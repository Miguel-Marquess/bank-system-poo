class BlockedAccount(Exception):
    def __str__(self):
        return "Conta bloqueada"
    
class IncorrectPassword(Exception):
    def __str__(self):
        return "Senha Incorreta. Tente novamente"

class UserExist(Exception):
    def __str__(self):
        return "O Usuario digitado ja existe. Tente novamente."

class UserNotExist(Exception):
    def __str__(self):
        return "O Usuario nao existe."

class SaldoInsuficiente(Exception):
    def __str__(self):
        return "O Saldo e insuficiente para essa operacao."
