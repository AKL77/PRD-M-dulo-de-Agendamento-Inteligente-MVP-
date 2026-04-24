from unittest import TestCase
from agenda import Agenda
from datetime import datetime

class TestAgenda(TestCase):
    def test_definir_horario_medico(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = "08:00", fim = "12:00")

        self.assertEqual(agenda.horario_inicio, "08:00")
        self.assertEqual(agenda.horario_fim, "12:00")

    def test_agendamento_consulta(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = "08:00", fim = "12:00")

        horario_consulta = datetime(2026, 4, 24, 9, 0)

        paciente = "03114976085"

        agenda.agendar_consulta(paciente, horario_consulta)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta], paciente)

    def test_agendamento_consulta_horario_indisponivel(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = "08:00", fim = "12:00")

        horario_consulta = datetime(2026, 4, 24, 7, 0)

        paciente = "03114976085"

        agendamento = agenda.agendar_consulta(paciente, horario_consulta)

        self.assertEqual(agendamento, "O horário informado não é contemplado pelo médico")

        self.assertNotIn(horario_consulta, agenda.consultas_marcadas)

