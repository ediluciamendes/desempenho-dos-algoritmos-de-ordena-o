#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Função para ordenar usando Selection Sort
void selection_sort(int arr[], int n, int *comp, int *trocas) {
    *comp = 0;
    *trocas = 0;
    for (int i = 0; i < n; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            (*comp)++;
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
        (*trocas)++;
    }
}

// Função para gerar vetor aleatório
void vetor_aleatorio(int arr[], int size) {
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 1000000 + 1;
    }
}

// Função para medir o desempenho
void desempenho(void (*sort_func)(int[], int, int*, int*), int arr[], int size, int *comp, int *trocas, double *tempo_execucao) {
    clock_t inicio, fim;
    inicio = clock();
    (*sort_func)(arr, size, comp, trocas);
    fim = clock();
    *tempo_execucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
}

int main() {
    int vector_size = 10000;
    int aleatorio_arr[vector_size];
    int ordenado_arr[vector_size];
    int inverso_arr[vector_size];
    int comp, trocas;
    double tempo_execucao;

    vetor_aleatorio(aleatorio_arr, vector_size);

    for (int i = 0; i < vector_size; i++) {
        ordenado_arr[i] = i + 1;
    }

    for (int i = 0; i < vector_size; i++) {
        inverso_arr[i] = vector_size - i;
    }

    // Medição de desempenho para Selection Sort
    desempenho(selection_sort, inverso_arr, vector_size, &comp, &trocas, &tempo_execucao);
    printf("Selection Sort\n");
    printf("Comparações: %d\n", comp);
    printf("Trocas: %d\n", trocas);
    printf("Tempo de execução: %.6f segundos\n", tempo_execucao);

    return 0;
}
