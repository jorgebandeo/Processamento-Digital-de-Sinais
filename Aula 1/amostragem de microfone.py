import sounddevice as sd
import numpy as np
import cv2

# Parâmetros de configuração
frequencia_amostragem = 14100  # Frequência de amostragem (Hz)
duracao_janela = 0.5  # Duração da janela de tempo (segundos) para visualização (aumentei para melhorar a resolução da FFT)
tamanho_janela = int(frequencia_amostragem * duracao_janela)  # Tamanho da janela de amostragem

# Buffer para armazenar o sinal amostrado
sinal_amostrado = np.zeros(tamanho_janela)

def audio_callback(indata, frames, time, status):
    global sinal_amostrado
    if status:
        print(status)
    # Atualiza o buffer com o novo áudio capturado
    sinal_amostrado = np.roll(sinal_amostrado, -frames)
    sinal_amostrado[-frames:] = indata[:, 0]

def obter_cor_pela_frequencia(frequencia_dominante):
    """Retorna uma cor baseada na frequência dominante, com gradiente ampliado."""
    frequencia_normalizada = frequencia_dominante / 2000.0  # Normaliza para 2kHz

    # Mapeia para um gradiente de cor perceptível (azul -> verde -> vermelho)
    r = int(np.clip(255 * frequencia_normalizada, 0, 255))
    g = int(np.clip(255 * (1 - abs(frequencia_normalizada - 0.5) * 2), 0, 255))
    b = int(np.clip(255 * (1 - frequencia_normalizada), 0, 255))
    
    return (b, g, r)

# Inicia o stream de áudio
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=frequencia_amostragem)
stream.start()

# Configurações da janela do OpenCV
cv2.namedWindow("Áudio em Tempo Real com Cores", cv2.WINDOW_NORMAL)

while True:
    # Cria uma imagem em branco
    img = np.zeros((400, tamanho_janela, 3), dtype=np.uint8)
    
    # Aplica FFT para obter as frequências do sinal
    fft = np.fft.fft(sinal_amostrado)
    fft_magnitude = np.abs(fft)[:tamanho_janela//2]  # Pegamos apenas a metade positiva do espectro
    frequencias = np.fft.fftfreq(tamanho_janela, 1/frequencia_amostragem)[:tamanho_janela//2]

    # Encontra a frequência dominante
    indice_frequencia_dominante = np.argmax(fft_magnitude)
    frequencia_dominante = abs(frequencias[indice_frequencia_dominante])

    # Obtém a cor correspondente à frequência dominante
    cor = obter_cor_pela_frequencia(frequencia_dominante)

    # Normaliza o sinal para o intervalo [0, 1]
    sinal_normalizado = (sinal_amostrado - np.min(sinal_amostrado)) / (np.max(sinal_amostrado) - np.min(sinal_amostrado))
    
    # Converte para coordenadas de pixel
    y = (1 - sinal_normalizado) * 200
    
    # Desenha uma linha contínua colorida pela frequência dominante
    for i in range(1, len(y)):
        cv2.line(img, (i-1, int(y[i-1])), (i, int(y[i])), cor, 1)
    
    # Exibe a imagem
    cv2.imshow("Áudio em Tempo Real com Cores", img)
    
    # Verifica se a tecla ESC foi pressionada para sair
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Finaliza o stream de áudio e fecha a janela
stream.stop()
stream.close()
cv2.destroyAllWindows()
