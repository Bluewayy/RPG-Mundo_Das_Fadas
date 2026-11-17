
import random

from combate import ResultadoCombate, SistemaCombate
from fadas import Fada
from interfaces import FabricaDeInimigos, InterfaceUsuario
from itens import Inventario, sortear_item
from menu_itens import MenuDeItens


class Jogo:
    VITORIAS_PARA_CHEFE = 3   
    DESCANSOS_MAXIMOS = 2    

    def __init__(self, ui: InterfaceUsuario, heroi: Fada,
                 fabrica: FabricaDeInimigos, inventario: Inventario,
                 combate: SistemaCombate, menu_itens: MenuDeItens):
        self.__ui = ui
        self.__heroi = heroi
        self.__fabrica = fabrica
        self.__inventario = inventario
        self.__combate = combate
        self.__menu_itens = menu_itens

        self.__vitorias = 0
        self.__descansos_restantes = self.DESCANSOS_MAXIMOS
        self.__rodando = True

    
    def iniciar(self) -> None:
        self.__ui.mostrar(
            f"\n{self.__heroi.nome}, a {self.__heroi.TITULO}, parte em uma "
            "jornada pela Floresta Sombria.\nDerrote os monstros e enfrente "
            "a Besta Sombria para salvar o Mundo das Fadas!"
        )

        while self.__rodando:
            opcoes = [
                "Explorar a floresta",
                "Ver status",
                "Usar item",
                f"Descansar na clareira ({self.__descansos_restantes} restantes)",
                "Sair do jogo",
            ]
            escolha = self.__ui.perguntar_opcao("Clareira das Fadas", opcoes)

            if escolha == 1:
                self.__explorar()
            elif escolha == 2:
                self.__mostrar_status()
            elif escolha == 3:
                self.__menu_itens.usar_item(self.__heroi, self.__inventario)
            elif escolha == 4:
                self.__descansar()
            elif escolha == 5:
                self.__ui.mostrar("Até a próxima aventura!")
                self.__rodando = False

    
    def __explorar(self) -> None:
        if self.__vitorias >= self.VITORIAS_PARA_CHEFE:
            self.__ui.mostrar(
                "A floresta escurece e você sente uma presença sombria... A Besta Sombria aparece!"
            )
           
            resultado = self.__combate.lutar(self.__heroi,  self.__fabrica.criar_chefe(),
                self.__inventario, pode_fugir=False)

            if resultado == ResultadoCombate.VITORIA:
                self.__final_vitoria()
            elif resultado == ResultadoCombate.DERROTA:
                self.__final_derrota()
            return

       
        sorte = random.random()
        if sorte < 0.60:
            self.__encontrar_inimigo()
        elif sorte < 0.85:
            item = sortear_item()
            self.__inventario.adicionar(item)
            self.__ui.mostrar(f"\nVocê encontrou um item brilhando: {item.nome}!")
        else:
            curado = self.__heroi.curar(10)
            self.__ui.mostrar(
                f"\nVocê achou uma fonte de orvalho mágico e recuperou {curado} de vida.")

    def __encontrar_inimigo(self) -> None:
        inimigo = self.__fabrica.criar_inimigo_comum()
        resultado = self.__combate.lutar(self.__heroi, inimigo, self.__inventario)

        if resultado == ResultadoCombate.VITORIA:
            self.__vitorias += 1
            self.__ui.mostrar(f"Vitórias: {self.__vitorias}/{self.VITORIAS_PARA_CHEFE}")
        elif resultado == ResultadoCombate.DERROTA:
            self.__final_derrota()

    def __descansar(self) -> None:
        if self.__descansos_restantes <= 0:
            self.__ui.mostrar("Você já descansou o bastante. Não há mais tempo!")
            return
        self.__descansos_restantes -= 1
        curado = self.__heroi.curar(25)
        self.__ui.mostrar(f"Você descansa sob as estrelas e recupera {curado} de vida.")

    def __mostrar_status(self) -> None:
        h = self.__heroi
        nomes = [item.nome for item in self.__inventario.listar()]
        itens = ", ".join(nomes) if nomes else "(vazio)"
        self.__ui.mostrar(
            f"\n--- {h.nome} ({h.TITULO}) ---\n"
            f"Vida: {h.vida}/{h.vida_maxima} | Ataque: {h.ataque} | Defesa: {h.defesa}\n"
            f"Habilidade: {h.nome_habilidade}\n"
            f"Vitórias: {self.__vitorias}/{self.VITORIAS_PARA_CHEFE}\n"
            f"Itens: {itens}"
        )


    def __final_vitoria(self) -> None:
        self.__ui.mostrar(
            "\n*** PARABÉNS! ***\n"
            "A luz volta à Floresta Sombria e as fadas celebram o seu nome!")
        self.__rodando = False

    def __final_derrota(self) -> None:
        self.__ui.mostrar(
            "\n*** FIM DE JOGO ***\n"
            "Sua luz se apagou... Mas toda fada pode tentar de novo!")
        self.__rodando = False