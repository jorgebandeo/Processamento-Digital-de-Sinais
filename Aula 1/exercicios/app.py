from flask import Flask, render_template, request, url_for, jsonify, send_from_directory
import numpy as np
import matplotlib.pyplot as plt
import os
import time

# Configure Matplotlib to use the Agg backend
plt.switch_backend('Agg')

app = Flask(__name__)

# Pastas para salvar as imagens e arquivos PCM gerados
IMAGE_FOLDER = './images'
PCM_FOLDER = './pcm'
TEMP_IMAGE = 'temp_signal.png'  # Nome da imagem temporária

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

if not os.path.exists(PCM_FOLDER):
    os.makedirs(PCM_FOLDER)

def generate_impulse(n0, window_time, Fs):
    N = int(Fs * window_time)  # Número total de amostras
    n = np.linspace(n0 - (window_time / 2), n0 + (window_time / 2), N)  # Eixo de tempo simétrico em torno de zero
    x = np.zeros(N)
    n0_index = np.argmin(np.abs(n - n0))  # Encontra o índice mais próximo de n0
    x[n0_index] = 1  # Posiciona o impulso em n0
    return n, x

def generate_step(n0, window_time, Fs):
    N = int(Fs * window_time)  # Número total de amostras
    n = np.linspace(n0 - (window_time / 2), n0 + (window_time / 2), N)  # Eixo de tempo simétrico em torno de zero
    x = np.zeros(N)
    x[n >= n0] = 1  # Degrau começa em n0
    return n, x

def save_pcm(filename, signal):
    """Salva o sinal no formato PCM"""
    signal_int16 = np.int16(signal * 32767)  # Convertendo para 16-bit PCM
    with open(filename, 'wb') as pcm_file:
        pcm_file.write(signal_int16.tobytes())

def save_temp_image(n, x, signal_type):
    """Salva a imagem temporária do sinal gerado"""
    plt.figure()
    plt.stem(n, x)
    plt.title(f'{signal_type.capitalize()} Signal')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')

    img_path = os.path.join(IMAGE_FOLDER, TEMP_IMAGE)
    plt.savefig(img_path)
    plt.close()

    return img_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    signal_type = request.form['signal_type']
    window_time = float(request.form['window_time'])
    Fs = int(request.form['Fs'])  # Frequência de amostragem escolhida pelo usuário

    n, x = None, None

    if signal_type == 'impulso':
        n0 = float(request.form['n0'])
        n, x = generate_impulse(n0, window_time, Fs)
    elif signal_type == 'degrau':
        n0 = float(request.form['n0'])
        n, x = generate_step(n0, window_time, Fs)
    elif signal_type == 'senoidal':
        f = float(request.form['f'])
        N = int(Fs * window_time)
        n = np.arange(N) / Fs
        x = np.sin(2 * np.pi * f * n)
    elif signal_type == 'exponencial':
        A = float(request.form['A'])
        a = float(request.form['a'])
        N = int(Fs * window_time)
        n =  np.arange(N) / Fs
        x = A * np.exp(a ** n)

    x_normalizado = x / np.max(np.abs(x)) #estudar metodo de normalização de maximos
    x_N_16bits = np.int16(x_normalizado * 16384) #converte para 16bits que é a referencia do sinal
    img_path = save_temp_image(n, x_N_16bits, signal_type)

    # Adiciona um timestamp para evitar cache
    timestamp = int(time.time())
    img_url = url_for('get_image', filename=TEMP_IMAGE) + f'?t={timestamp}'

    return jsonify({'img_url': img_url, 'n': n.tolist(), 'x': x_N_16bits.tolist(), 'signal_type': signal_type})

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    n = np.array(data['n'])
    x = np.array(data['x'])
    signal_type = data['signal_type']

    # Salvar imagem com um nome único
    timestamp = int(time.time())
    img_filename = f'signal_{timestamp}.png'
    img_path = os.path.join(IMAGE_FOLDER, img_filename)
    
    plt.figure()
    plt.stem(n, x)
    plt.title(f'{signal_type.capitalize()} Signal')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.savefig(img_path)
    plt.close()

    # Salvar sinal como PCM
    pcm_filename = f'signal_{timestamp}.pcm'
    pcm_path = os.path.join(PCM_FOLDER, pcm_filename)
    save_pcm(pcm_path, x)

    return jsonify({'message': 'Sinal salvo com sucesso', 'img_url': url_for('get_image', filename=img_filename), 'pcm_filename': pcm_filename})

if __name__ == '__main__':
    app.run(debug=True)
