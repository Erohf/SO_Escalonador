import matplotlib.pyplot as plt
from objetos import *
from matplotlib.patches import Patch

class Grafico:
    def __init__(self, numProcessos, tipoEscalonamento, speed):
        self.numProcessos = numProcessos
        self.tipoEscalonamento = tipoEscalonamento
        self.speed = speed
        self._iniciaGrafico()
        plt.ion()

    def _iniciaGrafico(self):
        self.fig, self.gantt = plt.subplots()
        self.gantt.title.set_text(f'{self.tipoEscalonamento}')
        self.gantt.set_xlim(0, 50)
        self.gantt.set_ylim(0, (self.numProcessos * 10) + 10)
        self.gantt.set_xlabel("Tempo")
        self.gantt.set_ylabel("Processos")

        ticks = [i * 10 for i in range(1, self.numProcessos + 1)]
        tickLabels = [f'{i}' for i in range(1, self.numProcessos + 1)]
        self.gantt.set_yticks(ticks)
        self.gantt.set_yticklabels(tickLabels)
        self.gantt.grid(True)

    def addExecucao(self, tInicio, tExecucao, idProcesso, overDeadline=False):
        color = 'gray' if overDeadline else 'tab:green'
        self.gantt.broken_barh([(tInicio, tExecucao)], ((10 * idProcesso) - 5, 10), facecolors=color)

    def addSobrecarga(self, tInicio, tSobrecarga, idProcesso):
        self.gantt.broken_barh([(tInicio, tSobrecarga)], ((10 * idProcesso) - 5, 10), facecolors='tab:red')

    def addEspera(self, tInicio, tEspera, idProcesso):
        self.gantt.broken_barh([(tInicio, tEspera)], ((10 * idProcesso) - 5, 10), facecolors='yellow')

    def _refreshPlot(self):
        plt.draw()
        plt.pause(0.5/self.speed)

    def salvaGrafico(self, tempoFinal):
        self.gantt.set_xlim(0, tempoFinal)
        ticks = [x for x in range(1, tempoFinal + 1)]
        self.gantt.set_xticks(ticks)

        legend_patches = [
            Patch(facecolor='tab:green', label='Executando'),
            Patch(facecolor='yellow', label='Espera'),
            Patch(facecolor='tab:red', label='Sobrecarga'),
            Patch(facecolor='tab:grey', label='Estourou Deadline')
        ]
        self.gantt.legend(handles=legend_patches, loc='upper right')

        plt.ioff()
        plt.savefig(f"resultado{self.tipoEscalonamento}.png")
        plt.show()