#include <stdio.h>
#define NSAMPLES 8 // MM
#define K 120 // COEF DESEJADOS

int main() {
    
    FILE *in_file, *out_file, *out_erro, *out_d_file, *out_e_file;
    int n_amost = 0, i = 0;
    short entrada, saida, saida_d, saida_e;
    double coefW[K]= {0x0};
    short sample[K] = {0x0};
    float d = 0, y = 0, e = 0; 
    double erro = 0;
    double u = 0.00000000001;
    int n = 0;

    float coef[NSAMPLES] = {
        #include "Coeficiente_MM_8.dat" // MM -> 8
    };
	
    //float coef[NSAMPLES] = {
    //    #include "Coeficiente_PB.dat" // MM -> 8
    //};
    
    if ((in_file = fopen("./ruido_branco.pcm", "rb")) == NULL){ // Sinal de entrada
        printf("\nErro: Nao abriu o arquivo de entrada 1\n");
        return 0;
    }

    if ((out_file = fopen("./saida_lms_dsp.pcm", "wb")) == NULL){ // Sinal de saida
        printf("\nErro: Nao abriu o arquivo de saida 2\n");
        return 0;
    }
    if ((out_d_file = fopen("./saida_lms_d_dsp.pcm", "wb")) == NULL){ // Sinal de saida
        printf("\nErro: Nao abriu o arquivo de saida 3\n");
        return 0;
    }
    if ((out_e_file = fopen("./saida_lms_e_dsp.pcm", "wb")) == NULL){ // Sinal de saida
        printf("\nErro: Nao abriu o arquivo de saida 4\n");
        return 0;
    }
    if ((out_erro = fopen("./error.dat", "wb")) == NULL){ // Erro
        printf("\nErro: Nao abriu o arquivo de saida 5\n");
        return 0;
    }

    do {
        n_amost = fread(&entrada, sizeof(short), 1, in_file);

        sample[0] = entrada;

        d = 0; 
        for (n = 0; n < NSAMPLES; n++){ // Desejado
            d += coef[n] * sample[n];
        }

        y = 0;
        for (n = 0; n < K; n++){ // Atual
            y += coefW[n] * sample[n];
        }

        erro = d - y;

        //if(i > K){ // Atualiza Coeficientes
        //    for(n = 0; n < K; n++){
        //        coefW[n] = coefW[n] + (u*erro*(sample[n]));
        //    }
        //}
        
        
        for(n = 0; n < K; n++){
        	//if((i-K)>=0){ // Atualiza Coeficientes
           	coefW[n] = coefW[n] + (u*erro*(sample[n]));
            //}
        }
        
        

        for (n = K-1; n > 0; n--){ // Atualiza Sample
            sample[n] = sample[n-1];
        }

        saida = (short)y;
        fwrite(&saida, sizeof(short), 1, out_file);
        saida_d = (short)d;
        fwrite(&saida_d, sizeof(short), 1, out_d_file);
        saida_e = (short)erro;
        fwrite(&saida_e, sizeof(short), 1, out_e_file);
        fprintf(out_erro, "\n%f,", erro);
        i++;
    } while (n_amost);
	
    printf("\nCoefs gerados!");
    for(n = 0; n < K; n++){
        printf("\n%f", coefW[n]);
    }

    fclose(out_erro);
    fclose(out_file);
    fclose(out_d_file);
    fclose(in_file);
    printf("\n\nFile ready!");
    return 0;
}
