class FIFO:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.chegada)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        tempo_atual = 0
        print("Executando escalonamento FIFO:")
        for processo in self.processos:
            if processo.chegada > tempo_atual:
                tempo_atual = processo.chegada
            processo.tempo = tempo_atual
            tempo_execucao = processo.execucao + self.sobrecarga
            print(f"Processo {processo.id} executado de {tempo_atual} até {tempo_atual + processo.execucao}")
            tempo_atual += tempo_execucao
            if self.sobrecarga > 0:
                print(f"Sobrecarga de {tempo_atual - self.sobrecarga} até {tempo_atual}")

class SJF:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: (p.chegada, p.execucao))
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        tempo_atual = 0
        print("Executando escalonamento SJF:")
        for processo in self.processos:
            if processo.chegada > tempo_atual:
                tempo_atual = processo.chegada
            processo.tempo = tempo_atual
            tempo_execucao = processo.execucao + self.sobrecarga
            print(f"Processo {processo.id} executado de {tempo_atual} até {tempo_atual + processo.execucao}")
            tempo_atual += tempo_execucao
            if self.sobrecarga > 0:
                print(f"Sobrecarga de {tempo_atual - self.sobrecarga} até {tempo_atual}")

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
                if self.sobrecarga > 0:
                    print(f"Sobrecarga de {tempo_atual - self.sobrecarga} até {tempo_atual}")
            else:
                processo.tempo = tempo_atual
                print(f"Processo {processo.id} executado de {tempo_atual} até {tempo_atual + processo.execucao}")
                tempo_atual += processo.execucao
                if self.sobrecarga > 0:
                    print(f"Sobrecarga de {tempo_atual - self.sobrecarga} até {tempo_atual}")

class EDF:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.deadline)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        print("Executando escalonamento EDF:")
        tempo_atual = 0
        for processo in self.processos:
            if processo.chegada > processo.deadline:
                print(f"Processo {processo.id} perdeu o deadline.")
            else:
                if processo.chegada > tempo_atual:
                    tempo_atual = processo.chegada
                processo.tempo = tempo_atual
                tempo_execucao = processo.execucao + self.sobrecarga
                print(f"Processo {processo.id} executado de {tempo_atual} até {tempo_atual + processo.execucao}")
                tempo_atual += tempo_execucao
                if self.sobrecarga > 0:
                    print(f"Sobrecarga de {tempo_atual - self.sobrecarga} até {tempo_atual}")
