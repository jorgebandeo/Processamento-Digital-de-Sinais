#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846
#define FS 8000       // Frequência de amostragem em Hz
#define FC 1000       // Frequência de corte para filtros em Hz
#define FB 300        // Frequência de banda para filtros passa-faixa e rejeita-faixa

// Função para ler um arquivo PCM de 16 bits em um array de inteiros
short* read_pcm(const char* file_path, int* num_samples) {
    FILE* file;
    fopen_s(&file, file_path, "rb");
    if (!file) {
        printf("Erro ao abrir o arquivo.\n");
        return NULL;
    }

    // Obtendo o tamanho do arquivo
    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Calculando o número de amostras
    *num_samples = file_size / sizeof(short);

    // Alocando memória para o sinal
    short* signal = (short*)malloc(file_size);
    if (!signal) {
        printf("Erro ao alocar memória.\n");
        fclose(file);
        return NULL;
    }

    // Lendo os dados do arquivo
    fread(signal, sizeof(short), *num_samples, file);
    fclose(file);

    return signal;
}

// Função para salvar os dados no domínio do tempo
void salvar_dados_tempo(double* original, double* filtrado, int num_samples) {
    FILE* file;
    fopen_s(&file, "dominio_tempo.csv", "w");
    if (!file) {
        printf("Erro ao criar arquivo CSV.\n");
        return;
    }
    fprintf(file, "Amostra,Sinal_Original,Sinal_Filtrado\n");
    for (int i = 0; i < num_samples; i++) {
        fprintf(file, "%d,%.6f,%.6f\n", i, original[i], filtrado[i]);
    }
    fclose(file);
    printf("Dados no domínio do tempo salvos em 'dominio_tempo.csv'.\n");
}

// Função para calcular a FFT e salvar o espectro de frequência
void salvar_espectro_frequencia(double* original, double* filtrado, int num_samples) {
    FILE* file;
    fopen_s(&file, "espectro_frequencia.csv", "w");
    if (!file) {
        printf("Erro ao criar arquivo CSV.\n");
        return;
    }
    fprintf(file, "Frequencia(Hz),Original_Magnitude,Filtrado_Magnitude\n");

    for (int i = 0; i < num_samples / 2; i++) {
        double re_original = 0.0, im_original = 0.0;
        double re_filtrado = 0.0, im_filtrado = 0.0;

        for (int j = 0; j < num_samples; j++) {
            re_original += original[j] * cos(2 * PI * i * j / num_samples);
            im_original -= original[j] * sin(2 * PI * i * j / num_samples);
            re_filtrado += filtrado[j] * cos(2 * PI * i * j / num_samples);
            im_filtrado -= filtrado[j] * sin(2 * PI * i * j / num_samples);
        }

        double mag_original = sqrt(re_original * re_original + im_original * im_original);
        double mag_filtrado = sqrt(re_filtrado * re_filtrado + im_filtrado * im_filtrado);
        fprintf(file, "%.2f,%.6f,%.6f\n", (i * FS) / (double)num_samples, mag_original, mag_filtrado);
    }
    fclose(file);
    printf("Espectro de frequência salvo em 'espectro_frequencia.csv'.\n");
}

// Função para calcular e salvar a resposta em frequência em dB
void salvar_resposta_frequencia_db(double* original, double* filtrado, int num_samples) {
    FILE* file;
    fopen_s(&file, "resposta_frequencia_db.csv", "w");
    if (!file) {
        printf("Erro ao criar arquivo CSV.\n");
        return;
    }
    fprintf(file, "Frequencia(Hz),Original_dB,Filtrado_dB\n");

    for (int i = 0; i < num_samples / 2; i++) {
        double re_original = 0.0, im_original = 0.0;
        double re_filtrado = 0.0, im_filtrado = 0.0;

        for (int j = 0; j < num_samples; j++) {
            re_original += original[j] * cos(2 * PI * i * j / num_samples);
            im_original -= original[j] * sin(2 * PI * i * j / num_samples);
            re_filtrado += filtrado[j] * cos(2 * PI * i * j / num_samples);
            im_filtrado -= filtrado[j] * sin(2 * PI * i * j / num_samples);
        }

        double mag_original = sqrt(re_original * re_original + im_original * im_original);
        double mag_filtrado = sqrt(re_filtrado * re_filtrado + im_filtrado * im_filtrado);
        double db_original = 20 * log10(mag_original);
        double db_filtrado = 20 * log10(mag_filtrado);
        fprintf(file, "%.2f,%.6f,%.6f\n", (i * FS) / (double)num_samples, db_original, db_filtrado);
    }
    fclose(file);
    printf("Resposta em frequência em dB salva em 'resposta_frequencia_db.csv'.\n");
}

