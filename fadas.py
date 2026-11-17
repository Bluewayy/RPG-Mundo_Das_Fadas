
from abc import abstractmethod

from criaturas import Criatura
from interfaces import Combatente, Curavel, Fortalecivel, Habilidoso


class Fada(Criatura, Habilidoso, Curavel, Fortalecivel):
    

    TITULO = "Fada"
    DESCRICAO = ""
    RECARGA = 3 

    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        super().__init__(nome, vida, ataque, defesa)
        self.__recarga = 0 

    @property
    def recarga_restante(self) -> int:
        return self.__recarga

    def pode_usar_habilidade(self) -> bool:
        return self.__recarga == 0

    def usar_habilidade(self, alvo: Combatente) -> str:
        if not self.pode_usar_habilidade():
            return f"{self.nome_habilidade} ainda está recarregando!"
        texto = self._executar_habilidade(alvo) 

        self.__recarga = self.RECARGA
        return texto

    @abstractmethod
    def _executar_habilidade(self, alvo: Combatente) -> str:
       ...

    def passar_turno(self) -> None:
        if self.__recarga > 0:
            self.__recarga -= 1

   
    def curar(self, quantidade: int) -> int:
        vida_antes = self.vida
        self.vida = self.vida + quantidade
        return self.vida - vida_antes

    def aumentar_ataque(self, quantidade: int) -> None:
        self.ataque = self.ataque + quantidade

    def aumentar_defesa(self, quantidade: int) -> None:
        self.defesa = self.defesa + quantidade


class FadaGuerreira(Fada):
    TITULO = "Fada Guerreira"
    DESCRICAO = "Equilibrada e resistente. Golpes fortes de perto."
    nome_habilidade = "Investida Cintilante"

    def __init__(self, nome: str):
        super().__init__(nome, vida=100, ataque=14, defesa=6)

    def _executar_habilidade(self, alvo: Combatente) -> str:
        
        dano = alvo.receber_dano(self.ataque * 2 + self.defesa)
        return (f"{self.nome} usa {self.nome_habilidade} e causa {dano} "
                f"de dano em {alvo.nome}!")


class FadaMaga(Fada):
    TITULO = "Fada Maga"
    DESCRICAO = "Frágil, mas com muito poder mágico."
    nome_habilidade = "Chuva de Estrelas"

    def __init__(self, nome: str):
        super().__init__(nome, vida=70, ataque=18, defesa=3)

    def _executar_habilidade(self, alvo: Combatente) -> str:
        
        total = 0
        for _ in range(3):
            total += alvo.receber_dano(int(self.ataque * 0.7))
        return (f"{self.nome} invoca {self.nome_habilidade}: 3 estrelas caem "
                f"sobre {alvo.nome} e causam {total} de dano no total!")


class FadaGuardia(Fada):
    TITULO = "Fada Guardiã"
    DESCRICAO = "Muito resistente. Protege a si mesma enquanto luta."
    nome_habilidade = "Escudo de Pétalas"

    def __init__(self, nome: str):
        super().__init__(nome, vida=120, ataque=10, defesa=9)

    def _executar_habilidade(self, alvo: Combatente) -> str:
        curado = self.curar(15)
        self.defesa = self.defesa + 1 

        dano = alvo.receber_dano(self.ataque + 4)
        return (f"{self.nome} ergue o {self.nome_habilidade}: recupera {curado} "
                f"de vida, ganha +1 de defesa e as pétalas ferem {alvo.nome} "
                f"em {dano} de dano!")


FADAS_DISPONIVEIS = [FadaGuerreira, FadaMaga, FadaGuardia]
