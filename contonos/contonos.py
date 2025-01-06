# Importa a biblioteca OpenCV, usada para processamento de imagens.
import cv2 

# Carrega a imagem "python2.png" do disco e armazena na variável 'imagem'.
imagem = cv2.imread("python2.png")

# Exibe as dimensões da imagem carregada (altura, largura e canais de cor).
print(imagem.shape)

# Exibe a imagem original em uma janela chamada "imagem".
cv2.imshow("imagem", imagem)

# Converte a imagem de colorida (BGR) para escala de cinza e armazena em 'imagem_cinza'.
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detecta bordas na imagem em escala de cinza usando o algoritmo Canny.
# Os limites inferiores e superiores para a detecção de bordas são 50 e 150, respectivamente.
bordas = cv2.Canny(imagem_cinza, 50, 150)

# Encontra os contornos na imagem de bordas.
# cv2.RETR_EXTERNAL captura apenas os contornos externos.
# cv2.CHAIN_APPROX_SIMPLE reduz a quantidade de pontos armazenados para cada contorno.
contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenha os contornos detectados na imagem original.
# Os contornos são desenhados em verde (cor RGB: 0, 255, 0) com espessura de linha 2.
cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 2)

# Exibe a imagem com os contornos destacados em uma janela chamada "Contornos".
cv2.imshow("Contornos", imagem)

# Aguarda até que o usuário pressione qualquer tecla para fechar as janelas.
cv2.waitKey(0)

# Fecha todas as janelas abertas.
cv2.destroyAllWindows()
