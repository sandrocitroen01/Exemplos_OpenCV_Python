import cv2  # Importa a biblioteca OpenCV, que é usada para processamento de imagens e vídeos

video = cv2.VideoCapture(0)  # Cria um objeto para capturar vídeo da câmera padrão (0 representa a primeira câmera conectada)

while True:  # Inicia um loop infinito para capturar e exibir vídeo continuamente
    ret, frame = video.read()  # Lê um quadro (frame) da câmera. 'ret' é um valor booleano que indica se a leitura foi bem-sucedida, e 'frame' contém o quadro capturado
    cv2.imshow("Video ao Vivo", frame)  # Exibe o quadro capturado em uma janela chamada "Video ao Vivo"

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Verifica se a tecla pressionada é 'q'. Se for, o loop é interrompido
        break  # Sai do loop caso a tecla 'q' seja pressionada

video.release()  # Libera a câmera, permitindo que outros programas a utilizem
cv2.destroyAllWindows()  # Fecha todas as janelas abertas pelo OpenCV
