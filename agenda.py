from datetime import datetime

class Agenda:
    def __init__(self):
        self.consultas_marcadas = {}
        self.horario_inicio = None
        self.horario_fim = None

    def configurar_expediente_medico(self, inicio, fim):
        self.horario_inicio = inicio
        self.horario_fim = fim

    def agendar_consulta(self, paciente, horario_consulta):
        self.consultas_marcadas[horario_consulta] = paciente