def options(opcoes):
    c=1
    print("BANCO POTIGUAR".center(40, "-"))
    for p in opcoes:
        print(f"{c} - {p}")
        c+=1
    print("-"*40)
    return input("Sua opcao >>> ")

