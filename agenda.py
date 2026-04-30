from datetime import datetime, time, timedelta

class Agenda:
    def __init__(self):
        self.consultas_marcadas = {}
        self.grade_horarios_de_atendimento = {}

    def configurar_expediente_medico(self, dia_semana, inicio, fim):
        self.grade_horarios_de_atendimento[dia_semana] = {
            "inicio": inicio,
            "fim": fim
        }

    # função feita integralmente com ia - apesar de entendê-la 
    def listar_consultas(self):
        if not self.consultas_marcadas:
            return "Nenhuma consulta está agendada"
        
        listagem = []

        for horario in sorted(self.consultas_marcadas.keys()):
            paciente = self.consultas_marcadas[horario]["paciente"]
            duracao = self.consultas_marcadas[horario]["duracao"]
            horario_fim = horario + duracao

            data_formatada = horario.strftime("%d/%m/%Y")
            hora_inicio = horario.strftime("%H:%M")
            hora_fim = horario_fim.strftime("%H:%M")

            listagem.append(f"[{data_formatada}] {hora_inicio} às {hora_fim} | Paciente (CPF): {paciente}")

        return "\n".join(listagem)
    
    def listar_consultas_por_dia(self, data):
        if not self.consultas_marcadas:
            return "Nenhuma consulta está agendada"
        
        listagem = []

        for horario in self.consultas_marcadas.keys():
            if horario.date() == data:
                paciente = self.consultas_marcadas[horario]["paciente"]
                duracao = self.consultas_marcadas[horario]["duracao"]
                horario_fim = horario + duracao

                data_formatada = horario.strftime("%d/%m/%Y")
                hora_inicio = horario.strftime("%H:%M")
                hora_fim = horario_fim.strftime("%H:%M")

                listagem.append(f"[{data_formatada}] {hora_inicio} às {hora_fim} | Paciente (CPF): {paciente}")
        
        if not self.consultas_marcadas:
            return "Nenhuma consulta está agendada no dia informado"

        return "\n".join(listagem)

    def agendar_consulta(self, paciente, horario_consulta, duracao_consulta_em_potencial):
        dia_da_semana_consulta_em_potencial = horario_consulta.weekday()
        horas = horario_consulta.time()

        if dia_da_semana_consulta_em_potencial not in self.grade_horarios_de_atendimento:
            return "O médico não antende no dia informado. Por favor, escolha outro dia."
        
        incio_expediente = self.grade_horarios_de_atendimento[dia_da_semana_consulta_em_potencial]["inicio"]
        fim_expediente = self.grade_horarios_de_atendimento[dia_da_semana_consulta_em_potencial]["fim"]

        inicio_agendamento_em_potencial = horario_consulta
        fim_agendamento_em_potencial = inicio_agendamento_em_potencial + duracao_consulta_em_potencial

        horas_fim_consulta = fim_agendamento_em_potencial.time()

        if horas < incio_expediente or horas_fim_consulta > fim_expediente:
            return "O horário informado não é contemplado pelo médico"


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

        return "Agendamento realizado com sucesso!"