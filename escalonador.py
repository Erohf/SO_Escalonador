from objetos import *
from algoritmos import *
import sys
import copy

def main():

    def sistema():
        int_quantum = int(input("\nQual o quantum do sistema? "))
        int_sobrecarga = int(input("\nQual a sobrecarga do sistema? "))
        while True:
            int_speed = float(input("\nEscolha uma velocidade entre 0.1 - 10 (1 sendo o padrão) para o plot do gráfico: "))
            if 0.1 <= int_speed <= 10:
                break
            else:
                print("Valor inválido. Por favor, insira um número entre 0.1 e 10.")
        sistema = Sistema(int_quantum, int_sobrecarga, int_speed)

        int_processos = int(input("\nQual o número de processos? "))
        processos = []

        for i in range(int_processos):
            int_id = i + 1
            int_chegada = int(input(f"\nQual o tempo de chegada do processo {int_id}? "))
            int_execucao = int(input(f"\nQual o tempo de execução do processo {int_id}? "))
            int_deadline = int(input(f"\nQual o deadline do processo {int_id}? "))

            processo = Processo(int_id, int_chegada, int_execucao, int_deadline)
            processos.append(processo)
            print(f"\nProcesso {int_id} criado com sucesso!")

        while True:
            choice(processos, sistema)

    def choice(processos, sistema):
        print("\nEscolha o algoritmo de escalonamento:")
        print("1. FIFO")
        print("2. SJF")
        print("3. EDF")
        print("4. Round Robin")
        print("5. Trocar Valores")
        print("6. Sair")

        escolha = int(input("Digite sua escolha: "))
        print(f"\nVocê escolheu o algoritmo: {escolha}")
        menu(escolha, processos, sistema)

    def menu(escolha, processos, sistema):
        from algoritmos import FIFO, SJF, EDF, RoundRobin

        if escolha == 1:
            escalonador = FIFO(copy.deepcopy(processos), sistema.quantum, sistema.sobrecarga)
        elif escolha == 2:
            escalonador = SJF(copy.deepcopy(processos), sistema.quantum, sistema.sobrecarga)
        elif escolha == 3:
            escalonador = EDF(copy.deepcopy(processos), sistema.quantum, sistema.sobrecarga)
        elif escolha == 4:
            escalonador = RoundRobin(copy.deepcopy(processos), sistema.quantum, sistema.sobrecarga)
        elif escolha == 5:
            main()
            return
        elif escolha == 6:
            sys.exit()
        else:
            print("Escolha inválida. Tente novamente.")
            return

        escalonador.executar(sistema.speed)

    sistema()

if __name__ == '__main__':
    main()