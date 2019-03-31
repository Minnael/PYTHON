import cv2

imagem = cv2.imread("fut.jpg")
vermelho = (0, 0, 255)
branco = (255, 255, 255)
preto =  (0, 0, 0)
verde =  (0, 255, 0)
azul =  (255, 0, 0)
ciano = (255, 255, 0)
amarelo = (0, 255, 255)

# de cima para baixo/de trás para frente
imagem [30:50, :] = (azul)
imagem [100:150, 50:100] = (vermelho)
imagem [:, 200:220] = (verde)
imagem [150:300, 250:350] = (amarelo)
imagem [300:400, 50:150] = (ciano)
imagem [250:350, 300:450] = (branco)
imagem [400:500, 500:900] = (preto)

cv2.imshow("Fut", imagem)


