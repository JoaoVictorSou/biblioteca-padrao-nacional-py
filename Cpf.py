from validate_docbr import CPF

class Cpf:
    def __init__(self, numero_cpf: str):
        if Cpf.cpf_valido(numero_cpf):
            self.__numero_documento = numero_cpf
        else:
            raise ValueError("CPF não segue regras estabelecidas.")
    
    def __str__(self):
        return Cpf.monta_mascara(self.__numero_documento)

    @staticmethod
    def cpf_valido(numero_cpf: str):
        # Verificação se há apenas números no valor informado
        int(numero_cpf)
        
        # Verificação quantidade de dígitos
        str_numero_cpf = str(numero_cpf)

        if len(str_numero_cpf) == 11:
            # Conferindo se o CPF segue as regras de negócio estabelecidas para o documento
            validador = CPF()
            return validador.validate(str_numero_cpf)
        else:
            raise ValueError("CPF deve conter exatamente 11 dígitos.")
        
    @staticmethod
    def monta_mascara(numero_cpf: str):
        if Cpf.cpf_valido(numero_cpf):
            str_numero_cpf = str(numero_cpf)
            # Cortando o CPF com base em 000.000.000-00
            return f"{str_numero_cpf[:3]}.{str_numero_cpf[3:6]}.{str_numero_cpf[6:9]}-{str_numero_cpf[9:]}"