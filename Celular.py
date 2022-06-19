import re

class Celular:
    def __init__(self, numero):
        if Celular.valida(numero):
            # O número será limpo, pois dessa forma poderá ter mais utilidade.
            self.__numero = self.__limpa_numero(numero)
            print(self.__numero)
        else:
            raise ValueError("Número é inválido!")

    def __str__(self):
        return Celular.monta_mascara(self.__numero)

    # Função consumida no escopo da classe para despoluir o número.
    def __limpa_numero(self, numero):
        numero_limpo = numero.replace(" ", "")
        numero_limpo = numero_limpo.replace("+", "")
        numero_limpo = numero_limpo.replace("(", "")
        numero_limpo = numero_limpo.replace(")", "")
        numero_limpo = numero_limpo.replace("-", "")
        numero_limpo = numero_limpo.strip()

        return numero_limpo

    @staticmethod
    def valida(numero):
        # Máximo: +55 (84) 9 9743-7563
        # Mínimo: "84997437563"
        # Separar em grupos serve também para fracionar a busca com .group(index) ou .findall()
        padrao = re.compile("([+]?[0-9]{2,3}[' ']?)?([(]?[0-9]{2}[)]?[' ']?)([9][' ']?)([0-9]{4}-?[0-9]{4})")
        
        return True if padrao.match(numero) else False
    
    @staticmethod
    def monta_mascara(numero):
        padrao = re.compile("([+]?[0-9]{2,3}[' ']?)?([(]?[0-9]{2}[)]?[' ']?)([9][' ']?)([0-9]{4}-?[0-9]{4})")
        partes_numero = padrao.findall(numero)[0]
        mascara_numero = ""

        # Só é possível montar uma máscara se o número informado possuir um segmento válido
        if Celular.valida(numero):
            # Caso o tamanho da primeira parte seja maior que 1, significa dizer que o código do país está preenchido.
            if len(partes_numero[0]) >= 2:
                # Caso não haja o caracter + no código do país, será adicionado
                if "+" not in partes_numero[0]:
                    mascara_numero += f"+{partes_numero[0]}"
                else:
                    # Caso não, essa parte só passará a compor a máscara do jeito que foi informado
                    mascara_numero += partes_numero[0]

                    # É necessário também que a primeira parte tenha um espaço ao final
                if " " not in partes_numero[0]:
                    mascara_numero += " "

            # Primeira "decoração" necessária para o DDD, caso não haja será adicionada
            if "(" not in partes_numero[1]:
                mascara_numero += f"({partes_numero[1]}"
            else:
                mascara_numero += partes_numero[1]

            # Segunda decoração para o DDD
            if ")" not in partes_numero[1]:
                # Aqui verificamos o final do DDD, isso é feito validando onde começa o DDD, na decoração "(" e onde termina, avaliando pelo tamanho.
                index_final_ddd = mascara_numero.index("(") + 3

                # Sabendo onde termina o DDD, a mascara é fatiada pegando do começo até o último dígito que se sabe do DDD.
                # Tal abordagem foi utlizada devido a impossibilidade da utilização do strip():
                # Caso o strip() fosse utilizado na condição de cima e esta não entrasse, o DDD ficaria colado ao 9. 
                mascara_numero = f"{mascara_numero[:index_final_ddd]}) "
                
            # Se não houver um espaço que separe o 9 do corpo do número, será adicionado
            if " " not in partes_numero[2]:
                mascara_numero += f"{partes_numero[2]} "
            else:
                mascara_numero += partes_numero[2]
            
            # Caso não haja hífen ao final do número, será adicionado
            if "-" not in partes_numero[3]:
                mascara_numero += f"{partes_numero[3][:4]}-{partes_numero[3][4:]}"
            else:
                mascara_numero += partes_numero[3]

            return mascara_numero
        else:
            raise ValueError("Numero é inválido!")

