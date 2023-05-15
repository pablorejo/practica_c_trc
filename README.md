# Practia c
## Encaminamiento axial
### 2 SALTOS
Para dos saltos vamos a tener 3 tipos distintos de rutas
1. Las rutas con origen A,C,E,G serán equivalentes 
2. Las rutas con origen H y D serán equivalentes
3. Las rutas con origen B y F serán equivalentes

Sin enbargo tendremos 4 tipos distintos de enlaces 
1. Tipo 1: 2 tráficos uno para cada sentido
2. Tipo 2: 4 tráficos dos por cada sentido
3. Tipo 3: 6 tráficos 3 por cada sentido
4. Tipo 4: 10 tráficos 5 por cada sentido

# Ejecución
Para ejecutar la configuracion simplemente usar el comando
```bash
python3 ficheros.py
```

## parametros
En caso de querer cambiar algunos parámetros:
1. Entrar en el `ficheros.py`
2. Editar las primeras lineas que convengan

## Un solo salto
Si hablamos de un solo salto tendremos que se cumple siempre que:
- m = 50
- A = 7.5*ri

Por lo tanto la probabilidad de bloqueo en  ese enlace será de E(50,A)

## Fichero de configuración 
M 1/lambda
M S


### Para ejecutarlo 
`IMPORTANTE`: Necesitas [instalar matplotlib]
```bash
python3 ficheros.py
```

#### Instalar matplotlib
1. 
```bash
sudo apt install python3-pip
```
2. 
```bash
pip install matplotlib
```