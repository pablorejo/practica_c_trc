import subprocess

import globales

def obtener_probabilidad_bloqueo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    pro = 0
    for linea in lineas:
        if linea.startswith("Probabilidad de bloqueo estimada:"):
            partes = linea.split(":")
            if pro < float(partes[1].strip()):
                pro = float(partes[1].strip())
            return pro

    return None



tolerancia = globales.TOLERANCIA_RELATIVA
for tip in globales.tipos:
    for i in range(0, 5):   
        print("Tolerancia = " + str(tolerancia))
        
        fichero_conf = globales.conf  + tip + "/" + tip +"_i_"+ str(i)+".cfg"
        print(fichero_conf)


        subprocess.run([globales.SimRedMMkk,"-s" + str(globales.S),"-q" + str(globales.CALIDAD),"-t" + str(tolerancia),"-c",fichero_conf], capture_output=True)
        print(fichero_conf)          

        subprocess.run(["mv",globales.conf  + tip + "/" + tip + "_i_" + str(i)+".cfg.out",   globales.out + "/" + tip + "/"], capture_output=True)

        print(globales.out  + tip + "/" + tip + "_i_" + str(i)+".cfg.out")
        Pb = obtener_probabilidad_bloqueo(globales.out  + tip + "/" + tip + "_i_" + str(i)+".cfg.out")
        tolerancia = min(1,(1-Pb)*globales.TOLERANCIA_RELATIVA/Pb)
        print("Pb max = " + str(Pb))

