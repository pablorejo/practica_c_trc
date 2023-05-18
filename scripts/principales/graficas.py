import matplotlib.pyplot as plt
import string
import numpy as np

import globales

tipos = globales.tipos


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

    return inter,prob


matriz_intervalos = []
matriz_probabilidades = []
for tip in tipos:
    intervalos = []
    probabilidades = [] 
    for i in range (0,6):
        if(tip != "con_reserva"):
            inter,prob = obtener_probabilidad_bloqueo(globales.out+ tip +"/" +tip+ "_i_" +str(i)+ ".cfg.out",i)
        else:
            inter,prob = obtener_probabilidad_bloqueo(globales.out+ tip +"/" +tip+ "_i_" +str(i)+ ".cfg.4k.out",i)
        intervalos.append(inter)
        probabilidades.append(prob)
    matriz_intervalos.append(intervalos)
    matriz_probabilidades.append(probabilidades)


# Tenemos que trasponer las matrizes para que se ponga bien


matriz_interval = []
for i in matriz_intervalos:
    matriz_transpuesta = [list(columna) for columna in zip(*i)]
    matriz_interval.append(matriz_transpuesta)

# Aqui guardamos las probabilidades de 
matriz_probab = []
for i in matriz_probabilidades:
    matriz_transpuesta = [list(columna) for columna in zip(*i)]
    matriz_probab.append(matriz_transpuesta)




indice = 0
# Para crear varias graficas para los distintos apartados axial, destrogiro
abecedario = list(string.ascii_lowercase)
for tip in tipos:
    # Crear un arreglo para los índices de las barras
    plt.figure(figsize=(10, 6))
    x = np.arange(len(matriz_probab[indice][0]))

    print("\n\nTipo " + tip + ": ")
    # Para poner en la misma gráfica los procesos
    for j in range(len(matriz_probab[indice])):
        
        # Crear la gráfica de barras
        r = 1- 0.04*j
        Y = 120/(r * 15)
        plt.plot(x, matriz_probab[indice][j], label="Trafico = " + str(abecedario[j]))
        
        print(" Trafico = " + str(abecedario[j]))
        print(matriz_probab[indice])
        # Agregar los intervalos de confianza como líneas de error
        for i, intervalo in enumerate(matriz_interval[indice][j]):
            plt.plot([x[i], x[i]], intervalo)
            
        # Obtener los valores del eje y
        valores_y = matriz_probab[indice][j]
        
        # # Imprimir los valores del eje y
        # for i, valor in enumerate(valores_y):
        #     plt.text(x[i], valor, str(valor), ha='center', va='bottom')



    # plt.ylim(0, max(valores_y) * 2)  # Aumenta
    # Configuración de la gráfica
    plt.xlabel('Índice')
    plt.ylabel('Probabilidad')
    plt.title('Probabilidades del trafico de tipo ' + str(tip))
    plt.legend(loc='upper right')
    # Mostrar la gráfica
    indice += 1
    plt.savefig(globales.image + tip)
plt.show()  


