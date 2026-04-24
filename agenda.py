from datetime import datetime, time

class Agenda:
    def __init__(self):
        self.consultas_marcadas = {}
        self.horario_inicio = None
        self.horario_fim = None

    def configurar_expediente_medico(self, inicio, fim):
        self.horario_inicio = inicio
        self.horario_fim = fim

    def agendar_consulta(self, paciente, horario_consulta):
        horas = horario_consulta.time()

        if(self.horario_inicio <= horas <= self.horario_fim):
            self.consultas_marcadas[horario_consulta] = paciente
        else:
            return "O horário informado não é contemplado pelo médico"