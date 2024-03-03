import re

class Cliente:
    def __init__(self, nome: str, endereco: str, cep: str, cpf: str):
        self.nome = nome
        self.endereco = endereco
        self.cep = cep
        self.cpf = cpf

    def get_nome(self):
        return self.nome
    
    def get_endereco(self):
        return self.endereco

    def get_cep(self):
        return self.cep
    
    def get_cpf(self):
        return self.cpf

    def validaCpf(cpf):
        cpf = re.sub(r'[^0-9]', '', cpf)
        
        if len(cpf) != 11:
            return False
        
        if cpf == cpf[0] * 11:
            return False
        
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[9]):
            return False
        
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        resto = 11 - (soma % 11)

        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[10]):
            return False
        
        return True

    def validaCep(cep):
        cep = re.sub(r'[^0-9]', '', cep)

        if len(cep) != 8:
            return False
        else:
            return True

    def cadastro():
        nome = input("Informe o nome: ")
        cpf = input("Informe o cpf: ")
        if Cliente.validaCpf(cpf) == False:
           return "CPF Inválido" 
        endereco = input("Informe o endereço: ")
        cep = input("Informe o cep: ")
        if Cliente.validaCep(cep) == False:
           return "CEP Inválido" 
        cli = Cliente(nome, endereco, cep, cpf)
        return cli
