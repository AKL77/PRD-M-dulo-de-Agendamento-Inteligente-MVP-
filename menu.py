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

        if opcao == "1":
            pass
        elif opcao == "2":
            print("Para realizar o agendamento informe as seguintes informações:")

            cpf_paciente = input("CPF do paciente\n")
            dia_agendamento = int(input("Dia do agendamento\n"))
            mes_agendamento = int(input("Mês do agendamento\n"))
            ano_agendamento = int(input("Ano do agendamento\n"))
            hora_agendamento = int(input("Hora desejada para o agendamento (ex: 9 para 09:00)\n"))
            minutagem_agendamento = int(input("Informe a minutagem do agendamento (ex: ex: 30)\n"))
            duracao_informada_agendamento = int(input("Duração da consulta\n"))

            horario_consulta = datetime(ano_agendamento, mes_agendamento, dia_agendamento, hora_agendamento, minutagem_agendamento)

            duracao_consulta = timedelta(minutes = duracao_informada_agendamento)

            resultado = sistema_agenda.agendar_consulta(cpf_paciente, horario_consulta, duracao_consulta)

            print(resultado)

        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente. \n")

if __name__ == "__main__":
    main()