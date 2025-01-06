import cv2
import pickle
import numpy as np

# Carrega as vagas salvas no arquivo
vagas = []
with open('vagas.pkl', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

# Abre o vídeo
video = cv2.VideoCapture('video.mp4')

# Loop principal
while True:
    # Lê um frame do vídeo
    check, img = video.read()

    # Verifica se o frame foi lido corretamente
    if not check:
        print("Fim do vídeo ou erro ao carregar o frame.")
        break

    # Converte o frame para escala de cinza
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3, 3), np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)

    # Inicializa o contador de vagas abertas
    vagasAbertas = 0
    for x, y, w, h in vagas:
        vaga = imgDil[y:y + h, x:x + w]
        count = cv2.countNonZero(vaga)
        cv2.putText(img, str(count), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        if count < 900:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            vagasAbertas += 1
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Exibe o total de vagas abertas
    cv2.rectangle(img, (90, 0), (415, 60), (0, 255, 0), -1)
    cv2.putText(img, f'LIVRE: {vagasAbertas}/69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    # Mostra os frames
    cv2.imshow('Video', img)
    cv2.imshow('Video Th', imgDil)

    # Permite sair ao pressionar 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("Encerrado pelo usuário.")
        break

# Libera recursos
video.release()
cv2.destroyAllWindows()
