#include <stdio.h>

// Fun��o LMS para processar uma �nica amostra
short lms_process(short entrada, short desejado, short *vetor_amostras, double *coefW, double u, int K) {
    double y_curr = 0.0; // Sa�da atual do filtro
    int i;

    // Inserir a nova amostra no vetor
    vetor_amostras[0] = entrada;

    // Calcular a sa�da do filtro
    for (i = 0; i < K; i++) {
        y_curr += coefW[i] * vetor_amostras[i];
    }

    // Atualizar os coeficientes adaptativos
    double erro = desejado - y_curr;
    for (i = 0; i < K; i++) {
        coefW[i] += u * erro * vetor_amostras[i];
    }

    // Deslocar o vetor de amostras para a direita
    for (i = K - 1; i > 0; i--) {
        vetor_amostras[i] = vetor_amostras[i - 1];
    }

    // Retornar a sa�da calculada como valor inteiro
    return (short)y_curr;
}
