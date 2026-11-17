
from combate import SistemaCombate
from fabricas import FabricaFlorestaSombria
from fadas import FADAS_DISPONIVEIS
from interface_usuario import ConsoleUI
from itens import CantoMagico, CirculoDeRunasDeCristal, Inventario, PoDePirlimpimpim
from jogo import Jogo
from menu_itens import MenuDeItens


def main() -> None:
    ui = ConsoleUI()

    ui.mostrar("=" * 44)
    ui.mostrar("        MUNDO DAS FADAS - RPG de Console")
    ui.mostrar("=" * 44)

    nome = ui.perguntar_texto("\nQual é o nome da sua fada? ") or "Fadinha"
    opcoes = [f"{classe.TITULO} - {classe.DESCRICAO}" for classe in FADAS_DISPONIVEIS]
    escolha = ui.perguntar_opcao("Escolha sua classe de fada", opcoes)
    classe_escolhida = FADAS_DISPONIVEIS[escolha - 1]
    heroi = classe_escolhida(nome) 

    inventario = Inventario()
    inventario.adicionar(PoDePirlimpimpim())
    inventario.adicionar(CantoMagico())
    inventario.adicionar(CirculoDeRunasDeCristal())

    menu_itens = MenuDeItens(ui)
    combate = SistemaCombate(ui, menu_itens)
    fabrica = FabricaFlorestaSombria()
    jogo = Jogo(ui, heroi, fabrica, inventario, combate, menu_itens)

    jogo.iniciar()


if __name__ == "__main__":
    main()
