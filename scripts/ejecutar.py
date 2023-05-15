import subprocess
# Configurarión
S = 120 #segundos Tiempo de servicio demandado
M = 50 # Número de recursos 2gb/40mb
SEMILLA = 333
TOLERANCIA_RELATIVA = 0.002
CALIDAD = 0.95
A_0 = 15 # A para i = 0


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



tolerancia = TOLERANCIA_RELATIVA
for i in range(0, 5):   
    print("Tolerancia = " + str(tolerancia))
    
    subprocess.run(["../SimRedMMkk","-s"+str(S),"-q" + str(CALIDAD),"-t" + str(tolerancia),"-c","../conf/axial/axial_i_"+str(i)+".cfg"], capture_output=False)

    subprocess.run(["mv","../conf/axial/axial_i_"+str(i)+".cfg.out", "../out/axial/"], capture_output=False)

    Pb = obtener_probabilidad_bloqueo("../out/axial/axial_i_"+str(i)+".cfg.out")

    tolerancia = min(1,(1-Pb)*TOLERANCIA_RELATIVA/Pb)
    print("Pb max = " + str(Pb))

