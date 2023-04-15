import os
import subprocess
import matplotlib.pyplot as plt

# Configurarión
S = 120 #segundos Tiempo de servicio demandado
M = 50 # Número de recursos 2gb/40mb
SEMILLA = 333
TOLERANCIA_RELATIVA = 0.002
CALIDAD = 0.95
A_0 = 15 # A para i = 0



#Nodos que se utilizan
enlaces = [
         [[0],[1]],
        [[2],[3],4],
         [6,6],
        [7,8,9],
        [10,11]
        ]

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


f = open("config_"+str(0)+".cfg","w")
f.write(
    (str(M) + " ") * len(enlaces)+ "\n" +
    str(len(enlaces)) + "\n\n"+
    "#Rutas de un salto\n")

for ruta in rutas_2_saltos:
    f.write(
        "M 16\n" +
        "M 120\n"
    )














## Poner las rutas a un salto
j = 0
i = 0
for enl in enlaces:
    # Funcion de tiempos médios lamda
    for ln in enl:
        r = 1-0.04*i
        y = (r*A_0)/S # Llegadas por segundo
        # Luego el tiempo entre llegadas es 1/y
        f.write(
            "M "+ str(1/y) + "\n" +
            "M "+ str(S)+"\n" +
            str(j) + "\n\n" 
        ) 
        j += 1

while True:
    y = 0
    for nod in nodos:
        x = 0
        for no in nod:
            
            x += 1
            no.index
        y += 1
    break

exit(0)
# # La tolerancia que se calculará así
# bi = 1
# t = min(1,(1-bi)/(bi)+0.002)
Bmin = 0
t = TOLERANCIA_RELATIVA
for i in range(0,5):

    f = open("config_"+str(i)+".cfg","w")
    f.write((str(M) + " ")*len(enlaces)+ "\n" +
            str(len(enlaces)) + "\n\n")
    j = 0
    for enl in enlaces:

        # Funcion de tiempos médios lamda
        r = 1-0.04*i
        y = (r + 15)/S # Llegadas por segundo
        # Luego el tiempo entre llegadas es 1/y

        f.write(
            "M "+ str(2/y) + "\n" +
            "M "+ str(S)+"\n" +
            str(j) + "\n\n" 
        ) 
        j += 1

    
    i +=1

    # if (i != 0):
    #     t = min(1,((1-Bmin)*TOLERANCIA_RELATIVA)/Bmin)

    # f.close()

    # os.system("./SimRedMMkk -s " + str(SEMILLA) + " -q " + str(CALIDAD) + " -t " + str(TOLERANCIA_RELATIVA) + " config_" + str(i) + ".cfg -c")


        
puntos_x = []
puntos_y = []
for i in range(0,6):
    puntos_x.append(i)
    ri = 1-(0.04)*i
    A = ri*A_0*2 # Llegadas por segundo
    

    output = subprocess.check_output("./Erlang.tcl "+str(M)+" "+str(A), shell=True)
    output_str = output.decode('utf-8')
    valor = [(float(num)) for num in output_str.split()][0]
    puntos_y.append(valor)

# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar puntos
ax.scatter(x = puntos_x, y = puntos_y)
# Guardar el gráfico en formato png
plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico

plt.yscale('log')
plt.ylabel('Probabilidad de bloqueo')
plt.xlabel('Valor de i')
plt.show()