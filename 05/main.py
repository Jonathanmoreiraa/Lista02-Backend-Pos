from datas import Datas
data_1 = input("Informe a primeira data no formato DD/MM/YYYY: ")
data_2 = input("Informe a primeira data no formato DD/MM/YYYY: ")

datas = Datas()
qtd_dias = datas.datas(data_1, data_2)
print(f"A quantidade de dias é {qtd_dias}")