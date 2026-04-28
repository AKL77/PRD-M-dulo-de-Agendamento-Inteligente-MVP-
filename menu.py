from agenda import Agenda
from datetime import time, timedelta, datetime

def exibir_menu_inicial():
    print("\n" + "*"*20)
    print("Menu Inicial")
    print("1 - Consultar agenda do médico")
    print("2 - Realizar agendamento")
    print("0 - Sair do sistema")
    print("\n" + "*"*20)

def main():
    sistema_agenda = Agenda()

    while True:
        exibir_menu_inicial()
        opcao = input("Para escolher uma opção informe o número correspondente\n")

        if opcao == 1:
            break
        elif opcao == 2:
            print("Para realizar o agendamento informe as seguintes informações:")

            cpf_paciente = input("CPF do paciente")
            dia_agendamento = input("Dia do agendamento")
            mes_agendamento = input("Mês do agendamento")
            ano = input("Ano do agendamento")
            horario_agendamento = input("Hora desejada para o agendamento (ex: 9 para 09:00)")
            minutagem_agendamento = input("Informe a minutagem do agendamento (ex: ex: 30)")
            duracao_consulta = input("Duração da consulta")

        elif opcao == 0:
            break

if __name__ == "__main__":
    main()