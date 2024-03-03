import math

class Calculadora:
    def soma(self, *args):
        soma = args[0] + args[1]
        return soma
    def subtracao(self, *args):
        sub = args[0] - args[1]
        return sub
    def multiplicacao(self, *args):
        mult = args[0] * args[1]
        return mult
    def divisao(self, *args):
        div = args[0] / args[1]
        return div
    def fatorial(self, *args):
        calc = Calculadora()
        if args[0] == 0:
            return 1
        else:
            return args[0] * calc.fatorial(args[0]-1)
    def radiciação(self, *args):
        conta = math.pow(args[0], 1/args[1])
        return conta