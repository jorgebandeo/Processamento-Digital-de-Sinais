#include <stdio.h>

// Função LMS para processar uma única amostra
short lms_process(short entrada, short desejado, short *vetor_amostras, double *coefW, double u, int K) {
    static int index = 0; // Índice circular
    double y_curr = 0.0;  // Saída atual do filtro
    double erro;
    int i;

    // Inserir a nova amostra no vetor no índice atual
    vetor_amostras[index] = entrada;

    // Calcular a saída do filtro
    for (i = 0; i < K; i++) {
        int idx = (index - i + K) % K; // Índice circular
        y_curr += coefW[i] * vetor_amostras[idx];
    }

    // Atualizar os coeficientes adaptativos
    erro = desejado - y_curr;
    for (i = 0; i < K; i++) {
        int idx = (index - i + K) % K;
        coefW[i] += u * erro * vetor_amostras[idx];
    }

    // Atualizar o índice circular
    index = (index + 1) % K;

    // Retornar a saída calculada como valor inteiro
    return (short)y_curr;
}

