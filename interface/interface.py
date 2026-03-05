from models.conta import Conta
from interface.menu import options
from models.excecoes import BlockedAccount, IncorrectPassword, UserExist, UserNotExist, SaldoInsuficiente

def bankView(banco):
    while True:
        menu = options(["Criar Conta", "Depositar", "Sacar", "Transferir", "Ver sua conta", "Sair do sistema"])
        try:
            if menu == "1":
                nome = input("Digite seu nome: ")
                saldo = float(input("Digite seu saldo: "))
                senha = input("Digite sua senha: ") 
                banco.criar_conta(nome, saldo, senha)
                print("Usuario criado com sucesso. ")
                for c in banco.contas_banco:
                    print("-"*40)
                    print(c)        
            elif menu == "2":
                nome = input("Seu titular: ")
                senha = input("Digite sua senha: ") 
                valor = int(input("Valor para deposito: "))
                banco.deposito(nome, valor, senha)
                print("Deposito feito com sucesso.")
            elif menu == "3":
                nome = input("Seu titular: ")
                senha = input("Digite sua senha: ")
                valor = float(input("Digite o valor para saque: "))
                banco.permissao_saque(nome, valor, senha)
                
            elif menu == "4":
                remetente = input("Digite seu nome: ")
                destino = input("Digite a quem vc quer transferir o saldo: ")
                senha = input("Digite sua senha: ")
                valor = float(input("Digite o valor: "))
                banco.transferencia(remetente, destino, valor, senha)
                print("Transferencia feita com sucesso.")
            elif menu == "5":
                nome = input("Digite seu titular: ")
                print("-"*40)
                print(banco.pegar_conta(nome))
            elif menu == "6":
                print("Obrigado. ")
                break
            else:
                print("Digite uma opcao valida. ")
        except (UserNotExist, IncorrectPassword, ValueError, BlockedAccount, UserExist, SaldoInsuficiente) as e:
            print(f"{e}. Tente novamente em {banco.timeout(nome)} segundos." if e.__class__ == BlockedAccount else e)