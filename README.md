# Mundo das Fadas — RPG de Console em Python

Jogo de RPG por turnos, jogado no terminal, criado para **aprender Orientação a
Objetos (POO)** e os **cinco princípios SOLID** de forma simples.

## Como rodar

**Requisito:** Python 3.8 ou superior (nenhuma biblioteca externa).

```bash
# 1. Entre na pasta do projeto
cd mundo-das-fadas

# 2. Execute o jogo
python main.py        # no Linux/Mac, se preciso: python3 main.py
```

## Como jogar

1. Digite o nome da sua fada e escolha a classe:

   | Classe | Vida | Ataque | Defesa | Habilidade especial |
   |---|---|---|---|---|
   | Fada Guerreira | 100 | 14 | 6 | **Investida Cintilante**: dano dobrado + força da armadura |
   | Fada Maga | 70 | 18 | 3 | **Chuva de Estrelas**: 3 golpes mágicos seguidos |
   | Fada Guardiã | 120 | 10 | 9 | **Escudo de Pétalas**: cura, +1 de defesa e fere o inimigo |

2. No menu da clareira você pode **explorar a floresta**, ver o status, usar
   itens ou descansar (2 vezes por partida).
3. Explorando, você encontra **Gobwebs**, **Corvos Sombrios** ou itens.
4. Depois de **3 vitórias**, a próxima exploração leva ao mini-chefe, o
   **Besta Sombria**. Derrote-o para vencer o jogo!
5. No combate, a cada turno você escolhe: atacar, usar a habilidade (tem
   tempo de recarga), usar um item ou fugir (não funciona contra o chefe).

**Itens:** *Pó de Estrelas* (cura 20 de vida), *Canto Mágico* (+2 de ataque
permanente) e *Círculo de Runas de Cristal* (+5 de defesa permanente).

## Estrutura do projeto

```
mundo-das-fadas/
├── main.py               # ponto de entrada; monta as peças do jogo
├── interfaces.py         # contratos (classes abstratas) usados em todo o projeto
├── criaturas.py          # classe base Criatura (encapsulamento + herança)
├── fadas.py              # Fada (abstrata) + Guerreira, Maga e Guardiã
├── inimigos.py           # Gobweb, Corvo Sombrio e Besta Sombria (mini-chefe)
├── itens.py              # Pó de Estrelas, Canto Mágico, Círculo de Runas e Inventário
├── menu_itens.py         # menu para escolher e usar itens
├── combate.py            # sistema de combate por turnos
├── fabricas.py           # fábrica que cria os inimigos da Floresta Sombria
├── interface_usuario.py  # implementação do terminal (print/input)
├── jogo.py               # fluxo principal da aventura
└── README.md
```

## Conceitos de POO e onde estão

| Conceito | Onde ver no código |
|---|---|
| **Classes e objetos** | Toda criatura é um objeto: `FadaMaga("Lila")`, `Gobweb()` |
| **Encapsulamento** | `criaturas.py`: atributos privados (`__vida`) com getters/setters via `@property`; `itens.py`: lista privada em `Inventario` |
| **Herança** | `Criatura` → `Fada` → `FadaMaga`; `Criatura` → `Inimigo` → `Gobweb` |
| **Polimorfismo** | `atacar()` sobrescrito em `Gobweb`, `CorvoSombrio` e `EntSombrio`; `_executar_habilidade()` diferente em cada fada; `usar()` diferente em cada item |
| **Abstração / Interfaces** | `interfaces.py`: classes abstratas com `ABC` e `@abstractmethod` |

## Como o SOLID foi aplicado

### S — Single Responsibility (Responsabilidade Única)
*Cada classe tem um único motivo para mudar.*

- `SistemaCombate` só cuida de lutas.
- `Inventario` só guarda itens.
- `ConsoleUI` só faz entrada/saída de texto.
- `FabricaFlorestaSombria` só cria inimigos.
- `Jogo` só controla o fluxo da aventura.

### O — Open/Closed (Aberto para extensão, fechado para modificação)
*Dá para adicionar coisas novas sem mexer no código que já funciona.*

- **Nova fada:** crie `class FadaCurandeira(Fada)` e inclua em `FADAS_DISPONIVEIS`.
- **Novo item:** crie uma classe que herde de `Item` e inclua em `ITENS_SORTEAVEIS`.
- **Novo inimigo:** crie uma classe que herde de `Inimigo`; o combate não muda.
- **Nova região:** crie outra `FabricaDeInimigos`.

### L — Liskov Substitution (Substituição de Liskov)
*Uma classe filha pode ser usada no lugar da classe mãe sem quebrar nada.*

- `SistemaCombate.lutar()` aceita qualquer `Combatente`: Gobweb, Corvo ou Ent
  funcionam sem que o combate saiba qual é.
- Todas as fadas funcionam onde se espera uma `Fada`.
- Todos os `atacar()` seguem o mesmo contrato: recebem um alvo e devolvem um texto.

### I — Interface Segregation (Segregação de Interfaces)
*Interfaces pequenas e específicas, em vez de uma gigante.*

- `Combatente` (lutar), `Habilidoso` (habilidade especial), `Curavel` (receber cura)
  e `Fortalecivel` (ganhar ataque/defesa) são contratos separados.
- Os inimigos implementam só `Combatente`: não são obrigados a ter habilidade.
- O `PoDePirlimpimpim` (Pó de Estrelas) só precisa de `Curavel`; o `CantoMagico` e o `CirculoDeRunasDeCristal` só de `Fortalecivel`.

### D — Dependency Inversion (Inversão de Dependência)
*Classes de alto nível dependem de abstrações, não de classes concretas.*

- `Jogo` e `SistemaCombate` recebem `InterfaceUsuario`, `FabricaDeInimigos` e
  `MenuDeItens` pelo **construtor** (injeção de dependência).
- Só o `main.py` conhece as classes concretas (`ConsoleUI`, `FabricaFlorestaSombria`).
- Resultado: trocar o terminal por uma interface gráfica exige apenas uma nova
  classe que herde de `InterfaceUsuario`.

## Ideias para evoluir o projeto

- Novos itens (ex.: *Orvalho de Flor*) ou novas fadas.
- Sistema de níveis e experiência.
- Salvar o jogo em arquivo.
- Testes automáticos usando uma `InterfaceUsuario` falsa (graças ao DIP, é fácil!).
