
import random

from inimigos import CorvoSombrio, BestaSombria, Gobweb
from interfaces import Combatente, FabricaDeInimigos


class FabricaFlorestaSombria(FabricaDeInimigos):
    def criar_inimigo_comum(self) -> Combatente:
        classe = random.choice([Gobweb, CorvoSombrio])
        return classe()

    def criar_chefe(self) -> Combatente:
        return BestaSombria()
