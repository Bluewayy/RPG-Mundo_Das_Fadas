
import random
from enum import Enum

from fadas import Fada
from interfaces import Combatente, InterfaceUsuario
from itens import Inventario
from menu_itens import MenuDeItens


class ResultadoCombate(Enum):
    
    VITORIA = 1
    DERROTA = 2
    FUGA = 3


class SistemaCombate:
    def __init__(self, ui: InterfaceUsuario, menu_itens: MenuDeItens):
        self.__ui = ui
        self.__menu_itens = menu_itens

    def lutar(self, heroi: Fada, inimigo: Combatente, inventario: Inventario,
              pode_fugir: bool = True) -> ResultadoCombate:
        self.__ui.mostrar(f"\n*** {inimigo.nome} apareceu! ***")

        while True:
            self.__mostrar_status(heroi, inimigo)

            
            if heroi.pode_usar_habilidade():
                texto_habilidade = f"Habilidade: {heroi.nome_habilidade}"
            else:
                texto_habilidade = (f"Habilidade: {heroi.nome_habilidade} "
                                    f"(recarregando: {heroi.recarga_restante})")
            opcoes = ["Atacar", texto_habilidade, "Usar item"]
            if pode_fugir:
                opcoes.append("Fugir")

            escolha = self.__ui.perguntar_opcao("Seu turno", opcoes)

            if escolha == 1:
                self.__ui.mostrar(heroi.atacar(inimigo))
            elif escolha == 2:
                if not heroi.pode_usar_habilidade():
                    self.__ui.mostrar("A habilidade ainda está recarregando!")
                    continue 
                self.__ui.mostrar(heroi.usar_habilidade(inimigo))
            elif escolha == 3:
                if not self.__menu_itens.usar_item(heroi, inventario):
                    continue 

            elif escolha == 4:  

                if random.random() < 0.5:
                    self.__ui.mostrar("Você bate as asinhas e foge da luta!")
                    return ResultadoCombate.FUGA
                self.__ui.mostrar("Não deu para fugir!")

            
            if not inimigo.esta_vivo():
                self.__ui.mostrar(f"\nVocê derrotou {inimigo.nome}!")
                return ResultadoCombate.VITORIA

            
            self.__ui.mostrar(inimigo.atacar(heroi))
            heroi.passar_turno() 

            
            if not heroi.esta_vivo():
                return ResultadoCombate.DERROTA

    @staticmethod
    def _barra(atual: int, maximo: int, tamanho: int = 10) -> str:
        cheios = round(tamanho * atual / maximo)
        return "[" + "#" * cheios + "-" * (tamanho - cheios) + "]"
    
    
    def __mostrar_status(self, heroi: Fada, inimigo: Combatente) -> None:
        self.__ui.mostrar("\n" + "-" * 44)
        for criatura in (heroi, inimigo):
            barra = self._barra(criatura.vida, criatura.vida_maxima)
            self.__ui.mostrar(f"{criatura.nome:<16} {barra} "
                              f"{criatura.vida}/{criatura.vida_maxima}")
        self.__ui.mostrar("-" * 44)
