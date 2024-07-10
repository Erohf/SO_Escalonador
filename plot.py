import matplotlib.pyplot as plt
from matplotlib.patches import Patch

class Grafico:
    def __init__(self, numProcessos, tipoEscalonamento):
        self.numProcessos = numProcessos
        self.tipoEscalonamento = tipoEscalonamento
        self._iniciaGrafico()

    def _iniciaGrafico(self):
        self.fig, self.gantt = plt.subplots()

        self.gantt.title.set_text(f'{self.tipoEscalonamento}')

        self.gantt.set_xlim(0, 50)
        self.gantt.set_ylim(0, (self.numProcessos * 10) + 10)

        self.gantt.set_xlabel("Tempo")
        self.gantt.set_ylabel("Processos")

        ticks = []
        tickLabels = []
        for i in range(1, self.numProcessos + 1):
            ticks.append(i*10)
            tickLabels.append(f'{i}')
        
        self.gantt.set_yticks(ticks)
        self.gantt.set_yticklabels(tickLabels)

        self.gantt.grid(True)
    
    def addExecucao(self, tInicio, tExecucao, idProcesso):
        self.gantt.broken_barh([(tInicio, tExecucao)], ((10*idProcesso)-5, 10), facecolors =('tab:green'))

    def addSobrecarga(self, tInicio, tSobrecarga, idProcesso):
        self.gantt.broken_barh([(tInicio, tSobrecarga)], ((10*idProcesso)-5, 10), facecolors =('tab:red'))
    
    def addEspera(self, tInicio, tEspera, idProcesso):
        self.gantt.broken_barh([(tInicio, tEspera)], ((10*idProcesso)-5, 10), facecolors ='yellow')
    
    def salvaGrafico(self, tempoFinal):
        self.gantt.set_xlim(0, tempoFinal)

        legend_patches = [
            Patch(facecolor='tab:green', label='Verde (Executando)'),
            Patch(facecolor='yellow', label='Amarelo (Espera)'),
            Patch(facecolor='tab:red', label='Red (Sobrecarga)')
        ]
        self.gantt.legend(handles=legend_patches, loc='upper right')

        plt.savefig(f"resultado{self.tipoEscalonamento}.png")
        plt.show()