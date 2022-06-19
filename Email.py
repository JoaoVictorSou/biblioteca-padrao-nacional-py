import re

class Email:
    def __init__(self, email):
        if Email.valida(email):
            self.__email = email
        else:
            raise ValueError("Email inválido!")

    def __str__(self):
        return self.__email

    @staticmethod
    def valida(email):
        padrao_marcado_email = re.compile("[\w,.]{5,50}@[a-z]{3,10}[.][a-z]{3,5}(.[a-z]{2,3})?")
        # No quantificador não se coloca espaço em branco entre os intervalos ex {2, 5};
        # Caso haja um espaço entre o marcador de caracteres, ele passará a procurar por espaços no padrão [a, b]
        # O termo especial \w não engloba pontos nem espaços vazios;
        # Caso haja um erro dentro de um padrão opicional esse será ignorado, ao que parece.

        return True if padrao_marcado_email.match(email) else False