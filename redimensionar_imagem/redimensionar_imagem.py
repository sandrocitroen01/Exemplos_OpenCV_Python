import cv2  # Importa a biblioteca OpenCV para manipulação de imagens e vídeos

# Carregar uma imagem
imagem = cv2.imread("python3.png")  # Lê a imagem "python3.png" e a carrega como uma matriz
print(imagem.shape)  # Exibe as dimensões da imagem carregada

# Redimensionar a imagem para 200x200 pixels
imagem_redimensionada = cv2.resize(imagem, (200, 200))  # Redimensiona a imagem
print(imagem_redimensionada.shape)  # Exibe as novas dimensões da imagem

# Exibir a imagem original e a redimensionada
cv2.imshow("Imagem", imagem)  # Exibe a imagem original
cv2.imshow("Imagem Redimensionada", imagem_redimensionada)  # Exibe a imagem redimensionada

# Esperar o usuário pressionar uma tecla antes de fechar
cv2.waitKey(0)  # Aguarda indefinidamente até que uma tecla seja pressionada
cv2.destroyAllWindows()  # Fecha todas as janelas abertas do OpenCV
