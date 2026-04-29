C4Context
    title Diagrama de Contexto (Nível 1) - Sistema de Agendamento
    
    Person(usuario, "Recepcionista / Médico", "Interage com o terminal para gerenciar horários e pacientes.")
    System(sistema, "Agendamento Inteligente", "Permite configuração de expediente e marcação de consultas evitando conflitos de horários.")

    Rel(usuario, sistema, "Configura horários e agenda consultas usando")

C4Component
    title Diagrama de Componentes (Nível 3) - Aplicação Console
    
    Person(usuario, "Recepcionista / Médico", "Interage com o terminal.")
    
    Container_Boundary(app, "Aplicação Python") {
        Component(menu, "Menu CLI", "menu.py", "Exibe as opções, captura os inputs do teclado e formata os dados.")
        Component(agenda, "Motor de Agendamento", "agenda.py", "Contém as regras de negócio, validação de interseção e armazenamento em dicionários.")
    }

    Rel(usuario, menu, "Digita comandos no terminal")
    Rel(menu, agenda, "Chama métodos e passa parâmetros", "Python Import")