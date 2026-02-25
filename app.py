from interface.interface import bankView
from models.banco import Banco

banco_potiguar = Banco()

if __name__ == "__main__":
    bankView(banco_potiguar)
