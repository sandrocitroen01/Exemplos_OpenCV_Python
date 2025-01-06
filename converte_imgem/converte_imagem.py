import cv2
# Carregar uma imagem
imagem = cv2.imread("python2.png")
print(imagem.shape)

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
print(imagem_cinza.shape)

# Mostrar as imagens
cv2.imshow("Imagem", imagem)
cv2.imshow("Imagem em Cinza", imagem_cinza)

# Esperar o usuário pressionar uma tecla antes de fechar
cv2.waitKey(0)
cv2.destroyAllWindows()
