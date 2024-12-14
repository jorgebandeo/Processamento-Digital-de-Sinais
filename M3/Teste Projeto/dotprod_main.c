/* programa para testes com arquivos
-- Lendo arquivo de entrada
-- Processa
-- Gera arquivo de saida
-- walter 1.0 
*/

#include <stdio.h>
#include <string.h>



#define 	FrameSize 1


static int frameCount = 1;

extern void proc_file( short *, short *, int);

int main(int argc,char *argv[])
{
    
	FILE *fin,*fout;

  short Vet_entr[FrameSize];
  short Vet_sai[FrameSize];
  
	
	int i;
	
	printf("***************************************************************\n");
	printf("* TESTE COM ARQUIVOS					           		      *\n");
	printf("*                                                             *\n");
	printf("***************************************************************\n");
	printf("\n");
	
	
	fin = fopen("..\\degrau_1_2.pcm","rb");
//	fin = fopen("..\\imp.pcm","rb");
    	if ((fin)==NULL)
  	{
    		printf("\nErro: nao abriu o arquivo de Entrada\n");
    		return 0;
  	}
    fout = fopen("..\\sai_audio_MM.pcm","wb");
    	if ((fout)==NULL)
  	{
    		printf("\nErro: nao abriu o arquivo de Saida\n");
    		return 0;
  	}

  	
  printf("Processando ... ");

  while (fread(Vet_entr,sizeof(short),FrameSize,fin) == FrameSize) 
  {

		proc_file( Vet_sai, Vet_entr, FrameSize);

		
		fwrite(&Vet_sai,sizeof(short),FrameSize,fout);	
	
		frameCount++;
	}

    printf("terminado!\n");
		
    
	
		fclose(fin);
		fclose(fout);
		
    return 0;
}


