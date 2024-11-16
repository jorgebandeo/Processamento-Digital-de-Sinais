/* Implementa��o de um filtro M�dia M�vel
L� um arquivo bin�rio com amostras em 16bits
Salva arquivo filtrado tamb�m em 16 bits
Walter vers�o 1.0
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>


#define NSAMPLES       4	// Tamanho da m�dia

int main()
{
    FILE* in_file, * out_file;
    int   n_amost;

    short entrada, saida;
    short sample[NSAMPLES] = { 0x0 };

    float y = 0;

    //Carregando os coeficientes do filtro m�dia m�vel

    float coef[NSAMPLES] = {
                 #include "coef.txt"
    };


    /* abre os arquivos de entrada e saida */
    if ((in_file = fopen("..//sweep_20_2k.pcm", "rb")) == NULL)
    {
        printf("/nErro: Nao abriu o arquivo de entrada/n");
        return 0;
    }
    if ((out_file = fopen("..//sweep_20_2k.pcm", "wb")) == NULL)
    {
        printf("/nErro: Nao abriu o arquivo de saida/n");
        return 0;
    }

    // zera vetor de amostras
    for (int i = 0; i < NSAMPLES; i++)
    {
        sample[i] = 0;
    }

    // execu��o do filtro
    do {

        //zera sa�da do filtro
        y = 0;

        //l� dado do arquivo
        n_amost = fread(&entrada, sizeof(short), 1, in_file);
        sample[0] = entrada;

        //Convolu��o e acumula��o
        for (int n = 0; n < NSAMPLES; n++)
        {
            y += coef[n] * sample[n];
        }

        //desloca amostra
        for (int n = NSAMPLES - 1; n > 0; n--)
        {
            sample[n] = sample[n - 1];
        }

        saida = (short)y;

        //escreve no arquivo de sa�da
        fwrite(&saida, sizeof(short), 1, out_file);

    } while (n_amost);


    //fecha os arquivos de entrada de sa�da
    fclose(out_file);
    fclose(in_file);
    return 0;
}
