Aqui está o README atualizado com seções para entradas de imagens e um quadro comparativo para preenchimento na seção **3.b**:

---

## **README para Resposta da Tarefa M3 - PDS 2024-2**

Este README serve como guia para a execução e resposta das questões apresentadas na Tarefa M3. As respostas devem ser acompanhadas de gráficos, análises e a tabela de comparação solicitada na **3.b**.

---

### **Estrutura das Tarefas**

---

### **1. Identificação de Sistema com Filtro Adaptativo**

#### **1.a** Desenvolver em Python
1. **Objetivo**: Plotar o erro \( e[n] \) para diferentes valores de \( u \) e \( K \).
2. **Resultado Esperado**:
   - Gráfico do erro \( e[n] \) para cada combinação de \( u \) e \( K \).
   - Valores que fazem o algoritmo convergir.

**Adicione a Imagem do Gráfico**:
![Gráfico da Questão 1.a](/questao_1/letra%20a/resultados_u1.0e-10_K100.png)

---

#### **1.b** Implementar em C
1. **Objetivo**: Implementar o filtro LMS em C usando os valores de \( u \) e \( K \) encontrados.
2. **Resultado Esperado**:
   - Arquivo `erro_Q1_C.pcm`.
   - Validação no Ocenaudio ou Python.

**Adicione a Imagem da Validação**:
![Validação da Questão 1.b](/questao_1/letra%20b/Captura%20de%20pantalla%202024-12-14%20101036.png)

---

#### **1.c** Executar no VisualDSP
1. **Objetivo**: Executar o programa no VisualDSP.
2. **Resultado Esperado**:
   - Arquivo `erro_Q1_VDSP.pcm`.
   - Validação no Ocenaudio ou Python.

**Adicione a Imagem da Validação**:
![Validação da Questão 1.c](/questao_1/letra_c/Captura%20de%20pantalla%202024-12-14%20101109.png)

---

### **2. Filtro IIR Passa-Alta e Identificação de Sistema**

#### **2.a** Aplicar Filtro IIR e Gerar `dn_Q2.pcm`
1. **Objetivo**: Projetar um filtro IIR passa-alta e aplicar ao sinal de entrada.
2. **Resultado Esperado**:
   - Gráfico do filtro projetado.
   - Arquivo `dn_Q2.pcm`.


---

#### **2.b** Identificação de Sistema em Python
1. **Objetivo**: Usar `x[n]` e `dn_Q2.pcm` para executar o filtro LMS em Python.
2. **Resultado Esperado**:
   - Gráfico do erro \( e[n] \) para diferentes valores de \( u \) e \( K \).
   - Valores para convergência.

**Adicione a Imagem do Gráfico**:
![Gráfico da Questão 2.b](/questao_2/letra%20b/resultados_u1.0e-10_K10.png)

---

#### **2.c** Implementar em C
1. **Objetivo**: Implementar a identificação do sistema em C com os valores encontrados.
2. **Resultado Esperado**:
   - Arquivo `erro_Q2_C.pcm`.
   - Validação no Ocenaudio ou Python.

**Adicione a Imagem da Validação**:
![Validação da Questão 2.c](/questao_2/letra%20c/Captura%20de%20pantalla%202024-12-14%20101133.png)

---

#### **2.d** Executar no VisualDSP
1. **Objetivo**: Executar o programa no VisualDSP.
2. **Resultado Esperado**:
   - Arquivo `erro_Q2_VDSP.pcm`.
   - Validação no Ocenaudio ou Python.

**Adicione a Imagem da Validação**:
![Validação da Questão 2.d](/questao_2/letra_d/Captura%20de%20pantalla%202024-12-14%20101201.png)


### **3. Otimização e Medição de Desempenho no VisualDSP**

#### **3.a** Medir Ciclos de Clock
1. **Objetivo**: Medir os ciclos (mínimo, máximo e médio) da execução original no VisualDSP.

| **Versão**    | **Ciclos Mínimos** | **Ciclos Máximos** | **Ciclos Médios** |
|---------------|--------------------|--------------------|--------------------|
| Original      | 3658               | 5781               | 5522               |

---

#### **3.b** Otimizar o Algoritmo
1. **Objetivo**: Otimizar o algoritmo no VisualDSP para maior eficiência.
2. **Resultado Esperado**:
   - Arquivo `erro_Q3_VDSP.pcm`.
   - Validação no Ocenaudio ou Python.

**Validação da Questão 3.b**:
![Validação da Questão 3.b](/questao_3/Captura%20de%20pantalla%202024-12-14%20101214.png)

---

#### **3.c** Comparar Ciclos de Clock
1. **Objetivo**: Comparar os ciclos antes e depois da otimização.

| **Versão**    | **Ciclos Mínimos** | **Ciclos Máximos** | **Ciclos Médios** |
|---------------|--------------------|--------------------|--------------------|
| Original      | 3658               | 5781               | 5522               |
| Otimizada     | 3658               | 5781               | 5522               |

