import cv2
# Carregar a imagem
imagem = cv2.imread("python.jpg")
print(imagem.shape)

# Detectar bordas usando o algoritmo Canny
bordas = cv2.Canny(imagem, 50, 150)

# Exibir a imagem original
cv2.imshow("imagem", imagem)

# Exibir a imagem com as bordas detectadas
cv2.imshow("Bordas Detectadas", bordas)

# Esperar o usuário pressionar uma tecla e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
