
from abc import ABC, abstractmethod
from typing import List


class Combatente(ABC):

    @property
    @abstractmethod
    def nome(self) -> str:
        ...

    @property
    @abstractmethod
    def vida(self) -> int:
        ...

    @property
    @abstractmethod
    def vida_maxima(self) -> int:
        ...

    @abstractmethod
    def esta_vivo(self) -> bool:
        ...

    @abstractmethod
    def receber_dano(self, dano_bruto: int) -> int:
       ...

    @abstractmethod
    def atacar(self, alvo: "Combatente") -> str:
        ...

class Habilidoso(ABC):
    

    nome_habilidade: str 

    @property
    @abstractmethod
    def recarga_restante(self) -> int:
        ...

    @abstractmethod
    def pode_usar_habilidade(self) -> bool:
        ...

    @abstractmethod
    def usar_habilidade(self, alvo: Combatente) -> str:
        ...

    @abstractmethod
    def passar_turno(self) -> None:
        ...


class Curavel(ABC):

    @abstractmethod
    def curar(self, quantidade: int) -> int:
        ...

class Fortalecivel(ABC):

    @abstractmethod
    def aumentar_ataque(self, quantidade: int) -> None:
        ...

    @abstractmethod
    def aumentar_defesa(self, quantidade: int) -> None:
        ...


class Item(ABC):

    @property
    @abstractmethod
    def nome(self) -> str:
        ...

    @property
    @abstractmethod
    def descricao(self) -> str:
        ...

    @abstractmethod
    def usar(self, alvo) -> str:
       ...

class InterfaceUsuario(ABC):


    @abstractmethod
    def mostrar(self, texto: str) -> None:
        ...

    @abstractmethod
    def perguntar_texto(self, pergunta: str) -> str:
        ...

    @abstractmethod
    def perguntar_opcao(self, titulo: str, opcoes: List[str]) -> int:
        ...

    @abstractmethod
    def pausar(self) -> None:
        ...



class FabricaDeInimigos(ABC):
   

    @abstractmethod
    def criar_inimigo_comum(self) -> Combatente:
        ...

    @abstractmethod
    def criar_chefe(self) -> Combatente:
        ...