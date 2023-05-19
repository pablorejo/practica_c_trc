#!/bin/bash
semilla=333
calidad=0.95





if [ ! -d "conf" ]; then
    mkdir conf
    cd conf
    mkdir axial con_reserva destrogiro exhaustivo
    cd ..
fi

if [ ! -d "out" ]; then
    mkdir out
    cd out
    mkdir axial con_reserva destrogiro exhaustivo
    cd ..
fi

if [ ! -d "log" ]; then
    mkdir log
fi

if [ ! -d "img" ]; then
    mkdir img
fi

if [ ! -d "resultados" ]; then
    mkdir resultados
fi

cd scripts/otros

echo Calculando probabilidades de bloqueo teóricas
python3 calculos_prob_bloqueo.py > ../../resultados/apartado_a.txt
python3 calculos_apartado_b.py > ../../resultados/apartado_b.txt


cd ../principales

echo Creando ficheros de configuración
python3 crear_ficheros.py > ../../log/crear_ficheros.log

echo Ejecutando el simulador
time python3 ejecutar.py > ../../log/ejecutar.log

echo Creando las gráficas
python3 graficas.py  > ../../log/graficas.log


cd ../..



