#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cycles.h>
#include <fract.h>
#define NSAMPLES 100 // Número máximo de coeficientes adaptativos
#define MAX_SAMPLES 100000 // Número máximo de amostras

// Protótipo da função externa
extern short lms_process(short entrada, short desejado, short *vetor_amostras, double *coefW, double u, int K);

int main() {
	cycle_stats_t stats;  
    FILE *file_x, *file_d, *file_out_erro, *file_out_y;
    short entrada, desejado, saida, erro;
    short vetor_amostras[NSAMPLES] = {0}; // Vetor de amostras
    double coefW[NSAMPLES] = {0.0};       // Coeficientes adaptativos inicializados com 0
    double u = 0.00000000001;             // Passo de adaptação
    int K = 10;                          // Tamanho do filtro adaptativo

    // Abrir arquivos
    file_x = fopen("..\\ruido_branco.pcm", "rb");
    file_d = fopen("..\\dn_Q2.pcm", "rb");
    file_out_erro = fopen("..\\erro_Q3_VDSP.pcm", "wb");
    file_out_y = fopen("..\\saida_Q3_VDSP.pcm", "wb");

    if (file_x == NULL || file_d == NULL || file_out_erro == NULL || file_out_y == NULL) {
        printf("Erro ao abrir os arquivos.\n");
        return 1;
    }
	CYCLES_INIT(stats);
    printf("Processando...\n");

    // Processamento LMS
    while (fread(&entrada, sizeof(short), 1, file_x) == 1 && fread(&desejado, sizeof(short), 1, file_d) == 1) {
        // Processar o filtro LMS
        CYCLES_START(stats);	
        saida = lms_process(entrada, desejado, vetor_amostras, coefW, u, K);

        // Calcular o erro
        erro = desejado - saida;
		CYCLES_STOP(stats);
        // Salvar o sinal de saída e erro nos arquivos
        fwrite(&saida, sizeof(short), 1, file_out_y);
        fwrite(&erro, sizeof(short), 1, file_out_erro);
    }
	CYCLES_PRINT(stats);
    printf("Processamento concluído. Arquivos gerados:\n");
    printf("- erro_Q3_VDSP.pcm\n");
    printf("- saida_Q3_VDSP.pcm\n");
	
    // Fechar arquivos
    fclose(file_x);
    fclose(file_d);
    fclose(file_out_erro);
    fclose(file_out_y);

    return 0;
}
