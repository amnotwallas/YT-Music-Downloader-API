import os

def crear_directorio_si_no_existe(ruta: str):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Directorio creado: {ruta}")
    else:
        print(f"El directorio ya existe: {ruta}")   