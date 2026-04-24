from unittest import TestCase
from agenda import Agenda
from datetime import datetime, time

class TestAgenda(TestCase):
    def test_definir_horario_medico(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        self.assertEqual(agenda.horario_inicio, time(8, 0))
        self.assertEqual(agenda.horario_fim, time(12, 0))

    def test_agendamento_consulta(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_consulta = datetime(2026, 4, 24, 9, 0)

        paciente = "031.149.760-85"

        agenda.agendar_consulta(paciente, horario_consulta)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta], paciente)

    def test_agendamento_consulta_horario_indisponivel(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_consulta = datetime(2026, 4, 24, 7, 0)

        paciente = "031.149.760-85"

        agendamento = agenda.agendar_consulta(paciente, horario_consulta)

        self.assertEqual(agendamento, "O horário informado não é contemplado pelo médico")

        self.assertNotIn(horario_consulta, agenda.consultas_marcadas)

    def test_agendamento_consulta_horario_ja_agendado(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_consulta_1 = datetime(2026, 4, 24, 8, 0)
        paciente_1 = "031.149.760-85"
        agendamento_1 = agenda.agendar_consulta(paciente_1, horario_consulta_1)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta_1], paciente_1)

        horario_consulta_2 = datetime(2026, 4, 24, 8, 0)
        paciente_2 = "777.777.777-77"
        agendamento_2 = agenda.agendar_consulta(paciente_2, horario_consulta_2)

        self.assertEqual(agendamento_2, "O horário informado não já está ocupado por outro agendamento. Escolha outro horário")



