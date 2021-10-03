import cv2
import numpy as np
import pandas as pd
from PIL import Image

imagen_escalagrises = cv2.imread('char.jpg', 0)
tamaño_imagen = imagen_escalagrises.shape
print(tamaño_imagen)
B = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
G = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
R = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
matrizGrises = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
matrizGrisesShifting = np.zeros((tamaño_imagen[0], tamaño_imagen[1]), dtype=int)
imagen2_color = cv2.imread('char.jpg', 1)


valor = -1
while valor < 1 or valor > 3:
    print("Input 1 for shifting horizontal , 2 vertical and 3 diagonal : ")
    valor = input()
    if valor.isalpha():
        valor = -1
    valor = float(valor)


#Creacion de la matrizGrises sin modficar
for y in range(tamaño_imagen[0]):
    for x in range(tamaño_imagen[1]):
        valor_rgb = imagen2_color[y, x]
        B[y][x] = valor_rgb[0]
        G[y][x] = valor_rgb[1]
        R[y][x] = valor_rgb[2]
        matrizGrises[y][x] = ((B[y][x] * 1 / 3) + (G[y][x] * 1 / 3) + (R[y][x] * 1 / 3))

#Shifting Horizontal
if valor == 1:
    for x in range(tamaño_imagen[1]):
        matrizGrisesShifting[0][x] = matrizGrises[0][x]

    for y in range(tamaño_imagen[0]):
        for x in range(tamaño_imagen[1]):
            if matrizGrises[y][x] != 0:
                print(str( matrizGrises[0][x]) + "*" + str(matrizGrises[0][x]) + "/" + str(matrizGrises[y][x]))
                matrizGrisesShifting[y][x] = matrizGrises[0][x] * (matrizGrises[0][x] / matrizGrises[y][x])
            else:
                matrizGrisesShifting[y][x] = matrizGrises[y][x]

#Shifting Vertical
if valor == 2:
    for x in range(tamaño_imagen[1]):
        matrizGrisesShifting[0][x] = matrizGrises[0][x]

    for y in range(tamaño_imagen[0]):
        for x in range(tamaño_imagen[1]):
            if matrizGrises[y][x] != 0:
                print(str( matrizGrises[y][0]) + "*" + str(matrizGrises[y][0]) + "/" + str(matrizGrises[y][x]))
                matrizGrisesShifting[y][x] = matrizGrises[y][0] * (matrizGrises[y][0] / matrizGrises[y][x])
            else:
                matrizGrisesShifting[y][x] = matrizGrises[y][x]


for y in range(tamaño_imagen[0]):
    for x in range(tamaño_imagen[1]):
        if matrizGrisesShifting[y][x] > 250:
            matrizGrisesShifting[y][x] = 250


img = Image.fromarray(matrizGrisesShifting.astype(np.uint8))
img.save('shifting.png')


matrizGrisesModificada = pd.DataFrame(matrizGrisesShifting)
matrizGrisesModificada.to_csv('grayScaleShifting.csv')
print("Finish")