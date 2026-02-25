def options(opcoes):
    c=1
    print("BANCO POTIGUAR".center(40, "-"))
    for p in opcoes:
        print(f"{c} - {p}")
        c+=1
    print("-"*40)
    return input("Sua opcao >>> ")

def excepts(verify_pass):
    if verify_pass == "CONTA_DESBLOQUEADA":
        print("Conta desbloqueada! Tente novamente.".center(40, "-"))
    elif verify_pass == "USUARIO_NAOEXISTE":
        print("O usuario nao existe. Crie seu usuario para continuar. ")
    elif verify_pass == "SENHA_INCORRETA":
        print("Senha digitada e incorreta. A acao nao pode prosseguir. ")
    elif verify_pass == "USUARIO_BLOQUEADO":
        print("A conta foi bloqueada. Tente novamente mais tarde. ")