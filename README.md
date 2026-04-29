C4Context
    title Diagrama de Contexto (Nível 1) - Sistema de Agendamento
    
    Person(usuario, "Recepcionista / Médico", "Interage com o terminal para gerenciar horários e pacientes.")
    System(sistema, "Agendamento Inteligente", "Permite configuração de expediente e marcação de consultas evitando conflitos de horários.")

    Rel(usuario, sistema, "Configura horários e agenda consultas usando")