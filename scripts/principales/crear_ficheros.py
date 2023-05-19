import globales

def cambiar_lineas(archivo_entrada, archivo_salida, Y):
    with open(archivo_entrada, 'r') as archivo:
        lineas = archivo.readlines()


    i = "M " + str(Y/2)
    lineas_modificadas = [linea.replace("M 4.0", i) for linea in lineas]
    i = "M " + str(Y)
    lineas_modificadas = [linea.replace("M 8.0", i) for linea in lineas]
    i2 = "M " + str(2*Y)
    lineas_modificadas = [linea.replace("M 16.0", i2) for linea in lineas_modificadas]
    i2 = "M " + str(4*Y)
    lineas_modificadas = [linea.replace("M 32.0", i2) for linea in lineas_modificadas]

    archivo.close()
    with open(archivo_salida, 'w') as archivo:
        archivo.writelines(lineas_modificadas)

    print("Archivo modificado con éxito.")
    archivo.close()
# Ejemplo de uso


# tipos = ["axial", "destrogiro","exhaustivo","exhaustivo_con_reserva"]
tipos = globales.tipos

for tip in tipos:
    archivo_entrada = globales.conf_default + tip + ".conf"  # Ruta del archivo de entrada

    i = 0
    while 1:
        archivo_salida = globales.conf + tip + "/" + tip + "_i_" + str(i) + ".cfg"  # Ruta del archivo de salida
        r = 1- 0.04*i
        Y = globales.S/(r * 15)
        cambiar_lineas(archivo_entrada, archivo_salida, Y)
        i +=1
        if i> 5:
            break
        

print("Ficheros creados")
