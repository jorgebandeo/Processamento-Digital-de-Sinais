#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define FS 8000  // Taxa de amostragem (8 kHz)
#define F0 400   // Frequência central (Hz)
#define Q 30     // Fator de qualidade
#define PI 3.14159265358979323846

// Estrutura para armazenar coeficientes do filtro
typedef struct {
    double b0, b1, b2;  // Numerador
    double a1, a2;      // Denominador
} FilterCoefficients;

// Função para calcular os coeficientes do filtro
FilterCoefficients calculate_notch_coefficients(double fs, double f0, double q) {
    FilterCoefficients coeffs;
    double omega = 2 * PI * f0 / fs;  // Frequência angular
    double alpha = sin(omega) / (2 * q);

    // Coeficientes do numerador
    coeffs.b0 = 1;
    coeffs.b1 = -2 * cos(omega);
    coeffs.b2 = 1;

    // Coeficientes do denominador
    coeffs.a1 = -2 * cos(omega);
    coeffs.a2 = 1 - alpha;

    // Normalizar todos os coeficientes pelo denominador a0 = 1 + alpha
    double a0 = 1 + alpha;
    coeffs.b0 /= a0;
    coeffs.b1 /= a0;
    coeffs.b2 /= a0;
    coeffs.a1 /= a0;
    coeffs.a2 /= a0;

    return coeffs;
}

void apply_filter(const short *input, short *output, int length, FilterCoefficients coeffs) {
    double x[3] = {0};  // Buffer de entrada
    double y[3] = {0};  // Buffer de saída

    for (int n = 0; n < length; n++) {
        // Atualizar buffers
        x[2] = x[1];
        x[1] = x[0];
        x[0] = input[n];

        y[2] = y[1];
        y[1] = y[0];

        // Aplicar equação do filtro
        y[0] = coeffs.b0 * x[0] + coeffs.b1 * x[1] + coeffs.b2 * x[2]
             - coeffs.a1 * y[1] - coeffs.a2 * y[2];

        // Converter para saída 16-bit
        output[n] = (short)y[0];
    }
}

int main() {
    // Calcular os coeficientes do filtro
    FilterCoefficients coeffs = calculate_notch_coefficients(FS, F0, Q);

    // Imprimir coeficientes calculados
    printf("Coeficientes do filtro:\n");
    printf("b0 = %.6f, b1 = %.6f, b2 = %.6f\n", coeffs.b0, coeffs.b1, coeffs.b2);
    printf("a1 = %.6f, a2 = %.6f\n", coeffs.a1, coeffs.a2);

    // Abrir arquivos de entrada e saída
    FILE *input_file = fopen("C:/Users/jorge/Desktop/Nova pasta/IIR_Rejeita_Faixa/Q2_voz_ruido.pcm", "rb");
    FILE *output_file = fopen("C:/Users/jorge/Desktop/Nova pasta/IIR_Rejeita_Faixa/Sai_C_M2_voz_ruido.pcm", "wb");

    if (!input_file || !output_file) {
        printf("Erro ao abrir arquivos.\n");
        return 1;
    }

    // Determinar tamanho do arquivo de entrada
    fseek(input_file, 0, SEEK_END);
    int length = ftell(input_file) / sizeof(short);  // Número de amostras
    fseek(input_file, 0, SEEK_SET);

    // Alocar memória para os sinais de entrada e saída
    short *input = malloc(length * sizeof(short));
    short *output = malloc(length * sizeof(short));

    if (input == NULL || output == NULL) {
        printf("Erro ao alocar memória.\n");
        fclose(input_file);
        fclose(output_file);
        return 1;
    }

    fread(input, sizeof(short), length, input_file);

    // Aplicar filtro
    apply_filter(input, output, length, coeffs);

    fwrite(output, sizeof(short), length, output_file);

    // Limpeza
    free(input);
    free(output);
    fclose(input_file);
    fclose(output_file);

    printf("Processamento concluído. Arquivo salvo como 'Sai_C_M2_voz_ruido.pcm'.\n");
    return 0;
}
