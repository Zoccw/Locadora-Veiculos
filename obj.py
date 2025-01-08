class Veiculo():
    def __init__(self, marca, modelo, ano, quantidade, cor, valor, tipo):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__quantidade = quantidade
        self.__valor = valor
        self.__tipo = tipo
        
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    def atributos(self):
        return {
            'marca': self.__marca,
            'modelo': self.__modelo,
            'ano': self.__ano,
            'cor': self.__cor,
            'quantidade': self.__quantidade,
            'valor': self.__valor,
            'tipo': self.__tipo,
        }


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade, cor, motor, valor, tipo):
        super().__init__(marca, modelo, ano, quantidade, cor, valor, tipo)
        self.__motor = motor

    @property
    def motor(self):
        return f'{self.__motor} CV'
    
    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    def atributos(self):
        atributos = super().atributos()
        atributos['motor'] = self.__motor
        return atributos

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade, cor, cilindradas, valor, tipo):
        super().__init__(marca, modelo, ano, quantidade, cor, valor, tipo)
        self.__cilindradas = cilindradas

    @property
    def cilindradas(self):
        return f'{self.__cilindradas} CC'
    
    @cilindradas.setter
    def cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas
    
    def atributos(self):
        atributos = super().atributos()
        atributos['cilindradas'] = self.__cilindradas
        return atributos

class Cliente:
    def __init__(self, nome, email, telefone, veiculo_alugado, data_devolucao):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__veiculo_alugado = []
        self.__data_devolucao = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def veiculo_alugado(self):
        return self.__veiculo_alugado
    
    @veiculo_alugado.setter
    def veiculo_alugado(self, veiculo_alugado):
        self.__veiculo_alugado = veiculo_alugado

    @property
    def data_devolucao(self):
        return self.__data_devolucao
    
    @data_devolucao.setter
    def data_devolucao(self, data_devolucao):
        self.__data_devolucao = data_devolucao

    def atributos(self):
        return {
            'nome': self.__nome,
            'email': self.__email,
            'telefone': self.__telefone,
            'veiculo alugado': self.__veiculo_alugado,
            'data de devolução': self.__data_devolucao
        }