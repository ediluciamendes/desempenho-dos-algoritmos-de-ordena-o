import time
import random

# Função para ordenar usando Quick Sort
def quick_sort(arr):
    comp = [0] # lista para armazenar o número de comparações
    trocas = [0] # lista para armazenar o número de trocas

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comp[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas[0] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        trocas[0] += 1
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    return comp[0], trocas[0]

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


# Medição de desempenho para quick Sort
comp, trocas, tempo_execucao = desempenho(quick_sort, inverso_arr)
print("quick Sort:")
print(f"Comparações: {comp}")
print(f"Trocas: {trocas}")
print(f"Tempo de execução: {tempo_execucao} segundos")
