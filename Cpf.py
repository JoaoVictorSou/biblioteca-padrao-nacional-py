class Cpf:
    def __init__(self, numero_cpf: str):
        self.numero_documento = numero_cpf if Cpf.cpf_valido(numero_cpf) else ""
    
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