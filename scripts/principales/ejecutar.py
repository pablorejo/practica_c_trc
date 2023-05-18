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
    archivo.close()
    return pro

print(len(globales.tipos))

for tip in globales.tipos:
    print(tip)
    tolerancia = globales.TOLERANCIA_RELATIVA
    for i in range(0, 6):   
        print("Tolerancia = " + str(tolerancia))
        
        fichero_conf = globales.conf  + tip + "/" + tip +"_i_"+ str(i)+".cfg"
        print(fichero_conf)

        if(str(tip) != "con_reserva"):
            txt = subprocess.run([globales.SimRedMMkk,"-s" + str(globales.SEMILLA),"-q" + str(globales.CALIDAD),"-t" + str(tolerancia),"-c",fichero_conf], capture_output=True)
            print(fichero_conf) 
            txt =  subprocess.run(["mv",globales.conf  + tip + "/" + tip + "_i_" + str(i)+".cfg.out",   globales.out + "/" + tip + "/"], capture_output=True)
            print(globales.out  + tip + "/" + tip + "_i_" + str(i)+".cfg.out")
            Pb = obtener_probabilidad_bloqueo(globales.out  + tip + "/" + tip + "_i_" + str(i)+".cfg.out")
        else:
            txt =  subprocess.run([globales.SimRedMMkk,"-s" + str(globales.SEMILLA),"-q" + str(globales.CALIDAD),"-t" + str(tolerancia),"-n" + str(globales.CIRCUITOS_RESERVADOS),"-c",fichero_conf], capture_output=True)
            print(fichero_conf) 
            txt =  subprocess.run(["mv",globales.conf  + tip + "/" + tip + "_i_" + str(i)+".cfg.4k.out",   globales.out + "/" + tip + "/"], capture_output=True)
            print(globales.out  + tip + "/" + tip + "_i_" + str(i)+".cfg.4k.out")
            Pb = obtener_probabilidad_bloqueo(globales.out  + tip + "/" + tip + "_i_" + str(i)+".cfg.4k.out")
        
        tolerancia = min(1,(1-Pb)*globales.TOLERANCIA_RELATIVA/Pb)
        print("Pb max = " + str(Pb))
        
