from unittest import TestCase
from agenda import Agenda
from datetime import datetime, time, timedelta

class TestAgenda(TestCase):
    def test_definir_horario_medico(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(dia_semana = 0, inicio = time(8, 0), fim = time(12, 0))
        agenda.configurar_expediente_medico(dia_semana = 1, inicio = time(12, 0), fim = time(16, 0))

        self.assertEqual(agenda.grade_horarios_de_atendimento[0]["inicio"], time(8, 0))
        self.assertEqual(agenda.grade_horarios_de_atendimento[0]["fim"], time(12, 0))
        
        self.assertEqual(agenda.grade_horarios_de_atendimento[1]["inicio"], time(12, 0))
        self.assertEqual(agenda.grade_horarios_de_atendimento[1]["fim"], time(16, 0))


    def test_agendamento_consulta(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(dia_semana = 4, inicio = time(8, 0), fim = time(12, 0))

        horario_consulta = datetime(2026, 4, 24, 9, 0)

        paciente = "031.149.760-85"

        duracao_consulta = timedelta(minutes=30)
        agenda.agendar_consulta(paciente, horario_consulta, duracao_consulta)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta]["paciente"], paciente)

    def test_agendamento_consulta_horario_indisponivel(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(dia_semana = 4, inicio = time(8, 0), fim = time(12, 0))

        horario_consulta = datetime(2026, 4, 24, 7, 0)

        paciente = "031.149.760-85"
        duracao_consulta = timedelta(minutes=30)
        agendamento = agenda.agendar_consulta(paciente, horario_consulta, duracao_consulta)

        self.assertEqual(agendamento, "O horário informado não é contemplado pelo médico")

        self.assertNotIn(horario_consulta, agenda.consultas_marcadas)

    def test_agendamento_consulta_horario_ja_agendado(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(dia_semana = 4, inicio = time(8, 0), fim = time(12, 0))

        horario_consulta_1 = datetime(2026, 4, 24, 8, 0)
        paciente_1 = "031.149.760-85"
        duracao_consulta_1 = timedelta(minutes=30)
        agenda.agendar_consulta(paciente_1, horario_consulta_1, duracao_consulta_1)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta_1]["paciente"], paciente_1)

        horario_consulta_2 = datetime(2026, 4, 24, 8, 0)
        paciente_2 = "777.777.777-77"
        duracao_consulta_2 = timedelta(minutes=20)
        agendamento_2 = agenda.agendar_consulta(paciente_2, horario_consulta_2, duracao_consulta_2)

        self.assertEqual(agendamento_2, "O horário informado já está ocupado por outro agendamento. Escolha outro horário")

    def test_agendamento_consultas_com_intesercao(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(dia_semana = 4, inicio = time(8, 0), fim = time(12, 0))

        horario_consulta_1 = datetime(2026, 4, 24, 8, 0)
        paciente_1 = "031.149.760-85"
        duracao_consulta_1 = timedelta(minutes=30)
        agenda.agendar_consulta(paciente_1, horario_consulta_1, duracao_consulta_1)

        self.assertEqual(agenda.consultas_marcadas[horario_consulta_1]["paciente"], paciente_1)

        horario_consulta_2 = datetime(2026, 4, 24, 8, 15)
        paciente_2 = "777.777.777-77"
        duracao_consulta_2 = timedelta(minutes=20)
        agendamento_2 = agenda.agendar_consulta(paciente_2, horario_consulta_2, duracao_consulta_2)

        self.assertEqual(agendamento_2, "O horário informado já está ocupado por outro agendamento. Escolha outro horário")
        self.assertNotIn(horario_consulta_2, agenda.consultas_marcadas)

    def test_listar_consultas_agendadas_cronologicamente(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(dia_semana = 2, inicio = time(8, 0), fim = time(12, 0))

        horario_consulta_2 = datetime(2026, 4, 29, 10, 0)
        paciente_2 = "676.767.676-76"
        duracao_consulta_2 = timedelta(minutes=30)

        agenda.agendar_consulta(paciente_2, horario_consulta_2, duracao_consulta_2)

        horario_consulta_1 = datetime(2026, 4, 29, 8, 0)
        paciente_1 = "031.149.760-85"
        duracao_consulta_1 = timedelta(minutes=45)

        agenda.agendar_consulta(paciente_1, horario_consulta_1, duracao_consulta_1)

        resultado = agenda.listar_consultas()

        resultado_esperado = (
            "[29/04/2026] 08:00 às 08:45 | Paciente (CPF): 031.149.760-85\n"
            "[29/04/2026] 10:00 às 10:30 | Paciente (CPF): 676.767.676-76"
        )

        self.assertEqual(resultado, resultado_esperado)

    def test_listar_consultas_dia_especifico(self):
        agenda = Agenda()

        agenda.configurar_expediente_medico(dia_semana=2, inicio=time(8, 0), fim=time(12, 0))
        agenda.configurar_expediente_medico(dia_semana=3, inicio=time(8, 0), fim=time(12, 0))

        horario_consulta_3 = datetime(2026, 4, 29, 10, 0)
        paciente_3 = "676.767.676-76"
        duracao_consulta_3 = timedelta(minutes=30)

        agenda.agendar_consulta(paciente_3, horario_consulta_3, duracao_consulta_3)

        horario_consulta_2 = datetime(2026, 4, 30, 10, 0)
        paciente_2 = "676.767.676-76"
        duracao_consulta_2 = timedelta(minutes=30)

        agenda.agendar_consulta(paciente_2, horario_consulta_2, duracao_consulta_2)

        horario_consulta_1 = datetime(2026, 4, 29, 8, 0)
        paciente_1 = "031.149.760-85"
        duracao_consulta_1 = timedelta(minutes=45)

        agenda.agendar_consulta(paciente_1, horario_consulta_1, duracao_consulta_1)

        data_busca = datetime(2026, 4, 29).date()

        resultado = agenda.listar_consultas_por_dia(data_busca)

        resultado_esperado = (
            "[29/04/2026] 08:00 às 09:00 | Paciente (CPF): 333.333.333-33\n"
            "[29/04/2026] 10:00 às 10:30 | Paciente (CPF): 111.111.111-11"
        )

        self.assertEqual(resultado, resultado_esperado)


