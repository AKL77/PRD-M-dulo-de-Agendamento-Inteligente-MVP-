from datetime import datetime, time, timedelta

class Agenda:
    def __init__(self):
        self.consultas_marcadas = {}
        self.horario_inicio_expediente = None
        self.horario_fim_expediente = None

    def configurar_expediente_medico(self, inicio, fim):
        self.horario_inicio_expediente = inicio
        self.horario_fim_expediente = fim

    def agendar_consulta(self, paciente, horario_consulta, duracao_consulta_em_potencial):
        horas = horario_consulta.time()

        if not (self.horario_inicio_expediente <= horas <= self.horario_fim_expediente):
            return "O horário informado não é contemplado pelo médico"

        inicio_agendamento_em_potencial = horario_consulta
        fim_agendamento_em_potencial = inicio_agendamento_em_potencial + duracao_consulta_em_potencial

        for horario_existente in self.consultas_marcadas:
            inicio_de_agendamento_existente = horario_existente
            duracao_da_consulta_existente = self.consultas_marcadas[horario_existente]["duracao"]
            fim_de_agendamento_existente = inicio_de_agendamento_existente + duracao_da_consulta_existente

            if inicio_agendamento_em_potencial < fim_de_agendamento_existente and inicio_de_agendamento_existente < fim_agendamento_em_potencial:
                return "O horário informado já está ocupado por outro agendamento. Escolha outro horário"

        self.consultas_marcadas[horario_consulta] = {
            "paciente": paciente,
            "duracao": duracao_consulta_em_potencial
        }