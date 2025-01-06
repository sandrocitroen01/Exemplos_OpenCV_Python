import cv2
# Carregar uma imagem
imagem = cv2.imread("python.jpg")  
print(imagem.shape)

# Mostrar a imagem em uma janela
cv2.imshow("Janela de Imagem", imagem)

# Esperar o usuário pressionar uma tecla antes de fechar
cv2.waitKey(0)
cv2.destroyAllWindows()
