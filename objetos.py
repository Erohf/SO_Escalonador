class Sistema:
    def __init__(self, quantum, sobrecarga):
        self.quantum = quantum
        self.sobrecarga = sobrecarga

class Processo:
    def __init__(self, id, chegada, execucao, deadline, tempo=None, prioridade=None):
        self.id = id
        self.chegada = chegada
        self.execucao = execucao
        self.execucaoRestante = execucao
        self.deadline = deadline
        self.prioridade = prioridade
        self.tempo = tempo

    def __str__(self):
        return (f"Processo ID: {self.id}, Chegada: {self.chegada}, Execução: {self.execucao}, Deadline: {self.deadline}, Tempo: {self.tempo}")

    def __eq__(self, other):
        return self.id == other.id


class Escolha:
    def __init__(self):
        print("\nMenu de ações:")
        print("1 - FIFO")
        print("2 - SJF")
        print("3 - EDF")
        print("4 - Round Robin")
        print("5 - Trocar valores")
        print("6 - Sair do programa")
        self.opcao = int(input("\nEscolha uma opção: "))
        while self.opcao not in [1, 2, 3, 4, 5, 6]:
            print("\nOpção inválida. Tente novamente.")
            self.opcao = int(input("Escolha uma opção (1-6): "))