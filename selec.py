import time
import random

# Função para ordenar usando Selection Sort
def selection_sort(arr):
    comp = 0
    trocas = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        trocas += 1
    return comp, trocas

#Função para gerar vetor aleatório
def vetor_aleatorio(size):
    return [random.randint(1, 1000000) for _ in range(size)]
# Função para gerar vetor ordenado
def vetor_ordenado(size):
    return list(range(1, size + 1))
# Função para gerar vetor invertido
def vetor_inverso(size):
    return list(range(size, 0, -1))

# Função para medir o desempenho
def desempenho(sort_func, arr):
    ini_tempo = time.time()
    comp, trocas = sort_func(arr)
    fim_tempo = time.time()
    tempo_execucao = fim_tempo - ini_tempo
    return comp, trocas, tempo_execucao


# Tamanho do vetor
vector_size = 10000

# Vetor aleatório
aleatorio_arr = vetor_aleatorio(vector_size)
#Vetor ordenado
ordenado_arr = vetor_ordenado(vector_size)
# Vetor invertido
inverso_arr = vetor_inverso(vector_size)

# Medição de desempenho para Selection Sort
comp, trocas, tempo_execucao = desempenho(selection_sort, inverso_arr)
print("Selection Sort")
print(f"Comparações: {comp}")
print(f"Trocas: {trocas}")
print(f"Tempo de execução: {tempo_execucao} segundos")
