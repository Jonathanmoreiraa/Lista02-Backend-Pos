import math

class Calculadora:
    def calcular(self, *args):
        if len(args) == 1 and type(args[0]) == float:
            raio = args[0]
            return math.pi * (raio * raio) 
        elif len(args) == 2 and type(args[0]) == float and type(args[1]) == float:
            lado1, lado2 = args
            return lado1 * lado2
        elif len(args) == 3 and type(args[0]) == int and type(args[1]) == int and type(args[2]) == int:
            lado1, lado2, lado3 = args
            return lado1 + lado2 + lado3
        elif len(args) == 2 and  type(args[0]) == int and  type(args[1]) == float:
            base, altura = args
            return 0.5 * base * altura
        elif len(args) == 3 and all(type(args) == tuple and len(arg) == 2 for arg in args):
            x1, y1 = args[0]
            x2, y2 = args[1]
            x3, y3 = args[2]
            return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
        else:
            return "Uso incorreto"
