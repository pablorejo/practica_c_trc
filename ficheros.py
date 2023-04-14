import os
S = 120 #segundos Tiempo de servicio demandado
M = 50 # Número de recursos 2gb/40mb
SEMILLA = 333
TOLERANCIA_RELATIVA = 0.01
CALIDAD = 0.95




# Vamos a definir los tipos de enlaces y el numero de traficos ofrecidos
enlaces = {2, 4, 6, 10}





# # La tolerancia que se calculará así
# bi = 1
# t = min(1,(1-bi)/(bi)+0.002)


i = 0
f = open("config.cfg","w")
f.write((str(M) + " ")*len(enlaces)+ "\n" +
        str(len(enlaces)) + "\n\n")
for enl in enlaces:

    # Funcion de tiempos médios lamda
    r = (1-0.04)*i
    i +=1
    y = (r + 15)/S # Llegadas por segundo
    # Luego el tiempo entre llegadas es 1/y

    f.write(
        "M "+ str(1/y) + "\n" +
        "M "+ str(S)+"\n" +
        str(i-1) + "\n\n" 
    ) 

f.close()

## Para ejecutar o fichero
os.system("./SimRedMMkk -s " + str(SEMILLA) + " -q " + str(CALIDAD) + " -t " + str(TOLERANCIA_RELATIVA) + " config.cfg")

# os.system("rm *.cfg")
