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


cd scripts/principales

python3 crear_ficheros.py > ../../log/crear_ficheros.log
python3 ejecutar.py > ../../log/ejecutar.log
python3 graficas.py > ../../log/graficas.log

cd ../..



