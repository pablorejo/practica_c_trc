import os
import subprocess
import matplotlib.pyplot as plt
import string

# Configurarión
S = 120 #segundos Tiempo de servicio demandado
M = 50 # Número de recursos 2gb/40mb
SEMILLA = 333
TOLERANCIA_RELATIVA = 0.002
CALIDAD = 0.95
A_0 = 15 # A para i = 0



#Nodos que se utilizan
enlaces = {'a':[0,1,10,11],
           'b':[2,7,4,9],
           'c':[3,8],
           'd':[5,6]}

nodos = [['A','B','C'],
         ['H','I','D'],
         ['G','F','E']]

# Fin configuracion




### Creamos la matriz de nodos
nodos_x_y = []
x = 0
for nod in nodos:
    y = 0
    for no in nod:
        nodos_x_y.append([x,y])
        y += 1
    x += 1


## Rutas a un salto
rutas_1_salto = []
enalce = 0
for nod_1 in nodos_x_y:
    for nod_2 in nodos_x_y:
        if nod_2 != nod_1:
            distancia = abs(nod_1[0]-nod_2[0])+abs(nod_1[1]-nod_2[1])
            if distancia == 1:
                ruta_1 = [nod_1,nod_2]  
                ruta_2 = [nod_2,nod_1]
                if ruta_1 not in rutas_1_salto and ruta_2 not in rutas_1_salto:
                    rutas_1_salto.append(ruta_1)

### Poniendo rutas a un salto en el fichero de configuración
f = open("config_"+str(0)+".cfg","w")
f.write(
    (str(M) + " ") * len(enlaces)+ "\n" +
    str(len(enlaces)) + "\n\n"+
    "#Rutas de un salto\n\n")
for ruta in rutas_1_salto:
    f.write( 
        "## Ruta de " + nodos[ruta[0][0]][ruta[0][1]] + "->" + nodos[ruta[1][0]][ruta[1][1]]  + "\n"+
        "M 8\n" +
        "M 120\n"
    )
        # str(rutas_1_salto.index(ruta)) + "\n\n"
    for i in enlaces:
        if rutas_1_salto.index(ruta) in enlaces[i]:
            f.write(
                str(rutas_1_salto.index(ruta)) + " " + i + "\n\n"

            )



## Rutas 2 saltos
rutas_2_saltos = [] ### Cuantas rutas de dos saltos tenemos nos dan 14
for nod_1 in nodos_x_y:
    for nod_2 in nodos_x_y:
        if nod_2 != nod_1:
            distancia = abs(nod_1[0]-nod_2[0])+abs(nod_1[1]-nod_2[1])
            if distancia == 2:
                ruta_1 = [nod_1,nod_2]  
                ruta_2 = [nod_2,nod_1]
                if ruta_1 not in rutas_2_saltos and ruta_2 not in rutas_2_saltos:
                    rutas_2_saltos.append(ruta_1)

tipo_E = []
tipo_F = []
tipo_G = []
tipo_H = []
tipo_I = []
tipo_J = []

rutas_escribir = [tipo_E,tipo_F,tipo_G,tipo_H,tipo_I,tipo_J]
for ruta in rutas_2_saltos:

    if ruta[0] == [1,1] or ruta[1] == [1,1]:
        rutas_escribir[4].append(ruta)


    elif (ruta[0][1] == 2 and ruta[1][1] == 2) or (ruta[0][1] == 0 and ruta[1][1] == 0):
        rutas_escribir[1].append(ruta)

    elif (ruta[0][0] == 2 and ruta[1][0] == 2) or (ruta[0][0] == 0 and ruta[1][0] == 0):
        rutas_escribir[0].append(ruta)

    elif ruta[0][1] == 1 and ruta[1][1] == 1:
        rutas_escribir[2].append(ruta)

    elif ruta[0][0] == 1 and ruta[1][0] == 1:
        rutas_escribir[3].append(ruta)


    else:
        rutas_escribir[5].append(ruta)

letras = list(string.ascii_lowercase)
i = 0
f.write("\n\n\n### Rutas de dos saltos")
for ruta in rutas_escribir:
    letra = letras[i+4]
    f.write("\n## Rutas de tipo " + letra.capitalize())
    for rut in ruta:
        f.write(
            "\n# Ruta de " + nodos[rut[0][0]][rut[0][1]] + "->" + nodos[rut[1][0]][rut[1][1]]  + "\n"+
            "M 16\n" +
            "M 120\n" + 
            letra + "\n"
        )
    i +=1

f.close()
exit(0)


