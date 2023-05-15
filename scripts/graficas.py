import matplotlib.pyplot as plt
import subprocess
import numpy as np

# tipos = ["axial", "destrogiro","exhaustivo","exhaustivo_con_reserva"]
tipos = ["axial"]
intervalos = []
probabilidades = []

def obtener_probabilidad_bloqueo(nombre_archivo,i):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    inter = []
    prob = [] 
    for linea in lineas:
        if linea.startswith("Probabilidad de bloqueo estimada:"):
            partes = linea.split(":")
            prob.append(float(partes[1].strip()))

        if linea.startswith("	Confidence interval 1:"):
            partes = linea.split("(")
            partes2 = partes[1].split(")")
            interbal = partes2[0].split(",")
            intervalo = (float(interbal[0]),float(interbal[1]))

            inter.append(intervalo)

    print(len(prob))
    return inter,prob



for tip in tipos:
    for i in range (0,5):
        inter,prob = obtener_probabilidad_bloqueo("../out/"+ tip +"/" +tip+ "_i_" +str(i)+ ".cfg.out",i)
        intervalos.append(inter)
        probabilidades.append(prob)


print(probabilidades)
print(intervalos)

