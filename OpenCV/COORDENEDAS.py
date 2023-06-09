import cv2   # "Biblioteca OPENCV adicionada"

imagem = cv2.imread('ezio.jpg')  # "Seleciona/Ler imagem"
for y in range(0, imagem.shape[0], 20):  # "Varer altura" && "Percorre altura"

   for x in range(0, imagem.shape[1], 20): # "Varer largura" && "Percorre colunas"

    imagem[y : y + 10, x : x + 10] = (0, 255, 255) # "Cores da tupla (RGB)"

cv2.imshow("imagem modificada", imagem)  # "Mostra imagem"
cv2.waitKey(0)
