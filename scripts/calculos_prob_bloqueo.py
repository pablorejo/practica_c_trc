import numpy as np
import subprocess


i = 6
m = 50
num_traficos_distintos_1_salto = 4
num_traficos_distintos_2_salto = 6
B_1_salto = np.empty([num_traficos_distintos_1_salto, i], dtype = float)
B_2_salto = np.empty([num_traficos_distintos_2_salto, i], dtype = float)
A_lista = np.empty([i, num_traficos_distintos_1_salto], dtype = float)
r = np.empty([i], dtype = float)
peticiones_segundo = np.empty([i], dtype = float)


#Cálculos 1 salto

for n in range(i):
    r[n] = 1 - 0.04*n
    peticiones_segundo[n] = 15*r[n]
    for trafico in range(num_traficos_distintos_1_salto):
        x = 2
        if(trafico == num_traficos_distintos_1_salto -1):
            x = 3
        A = (x + trafico)*peticiones_segundo[n]
        A_lista[n][trafico] = A
        resultado = subprocess.run(["./Erlang.tcl",str(m), str(A)], capture_output=True, text=True)
        B = resultado.stdout.split()[0]
        B_1_salto[trafico][n] = B

#Cálculos 2 saltos

for n in range(i):
    B_2_salto[0][n] = 1 - ((1 - B_1_salto[1][n])*(1 - B_1_salto[3][n]))
    B_2_salto[1][n] = 1 - ((1 - B_1_salto[0][n])*(1 - B_1_salto[0][n]))
    B_2_salto[2][n] = 1 - ((1 - B_1_salto[1][n])*(1 - B_1_salto[1][n]))
    B_2_salto[3][n] = 1 - ((1 - B_1_salto[3][n])*(1 - B_1_salto[3][n]))
    B_2_salto[4][n] = 1 - ((1 - B_1_salto[2][n])*(1 - B_1_salto[2][n]))
    B_2_salto[5][n] = 1 - ((1 - B_1_salto[2][n])*(1 - B_1_salto[3][n]))

print("\nValores de r \n")
print(r)
print("\n")
print("Valores de lambda sin dividir por S\n")
print(peticiones_segundo)
print("\n")
print("Valores de A \n")
print(A_lista)
print("\n")
print("valores de B un salto\n")
print(B_1_salto)
print("\nValores de B dos saltos\n")
print(B_2_salto)