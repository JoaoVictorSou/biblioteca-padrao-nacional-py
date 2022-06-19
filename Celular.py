from multiprocessing.sharedctypes import Value
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
        padrao = re.compile("[(][0-9]{2}[)][9][0-9]{4}-[0-9]{4}")
        
        return True if padrao.match(numero) else False
    
celular = Celular("(84)98755-3968")
print(celular)
