import re


class Validador:
    def __init__(self, cpf: str):
        self.cpf = cpf
    
    def validador(self):
        cpf_old = self.cpf
        
        cpf = re.sub(r'[^0-9]', '', cpf_old)
        
        if len(cpf) != 11:
            return f"O CPF {cpf_old} não é válido."

        if cpf == cpf[0] * 11:
            return f"O CPF {cpf_old} não é válido."
                    
        qtd = False
        validacao1 = False
        validacao2 = False

        if len(cpf) == 11:
            qtd = True
            cpf = [int(digito) for digito in cpf]
            
            soma = sum(a*b for a, b in zip (cpf[0:9], range (10, 1, -1)))
            digito = (soma * 10 % 11) % 10
            if cpf[9] == digito:
                validacao1 = True

            soma1 = sum(a*b for a, b in zip(cpf [0:10], range (11, 1, -1)))
            digito1 = (soma1 *10 % 11) % 10
            if cpf[10] == digito1:
                validacao2 = True

            if qtd == True and validacao1 == True and validacao2 == True:
                return f"O CPF {cpf_old} é válido."
            else:
                return f"O CPF {cpf_old} não é válido."
        else:
            return f"O CPF {cpf_old} não é válido."