
import random
from typing import List

from interfaces import Curavel, Fortalecivel, Item



class PoDePirlimpimpim(Item):
    nome = "Pó de Estrelas"
    descricao = "Cura 20 pontos de vida."
    CURA = 20

    def usar(self, alvo: Curavel) -> str:
        curado = alvo.curar(self.CURA)
        return f"O {self.nome} brilha e você recupera {curado} de vida!"


class CantoMagico(Item):
    nome = "Canto Mágico"
    descricao = "Aumenta o ataque em 2 para sempre."
    BONUS = 2

    def usar(self, alvo: Fortalecivel) -> str:
        alvo.aumentar_ataque(self.BONUS)
        return f"A {self.nome} enche você de poder: +{self.BONUS} de ataque!"


class CirculoDeRunasDeCristal(Item):
    nome = "Círculo de Runas de Cristal"
    descricao = "Aumenta a defesa em 5 para sempre."
    BONUS = 5

    def usar(self, alvo: Fortalecivel) -> str:
        alvo.aumentar_defesa(self.BONUS)
        return f"O {self.nome} envolve você com runas: +{self.BONUS} de defesa!"


ITENS_SORTEAVEIS = [PoDePirlimpimpim, CantoMagico, CirculoDeRunasDeCristal]
PESOS_DE_SORTEIO = [60, 30, 20]  


def sortear_item() -> Item:
    classe = random.choices(ITENS_SORTEAVEIS, weights=PESOS_DE_SORTEIO)[0]
    return classe()


class Inventario:

    def __init__(self):
        self.__itens: List[Item] = []

    def adicionar(self, item: Item) -> None:
        self.__itens.append(item)

    def remover(self, item: Item) -> None:
        self.__itens.remove(item)

    def listar(self) -> List[Item]:
        return list(self.__itens)  

    def esta_vazio(self) -> bool:
        return len(self.__itens) == 0
