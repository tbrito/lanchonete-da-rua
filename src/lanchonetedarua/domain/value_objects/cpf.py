class CPF:
    def __init__(self, valor):
        cpf_limpo = self._limpar_cpf(valor)

        if self._validar(list(map(int, cpf_limpo))):
            self.valor = cpf_limpo

        else:
            self.valor = None

    def _limpar_cpf(self, cpf):
        return ''.join(filter(str.isdigit, cpf))

    def _calcular_digitos_verificadores(self, cpf):
        cpf = list(map(int, cpf))
        soma = sum(cpf[i] * (10 - i) for i in range(9))
        resto = soma % 11
        if resto < 2:
            cpf.append(0)
        else:
            cpf.append(11 - resto)

        soma = sum(cpf[i] * (11 - i) for i in range(10))
        resto = soma % 11
        if resto < 2:
            cpf.append(0)
        else:
            cpf.append(11 - resto)

        return cpf[-2:]

    def _validar_digitos_verificadores(self, cpf):
        return cpf[-2:] == self._calcular_digitos_verificadores(cpf[:-2])

    def _validar(self, cpf):
        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * len(cpf):
            return False
        cpf_verificado = self._validar_digitos_verificadores(cpf)
        return cpf_verificado

    def formatado(self):
        cpf_formatado = '{}.{}.{}-{}'.format(
            self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:]
        )
        return cpf_formatado
