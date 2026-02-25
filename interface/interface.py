from models.conta import Conta
from interface.menu import options, excepts
def bankView(banco):
    while True:
        menu = options(["Criar Conta", "Depositar", "Sacar", "Transferir", "Ver sua conta", "Sair do sistema"])

        if menu == "1":
            nome = input("Digite seu nome: ")
            saldo = float(input("Digite seu saldo: "))
            senha = input("Digite sua senha: ")
            criar_usuario = banco.criar_conta(nome, saldo, senha)
            if criar_usuario == "USUARIO_EXISTE":
                print("O usuario ja existe. ")
            else:
                print("Usuario criado com sucesso. ")
            for c in banco.contas_banco:
                print("-"*40)
                print(c)
                
        elif menu == "2":
            nome = input("Seu titular: ")
            senha = input("Digite sua senha: ")
            verify_pass = banco.bank_verify_password(nome, senha)
            if verify_pass == "OK":
                valor = float(input("Valor a depositar: "))
                banco.deposity_bank(nome, valor)
                print("Deposito feito com sucesso. ")
            excepts(verify_pass)
            
        elif menu == "3":
            nome = input("Seu titular: ")
            senha = input("Digite sua senha: ")
            verify_pass = banco.bank_verify_password(nome, senha)
            if verify_pass == "OK":
                valor = float(input("Digite o valor para saque: "))
                draft = banco.draft_permission(nome, valor)
                if draft == "SALDO_INSUFICIENTE":
                    print("Saldo insuficiente pra continuar")
                else:
                    print("Saque feito com sucesso. ")
            excepts(verify_pass)
        elif menu == "4":
            remetente = input("Digite seu nome: ")
            destino = input("Digite a quem vc quer transferir o saldo: ")
            senha = input("Digite sua senha: ")
            verify_pass = banco.bank_verify_password(remetente, senha)
            if verify_pass == "OK":
                valor = float(input("Digite o valor: "))
                transfer = banco.permission_transfer(remetente, destino, valor)
                if transfer == "SALDO_INSUFICIENTE":
                    print("Voce nao tem saldo suficiente para ESSA transferencia. ")
                elif transfer == "USUARIO_NAOEXISTE":
                    print("O seu destino nao tem conta registrada. ")
                else:
                    print('Transferencia feita com sucesso.')
            excepts(verify_pass)
        elif menu == "5":
            nome = input("Digite seu titular: ")
            c = banco.find_account(nome)
            if c:
                print("-"*40)
                print(c)
            else:
                print("Usuario nao existe")
        elif menu == "6":
            print("Obrigado. ")
            break
        else:
            print("Digite uma opcao valida. ")