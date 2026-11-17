
from interfaces import InterfaceUsuario
from itens import Inventario


class MenuDeItens:
    def __init__(self, ui: InterfaceUsuario):
        self.__ui = ui

    def usar_item(self, heroi, inventario: Inventario) -> bool:
        
        if inventario.esta_vazio():
            self.__ui.mostrar("Sua bolsa está vazia!")
            return False

        itens = inventario.listar()
        opcoes = [f"{item.nome} - {item.descricao}" for item in itens]
        opcoes.append("Voltar")

        escolha = self.__ui.perguntar_opcao("Sua bolsa de itens", opcoes)
        if escolha == len(opcoes): 

            return False

        item = itens[escolha - 1]
        self.__ui.mostrar(item.usar(heroi)) 

        inventario.remover(item)
        return True
