import pickle
from pathlib import Path

class Serializar:
    salvar_arquivo = 'locadora_data.pkl'
    @classmethod
    def save_locadora(self, locadora):
        try:
            with open(self.salvar_arquivo, 'wb') as file:
                pickle.dump(locadora, file)
            return True and print(f'{locadora.nome} foi salva com sucesso!')
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
            return False
    @classmethod
    def load_locadora(self):
        if not Path(self.salvar_arquivo).exists():
            return None 
        try:
            with open(self.salvar_arquivo, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return None