from agenda import Agenda
from datetime import time, timedelta, datetime

from enums import DiasDaSemana

def exibir_menu_inicial():
    print("\n" + "*"*20)
    print("Menu Inicial")
    print("1 - Consultar agenda do médico")
    print("2 - Realizar agendamento")
    print("3 - Editar horário de atendimento do médico")
    print("0 - Sair do sistema")
    print("\n" + "*"*20)

def main():
    sistema_agenda = Agenda()

    while True:
        exibir_menu_inicial()
        opcao = input("Para escolher uma opção informe o número correspondente\n")

        if opcao == "1":
            print("Quer verificar as consultas de um dia específico ou consultar todos os agendamentos?")
            print("1 - Verificar consultas marcadas para um dia específico")
            print("2 - Verificar todas as consultas marcadas")
            escolha = input()

            if escolha == "1":
                print("Serão necessárias as seguintes informações para verificar as consultas agendadas em um dia específico:")
                try:
                    data_informada = input("Informe a data desejada para o agendamento. Siga o seguinte formato dd/mm/aaaa")
                    dia_string, mes_string, ano_string = data_informada.split("/")
                    dia_consulta = int(dia_string)
                    mes_consulta = int(mes_string)
                    ano_consulta = int(ano_string)

                    data_buscada = datetime(ano_consulta, mes_consulta, dia_consulta).date()
                    
                    resultado_busca = sistema_agenda.listar_consultas_por_dia(data_buscada)
                    
                    print("\n" + "*"*30)
                    print(resultado_busca)
                    print("*"*30 + "\n")
                    
                except ValueError:
                    print("\nFormato inválido. Tente novamente!")

            elif escolha == "2":
                print("\n" + "*"*20)
                print("CONSULTAS AGENDADAS")
                print(sistema_agenda.listar_consultas())
        elif opcao == "2":
            print("Para realizar o agendamento informe as seguintes informações:")

            cpf_paciente = input("CPF do paciente\n")

            try:
                data_informada = input("Informe a data desejada para o agendamento. Siga o seguinte formato dd/mm/aaaa\n")
                dia_string, mes_string, ano_string = data_informada.split("/")
                dia_agendamento = int(dia_string)
                mes_agendamento = int(mes_string)
                ano_agendamento = int(ano_string)

                hora_informada = input("Informe o horário desejado. Siga o seguinte formato hh:mm\n")
                hora_string, minuto_string = hora_informada.split(":")
                hora_agendamento = int(hora_string)
                minutagem_agendamento = int(minuto_string)

                duracao_informada_agendamento = int(input("Informe a Duração da consulta (em minutos)\n"))

                horario_consulta = datetime(ano_agendamento, mes_agendamento, dia_agendamento, hora_agendamento, minutagem_agendamento)
                duracao_consulta = timedelta(minutes = duracao_informada_agendamento)
                resultado = sistema_agenda.agendar_consulta(cpf_paciente, horario_consulta, duracao_consulta)

                print(resultado)
            except ValueError:
                print("\nFormato inválido! Tente novamente.")
        elif opcao == "3":
            print("Para editar o expediente do médico é necessário informar as seguintes informações")

            print("Qual dia da semana deseja editar:")
            print("0 -> Segunda-feira")
            print("1 -> Terça-feira")
            print("2 -> Quarta-feira")
            print("3 -> Quinta-feira")
            print("4 -> Sexta-feira")
            print("5 -> Sábado")
            print("6 -> Domingo")
            dia_semana = int(input())

            valores_validos = [dia.value for dia in DiasDaSemana]

            if dia_semana not in valores_validos:
                print("\nDia da semana inválido.")
                continue

            hora_informada = input("Informe o horário de incício do expediente. Siga o seguinte formato hh:mm \n")
            hora_string, minuto_string = hora_informada.split(":")
            hora_inicio_expediente = int(hora_string)
            minutagem_inicio_expediente = int(minuto_string)
            print(f"Horário de início informado: {hora_inicio_expediente:02d}:{minutagem_inicio_expediente:02d}")


            hora_informada = input("Informe o horário de fim do expediente. Siga o seguinte formato hh:mm \n")
            hora_string, minuto_string = hora_informada.split(":")
            hora_fim_expediente = int(hora_string)
            minutagem_fim_expediente = int(minuto_string)
            print(f"Horário de fim informado: {hora_fim_expediente:02d}:{minutagem_fim_expediente:02d}")

            inicio = time(hora_inicio_expediente, minutagem_inicio_expediente)
            fim = time(hora_fim_expediente, minutagem_fim_expediente)
            sistema_agenda.configurar_expediente_medico(dia_semana, inicio, fim)

            try:
                if inicio >= fim:
                    print("\nErro: O horário de fim deve ser posterior ao horário de início.")
                else:
                    sistema_agenda.configurar_expediente_medico(dia_semana, inicio, fim)
                    print(f"\nExpediente configurado com sucesso: {inicio.strftime('%H:%M')} às {fim.strftime('%H:%M')}")

            except ValueError:
                print("\nFormato de hora inválido.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente. \n")

if __name__ == "__main__":
    main()