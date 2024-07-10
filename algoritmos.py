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
            print(f"Tempo atual: {tempo_atual}")
            print(f"Processos na fila: {[p.id for p in queue]}")
            print(f"Processos prontos: {[p.id for p in processosProntos]}")
            
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
        
        processosProntos.sort(key=lambda p: p.execucao)

class RoundRobin:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.chegada)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        grafico = Grafico(len(self.processos), "RoundRobin")

        print(f"Executando escalonamento Round Robin com quantum = {self.quantum}:")
        tempo_atual = 0
        queue = self.processos[:]
        processosProntos = []
        quantumRestante = self.quantum
        inSobrecarga = False
        
        while queue:
            self.updatePronto(processosProntos, queue, tempo_atual)
            if len(processosProntos) == 0:
                tempo_atual += 1
            else:
                for processo in processosProntos:
                    if processo == processosProntos[0]:
                        if quantumRestante == 0:
                            inSobrecarga = True
                            grafico.addSobrecarga(tempo_atual, 1, processo.id)
                            quantumRestante = self.quantum
                        else:    
                            grafico.addExecucao(tempo_atual, 1, processo.id)
                            processo.execucaoRestante -= 1
                            quantumRestante -= 1
                    else:
                        grafico.addEspera(tempo_atual, 1, processo.id)

                tempo_atual += 1
        
                if processosProntos[0].execucaoRestante == 0:
                    processosProntos[0].tempo = tempo_atual
                    queue.remove(processosProntos[0])
                    processosProntos.pop(0)
                    quantumRestante = self.quantum
                elif inSobrecarga:
                    self.updatePronto(processosProntos, queue, tempo_atual)
                    temp = processosProntos.pop(0)
                    processosProntos.append(temp)
                    inSobrecarga = False

        grafico.salvaGrafico(tempo_atual)
    
    def updatePronto(self, processosProntos, queue, tempo_atual):
        for processo in queue:
            if (processo.chegada <= tempo_atual) and (processo not in processosProntos):
                processosProntos.append(processo)

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
                processo.tempo = tempo_atual + processo.execucaoRestante
                tempo_atual += processo.execucaoRestante
                print(f"Processo {processo.id} finalizado no tempo {processo.tempo}.")
