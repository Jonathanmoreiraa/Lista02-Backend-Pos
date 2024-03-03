from primos import Primos

numero_1 = int(input("Informe um número inteiro e maior que 0: "))
if numero_1 > 0:
    numero_2 = int(input("Informe outro número inteiro e maior que 0: "))
    if numero_2 > 0:
        primos = Primos(numero_1, numero_2)
        qtd = primos.contaPrimos(numero_1, numero_2)
        print(f"A quantidade de números primos entre {numero_1} e {numero_2} é {qtd}")
    else:
        print("Informe um número positivo e maior que zero!")
else:
    print("Informe um número positivo e maior que zero!")