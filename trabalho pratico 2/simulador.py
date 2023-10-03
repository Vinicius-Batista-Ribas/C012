class Processo:
    def __init__(self, nome, tempoExecucao, prioridade):
        self.nome = nome
        self.tempoExecucao = tempoExecucao
        self.prioridade = prioridade
        self.tempoEspera = 0

# FIRST COME FIRST SERVED
def fcfs(lista):
    return lista.pop(0)

# SHORTEST JOB FIRST
def sjf(lista):
    lista.sort(key=lambda x: x.tempoExecucao)
    return lista.pop(0)

# PRIORITY SCHEDULING
def ps(lista):
    lista.sort(key=lambda x: x.prioridade)
    return lista.pop(0)

# ROUND ROBIN SCHEDULING
def rr(lista, quantum):
    processo = lista.pop(0)
    if processo.tempoExecucao > quantum:
        processo.tempoExecucao -= quantum
        lista.append(processo)
    return processo

processos = [
    Processo("P1", 24, 2),
    Processo("P2", 3, 1),
    Processo("P3", 3, 3),
   # Processo("P4", 1, 4),
  #  Processo("P5", 5, 4)
]

while True:
    op = input("Escolha entre os Algoritmos (FCFS, SJF, PS, RR): ").upper()
    if op in ["FCFS", "SJF", "PS", "RR"]:
        break
    print("Algoritmo não suportado")

if op == "RR":
    quantum = int(input("Digite o quantum para o escalonamento RR: "))
else:
    quantum = None

esperaTotal = 0 

filaDeProcessos = processos.copy()
while filaDeProcessos:
    if op == "FCFS":
        atual = fcfs(filaDeProcessos)
    elif op == "SJF":
        atual = sjf(filaDeProcessos)
    elif op == "PS":
        atual = ps(filaDeProcessos)
    elif op == "RR":
        atual = rr(filaDeProcessos, quantum)

    print("Executando " + atual.nome)
