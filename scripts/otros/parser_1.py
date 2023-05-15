



f = open("prueba.cfg.out","r")

while True:
    lines =  f.readlines()
    if "Trafico/s promediado/s en" in lines:
        tipo_trafico = lines[-2:]
