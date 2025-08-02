import os
# This utility function checks if a directory exists and creates it if it does not
# It is useful for ensuring that the download directory is ready before saving files
def crear_directorio_si_no_existe(ruta: str):
    # Check if the directory exists
    # If it does not, create it
    # Print a message indicating whether the directory was created or already exists
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Directorio creado: {ruta}")
    else:
        print(f"El directorio ya existe: {ruta}")   