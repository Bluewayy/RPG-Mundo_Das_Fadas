
import random

from interfaces import Combatente


class Criatura(Combatente):
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):

        self.__nome = nome
        self.__vida_maxima = vida
        self.__vida = vida
        self.__ataque = ataque
        self.__defesa = defesa

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, valor: int) -> None:
       
        self.__vida = max(0, min(valor, self.__vida_maxima))

    @property
    def vida_maxima(self) -> int:
        return self.__vida_maxima

    @property
    def ataque(self) -> int:
        return self.__ataque

    @ataque.setter
    def ataque(self, valor: int) -> None:
        self.__ataque = max(0, valor) 

    @property
    def defesa(self) -> int:
        return self.__defesa

    @defesa.setter
    def defesa(self, valor: int) -> None:
        self.__defesa = max(0, valor)

   
    def esta_vivo(self) -> bool:
        return self.__vida > 0

    def receber_dano(self, dano_bruto: int) -> int:
        
        dano_real = max(1, dano_bruto - self.defesa)
        self.vida = self.vida - dano_real  
        return dano_real

    def atacar(self, alvo: Combatente) -> str:
       
        dano = alvo.receber_dano(self.ataque + random.randint(0, 3))
        return f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!"
