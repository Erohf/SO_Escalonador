class FIFO:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.chegada)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        tempo_atual = 0
        print("Executando escalonamento FIFO:")
        for processo in self.processos:
            processo.tempo = tempo_atual
            tempo_atual += processo.execucao
            print(f"Processo {processo.id} executado de {processo.tempo} até {tempo_atual}")

class SJF:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: (p.chegada, p.execucao))
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        tempo_atual = 0
        print("Executando escalonamento SJF:")
        for processo in self.processos:
            processo.tempo = tempo_atual
            tempo_atual += processo.execucao
            print(f"Processo {processo.id} executado de {processo.tempo} até {tempo_atual}")

class RoundRobin:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.chegada)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        print(f"Executando escalonamento Round Robin com quantum de {self.quantum}:")
        tempo_atual = 0
        queue = self.processos[:]
        
        while queue:
            processo = queue.pop(0)
            if processo.chegada > tempo_atual:
                tempo_atual = processo.chegada
            if processo.execucao > self.quantum:
                processo.tempo = tempo_atual
                print(f"Processo {processo.id} executado de {tempo_atual} até {tempo_atual + self.quantum}")
                tempo_atual += self.quantum
                processo.execucao -= self.quantum
                queue.append(processo)
            else:
                processo.tempo = tempo_atual
                print(f"Processo {processo.id} executado de {tempo_atual} até {tempo_atual + processo.execucao}")
                tempo_atual += processo.execucao

class EDF:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.deadline)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        print("Executando escalonamento EDF:")
        for processo in self.processos:
            processo.tempo = processo.chegada
            print(f"Processo {processo.id} executado de {processo.tempo} até {processo.tempo + processo.execucao}")
