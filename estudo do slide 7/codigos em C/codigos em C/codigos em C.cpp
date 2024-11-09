#include <stdio.h>
#include <math.h>

#define FC 1000         // Frequência de corte em Hz
#define FS 8000         // Frequência de amostragem em Hz
#define PI 3.14159265358979323846

// Função para calcular a transformação bilinear com precisão aprimorada
void bilinear(double b_analog[], double a_analog[], double fs, double b_digital[], double a_digital[]) {
    double wc = 2 * PI * FC; // Frequência angular de corte
    double T = 1.0 / fs;
    double K = 2 * fs; // Fator de transformação ajustado

    // Ajustando os coeficientes digitais
    b_digital[0] = K * b_analog[0] / (K + wc);       // b0
    b_digital[1] = -b_digital[0];                    // b1
    a_digital[0] = 1;                                // a0
    a_digital[1] = -(wc - K) / (K + wc);              // a1

    // Multiplicação por -1 para garantir que o coeficiente seja negativo
    a_digital[1] *= -1;
}

// Função para calcular os zeros e pólos
void calculate_zeros_poles(double b_digital[], double a_digital[], double* zero, double* pole) {
    *zero = -b_digital[1] / b_digital[0]; // Zero do filtro
    *pole = -a_digital[1] / a_digital[0]; // Polo do filtro
}

// Função principal para execução do código
int main() {
    // Coeficientes analógicos do filtro passa-alta
    double b_analog[2] = { 1, 0 };   // Numerador de H(s) = s / (s + wc)
    double a_analog[2] = { 1, 2 * PI * FC };  // Denominador de H(s) = s / (s + wc)

    // Coeficientes digitais
    double b_digital[2];
    double a_digital[2];

    // Transformação bilinear
    bilinear(b_analog, a_analog, FS, b_digital, a_digital);

    // Exibindo os coeficientes digitais do filtro
    printf("Coeficientes do filtro passa-alta digital H(z):\n");
    printf("Numerador (b): %.7f, %.7f\n", b_digital[0], b_digital[1]);
    printf("Denominador (a): %.7f, %.7f\n", a_digital[0], a_digital[1]);

    // Calculando e exibindo os zeros e pólos
    double zero, pole;
    calculate_zeros_poles(b_digital, a_digital, &zero, &pole);

    printf("\nZero: %.7f\n", zero);
    printf("Pólo: %.7f\n", pole);

    return 0;
}
