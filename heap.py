import time
import random

# Função para ajustar o heap
def heapify(arr, n, i):
    comp = 0
    trocas = 0
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    comp += 1

    if r < n and arr[r] > arr[largest]:
        largest = r
    comp += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        trocas += 1
        heapify(arr, n, largest)
    
    return comp, trocas

# Função para ordenar usando Heap Sort
def heap_sort(arr):
    comp = 0
    trocas = 0
    n = len(arr)

    # Construindo o max heap
    for i in range(n // 2 - 1, -1, -1):
        comp_tmp, trocas_tmp = heapify(arr, n, i)
        comp += comp_tmp
        trocas += trocas_tmp

    # Extrair elementos um por um do heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        trocas += 1
        comp_tmp, trocas_tmp = heapify(arr, i, 0)
        comp += comp_tmp
        trocas += trocas_tmp

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
vector_size = 1000000

# Vetor aleatório
aleatorio_arr = vetor_aleatorio(vector_size)
#Vetor ordenado
ordenado_arr = vetor_ordenado(vector_size)
# Vetor invertido
inverso_arr = vetor_inverso(vector_size)


# Medição de desempenho para heap Sort
comp, trocas, tempo_execucao = desempenho(heap_sort, inverso_arr)
print("heap Sort:")
print(f"Comparações: {comp}")
print(f"Trocas: {trocas}")
print(f"Tempo de execução: {tempo_execucao} segundos")
