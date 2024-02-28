import time
import random

# Função para ordenar usando Merge Sort
def merge_sort(arr):
    comp = [0] # lista para armazenar o número de comparações
    trocas = [0] # lista para armazenar o número de trocas

    def merge(arr, esque, direita):
        i = j = k = 0

        while i < len(esque) and j < len(direita):
            comp[0] += 1
            if esque[i] < direita[j]:
                arr[k] = esque[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esque):
            arr[k] = esque[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

    def merge_sort_aux(arr):
        if len(arr) > 1:
            meio = len(arr) // 2
            esquerda = arr[:meio]
            direita = arr[meio:]

            merge_sort_aux(esquerda)
            merge_sort_aux(direita)

            merge(arr, esquerda, direita)

    merge_sort_aux(arr)
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


# Medição de desempenho para Merge Sort
comp, trocas, tempo_execucao = desempenho(merge_sort, inverso_arr)
print("Merge Sort:")
print(f"Comparações: {comp}")
print(f"Trocas: {trocas}")
print(f"Tempo de execução: {tempo_execucao} segundos")

