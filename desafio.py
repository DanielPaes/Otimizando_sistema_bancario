mensagem = """
====================================
           Seja bem vindo!
------------------------------------
Por gentiliza, escolha uma operação:

[d] - Depósito
[s] - Saque
[e] - Extrato
[cu] - Criar Usuário
[cc] - Criar Conta
[q] - Sair
------------------------------------
"""

# Declaração e inicialização de variáveis
saldo = 0
qtd_saques = 0
extrato = ""
limite_valor_saque = 500
limite__qtd_saques = 3
usuarios = []
contas = []
AGENCIA = "0001"
conta = 1

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        print("\nDepóstio realizado com sucesso.")
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("\nDepósito não realizado. Valor não permitido.")
    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite_valor_saque, qtd_saques, limite__qtd_saques):
    if valor > 0 and valor < limite_valor_saque:
        if valor < saldo :
            if qtd_saques < limite__qtd_saques:
                saldo -= valor
                print("\nSaque realizado com sucesso.\n")
                qtd_saques += 1
                extrato += f"Saque: R${valor:.2f}\n"
            else:
                print("\nSaque não permitido. Limite de saques diário excedido.")
        else:
            print("\nSaque não realizado. Saldo insuficiente.")

    else:
        print("\nValor inválido. Saque não realizado.")
    return saldo, extrato, qtd_saques

def mostra_extrato(saldo, /, *, extrato):
    print("\n\n==============EXTRATO===============\n")
    print("Nenhuma operação realizada\n" if extrato == '' else extrato)
    print("----------------------------------")
    print(f"\nSaldo: R${saldo:.2f}")
    print("\n====================================\n")

def criar_usuario():
    cpf = input("Informe o CPF (apenas números):")
    
    if not consulta_usuario(cpf):
        nome = input("Informe o nome completo:")
        data_nascimento = input("Informe a data de nascimento:")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado):")
        usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereço": endereco})
        print("\nUsuário criado com sucesso.")
    else:
        print("Usuário já existe.")        

def criar_conta(agencia, conta, cpf_usuario):

    usuario = consulta_usuario(cpf_usuario)

    if usuario:
        print("Usuario existente. Criaremos a conta.")
        print(agencia, conta)
    else:
        print("Primeiro, crie o usuário.")

def consulta_usuario(cpf):
    usuario = []
    for i in usuarios:
        if i["cpf"] == cpf:
            usuario.append(i)
        else:
            return
        return usuario
    
while True:

    # Leitura da operação que será executada.
    op = input(mensagem)

    # Sai do do programa
    if op.lower() == 'q':
        break

    elif op.lower() == 'cu':
        criar_usuario()

    elif op.lower() == 'cc':
        cpf_usuario = input("Informe o CPF do usuário:")
        criar_conta(AGENCIA, conta, cpf_usuario)

    # Operação de depósito
    elif op.lower() == 'd':
        try:
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)
        except:
            print("Ocorreu algum erro. Tente novamente.")
        
       
    # Operação de saque
    elif op.lower() == 's':
        try:
            valor =  float(input("\nInforme o valor de saque: "))
            saldo, extrato, qtd_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, limite_valor_saque=limite_valor_saque, qtd_saques= qtd_saques, limite__qtd_saques = limite__qtd_saques)
        except:
            print("Ocorreu algum erro. Tente novamente.")

    # Impressão do extrato
    elif op.lower() == 'e':        
        mostra_extrato(saldo, extrato=extrato)

    # Operação selecionada inválida
    else:
        print("\nOperação inválida. Tente novamente.")

