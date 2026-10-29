import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Tarefa:
    descricao: str
    concluida: bool = False


def exibir_tarefas(tarefas: List[Tarefa]) -> None:
    if not tarefas:
        print("\n📌 Sua lista de tarefas está vazia!")
        return

    print("\n📌 Suas Tarefas:")
    for numero, tarefa in enumerate(tarefas, start=1):
        status = " (concluída)" if tarefa.concluida else ""
        print(f"  {numero}. {tarefa.descricao}{status}")


def adicionar_tarefa(tarefas: List[Tarefa]) -> None:
    descricao = input("\nDigite a descrição da tarefa: ").strip()
    if not descricao:
        print("⚠️ A tarefa não pode estar vazia.")
        return

    tarefas.append(Tarefa(descricao))
    print(f"✅ Tarefa '{descricao}' adicionada com sucesso!")


def selecionar_tarefa(
    tarefas: List[Tarefa], concluida: bool
) -> Optional[int]:
    indices = [
        indice
        for indice, tarefa in enumerate(tarefas)
        if tarefa.concluida == concluida
    ]

    if not indices:
        if concluida:
            mensagem = "Não há tarefas concluídas para remover."
        elif tarefas:
            mensagem = "Não há tarefas pendentes."
        else:
            mensagem = "Não há tarefas para concluir."
        print(f"\n📌 {mensagem}")
        return None

    titulo = "concluídas" if concluida else "pendentes"
    print(f"\n📌 Tarefas {titulo}:")
    for numero, indice in enumerate(indices, start=1):
        print(f"  {numero}. {tarefas[indice].descricao}")

    acao = "remover" if concluida else "concluir"
    try:
        numero = int(input(f"\nDigite o número da tarefa que deseja {acao}: "))
    except ValueError:
        print("⚠️ Digite um número inteiro válido.")
        return None

    if not 1 <= numero <= len(indices):
        print("⚠️ Número de tarefa inválido.")
        return None

    return indices[numero - 1]


def marcar_tarefa_concluida(tarefas: List[Tarefa]) -> None:
    indice = selecionar_tarefa(tarefas, concluida=False)
    if indice is None:
        return

    tarefa = tarefas[indice]
    tarefa.concluida = True
    print(f"✅ Tarefa '{tarefa.descricao}' concluída!")


def remover_tarefa_concluida(tarefas: List[Tarefa]) -> None:
    indice = selecionar_tarefa(tarefas, concluida=True)
    if indice is None:
        return

    removida = tarefas.pop(indice)
    print(f"🗑️ Tarefa '{removida.descricao}' removida com sucesso!")


def exibir_menu() -> None:
    print("\n================================")
    print("      📝 LISTA DE TAREFAS       ")
    print("================================")
    print("1. Ver tarefas")
    print("2. Adicionar nova tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa concluída")
    print("5. Sair")


def gerenciar_tarefas() -> None:
    tarefas: List[Tarefa] = []
    acoes = {
        "1": lambda: exibir_tarefas(tarefas),
        "2": lambda: adicionar_tarefa(tarefas),
        "3": lambda: marcar_tarefa_concluida(tarefas),
        "4": lambda: remover_tarefa_concluida(tarefas),
    }

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1 a 5): ").strip()

        if opcao == "5":
            print("\nSaindo do gerenciador de tarefas. Até logo! 👋")
            return

        acao = acoes.get(opcao)
        if acao is None:
            print("\n❌ Opção inválida! Escolha entre 1 e 5.")
            continue

        acao()


def configurar_saida() -> None:
    reconfigurar = getattr(sys.stdout, "reconfigure", None)
    if reconfigurar is not None:
        reconfigurar(encoding="utf-8")


if __name__ == "__main__":
    configurar_saida()
    gerenciar_tarefas()
