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
   - **Gráfico de polos e zeros:** 

2. **Atenuação em dB nas frequências de 100 Hz e 1 kHz:**
   - Frequência de 100 Hz: 
   - Frequência de 1 kHz: 

3. **Programa em Python para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Gráficos dos sinais de entrada e saída para diferentes tamanhos de filtro: 
4. **Identificação do tamanho do filtro MM ideal:**
   - Qual o tamanho que oferece maior redução dos *spikes* sem comprometer o sinal de interesse? 
   - Sinal de saída salvo em `Sai_Sin_spike.pcm`: [x] Sim / [ ] Não

---

## **Tarefa 2: Filtro IIR Rejeita-Faixa (Segunda Ordem)**

### **Descrição**
Projetar um filtro IIR Rejeita-Faixa para reduzir o ruído presente no arquivo `Q2_voz_ruido.pcm`.

### **Passos**
1. **Identificação da frequência do ruído via Espectrograma no “Ocenaudio”:**
   - Frequência identificada:

   ![Espectrograma do Ruído](../IIR_Rejeita_Faixa/Espectrograma do Ocenaudio.png "Espectrograma gerado no Ocenaudio")

2. **Resposta em frequência do filtro e polos e zeros:**
   - **Gráfico da resposta em frequência:** 
   - **Gráfico de polos e zeros:**
3. **Atenuação em dB nas frequências de 200 Hz e 1 kHz:**
   - Frequência de 200 Hz: 
   - Frequência de 1 kHz: 

4. **Programa em Python para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Sinal de saída salvo em `Sai_M2_voz_ruido.pcm`: [x] Sim / [ ] Não

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
   - **Gráfico de polos e zeros:** 

2. **Atenuação em dB nas frequências de 100 Hz e 1 kHz:**
   - Frequência de 100 Hz: 
   - Frequência de 1 kHz: 

3. **Programa em Python para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Sinal de saída salvo em `Sai_Q3_voz_ruido.pcm`: [x] Sim / [ ] Não

4. **Parâmetros do filtro FIR ideal:**
   - Número de coeficientes utilizado: 
   - Tipo de janela utilizada: 

5. **Programa em C para aplicar o filtro:**
   - Código desenvolvido? [x] Sim / [ ] Não
   - Sinal de saída salvo em `Sai_C_Q3_voz_ruido.pcm`: [x] Sim / [ ] Não

6. **Teste com sinal senoidal de 200 Hz:**
   - **Geração do sinal:** 
   - **Sinal de saída processado pelo filtro:** [x] Sim / [ ] Não
   - Atenuação calculada em dB: 

---

