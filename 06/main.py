from validador import Validador
cpf = input("Informe o CPF: ")

validar = Validador(cpf)
print(validar.validador())