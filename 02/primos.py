import re

class Primos:
    def __init__(self, num_1: int, num_2: int):
        self.num_1 = num_1
        self.num_2 = num_2
    
    def contaPrimos(self, *args):
        count = 0
        for j in range(args[0], args[1]+1):
            m = 0
            for i in range(2, j):
                if j % i == 0:
                    m += 1
            if m == 0:
                count +=1
        return count