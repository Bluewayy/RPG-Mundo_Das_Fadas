
from typing import List

from interfaces import InterfaceUsuario


class ConsoleUI(InterfaceUsuario):
    def mostrar(self, texto: str) -> None:
        print(texto)

    def perguntar_texto(self, pergunta: str) -> str:
        return input(pergunta).strip()

    def perguntar_opcao(self, titulo: str, opcoes: List[str]) -> int:
        print(f"\n=== {titulo} ===")
        for numero, opcao in enumerate(opcoes, start=1):
            print(f"  {numero}) {opcao}")
        while True:  # repete até o jogador digitar uma opção válida
            resposta = input("Escolha: ").strip()
            if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
                return int(resposta)
            print("Opção inválida. Digite um dos números do menu.")

    def pausar(self) -> None:
        input("\n(Pressione ENTER para continuar...)")
