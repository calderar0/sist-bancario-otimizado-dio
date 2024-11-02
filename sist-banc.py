import textwrap

def menu():
    menu = """
    ############### MENU ###############
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    else:
        print('Valor inválido!')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_limite = numero_saques >= limite_saques
    maior_que_saldo = valor > saldo
    maior_que_limite = valor > limite
    if excedeu_limite:
        print('Limite de saques excedido!')
    elif maior_que_saldo:
        print('Saldo insuficiente!')
    elif maior_que_limite:
        print('Limite de saque excedido!')
    else:
        if valor > 0:
            saldo -= valor
            extrato.append(f'Saque: R$ {valor:.2f}')
            numero_saques += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido!')
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, /, *, extrato):
    print(f'Saldo: R$ {saldo:.2f}')
    print('Extrato:')
    for operacao in extrato:
        print(operacao)
    
def novo_usuario(usuarios):
    cpf = input('Digite o CPF: ')
    usuario = filtrar_usuario(usuarios, cpf)
    if usuario:
        print('Usuário já cadastrado!')
        return
    else:
        nome = input('Digite o nome: ')
        nasc = input('Digite a data de nascimento: ')
        end = input('Digite o endereço: ')
        usuarios.append({'cpf': cpf, 'nome': nome , 'nasc': nasc, 'end': end})
        print('Usuário cadastrado com sucesso!')

def filtrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def nova_conta(agencia, usuarios, num_conta):
    cpf = input('Digite o CPF: ')
    usuario = filtrar_usuario(usuarios, cpf)
    if usuario:
        print('Usuário encontrado!')
        return {'agencia': agencia, 'num_conta': num_conta, 'usuario': usuario}
    print('Usuário não encontrado!')

def listar_contas(contas):
    for conta in contas:
        print(conta)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    num_conta = 1

    while True:
        opcao = menu()
        if opcao == '1':
            valor = float(input('Digite o valor a ser depositado: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == '2':
            valor = float(input('Digite o valor a ser sacado: '))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == '3':
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == '4':
            conta = nova_conta(AGENCIA, usuarios, num_conta)
            if conta:
                contas.append(conta)
                num_conta += 1
        elif opcao == '5':
            listar_contas(contas)
        elif opcao == '6':
            novo_usuario(usuarios)
        elif opcao == '7':
            break
        else:
            print('Opção inválida!')

main()