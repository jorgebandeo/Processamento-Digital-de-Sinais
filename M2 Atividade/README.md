# README - Tarefa M2: PDS 2024-2

Este documento serve como guia para responder aos requisitos e acompanhar o desenvolvimento da Tarefa M2 de Processamento Digital de Sinais (PDS) do semestre 2024-2. Por favor, preencha as respostas e atualize o progresso conforme os itens forem concluídos.

---

## **Introdução**
Os sinais fornecidos pelo professor possuem as seguintes características:
- **Frequência de Amostragem (Fs):** 8 kHz
- **Canal:** Mono
- **Quantização:** 16 bits

---

## **Tarefa 1: Filtro Média Móvel (MM)**

### **Descrição**
Projetar um filtro média móvel para reduzir os *spikes* presentes no arquivo `Sin_spike.pcm`.

### **Passos**
1. **Resposta em frequência do filtro e polos e zeros (8 coeficientes):**
   - **Gráfico da resposta em frequência:** 
      ![Espectrograma do Ruído](/MM/Resultados/Resposta_Frequencia/Resposta_Frequencia_Filtro_8.png)

   - **Gráfico de polos e zeros:** 
      ![Espectrograma do Ruído](/MM/Resultados/Polos_Zeros/Polos_Zeros_Filtro_8.png)

2. **Atenuação em dB nas frequências de 100 Hz e 1 kHz:**
   - Frequência de 100 Hz: -0,14 dB
   - Frequência de 1 kHz: -65 dB

3. **Programa em Python para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Gráficos dos sinais de entrada e saída para diferentes tamanhos de filtro: 
         ![Espectrograma do Ruído](/MM/Resultados/Entrada_Saida/Entrada_Saida_Filtro_17.png)
4. **Identificação do tamanho do filtro MM ideal:**
   - Qual o tamanho que oferece maior redução dos *spikes* sem comprometer o sinal de interesse? 
   17
   - Sinal de saída salvo em `Sai_Sin_spike.pcm`: [x] Sim / [ ] Não

---

## **Tarefa 2: Filtro IIR Rejeita-Faixa (Segunda Ordem)**

### **Descrição**
Projetar um filtro IIR Rejeita-Faixa para reduzir o ruído presente no arquivo `Q2_voz_ruido.pcm`.

### **Passos**
1. **Identificação da frequência do ruído via Espectrograma no “Ocenaudio”:**
   - Frequência identificada:

   ![Espectrograma do Ruído](/IIR_Rejeita_Faixa/Espectrograma%20do%20Ocenaudio.png)

2. **Resposta em frequência do filtro e polos e zeros:**
   - **Gráfico da resposta em frequência:** 
      ![Espectrograma do Ruído](/IIR_Rejeita_Faixa/Reultados/resposta_frequencia.png)
   - **Gráfico de polos e zeros:**
      ![Espectrograma do Ruído](/IIR_Rejeita_Faixa/Reultados/polos_zeros.png)
3. **Atenuação em dB nas frequências de 200 Hz e 1 kHz:**
   - Frequência de 200 Hz: 0 dB
   - Frequência de 1 kHz: 0 dB

4. **Programa em Python para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Sinal de saída salvo em `Sai_M2_voz_ruido.pcm`: [x] Sim / [ ] Não
   ![Espectrograma do Ruído](/IIR_Rejeita_Faixa/Reultados/sinais_entrada_saida.png)

5. **Programa em C para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Sinal de saída salvo em `Sai_C_M2_voz_ruido.pcm`: [x] Sim / [ ] Não

---

## **Tarefa 3: Filtro FIR Sinc Janelado Passa-Alta**

### **Descrição**
Projetar um filtro FIR Passa-Alta utilizando a técnica de janelamento para reduzir o ruído do arquivo `Q3_voz_ruido.pcm`.

### **Passos**
1. **Resposta em frequência do filtro e polos e zeros:**
   - **Gráfico da resposta em frequência:** 
      ![Espectrograma do Ruído](/filtro_FIR_Sinc_janelado_Passa_Alta/Resultados%20Voz%20com%20Ruido/resposta_frequencia_fir.png)
   - **Gráfico de polos e zeros:** 
      ![Espectrograma do Ruído](/filtro_FIR_Sinc_janelado_Passa_Alta/Resultados%20Voz%20com%20Ruido/polos_zeros_fir.png)
2. **Atenuação em dB nas frequências de 100 Hz e 1 kHz:**
   - Frequência de 100 Hz: -64,03 dB
   - Frequência de 1 kHz: 0 dB

3. **Programa em Python para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Sinal de saída salvo em `Sai_Q3_voz_ruido.pcm`: [x] Sim / [ ] Não
         ![Espectrograma do Ruído](/filtro_FIR_Sinc_janelado_Passa_Alta/Resultados%20Voz%20com%20Ruido/sinais_entrada_saida.png)
4. **Parâmetros do filtro FIR ideal:**
   - Número de coeficientes utilizado: 301
   - Tipo de janela utilizada: Hamming

5. **Programa em C para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Sinal de saída salvo em `Sai_C_Q3_voz_ruido.pcm`: [x] Sim / [ ] Não


6. **Teste com sinal senoidal de 200 Hz:**
   - **Geração do sinal:** 
         ![Espectrograma do Ruído](/filtro_FIR_Sinc_janelado_Passa_Alta/Resultados%20Seno%20de%20200Hz/sinais_entrada_saida.png)
   - **Sinal de saída processado pelo filtro:** [x] Sim / [ ] Não
   - Atenuação calculada em dB: -9,91 dB
            ![Espectrograma do Ruído](/filtro_FIR_Sinc_janelado_Passa_Alta/Resultados%20Seno%20de%20200Hz/Captura%20de%20pantalla%202024-11-16%20155423.png) 

---