// Função para aplicar filtros e salvar dados após a aplicação
void aplicar_filtro_e_salvar(double* sinal_original, int num_samples, void (*filtro)(double*, int, double*)) {
    double* sinal_filtrado = (double*)malloc(num_samples * sizeof(double));
    if (!sinal_filtrado) {
        printf("Erro ao alocar memória para o sinal filtrado.\n");
        return;
    }

    filtro(sinal_original, num_samples, sinal_filtrado);

    salvar_dados_tempo(sinal_original, sinal_filtrado, num_samples);
    salvar_espectro_frequencia(sinal_original, sinal_filtrado, num_samples);
    salvar_resposta_frequencia_db(sinal_original, sinal_filtrado, num_samples);

    free(sinal_filtrado);
}

// Função para aplicar o filtro passa-baixa de segunda ordem
void aplica_filtro_passa_baixa(double* signal, int num_samples, double* filtered_signal) {
    double K = tan((PI * FC) / FS);
    double b0 = K * K / (1 + sqrt(2) * K + K * K);
    double b1 = 2 * b0;
    double b2 = b0;
    double a1 = (2 * (K * K - 1)) / (1 + sqrt(2) * K + K * K);
    double a2 = (1 - sqrt(2) * K + K * K) / (1 + sqrt(2) * K + K * K);

    // Aplicando o filtro
    for (int i = 0; i < num_samples; i++) {
        filtered_signal[i] = b0 * signal[i];
        if (i > 0) filtered_signal[i] += b1 * signal[i - 1] - a1 * filtered_signal[i - 1];
        if (i > 1) filtered_signal[i] += b2 * signal[i - 2] - a2 * filtered_signal[i - 2];
    }
}

// Função para aplicar o filtro passa-alta de segunda ordem
void aplica_filtro_passa_alta(double* signal, int num_samples, double* filtered_signal) {
    double K = tan((PI * FC) / FS);
    double b0 = 1 / (1 + sqrt(2) * K + K * K);
    double b1 = -2 * b0;
    double b2 = b0;
    double a1 = (2 * (K * K - 1)) / (1 + sqrt(2) * K + K * K);
    double a2 = (1 - sqrt(2) * K + K * K) / (1 + sqrt(2) * K + K * K);

    // Aplicando o filtro
    for (int i = 0; i < num_samples; i++) {
        filtered_signal[i] = b0 * signal[i];
        if (i > 0) filtered_signal[i] += b1 * signal[i - 1] - a1 * filtered_signal[i - 1];
        if (i > 1) filtered_signal[i] += b2 * signal[i - 2] - a2 * filtered_signal[i - 2];
    }
}

// Função para aplicar o filtro passa-faixa de segunda ordem
void aplica_filtro_passa_faixa(double* signal, int num_samples, double* filtered_signal) {
    double C = (tan((PI * FB) / FS) - 1) / (tan((2 * PI * FB) / FS) + 1);
    double D = -cos((2 * PI * FC) / FS);
    double b0 = (1 / 2.0) * (1 - C);
    double b1 = D * (1 - C);
    double b2 = (1 / 2.0) * (1 - C);
    double a1 = D * (1 - C);
    double a2 = -C;

    // Aplicando o filtro
    for (int i = 0; i < num_samples; i++) {
        filtered_signal[i] = b0 * signal[i];
        if (i > 0) filtered_signal[i] += b1 * signal[i - 1] - a1 * filtered_signal[i - 1];
        if (i > 1) filtered_signal[i] += b2 * signal[i - 2] - a2 * filtered_signal[i - 2];
    }
}

