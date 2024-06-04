

def depositar(s, v, e):

    if v > 0:
        s += v
        e += f'Deposito: R$ {v:.2f}'
        print('Depósito realizado com sucesso!!')

    else:
        print('Valor inválido!')

    return s, e

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques ):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente.")

    elif excedeu_limite:
        print(" O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print('saque realizado com sucesso!')

    else:
        print('valor informado invalido!')

    return saldo, extrato

def exibir_extrato(s, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {s:.2f}")
    print("==========================================")

def novo_usuario(usuarios):
    cpf = input('informe seu cpf (somente números):  ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('usuário já cadastrado!')

    nome = input('informe seu nome: ')
    nascimento = input('sua data de nascimento: ')
    endereco = input('informe seu endereço (logadouro, número, bairro, cidade/estado): ')
    usuarios.append({"nome":nome, "nascimento":nascimento, "cpf":cpf, "endreco":endereco})
    print('usuário cadastrado com sucesso!!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe seu cpf:  ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('conta criada com sucesso!!')
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print('usuário não encontrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f'agencia: {conta['agencia']}, conta: {conta['numero_conta']}, titular: {conta['usuario']['nome']}'
    
    print(linha)

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    

    AGENCIA = '0001'


    while True:

        op = int(input("""
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Novo usuário 
            [5] Nova conta
            [6] Listar contas         
            [7] Sair
            selecione uma opção:            
        """)) 
    
        if op == 1:
            valor = float(input('valor do deposito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif op == 2:
        
            valor = float(input('informe o valor do saque:R$ '))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

            

        elif op == 3:
            exibir_extrato(saldo, extrato=extrato)
            
        elif op == 4:
            novo_usuario(usuarios)

        elif op == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                

        elif op == 6:
            listar_contas(contas)


        else:
            print("por favor selecione novamente a operação desejada.")



    

main()