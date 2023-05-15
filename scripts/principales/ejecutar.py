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
for i in range(0, 5):   
    print("Tolerancia = " + str(tolerancia))
    
    subprocess.run(["../SimRedMMkk","-s"+str(S),"-q" + str(globales.CALIDAD),"-t" + str(tolerancia),"-c","../conf/axial/axial_i_"+str(i)+".cfg"], capture_output=True)

    subprocess.run(["mv","../conf/axial/axial_i_"+str(i)+".cfg.out", "../out/axial/"], capture_output=True)

    Pb = obtener_probabilidad_bloqueo("../out/axial/axial_i_"+str(i)+".cfg.out")

    tolerancia = min(1,(1-Pb)*globales.TOLERANCIA_RELATIVA/Pb)
    print("Pb max = " + str(Pb))

