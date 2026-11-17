
import random

from criaturas import Criatura
from interfaces import Combatente


class Inimigo(Criatura):
   ...

class Gobweb(Inimigo):
    def __init__(self):
        super().__init__("Gobweb", vida=30, ataque=9, defesa=2)

    def atacar(self, alvo: Combatente) -> str:
        dano = alvo.receber_dano(self.ataque + random.randint(0, 2))
        return f"{self.nome} joga uma teia pegajosa em {alvo.nome} e causa {dano} de dano!"


class CorvoSombrio(Inimigo):
    CHANCE_CRITICO = 0.25

    def __init__(self):
        super().__init__("Corvo Sombrio", vida=40, ataque=12, defesa=3)

    def atacar(self, alvo: Combatente) -> str:
        ataque_total = self.ataque + random.randint(0, 3)
        if random.random() < self.CHANCE_CRITICO:
            dano = alvo.receber_dano(ataque_total * 2)
            return (f"{self.nome} mergulha em um GOLPE CRÍTICO contra "
                    f"{alvo.nome} e causa {dano} de dano!")
        dano = alvo.receber_dano(ataque_total)
        return f"{self.nome} bica {alvo.nome} e causa {dano} de dano!"


class BestaSombria(Inimigo):
   

    def __init__(self):
        super().__init__("Besta Sombria", vida=80, ataque=13, defesa=6)
        self.__ataques_feitos = 0  

    def atacar(self, alvo: Combatente) -> str:
        self.__ataques_feitos += 1
        if self.__ataques_feitos % 3 == 0: 
            dano = alvo.receber_dano(self.ataque * 2)
            return (f"{self.nome} ergue os galhos e desfere um ESMAGAMENTO em "
                    f"{alvo.nome}: {dano} de dano!")
        dano = alvo.receber_dano(self.ataque + random.randint(0, 3))
        return f"{self.nome} golpeia {alvo.nome} com um galho e causa {dano} de dano!"
