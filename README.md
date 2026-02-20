# Sistema Bancário em Python (POO)

Projeto simples de sistema bancário feito em Python usando Programação Orientada a Objetos.

---

## Objetivo

- Praticar organização de código em mútiplos arquivos
- Separação entre regra de negócio e interface 
- Uso de exceções personalizadas

---

## Funcionalidades

- Criar conta
- Depositar
- Sacar
- Transferir entre contas
- Ver informaçôes da conta
- Sistema de bloqueio após 3 tentativas de senha incorreta
- Desbloqueio após 30 segundos

---

## Estrutura do Projeto

```
│
├── banco.py       # Gerencia as contas e regras do banco
├── conta.py       # Classe Conta com regras internas
├── excecoes.py    # Exceções personalizadas
├── interface.py   # Menu e interação com usuário
├── main.py        # Ponto de entrada do sistema
└── README.md
```

---

## Regra de segurança

- Após 3 tentativas incorretas, a conta é bloqueada. E ações como Depositar, sacar e transferir sao impossibilitadas
- O bloqueio é de 30 segundos (Utilizada a biblioteca interna `time` do python para pegar o tempo atual em segundos)
- Quando o usúario tenta realizar uma ação após os 30 segundos, a conta é desbloqueada. 

---

## Como executar

```
python main.py
```

---

## Melhorias

- Substituir lista por dicionário para melhorar busca de contas
- Implementar persistência de dados
- Melhorar validação de entradas
- Implementar hash de senha

---

***Projeto desenvolvido com foco em aprendizado e evolução em Python***
