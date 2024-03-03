from cliente import Cliente

new = 1

while (new == 1 or new == "1"):
    cliente = Cliente.cadastro()
    if cliente and type(cliente) != str:
        print(f"Nome: {cliente.get_nome()}\nCpf: {cliente.get_cpf()}\nEndereço: {cliente.get_endereco()}\nCEP: {cliente.get_cep()}")
    else:
        print(cliente)
    new = input("Deseja começar novamente? \nDigite 1 para sim e 0 para não.\n")

    
