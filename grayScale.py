import cv2
import numpy as np
import pandas as pd
from PIL import Image


imagen_escalagrises = cv2.imread('originalImage.jpg', 0)
tamaño_imagen = imagen_escalagrises.shape
print(tamaño_imagen)
B = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
G = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
R = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
imagenColor = np.empty((tamaño_imagen[0], tamaño_imagen[1]), dtype=object)
resultados = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)


imagen2_color = cv2.imread('originalImage.jpg', 1)
for y in range(tamaño_imagen[0]):
    for x in range(tamaño_imagen[1]):
        valor_rgb = imagen2_color[y, x]
        B[y][x]=valor_rgb[0]
        G[y][x]=valor_rgb[1]
        R[y][x]=valor_rgb[2]
        imagenColor[y][x] = str(R[y][x]) + "," + str(G[y][x]) + "," + str(B[y][x])
        resultados[y][x] = ((B[y][x] * 1/3) + (G[y][x] * 1/3) + (R[y][x] * 1/3))

img = Image.fromarray(resultados.astype(np.uint8))
img.save('imageGrayScale.png')

resultados = pd.DataFrame(resultados)
resultados.to_csv('grayScale.csv')
imagenColor = pd.DataFrame(imagenColor)
imagenColor.to_csv('RGB.csv')

print("Finalizado")



