void proc_file(short *sai, short *entr, int N) {
    int i;
    int MM = 4; // Tamanho da janela da média móvel
    
    for (i = 0; i < N; i++) {
        int j;
        int aux = 0;
        
        for (j = -MM; j <= 0; j++) { // Correção na iteração de j
            if (i + j >= 0 && i + j < N) { // Verifica limites para evitar acesso fora do array
                aux += entr[i + j];
            }
        
        sai[i] =(short)(aux / MM); // Calcula a média e converte para short
        }
    }

    return;
}