from validate_docbr import CPF, CNPJ
from Cpf import Cpf
from Cnpj import Cnpj

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len (documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Documento não é reconhecido por essa quantidade de dígitos.")