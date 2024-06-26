class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro, endereco):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.statusCadastro = statusCadastro
        self.endereco = endereco
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if len(value) > 0:
            self._nome = value
        else:
            raise ValueError("O nome não pode ser vazio.")
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, value):
        if value > 18:
            self._idade = value
        else:
            raise ValueError("A idade precisa ser maior que 18 anos.")
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
        if value >= 0:
            self._saldo = value
        else:
            raise ValueError("O saldo não pode ser negativo.")
    
    @property
    def statusCadastro(self):
        return self._statusCadastro
    
    @statusCadastro.setter
    def statusCadastro(self, value):
        if value:
            self._statusCadastro = value
        else:
            raise ValueError("O status do cadastro precisa ser verdadeiro.")
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, value):
        if len(value) >= 3:
            self._endereco = value
        else:
            raise ValueError("O endereço não pode ser vazio e precisa ter pelo menos 3 letras.")
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Status do cadastro: {self.statusCadastro}")
        print(f"Endereço: {self.endereco}")

if __name__ == "__main__":
    try:
        cadastro1 = Cadastro("João", 25, 1500.75, True, "Rua A")
        
        cadastro1.exibir_dados()
        
        print("\n")
        cadastro2 = Cadastro("", 17, -100.0, False, "Av")
        
    except ValueError as e:
        print(f"Erro ao criar cadastro: {e}")
