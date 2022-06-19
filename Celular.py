import re

class Celular:
    def __init__(self, numero):
        if Celular.valida(numero):
            self.__numero = numero
        else:
            raise ValueError("Número é inválido!")

    def __str__(self):
        return self.__numero

    @staticmethod
    def valida(numero):
        # Máximo: +55 (84) 9 9743-7563
        # Mínimo: "84997437563"
        # Separar em grupos serve também para fracionar a busca com .group(index) ou .findall()
        padrao = re.compile("([+]?[0-9]{2,3}[' ']?)?([(]?[0-9]{2}[)]?[' ']?)([9][' ']?)([0-9]{4}-?[0-9]{4})")
        
        return True if padrao.match(numero) else False

