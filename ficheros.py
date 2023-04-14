import os
import subprocess
import matplotlib.pyplot as plt

# Configurarión
S = 120 #segundos Tiempo de servicio demandado
M = 50 # Número de recursos 2gb/40mb
SEMILLA = 333
TOLERANCIA_RELATIVA = 0.002
CALIDAD = 0.95


# Vamos a definir los tipos de enlaces y el numero de traficos ofrecidos
enlaces = {2, 4, 6, 10}
# Fin configuracion




# # La tolerancia que se calculará así
# bi = 1
# t = min(1,(1-bi)/(bi)+0.002)


for i in range(0,5):

    f = open("config_"+str(i)+".cfg","w")
    f.write((str(M) + " ")*len(enlaces)+ "\n" +
            str(len(enlaces)) + "\n\n")
    j = 0
    for enl in enlaces:

        # Funcion de tiempos médios lamda
        r = (1-0.04)*i
        y = (r + 15)/S # Llegadas por segundo
        # Luego el tiempo entre llegadas es 1/y

        f.write(
            "M "+ str(1/y) + "\n" +
            "M "+ str(S)+"\n" +
            str(j) + "\n\n" 
        ) 
        j += 1
    i +=1
    f.close()

    ## Para ejecutar o fichero 
    # os.system("./SimRedMMkk -s " + str(SEMILLA) + " -q " + str(CALIDAD) + " -t " + str(TOLERANCIA_RELATIVA) "config_" + str(i) + ".cfg -c")

# os.system("rm *.cfg")

puntos_x = []
puntos_y = []
for i in range(0,5):
    puntos_x.append(i)
    r = (1-0.04)*i
    A = r*7.5 # Llegadas por segundo
    

    output = subprocess.check_output("./Erlang.tcl 50 "+str(A), shell=True)
    output_str = output.decode('utf-8')
    valor = [(float(num)) for num in output_str.split()][0]
    puntos_y.append(valor)
    print(puntos_y)

# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar puntos
ax.scatter(x = puntos_x, y = puntos_y)
# Guardar el gráfico en formato png
plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico

plt.yscale('log')
           
plt.show()