from unittest import TestCase
from agenda import Agenda
from datetime import datetime, time, timedelta

class TestAgenda(TestCase):
    def test_definir_horario_medico(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        self.assertEqual(agenda.horario_inicio_expediente, time(8, 0))
        self.assertEqual(agenda.horario_fim_expediente, time(12, 0))

    def test_agendamento_consulta(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_consulta = datetime(2026, 4, 24, 9, 0)

        paciente = "031.149.760-85"

        duracao_consulta = timedelta(minutes=30)
        agenda.agendar_consulta(paciente, horario_consulta, duracao_consulta)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta]["paciente"], paciente)

    def test_agendamento_consulta_horario_indisponivel(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_consulta = datetime(2026, 4, 24, 7, 0)

        paciente = "031.149.760-85"
        duracao_consulta = timedelta(minutes=30)
        agendamento = agenda.agendar_consulta(paciente, horario_consulta, duracao_consulta)

        self.assertEqual(agendamento, "O horário informado não é contemplado pelo médico")

        self.assertNotIn(horario_consulta, agenda.consultas_marcadas)

    def test_agendamento_consulta_horario_ja_agendado(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_consulta_1 = datetime(2026, 4, 24, 8, 0)
        paciente_1 = "031.149.760-85"
        duracao_consulta_1 = timedelta(minutes=30)
        agendamento_1 = agenda.agendar_consulta(paciente_1, horario_consulta_1, duracao_consulta_1)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta_1]["paciente"], paciente_1)

        horario_consulta_2 = datetime(2026, 4, 24, 8, 0)
        paciente_2 = "777.777.777-77"
        duracao_consulta_2 = timedelta(minutes=20)
        agendamento_2 = agenda.agendar_consulta(paciente_2, horario_consulta_2, duracao_consulta_2)

        self.assertEqual(agendamento_2, "O horário informado já está ocupado por outro agendamento. Escolha outro horário")

    def test_agendamento_consultas_com_intesercao(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_consulta_1 = datetime(2026, 4, 24, 8, 0)
        paciente_1 = "031.149.760-85"
        duracao_consulta_1 = timedelta(minutes=30)
        agendamento_1 = agenda.agendar_consulta(paciente_1, horario_consulta_1, duracao_consulta_1)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta_1]["paciente"], paciente_1)

        horario_consulta_2 = datetime(2026, 4, 24, 8, 15)
        paciente_2 = "777.777.777-77"
        duracao_consulta_2 = timedelta(minutes=20)
        agendamento_2 = agenda.agendar_consulta(paciente_2, horario_consulta_2, duracao_consulta_2)

        self.assertEqual(agendamento_2, "O horário informado já está ocupado por outro agendamento. Escolha outro horário")
        self.assertNotIn(horario_consulta_2, agenda.consultas_marcadas)

    def test_agendamento_consulta_duracao_diferente(self):
        agenda = Agenda()
        agenda.configurar_expediente_medico(inicio = time(8, 0), fim = time(12, 0))

        horario_1 = datetime(2026, 4, 24, 8, 0)
        paciente_1 = "676.767.676-67"
        duracao_1 = timedelta(minutes=60)
        agenda.agendar_consulta(paciente_1, horario_1, duracao_1)

        horario_2 = datetime(2026, 4, 24, 8, 30)
        paciente_2 = "000.000.000-00"
        duracao_2 = timedelta(minutes=30)
        resultado_falha = agenda.agendar_consulta(paciente_2, horario_2, duracao_2)

        self.assertEqual(resultado_falha, "O horário informado já está ocupado por outro agendamento. Escolha outro horário")
        self.assertNotIn(horario_2, agenda.consultas_marcadas)


