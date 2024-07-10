from objetos import *
from algoritmos import *
import sys
import copy

def main():

    def sistema():
        int_quantum = int(input("\nQual o quantum do sistema? "))
        int_sobrecarga = int(input("\nQual a sobrecarga do sistema? "))
        sistema = Sistema(int_quantum, int_sobrecarga)

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
            choice(processos, sistema.quantum, sistema.sobrecarga)

    def choice(processos, quantum, sobrecarga):
        print("\nEscolha o algoritmo de escalonamento:")
        print("1. FIFO")
        print("2. SJF")
        print("3. EDF")
        print("4. Round Robin")
        print("5. Reiniciar")
        print("6. Sair")

        escolha = int(input("Digite sua escolha: "))
        print(f"\nVocê escolheu o algoritmo: {escolha}")
        menu(escolha, processos, quantum, sobrecarga)

    def menu(escolha, processos, quantum, sobrecarga):
        from algoritmos import FIFO, SJF, EDF, RoundRobin

        if escolha == 1:
            escalonador = FIFO(copy.deepcopy(processos), quantum, sobrecarga)
        elif escolha == 2:
            escalonador = SJF(copy.deepcopy(processos), quantum, sobrecarga)
        elif escolha == 3:
            escalonador = EDF(copy.deepcopy(processos), quantum, sobrecarga)
        elif escolha == 4:
            escalonador = RoundRobin(copy.deepcopy(processos), quantum, sobrecarga)
        elif escolha == 5:
            main()
            return
        elif escolha == 6:
            sys.exit()
        else:
            print("Escolha inválida. Tente novamente.")
            return

        escalonador.executar()

        print("\nLista de Processos Armazenados:")
        for processo in processos:
            print(processo)

    sistema()

if __name__ == '__main__':
    main()
