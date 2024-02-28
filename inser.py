import time
import random

# Função para ordenar usando Insertion Sort
def insertion_sort(arr):
    comp = 0
    trocas = 0
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            comp += 1
            arr[j + 1] = arr[j]
            trocas += 1
            j -= 1
        arr[j + 1] = chave
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

# Medição de desempenho para Insertion Sort
comp, trocas, tempo_execucao = desempenho(insertion_sort, inverso_arr )
print("Insertion Sort")
print(f"Comparações: {comp}")
print(f"Trocas: {trocas}")
print(f"Tempo de execução: {tempo_execucao} segundos")
