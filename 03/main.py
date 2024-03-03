from calculadora import Calculadora

calculadora = Calculadora()

print(f"A área do circulo: \n{calculadora.calcular(15.0)}")
print(f"A área do quadrado: \n{calculadora.calcular(6.0, 6.0)}")
print(f"A Perímetro do triângulo: \n{calculadora.calcular(19, 19, 19)}")
print(f"A Área do triângulo: \n{calculadora.calcular(3, 4.0)}")
print(f"Área do triângulo (coordenadas cartesianas): \n{calculadora.calcular((4, 0), (0, 0), (0, 6))}")
print(calculadora.calcular("String"))