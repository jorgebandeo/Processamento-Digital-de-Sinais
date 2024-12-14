#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_SAMPLES 100000 // Número máximo de amostras esperado

void initialize_array(double *array, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = 0.0;
    }
}

int main() {
    FILE *file_x, *file_d, *file_out_erro, *file_out_y;
    short x[MAX_SAMPLES], d[MAX_SAMPLES], e[MAX_SAMPLES], y[MAX_SAMPLES];
    double w[100]; // Tamanho do filtro escolhido (K=100)
    int N = 0; // Número de amostras
    double u = 0.0000000001; // Passo de adaptação escolhido
    int K = 10; // Tamanho do filtro

    // Abrir arquivos de entrada
    file_x = fopen("ruido_branco.pcm", "rb");
    file_d = fopen("dn_Q2.pcm", "rb");
    file_out_erro = fopen("erro_Q2_C.pcm", "wb");
    file_out_y = fopen("saida_Q2_C.pcm", "wb");

    if (file_x == NULL || file_d == NULL || file_out_erro == NULL || file_out_y == NULL) {
        printf("Erro ao abrir os arquivos.\n");
        return 1;
    }

    // Ler os sinais de entrada e desejado
    while (fread(&x[N], sizeof(short), 1, file_x) && fread(&d[N], sizeof(short), 1, file_d)) {
        N++;
    }

    fclose(file_x);
    fclose(file_d);

    // Inicializar coeficientes
    initialize_array(w, K);

    // Processamento LMS
    for (int i = 0; i < N; i++) {
        double y_curr = 0.0, erro = 0.0;

        // Calcular a saída do filtro
        for (int j = 0; j < K; j++) {
            if (i - j >= 0) {
                y_curr += w[j] * x[i - j];
            }
        }

        // Armazenar o sinal de saída
        y[i] = (short)y_curr;

        // Calcular o erro
        erro = d[i] - y_curr;
        e[i] = (short)erro;

        // Atualizar coeficientes
        for (int j = 0; j < K; j++) {
            if (i - j >= 0) {
                w[j] += u * erro * x[i - j];
            }
        }
    }

    // Salvar os sinais no arquivo de saída
    fwrite(e, sizeof(short), N, file_out_erro);  // Salvar o sinal de erro
    fwrite(y, sizeof(short), N, file_out_y);    // Salvar o sinal de saída
    fclose(file_out_erro);
    fclose(file_out_y);

    printf("Processamento concluído.\n");
    printf("Sinal de erro salvo em 'erro_Q2_C.pcm'.\n");
    printf("Sinal de saída salvo em 'saida_Q2_C.pcm'.\n");

    return 0;
}
