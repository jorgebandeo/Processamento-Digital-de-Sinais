#include <stdio.h>

// Fun��o LMS para processar uma �nica amostra
short lms_process(short entrada, short desejado, short *vetor_amostras, double *coefW, double u, int K) {
    static int index = 0; // �ndice circular
    double y_curr = 0.0;  // Sa�da atual do filtro
    double erro;
    int i;

    // Inserir a nova amostra no vetor no �ndice atual
    vetor_amostras[index] = entrada;

    // Calcular a sa�da do filtro
    for (i = 0; i < K; i++) {
        int idx = (index - i + K) % K; // �ndice circular
        y_curr += coefW[i] * vetor_amostras[idx];
    }

    // Atualizar os coeficientes adaptativos
    erro = desejado - y_curr;
    for (i = 0; i < K; i++) {
        int idx = (index - i + K) % K;
        coefW[i] += u * erro * vetor_amostras[idx];
    }

    // Atualizar o �ndice circular
    index = (index + 1) % K;

    // Retornar a sa�da calculada como valor inteiro
    return (short)y_curr;
}

