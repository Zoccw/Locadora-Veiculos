from obj import *
from datetime import datetime, timedelta, date
class Locadora:

    def __init__(self, nome):
        self.__nome = nome
        self.__veiculos = []
        self.__clientes = []
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def veiculos(self):
        return self.__veiculos
    
    @property
    def clientes(self):
        return self.__clientes
    
    def mostrar_veiculo(self, veiculo):
        quantidade_info = "Todos os veículos deste modelo estão alugados." if veiculo.quantidade == 0 else str(veiculo.quantidade)
        if veiculo.tipo == 'carro':
            return f"Veículo: {veiculo.tipo}, Marca: {veiculo.marca}, Modelo: {veiculo.modelo}, Ano: {veiculo.ano}, Quantidade: {quantidade_info}, Cor: {veiculo.cor}, Motor: {veiculo.motor}, Valor: R${veiculo.valor:.2f}"
        elif veiculo.tipo == 'moto':
            return f"Veículo: {veiculo.tipo}, Marca: {veiculo.marca}, Modelo: {veiculo.modelo}, Ano: {veiculo.ano}, Quantidade: {quantidade_info}, Cor: {veiculo.cor}, Cilindradas: {veiculo.cilindradas}, Valor: R${veiculo.valor:.2f}"    

    def listar_veiculos(self, select=False):
        veiculos_list = []
        for veiculo in self.veiculos:
            veiculos_list.append(self.mostrar_veiculo(veiculo))
        if not veiculos_list:
            print('\nNenhum veículo cadastrado.')
            return
        if select == True:
            for num, veiculo in enumerate(veiculos_list, start=1):
                print(f'[{num}] {veiculo}')
            return self.selecionar(veiculos_list, "\nDigite o número do veículo que deseja selecionar: ")
        else:
            for num, veiculo in enumerate(veiculos_list, start=1):
                print(f'[{num}] {veiculo}')

    def remover_veiculos(self):
            numero=self.listar_veiculos(select=True)
            if numero == None:
                return
            self.veiculos.pop(numero-1)
            print('\nVeículo Removido.')

    def add_veiculos(self, veiculo):
        self.veiculos.append(veiculo)
    
    def editar_veiculos(self):
        numero = self.listar_veiculos(select=True)
        if numero == None:
            return
        veiculo = self.veiculos[numero-1]
        print("\nAtribudos disponíveis:\n")
        for atributo in veiculo.atributos().keys():
            print(atributo)
        atributo = input("\nDigite o atributo que deseja editar: ")
        if atributo in veiculo.atributos().keys():
            if atributo == 'tipo':
                print('\nNão é possível mudar o tipo do veículo. Caso queira modificá-lo, remova o veículo e adicione-o novamente.')
            elif atributo in ['quantidade', 'cilindradas', 'motor']:
                novo_valor = self.validar_valor(f"Digite o novo valor para {atributo}: ")
                setattr(veiculo, atributo, novo_valor)
                print(f"\nVeículo editado com sucesso!")
            elif atributo == 'ano':
                novo_valor = self.validar_valor(f"Digite o novo valor para {atributo}: ", is_year=True)
                setattr(veiculo, atributo, novo_valor)
                print(f"\nVeículo editado com sucesso!")
            elif atributo == 'valor':
                novo_valor = self.validar_valor(f"Digite o novo valor para {atributo}: ", is_float=True)
                setattr(veiculo, atributo, novo_valor)
                print(f"\nVeículo editado com sucesso!")
            else:
                novo_valor = self.validar_nome('valor', f'Digite um novo valor para {atributo}: ')
                setattr(veiculo, atributo, novo_valor)
                print(f"\nVeículo editado com sucesso!")
        else:
            print("\nAtributo não encontrado")
        
    def mostrar_clientes(self, cliente):
        def formatar_data(data):
            hoje= datetime.now().date()
            data_devolucao = data.date()
            if data_devolucao == hoje:
                return f"{data.strftime('%d/%m/%Y')}, Hoje"
            elif data_devolucao < hoje:
                return f"{data.strftime('%d/%m/%Y')}, Data de devolução passou"
            else:
                return data.strftime('%d/%m/%Y')
        veiculo_info = ', '.join(f"{veiculo} (Devolução: {formatar_data(data)})" for veiculo, data in zip(cliente.veiculo_alugado, cliente.data_devolucao)) if cliente.veiculo_alugado else 'Nenhum'
        return f"Cliente: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}, Veículo alugado: {veiculo_info}"
    
    def listar_clientes(self, select=False):
        clientes_list = []
        for cliente in self.clientes:
            clientes_list.append(self.mostrar_clientes(cliente))
        if not clientes_list:
            print("\nNenhum cliente cadastrado.")
            return
        if select == True:
            for num, cliente in enumerate(clientes_list, start=1):
                print(f'[{num}] {cliente}')
            return self.selecionar(clientes_list, "\nDigite o número do cliente que deseja selecionar: ")
        else:
            for num, cliente in enumerate(clientes_list, start=1):
                print(f'[{num}] {cliente}')

    def remover_clientes(self):
        numero=self.listar_clientes(select=True)
        if numero == None:
            return
        self.clientes.pop(numero-1)
        print('\Cliente Removido.')

    def add_clientes(self, cliente):
        self.clientes.append(cliente)
    
    def validar_telefone(self, prompt):
        while True:
            telefone=self.validar_valor(prompt)
            if len(str(telefone)) == 11:
                telefone = str(telefone)
                telefone = f'({telefone[:2]}){telefone[2:]}'
                break
            else:   
                print("Telefone inválido. Deve ter no mínimo 11 digitos.")
        return telefone
    
    def selecionar(self, lista, prompt):
        numero = self.validar_valor(prompt)
        while True:
            if numero <= len(lista):
                return numero
            else:
                print("\nNúmero inválido. Por favor, digite um número válido.\n")
                numero = self.validar_valor(prompt)
                
    def editar_clientes(self):
        numero = self.listar_clientes(select=True)
        if numero == None:
            return
        cliente = self.clientes[numero-1]
        print("\nAtribudos disponíveis:\n")
        for atributo in cliente.atributos().keys():
            print(atributo)
        atributo = input("\nDigite o atributo que deseja editar: ").lower()
        if atributo in cliente.atributos().keys():
            if atributo in ['veiculo alugado', 'data de devolução']:
                print("\nNão é possível editar esse atributo, caso queira muda-lo utilize a função alugar ou devolver veículo")
            elif atributo == 'telefone':
                novo_valor = self.validar_telefone('Digite o novo valor para telefone: ')
                setattr(cliente, atributo, novo_valor)
                print('\nCliente editado com sucesso!')
            else:
                novo_valor = input(f"Digite o novo valor para {atributo}: ")
                setattr(cliente, atributo, novo_valor)
                print("\nCliente editado com sucesso!")
        else:
            print("Atributo não encontrado")
        

    def alugar_veiculo(self):

        numero_cliente = self.listar_clientes(select=True)
        if not self.clientes:
            return
        numero_veiculo = self.listar_veiculos(select=True)
        if not self.veiculos:
            return
        cliente = self.clientes[numero_cliente-1]
        veiculo = self.veiculos[numero_veiculo-1]
        if veiculo.modelo in cliente.veiculo_alugado and veiculo.quantidade == 0:
            print("Veiculo já foi alugado")
            return
        if veiculo.quantidade > 0:
            data_aluguel = datetime.now()
            dias = self.validar_valor('\nDigite a quantidade de dias para o aluguel: ')
            data_retorno= data_aluguel + timedelta(days=dias)
            custo_total = veiculo.valor * dias
            while True:
                print(f"\nO custo total vai ser de R${custo_total:.2f} e terá que ser devolvido na data {data_retorno.strftime('%d/%m/%Y')}")
                decisão=input("Aceitar? (S/N):").lower().strip()
                if decisão == "s":
                    cliente.data_devolucao.append(data_retorno)
                    cliente.veiculo_alugado.append(veiculo.modelo)
                    veiculo.quantidade -= 1
                    print("\nVeículo alugado com sucesso.")
                    break
                elif decisão == "n":
                    print("\nCompra cancelada.")
                    return
                else:
                    print('\nDigite uma opção válida')
        else:
            print('Veiculo indisponível para aluguel')

    
    def devolver_veiculo(self):
        numero_cliente = self.listar_clientes(select=True)
        if not self.clientes:
            return
        cliente = self.clientes[numero_cliente-1]
        if not cliente.veiculo_alugado:
            print("Este cliente não possui veículos alugados.")
            return
        print("\nVeículos alugados:")
        for i, (veiculo_marca, veiculo_data_devolucao) in enumerate(zip(cliente.veiculo_alugado, cliente.data_devolucao), 1):
            print(f"[{i}] Modelo: {veiculo_marca} Devolução: {veiculo_data_devolucao.strftime('%d/%m/%Y')}")
        numero_veiculo = self.selecionar(cliente.veiculo_alugado,"\nDigite o número do veículo que deseja devolver: ")
        modelo_devolvido = cliente.veiculo_alugado.pop(numero_veiculo-1)
        cliente.data_devolucao.pop(numero_veiculo-1) 
        for veiculo in self.veiculos:
            if veiculo.modelo == modelo_devolvido:
                veiculo.quantidade += 1
                print("Veículo devolvido com sucesso.")
        
    def validar_valor(self, prompt, is_year=False, is_float=False):
        while True:
            valor = input(prompt).strip()
            try:
                if is_year==False and is_float == True:
                    valor = float(valor)
                else:
                    valor = int(valor)
                if valor <= 0:
                    raise Exception("Valor inválido. Deve ser maior que zero.")
                if is_year and valor > date.today().year:
                    raise Exception("Ano inválido. Deve ser menor ou igual ao ano atual.")
                return valor
            except ValueError:
                print("Valor inválido, Digite um valor válido")
            except Exception as error_msg:
                print(error_msg)

    @staticmethod
    def validar_nome(designacao, prompt):
        while True:
            nome=str(input(prompt)).strip()
            if not nome:
                print(f'Digite um {designacao} válido')
            else:
                return nome
