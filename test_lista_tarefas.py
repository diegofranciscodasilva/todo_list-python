import unittest
from io import StringIO
from unittest.mock import patch

from lista_tarefas import (
    Tarefa,
    gerenciar_tarefas,
    marcar_tarefa_concluida,
    remover_tarefa_concluida,
    selecionar_tarefa,
)


class TestListaTarefas(unittest.TestCase):
    def test_marca_tarefa_pendente_como_concluida(self):
        tarefas = [Tarefa("Estudar Python")]

        with patch("sys.stdout", new_callable=StringIO), patch(
            "builtins.input", return_value="1"
        ):
            marcar_tarefa_concluida(tarefas)

        self.assertTrue(tarefas[0].concluida)

    def test_remove_tarefa_concluida_sem_remover_pendentes(self):
        pendente = Tarefa("Preparar café")
        concluida = Tarefa("Estudar Python", concluida=True)
        tarefas = [pendente, concluida]

        with patch("sys.stdout", new_callable=StringIO), patch(
            "builtins.input", return_value="1"
        ):
            remover_tarefa_concluida(tarefas)

        self.assertEqual(tarefas, [pendente])

    def test_rejeita_numero_de_tarefa_invalido(self):
        tarefas = [Tarefa("Estudar Python")]

        with patch("sys.stdout", new_callable=StringIO), patch(
            "builtins.input", return_value="2"
        ):
            indice = selecionar_tarefa(tarefas, concluida=False)

        self.assertIsNone(indice)
        self.assertFalse(tarefas[0].concluida)

    def test_rejeita_entrada_que_nao_e_numero(self):
        tarefas = [Tarefa("Estudar Python")]

        with patch("sys.stdout", new_callable=StringIO), patch(
            "builtins.input", return_value="abc"
        ):
            indice = selecionar_tarefa(tarefas, concluida=False)

        self.assertIsNone(indice)

    def test_nao_seleciona_quando_nao_ha_tarefas_do_status_pedido(self):
        tarefas = [Tarefa("Estudar Python", concluida=True)]

        with patch("sys.stdout", new_callable=StringIO), patch(
            "builtins.input"
        ) as entrada:
            indice = selecionar_tarefa(tarefas, concluida=False)

        self.assertIsNone(indice)
        entrada.assert_not_called()

    def test_fluxo_do_menu_adiciona_conclui_e_remove_tarefa(self):
        saida = StringIO()
        respostas = ["2", "Estudar Python", "3", "1", "1", "4", "1", "5"]

        with patch("sys.stdout", saida), patch(
            "builtins.input", side_effect=respostas
        ):
            gerenciar_tarefas()

        self.assertIn("Tarefa 'Estudar Python' concluída!", saida.getvalue())
        self.assertIn("Tarefa 'Estudar Python' removida com sucesso!", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
