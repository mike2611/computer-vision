import cv2
import numpy as np
from PIL import Image


imagen_escalagrises = cv2.imread('originalImage.jpg', 0)
tamaño_imagen = imagen_escalagrises.shape

B = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
G = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
R = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
matrizCopia = np.zeros((tamaño_imagen[0] , tamaño_imagen[1] * 2), dtype=int)

imagen2_color = cv2.imread('originalImage.jpg', 1)

for y in range(tamaño_imagen[0]):
    for x in range(tamaño_imagen[1]):
        valor_rgb = imagen2_color[y, x]
        B[y][x]=valor_rgb[0]
        G[y][x]=valor_rgb[1]
        R[y][x]=valor_rgb[2]
        matrizCopia[y][x] = ((B[y][x] * 1 / 3) + (G[y][x] * 1 / 3) + (R[y][x] * 1 / 3))


for y in range(tamaño_imagen[0]):
    for x in range(tamaño_imagen[1]):
        valor_rgb = imagen2_color[y, x]
        B[y][x]=valor_rgb[0]
        G[y][x]=valor_rgb[1]
        R[y][x]=valor_rgb[2]
        matrizCopia[y][x + tamaño_imagen[1]] = ((B[y][x] * 1 / 3) + (G[y][x] * 1 / 3) + (R[y][x] * 1 / 3))

img = Image.fromarray((matrizCopia).astype(np.uint8))
img.save('copyImage.png')


matrizCopia = matrizCopia + matrizCopia

print("Finish")
