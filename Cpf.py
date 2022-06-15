class Cpf:
    def __init__(self, numero_cpf: str):
        self.__numero_documento = numero_cpf if Cpf.cpf_valido(numero_cpf) else ""
    
    def __str__(self):
        return Cpf.monta_estrutura(self.__numero_documento)

    @staticmethod
    def cpf_valido(numero_cpf: str):
        # Verificação se há apenas números no valor informado
        int(numero_cpf)
        
        # Verificação quantidade de dígitos
        str_numero_cpf = str(numero_cpf)

        if len(str_numero_cpf) == 11:
            return True
        else:
            raise ValueError("CPF deve conter exatamente 11 dígitos.")
        
    @staticmethod
    def monta_estrutura(numero_cpf: str):
        if Cpf.cpf_valido(numero_cpf):
            str_numero_cpf = str(numero_cpf)
            # Cortando o CPF com base em 000.000.000-00
            return f"{str_numero_cpf[:3]}.{str_numero_cpf[3:6]}.{str_numero_cpf[6:9]}-{str_numero_cpf[9:]}"