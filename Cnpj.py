from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, numero_cnpj: str):
        if Cnpj.cnpj_valido(numero_cnpj):
            self.__numero_documento = numero_cnpj
        else:
            raise ValueError("CPNJ inválido!")

    def __str__(self):
        return Cnpj.monta_mascara(self.__numero_documento)

    @staticmethod
    def valido(numero_cnpj):
        cnpj = CNPJ()
        # VALIDAÇÃO SE POSSUE APENAS ALGARISMOS NUMÉRICOS
        int(numero_cnpj)

        # VALIDAÇÃO QUANTIDADE DE ALGARISMOS
        str_numero_cnpj = str(numero_cnpj)
        if len(str_numero_cnpj) == 14:
            return cnpj.validate(numero_cnpj)
        else:
            raise ValueError("CNPJ deve conter 14 dígitos!")
    
    @staticmethod
    def monta_mascara(numero_cnpj):
        cnpj = CNPJ()
        return cnpj.mask(numero_cnpj)