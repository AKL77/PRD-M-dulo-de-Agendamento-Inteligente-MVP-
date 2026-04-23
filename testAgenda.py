from unittest import TestCase
from agenda import Agenda

class TestAgenda(TestCase):
    def test_definir_horario_medico(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = "08:00", fim = "12:00")

        self.assertEqual(agenda.horario_inicio, "08:00")
        self.assertEqual(agenda.horario_fim, "12:00")