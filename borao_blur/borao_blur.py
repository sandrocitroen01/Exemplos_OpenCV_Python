import cv2  # Importa a biblioteca OpenCV

# Carregar a imagem
imagem = cv2.imread("python3.png")  # Lê a imagem do arquivo
print(imagem.shape)  # Exibe as dimensões da imagem carregada

# Aplicar um filtro de desfoque (Gaussian Blur) com um kernel maior
blur = cv2.GaussianBlur(imagem, (35, 35), 0)  # Aumenta o kernel para 35x35 para mais desfoque

# Mostrar a imagem original e a borrada
cv2.imshow("Imagem", imagem)  # Exibe a imagem original
cv2.imshow("Imagem Borrada", blur)  # Exibe a imagem borrada

# Esperar o usuário pressionar uma tecla antes de fechar
cv2.waitKey(0)  # Aguarda indefinidamente até que uma tecla seja pressionada
cv2.destroyAllWindows()  # Fecha todas as janelas abertas
