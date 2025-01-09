from param import *
from serializacao import *

serializar = Serializar()
locadora = serializar.load_locadora()

if locadora is None:
    locadora_nome = Locadora.validar_nome('nome', 'Digite o nome da Locadora: ')
    locadora = Locadora(locadora_nome)

while True:
    print(f'\nBem-Vindo a {locadora.nome}')
    print('\n(1) Veículos')
    print('(2) Clientes')
    print('(3) Mudar o nome da locadora')
    print('(4) Alugar')
    print('(0) Sair e Salvar')
    opcao = input('\nEscolha uma opção: ').strip()

    if opcao == '1': #Veículos
        while True:
            print('\n(1) Adicionar veículos')
            print('(2) Listar veículos')
            print('(3) Remover veículos')
            print('(4) Editar veículos')
            print('(0) Voltar')
            sub_opcao = input('\nEscolha uma opção: ').strip()

            if sub_opcao == '0':
                break

            elif sub_opcao == '1':
                tipo = locadora.validar_nome('tipo', 'Digite o tipo do veículo (moto ou carro): ')
                if tipo not in ['carro', 'moto']:
                    print('Tipo de veículo inválido. Escolha entre moto ou carro')
                    continue
                marca = locadora.validar_nome('marca', 'Digite a marca do veículo: ')
                modelo = locadora.validar_nome('modelo', 'Digite o modelo do veículo: ')
                ano = locadora.validar_valor('Digite o ano do veículo: ', is_year=True)
                quantidade = locadora.validar_valor('Digite a quantidade do veículo: ')
                while True:
                    cor = input("Digite a cor do veículo: ")
                    if cor.isalpha():
                        break
                    else:
                        print("Cor inválida.")
                valor = locadora.validar_valor('Digite o valor do aluguel do veículo por dia: ', is_float=True)
                if tipo == 'carro':
                    motor = locadora.validar_valor('Digite a potência do motor: ')
                    veiculo = Carro(marca, modelo, ano, quantidade, cor, motor, valor, tipo)
                elif tipo == 'moto':
                    cilindradas = locadora.validar_valor('Digite a cilindradas da moto: ')
                    veiculo = Moto(marca, modelo, ano, quantidade, cor, cilindradas, valor, tipo)
                locadora.add_veiculos(veiculo)
                print('\n Veículo adicionado')

            elif sub_opcao == '2':
                locadora.listar_veiculos()

            elif sub_opcao == '3':
                locadora.remover_veiculos()

            elif sub_opcao == '4':
                locadora.editar_veiculos()
                
    elif opcao == '2': #Clientes
        while True:
            print('\n(1) Adicionar clientes')
            print('(2) Listar clientes')
            print('(3) Remover clientes')
            print('(4) Editar clientes')
            print('(0) Voltar')
            sub_opcao = input('\nEscolha uma opção: ').strip()

            if sub_opcao == '0':
                break
            
            elif sub_opcao == '1':
                nome = locadora.validar_nome('nome', 'Digite o nome do cliente: ')
                email = locadora.validar_nome('email', 'Digite o email do cliente: ')
                telefone = locadora.validar_telefone('Digite o telefone do cliente: ')
                veiculo_alugado = None
                data_devolucao = None
                cliente = Cliente(nome, email, telefone, veiculo_alugado, data_devolucao)
                locadora.add_clientes(cliente)
                print('\nCliente adicionado')

            elif sub_opcao == '2':
                locadora.listar_clientes()

            elif sub_opcao == '3':
                locadora.remover_clientes()

            elif sub_opcao == '4':
                locadora.editar_clientes()

    elif opcao == '3': #Locadora
        locadora.nome = locadora.validar_nome('nome', 'Digite o nome da locadora: ')


    elif opcao == '4':
        while True:
            print ('\n(1) Alugar veículo')     
            print ('(2) Devolver veículo')
            print ('(0) Voltar')
            sub_opcao = input('\nEscolha uma opção: ').strip()
            
            if sub_opcao == '0':
                break
            
            elif sub_opcao == '1':
                locadora.alugar_veiculo()
                
            elif sub_opcao == '2':
                locadora.devolver_veiculo()
            
    elif opcao == '0': #Sair
        serializar.save_locadora(locadora)
        print('\nAté mais!\n')
        break