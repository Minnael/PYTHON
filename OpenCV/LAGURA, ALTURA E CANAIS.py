import cv2

imagem = cv2.imread("fut.jpg")

print("Hello world")
print("  ")
print('Largura em pixels:')
print(imagem.shape[1])
print('Altura em pixels:')
print(imagem.shape[0])
print('Qtde de canais:')
print(imagem.shape[2])

cv2.imshow("Nome da janela", imagem)
cv2.waitkey(0)

cv.imwrite("Saida.jpg", imagem)
