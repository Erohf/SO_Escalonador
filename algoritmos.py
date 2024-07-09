from plot import *

class FIFO:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.chegada)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        grafico = Grafico(len(self.processos), "FIFO")

        queue = self.processos[:]
        tempo_atual = 0
        print("Executando escalonamento FIFO:")
        
        while queue:
            for processo in queue:
                if processo == queue[0]:
                    if processo.chegada <= tempo_atual:
                        grafico.addExecucao(tempo_atual, 1, processo.id)
                        processo.execucaoRestante -= 1
                else:
                    if processo.chegada <= tempo_atual:
                        grafico.addEspera(tempo_atual, 1, processo.id)

            tempo_atual += 1

            if queue[0].execucaoRestante == 0:
                queue[0].tempo = tempo_atual
                queue.pop(0)
        
        grafico.salvaGrafico(tempo_atual)

class SJF:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: (p.chegada, p.execucao))
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        grafico = Grafico(len(self.processos), "SJF")

        queue = self.processos[:]
        processosProntos = []
        tempo_atual = 0
        print("Executando escalonamento SJF:")

        self.updatePronto(processosProntos, queue, tempo_atual)
        while queue:
            if len(processosProntos) == 0:
                self.updatePronto(processosProntos, queue, tempo_atual)
                tempo_atual += 1
            else:
                for processo in queue:
                    if processo == processosProntos[0]:
                        if processo.chegada <= tempo_atual:
                            grafico.addExecucao(tempo_atual, 1, processo.id)
                            processo.execucaoRestante -= 1
                    else:
                        if processo.chegada <= tempo_atual:
                            grafico.addEspera(tempo_atual, 1, processo.id)

                tempo_atual += 1
        
                if processosProntos[0].execucaoRestante == 0:
                    processosProntos[0].tempo = tempo_atual
                    queue.remove(processosProntos[0])
                    processosProntos.pop(0)
                    self.updatePronto(processosProntos, queue, tempo_atual)
            
        grafico.salvaGrafico(tempo_atual)
    
    def updatePronto(self, processosProntos, queue, tempo_atual):
        for processo in queue:
            if (processo.chegada <= tempo_atual) and (processo not in processosProntos):
                processosProntos.append(processo)
        
        processosProntos.sort(key = lambda p: p.execucao)

        

            
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
