#include <stdio.h>
#include <stdlib.h>

// Função para contar o número de coeficientes no arquivo
int contar_coeficientes(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Erro ao abrir o arquivo '%s'.\n", filename);
        exit(1);
    }

    int count = 0;
    double temp;
    while (fscanf(file, "%lf", &temp) == 1) {
        count++;
    }

    fclose(file);
    return count;
}

// Função para carregar os coeficientes do arquivo
void carregar_coeficientes(const char *filename, double *b, int numtaps) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Erro ao abrir o arquivo '%s'.\n", filename);
        exit(1);
    }

    for (int i = 0; i < numtaps; i++) {
        if (fscanf(file, "%lf", &b[i]) != 1) {
            printf("Erro ao ler coeficiente %d do arquivo.\n", i);
            fclose(file);
            exit(1);
        }
    }

    fclose(file);
    printf("Coeficientes carregados com sucesso.\n");
}

// Função para aplicar o filtro FIR
void aplicar_filtro_fir(const double *b, int numtaps, const short *input, short *output, int length) {
    for (int n = 0; n < length; n++) {
        double y = 0.0;
        for (int k = 0; k < numtaps; k++) {
            if (n - k >= 0) {
                y += b[k] * input[n - k];
            }
        }
        if (y > 32767) y = 32767;
        if (y < -32768) y = -32768;
        output[n] = (short)y;
    }
}

int main() {
    const char *coef_file = "C:/Users/jorge/Desktop/Nova pasta/filtro_FIR_Sinc_janelado_Passa_Alta/Resultados/coeficientes_fir.txt";
    const char *input_file = "C:/Users/jorge/Desktop/Nova pasta/filtro_FIR_Sinc_janelado_Passa_Alta/Q3_voz_ruido.pcm";
    const char *output_file = "C:/Users/jorge/Desktop/Nova pasta/filtro_FIR_Sinc_janelado_Passa_Alta/Sai_C_Q3_voz_ruido.pcm";

    // Contar o número de coeficientes no arquivo
    int numtaps = contar_coeficientes(coef_file);
    printf("Número de coeficientes encontrados: %d\n", numtaps);

    // Alocar memória para os coeficientes
    double *b = malloc(numtaps * sizeof(double));
    if (!b) {
        printf("Erro ao alocar memória para os coeficientes.\n");
        return 1;
    }

    // Carregar os coeficientes
    carregar_coeficientes(coef_file, b, numtaps);

    // Abrir arquivos de entrada e saída
    FILE *input = fopen(input_file, "rb");
    FILE *output = fopen(output_file, "wb");
    if (!input || !output) {
        printf("Erro ao abrir arquivos de entrada/saída.\n");
        free(b);
        return 1;
    }

    // Determinar o tamanho do sinal de entrada
    fseek(input, 0, SEEK_END);
    int length = ftell(input) / sizeof(short);
    fseek(input, 0, SEEK_SET);

    // Alocar memória para os sinais de entrada e saída
    short *input_signal = malloc(length * sizeof(short));
    short *output_signal = malloc(length * sizeof(short));
    if (!input_signal || !output_signal) {
        printf("Erro ao alocar memória para os sinais.\n");
        free(b);
        fclose(input);
        fclose(output);
        return 1;
    }

    // Ler sinal de entrada
    fread(input_signal, sizeof(short), length, input);

    // Aplicar filtro FIR
    aplicar_filtro_fir(b, numtaps, input_signal, output_signal, length);

    // Salvar sinal filtrado
    fwrite(output_signal, sizeof(short), length, output);

    // Limpar memória e fechar arquivos
    free(input_signal);
    free(output_signal);
    free(b);
    fclose(input);
    fclose(output);

    printf("Processamento concluído. Sinal salvo em '%s'.\n", output_file);
    return 0;
}
