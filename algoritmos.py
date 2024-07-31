from plot import *

class FIFO:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.chegada)
        self.quantum = quantum
        self.sobrecarga = sobrecarga
        self.listaProcessos = self.processos[:]

    def executar(self):
        grafico = Grafico(len(self.processos), "FIFO")

        queue = self.processos[:]
        tempo_atual = 0
        turnaround = 0
        turnaroundMedio = 0
        
        print("\nExecutando escalonamento FIFO:")
        
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
                turnaround = queue[0].tempo - queue[0].chegada
                queue[0].turnaround = turnaround
                turnaroundMedio += turnaround
                print (queue[0])
                queue.pop(0) 

        print(f"\nTurnaround médio: {turnaroundMedio/len(self.processos)}")

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
        turnaround = 0
        turnaroundMedio = 0

        print("Executando escalonamento SJF:")
        self.updatePronto(processosProntos, queue, tempo_atual)
        while queue:
            self.updatePronto(processosProntos, queue, tempo_atual)
            if len(processosProntos) == 0:
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
                    turnaround = processosProntos[0].tempo - processosProntos[0].chegada
                    processosProntos[0].turnaround = turnaround
                    turnaroundMedio += turnaround
                    print(processosProntos[0])
                    queue.remove(processosProntos[0])
                    processosProntos.pop(0)
                    processosProntos.sort(key = lambda p: p.execucao)
        
        print(f"\nTurnaround médio: {turnaroundMedio/len(self.processos)}")

        grafico.salvaGrafico(tempo_atual)
    
    def updatePronto(self, processosProntos, queue, tempo_atual):
        for processo in queue:
            if (processo.chegada <= tempo_atual) and (processo not in processosProntos):
                processosProntos.append(processo)

class RoundRobin:
    def __init__(self, processos, quantum, sobrecarga):
        self.processos = sorted(processos, key=lambda p: p.chegada)
        self.quantum = quantum
        self.sobrecarga = sobrecarga

    def executar(self):
        grafico = Grafico(len(self.processos), "RoundRobin")

        print(f"\nExecutando escalonamento Round Robin com quantum = {self.quantum}:")
        tempo_atual = 0
        turnaround = 0
        turnaroundMedio = 0
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
                    turnaround = processosProntos[0].tempo - processosProntos[0].chegada
                    processosProntos[0].turnaround = turnaround
                    turnaroundMedio += turnaround
                    print(processosProntos[0])
                    queue.remove(processosProntos[0])
                    processosProntos.pop(0)
                    quantumRestante = self.quantum
                elif inSobrecarga:
                    self.updatePronto(processosProntos, queue, tempo_atual)
                    temp = processosProntos.pop(0)
                    processosProntos.append(temp)
                    inSobrecarga = False

        print(f"\nTurnaround médio: {turnaroundMedio/len(self.processos)}")

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
        grafico = Grafico(len(self.processos), "EDF")

        print(f"Executando escalonamento EDF com quantum = {self.quantum}:")
        tempo_atual = 0
        turnaround = 0
        turnaroundMedio = 0
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
                            grafico.addExecucao(tempo_atual, 1, processo.id, (processo.deadline <= tempo_atual))
                            processo.execucaoRestante -= 1
                            quantumRestante -= 1
                    else:
                        grafico.addEspera(tempo_atual, 1, processo.id)

                tempo_atual += 1
        
                if processosProntos[0].execucaoRestante == 0:
                    processosProntos[0].tempo = tempo_atual
                    turnaround = processosProntos[0].tempo - processosProntos[0].chegada
                    processosProntos[0].turnaround = turnaround
                    turnaroundMedio += turnaround
                    print(processosProntos[0])
                    queue.remove(processosProntos[0])
                    processosProntos.pop(0)
                    quantumRestante = self.quantum
                    processosProntos.sort(key = lambda p: p.deadline)
                elif inSobrecarga:
                    self.updatePronto(processosProntos, queue, tempo_atual)
                    temp = processosProntos.pop(0)
                    processosProntos.append(temp)
                    inSobrecarga = False
                    processosProntos.sort(key = lambda p: p.deadline)

        print(f"\nTurnaround médio: {turnaroundMedio/len(self.processos)}")

        grafico.salvaGrafico(tempo_atual)

    def updatePronto(self, processosProntos, queue, tempo_atual):
        for processo in queue:
            if (processo.chegada <= tempo_atual) and (processo not in processosProntos):
                processosProntos.append(processo)
