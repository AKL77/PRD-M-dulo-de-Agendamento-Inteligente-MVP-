from datetime import datetime, time, timedelta

class Agenda:
    def __init__(self):
        self.consultas_marcadas = {}
        # self.horario_inicio_expediente = None
        # self.horario_fim_expediente = None
        self.grade_horarios_de_atendimento = {}

    def configurar_expediente_medico(self, dia_semana, inicio, fim):
        # self.horario_inicio_expediente = inicio
        # self.horario_fim_expediente = fim
        self.grade_horarios_de_atendimento[dia_semana] = {
            "inicio": inicio,
            "fim": fim
        }

    def agendar_consulta(self, paciente, horario_consulta, duracao_consulta_em_potencial):
        dia_da_semana_consulta_em_potencial = horario_consulta.weekday()
        horas = horario_consulta.time()

        if dia_da_semana_consulta_em_potencial not in self.grade_horarios_de_atendimento:
            return "O médico não antende no dia informado. Por favor, escolha outro dia."
        
        incio_expediente = self.grade_horarios_de_atendimento[dia_da_semana_consulta_em_potencial]["inicio"]
        fim_expediente = self.grade_horarios_de_atendimento[dia_da_semana_consulta_em_potencial]["fim"]

        if not (incio_expediente <= horas <= fim_expediente):
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