// Função para aplicar o filtro rejeita-faixa de segunda ordem
void aplica_filtro_rejeita_faixa(double* signal, int num_samples, double* filtered_signal) {
    double C = (tan((PI * FB) / FS) - 1) / (tan((2 * PI * FB) / FS) + 1);
    double D = -cos((2 * PI * FC) / FS);
    double b0 = (1 / 2.0) * (1 + C);
    double b1 = 0;
    double b2 = (1 / 2.0) * (-C - 1);
    double a1 = D * (1 - C);
    double a2 = -C;

    // Aplicando o filtro
    for (int i = 0; i < num_samples; i++) {
        filtered_signal[i] = b0 * signal[i];
        if (i > 0) filtered_signal[i] += b1 * signal[i - 1] - a1 * filtered_signal[i - 1];
        if (i > 1) filtered_signal[i] += b2 * signal[i - 2] - a2 * filtered_signal[i - 2];
    }
}

// Função para aplicar a FFT e exibir a resposta em frequência
void calcula_fft(double* signal, int num_samples) {
    printf("FFT calculada (simplificada):\n");
    for (int i = 0; i < num_samples / 2; i++) {
        double re = 0.0;
        double im = 0.0;
        for (int j = 0; j < num_samples; j++) {
            re += signal[j] * cos(2 * PI * i * j / num_samples);
            im -= signal[j] * sin(2 * PI * i * j / num_samples);
        }
        double magnitude = sqrt(re * re + im * im);
        printf("Frequência %d Hz: Magnitude = %.2f dB\n", (int)(i * FS / num_samples), 20 * log10(magnitude));
    }
}

// Função do menu para o usuário selecionar a operação
void menu() {
    printf("Selecione a operação:\n");
    printf("1. Ler arquivo PCM\n");
    printf("2. Aplicar filtro passa-baixa\n");
    printf("3. Aplicar filtro passa-alta\n");
    printf("4. Aplicar filtro passa-faixa\n");
    printf("5. Aplicar filtro rejeita-faixa\n");
    printf("6. Sair\n");
    printf("Escolha uma opção: ");
}

int main() {
    int option, num_samples;
    short* pcm_data = NULL;
    double* signal = NULL;

    while (1) {
        menu();
        scanf_s("%d", &option);

        switch (option) {
        case 1:
            pcm_data = read_pcm("sweep_20_2k.pcm", &num_samples);
            if (pcm_data) {
                signal = (double*)malloc(num_samples * sizeof(double));
                for (int i = 0; i < num_samples; i++) {
                    signal[i] = pcm_data[i];
                }
                printf("Arquivo PCM lido com sucesso. Número de amostras: %d\n", num_samples);
            }
            else {
                printf("Falha ao ler o arquivo PCM.\n");
            }
            break;

        case 2:
            if (signal) {
                aplicar_filtro_e_salvar(signal, num_samples, aplica_filtro_passa_baixa);
            }
            else {
                printf("Por favor, carregue um arquivo PCM primeiro.\n");
            }
            break;

        case 3:
            if (signal) {
                aplicar_filtro_e_salvar(signal, num_samples, aplica_filtro_passa_alta);
            }
            else {
                printf("Por favor, carregue um arquivo PCM primeiro.\n");
            }
            break;

        case 4:
            if (signal) {
                aplicar_filtro_e_salvar(signal, num_samples, aplica_filtro_passa_faixa);
            }
            else {
                printf("Por favor, carregue um arquivo PCM primeiro.\n");
            }
            break;

        case 5:
            if (signal) {
                aplicar_filtro_e_salvar(signal, num_samples, aplica_filtro_rejeita_faixa);
            }
            else {
                printf("Por favor, carregue um arquivo PCM primeiro.\n");
            }
            break;

        case 6:
            printf("Saindo...\n");
            free(pcm_data);
            free(signal);
            return 0;

        default:
            printf("Opção inválida. Tente novamente.\n");
        }
    }
}