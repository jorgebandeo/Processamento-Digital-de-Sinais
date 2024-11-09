#include <stdio.h>
#include <math.h>

#define FC 1000         // Frequência de corte em Hz
#define FS 8000         // Frequência de amostragem em Hz
#define PI 3.14159265358979323846

// Função para calcular os coeficientes do filtro passa-baixa
void calculate_coefficients(double* a, double* b) {
    double T = 1.0 / FS;
    double wc = 2 * PI * FC; // Frequência angular de corte

    // Cálculo dos coeficientes usando a fórmula correta
    *a = (T * wc) / (2 + T * wc);     // Coeficiente a
    *b = -((2 - T * wc) / (2 + T * wc)); // Coeficiente b, ajustado para ser negativo
}

// Função para aplicar o filtro passa-baixa discreto
void aplica_filtro_pb(double x[], double y[], int n, double a, double b) {
    y[n] = a * x[n] + a * x[n - 1] - b * y[n - 1];
}

// Função para calcular a resposta em frequência
void calculate_freq_response(double a, double b, int num_points, double fs) {
    FILE* file;
    fopen_s(&file, "freq_response.csv", "w"); // Usando fopen_s para compatibilidade com o Visual Studio
    if (file == NULL) {
        printf("Erro ao abrir o arquivo\n");
        return;
    }

    fprintf(file, "Frequency(Hz),Magnitude(dB)\n");

    for (int i = 0; i < num_points; i++) {
        double w = (PI * i) / (num_points - 1); // Frequência angular
        double numerator = a * (1 + cos(w));
        double denominator = 1 + b * cos(w);
        double magnitude = 20 * log10(fabs(numerator / denominator));

        double frequency_hz = (w * fs) / (2 * PI);
        fprintf(file, "%.2f,%.2f\n", frequency_hz, magnitude);
    }

    fclose(file);
}

int main() {
    // Variáveis para armazenar os coeficientes calculados
    double a, b;

    // Calculando os coeficientes usando a fórmula corrigida
    calculate_coefficients(&a, &b);

    // Exibindo os coeficientes
    printf("Coeficientes calculados:\n");
    printf("a = %.6f\n", a);
    printf("b = %.6f\n\n", b);

    // Exemplo de sinal de entrada (sinal de teste)
    double x[100] = { 1.0, 0.0 }; // Exemplo simples: impulso unitário
    for (int i = 1; i < 100; i++) {
        x[i] = 0.0; // Zera o restante do sinal de entrada após o impulso
    }

    // Inicializando o buffer de saída com zero
    double y[100] = { 0 };

    // Aplicando o filtro para cada amostra a partir de n = 1
    for (int n = 1; n < 100; n++) {
        aplica_filtro_pb(x, y, n, a, b);
    }

    // Exibindo os resultados da aplicação do filtro
    printf("Saída do filtro y[n]:\n");
    for (int i = 0; i < 100; i++) {
        printf("y[%d] = %.6f\n", i, y[i]);
    }

    // Calculando e salvando a resposta em frequência em um arquivo CSV
    calculate_freq_response(a, b, 8000, FS);

    printf("\nResposta em frequência salva em 'freq_response.csv'\n");
    return 0;
}
