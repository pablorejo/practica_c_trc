import matplotlib.pyplot as plt
import subprocess

def obtener_probabilidad_bloqueo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    probabilidades = []
    intervalos = []
    for linea in lineas:
        if linea.startswith("Probabilidad de bloqueo estimada:"):
            partes = linea.split(":")
            probabilidades.append(float(partes[1].strip()))

        if linea.startswith("	Confidence interval 1:"):
            partes = linea.split("(")
            partes2 = partes[1].split(")")

            interbal = partes2[0].split(",")
            intervalo = (float(interbal[0]),float(interbal[1]))

            intervalos.append(intervalo)

    return None

obtener_probabilidad_bloqueo("../out/axial/axial_i_4.cfg.out")



# # Datos de ejemplo
# probabilidades = [0.00346355, 0.00287234, 0.00409123]
# confidence_intervals = [(0.00344266, 0.00348443), (0.00286212, 0.00288256), (0.00407892, 0.00410354)]
# probabilidades2 = [0.00346355, 0.00287234, 0.00409123]
# confidence_intervals2 = [(0.00344266, 0.00348443), (0.00286212, 0.00288256), (0.00407892, 0.00410354)]

# # Configuración del gráfico
# fig, ax = plt.subplots()
# ax.set_title('Probabilidad Estimada de Bloqueo')
# ax.set_ylabel('Probabilidad')

# # Crear una lista de valores para cada caja del boxplot
# boxplot_data = [[ci[0], p, ci[1]] for p, ci in zip(probabilidades, confidence_intervals)]

# # Dibujar el boxplot
# bp = ax.boxplot(boxplot_data, positions=[0.8, 1.8, 2.8], widths=0.4, patch_artist=True, medianprops={'color': 'red'})

# # Configurar colores de las cajas
# colors = ['lightblue', 'lightgreen', 'lightyellow']
# for patch, color in zip(bp['boxes'], colors):
#     patch.set_facecolor(color)

# # Crear una lista de valores para cada caja del boxplot
# boxplot_data2 = [[ci[0], p, ci[1]] for p, ci in zip(probabilidades2, confidence_intervals2)]

# # Dibujar el boxplot
# bp2 = ax.boxplot(boxplot_data2, positions=[1.2, 2.2, 3.2], widths=0.4, patch_artist=True, medianprops={'color': 'red'})

# # # Configurar colores de las cajas
# # colors2 = ['lightpink', 'lightorange', 'lightcyan']
# # for patch, color in zip(bp2['boxes'], colors2):
# #     patch.set_facecolor(color)

# # Etiquetas de los ejes
# ax.set_xlabel('Intervalo de Confianza')
# # ax.set_xticklabels(['', '1', '2', '3', ''])

# # Mostrar el gráfico
# plt.show()
