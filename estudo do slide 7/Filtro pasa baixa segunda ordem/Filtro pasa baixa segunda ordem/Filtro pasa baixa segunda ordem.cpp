#include <stdio.h>
#include <math.h>

#define FC 1000         // Frequência de corte em Hz
#define FS 8000         // Frequência de amostragem em Hz
#define PI 3.14159265358979323846

// Função para calcular os coeficientes do filtro passa-baixa de segunda ordem
void calculate_coefficients(double* b0, double* b1, double* b2, double* a1, double* a2) {
    double K = tan((PI * FC) / FS);  // Cálculo de K

    // Cálculo dos coeficientes do filtro
    *b0 = K * K / (1 + sqrt(2) * K + K * K);
    *b1 = 2 * (*b0);
    *b2 = *b0;
    *a1 = (2 * (K * K - 1)) / (1 + sqrt(2) * K + K * K);
    *a2 = (1 - sqrt(2) * K + K * K) / (1 + sqrt(2) * K + K * K);
}

// Função para aplicar o filtro passa-baixa de segunda ordem
double apply_filter(double x[], double y[], int n, double b0, double b1, double b2, double a1, double a2) {
    // Aplicando a equação de diferença do filtro de segunda ordem
    y[n] = b0 * x[n] + b1 * x[n - 1] + b2 * x[n - 2] - a1 * y[n - 1] - a2 * y[n - 2];
    return y[n];
}

// Função para calcular a resposta em frequência e salvar em um arquivo CSV
void calculate_freq_response(double b[], double a[], int num_points, double fs) {
    FILE* file;
    fopen_s(&file, "freq_response.csv", "w"); // Usando fopen_s para compatibilidade com o Visual Studio
    if (file == NULL) {
        printf("Erro ao abrir o arquivo\n");
        return;
    }

    fprintf(file, "Frequency(Hz),Magnitude(dB)\n");

    for (int i = 0; i < num_points; i++) {
        double w = (PI * i) / (num_points - 1); // Frequência angular

        // Cálculo da resposta em frequência H(w) para o filtro de segunda ordem
        double numerator = b[0] + b[1] * cos(-w) + b[2] * cos(-2 * w);
        double denominator = 1 + a[1] * cos(-w) + a[2] * cos(-2 * w);
        double magnitude = 20 * log10(fabs(numerator / denominator));

        double frequency_hz = (w * fs) / (2 * PI);
        fprintf(file, "%.2f,%.2f\n", frequency_hz, magnitude);
    }

    fclose(file);
}

int main() {
    // Coeficientes do filtro
    double b0, b1, b2, a1, a2;
    calculate_coefficients(&b0, &b1, &b2, &a1, &a2);

    // Exibindo os coeficientes calculados
    printf("Coeficientes calculados:\n");
    printf("b0 = %.6f\n", b0);
    printf("b1 = %.6f\n", b1);
    printf("b2 = %.6f\n", b2);
    printf("a1 = %.6f\n", a1);
    printf("a2 = %.6f\n", a2);

    // Configurando arrays de coeficientes para cálculo da resposta em frequência
    double b[] = { b0, b1, b2 };
    double a[] = { 1, a1, a2 };

    // Exemplo de sinal de entrada (impulso unitário)
    double x[100] = { 1.0, 0.0 }; // Primeira amostra = 1, demais = 0
    for (int i = 2; i < 100; i++) {
        x[i] = 0.0;
    }

    // Inicializando o buffer de saída com zero
    double y[100] = { 0 };

    // Aplicando o filtro para cada amostra a partir de n = 2
    for (int n = 2; n < 100; n++) {
        apply_filter(x, y, n, b0, b1, b2, a1, a2);
    }

    // Exibindo os resultados da aplicação do filtro
    printf("\nSaída do filtro y[n]:\n");
    for (int i = 0; i < 100; i++) {
        printf("y[%d] = %.6f\n", i, y[i]);
    }

    // Calculando e salvando a resposta em frequência em um arquivo CSV
    calculate_freq_response(b, a, 8000, FS);

    printf("\nResposta em frequência salva em 'freq_response.csv'\n");
    return 0;
}
