from objetos import *
from algoritmos import *

def main():
    int_quantum = int(input("\nQual o quantum do sistema? "))

    int_sobrecarga = int(input("\nQual a sobrecarga do sistema? "))

    sistema = Sistema(int_quantum, int_sobrecarga)

    int_processos = int(input("\nQual o número de processos? "))

    processos = []

    for i in range(int_processos):
        int_id = i+1

        int_chegada = int(input(f"\nQual o tempo de chegada do processo {int_id}? "))

        int_execucao = int(input(f"\nQual o tempo de execução do processo {int_id}? "))

        int_deadline = int(input(f"\nQual o deadline do processo {int_id}? "))

        # print(f"Qual a prioridade do processo {i}?")
        # int_prioridade = int(input())

        processo = Processo(int_id, int_chegada, int_execucao, int_deadline)
        processos.append(processo)

        print(f"\nProcesso {int_id} criado com sucesso!")

    escolha = Escolha()
    print(f"\nVocê escolheu o algoritmo: {escolha.opcao}")

    if escolha.opcao == 1:
        escalonador = FIFO(processos, sistema.quantum, sistema.sobrecarga)
    elif escolha.opcao == 2:
        escalonador = SJF(processos, sistema.quantum, sistema.sobrecarga)
    elif escolha.opcao == 3:
        escalonador = EDF(processos, sistema.quantum, sistema.sobrecarga)
    elif escolha.opcao == 4:
        escalonador = RoundRobin(processos, sistema.quantum, sistema.sobrecarga)
    
    escalonador.executar()

    print("\nLista de Processos Armazenados:")
    for processo in processos:
        print(processo)

if __name__ == '__main__':
    main()
