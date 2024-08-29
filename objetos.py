class Sistema:
    def __init__(self, quantum, sobrecarga, speed=1):
        self.quantum = quantum
        self.sobrecarga = sobrecarga
        self.speed = speed

class Processo:
    def __init__(self, id, chegada, execucao, deadline, tempo=0, prioridade=None):
        self.id = id
        self.chegada = chegada
        self.execucao = execucao
        self.execucaoRestante = execucao
        self.deadline = deadline + chegada
        self.prioridade = prioridade
        self.tempo = tempo
        self.turnaround = 0

    def __str__(self):
        return (f"Processo ID: {self.id}, Chegada: {self.chegada}, Execução: {self.execucao}, Deadline: {self.deadline}, Turnaround: {self.turnaround}")

    def __eq__(self, other):
        return self.id == other.id