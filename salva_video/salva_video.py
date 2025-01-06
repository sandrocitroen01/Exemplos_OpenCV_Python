import cv2  # Importa a biblioteca OpenCV, que é usada para processamento de imagens e vídeos

video = cv2.VideoCapture(0)  # Inicializa a captura de vídeo, usando a câmera padrão (0 é o índice da câmera)
quatrocc = cv2.VideoWriter_fourcc(*'XVID')  # Define o codec de vídeo a ser utilizado (XVID neste caso)
salvar = cv2.VideoWriter('meu_video.avi', quatrocc, 20.0, (640, 480))  # Cria o objeto de gravação de vídeo. 'meu_video.avi' é o nome do arquivo, 20.0 é a taxa de quadros por segundo, e (640, 480) é a resolução do vídeo

while True:  # Inicia um loop infinito para capturar e exibir os quadros do vídeo
    ret, frame = video.read()  # Lê um quadro da câmera. 'ret' indica se a leitura foi bem-sucedida, e 'frame' contém o quadro capturado
    salvar.write(frame)  # Escreve o quadro capturado no arquivo de vídeo
    cv2.imshow("Gravando", frame)  # Exibe o quadro na janela chamada "Gravando"

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Verifica se a tecla 'q' foi pressionada
        break  # Interrompe o loop caso a tecla 'q' seja pressionada

video.release()  # Libera a câmera, permitindo que outros programas a utilizem
salvar.release()  # Libera o objeto de gravação de vídeo, salvando o arquivo final
cv2.destroyAllWindows()  # Fecha todas as janelas abertas pelo OpenCV

