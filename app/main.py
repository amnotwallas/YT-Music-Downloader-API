from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models import CancionesRequest
from app.downloader import buscar_video, descargar_mp3
from app.config import DOWNLOAD_DIR
import os

app = FastAPI(title="YT Music Downloader API")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar * por ["http://localhost"] si quieres limitarlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
This endpoint allows users to download multiple songs by providing a list of song titles or identifiers.
It searches for each song on YouTube, downloads the audio as MP3, and returns the download status for each song.
"""
@app.post("/descargar")
# This endpoint handles the downloading of multiple songs
# It accepts a request containing a list of song titles or identifiers
def descargar_canciones(request: CancionesRequest):
    resultados = []
    for cancion in request.canciones:
        # For each song, search for the video and download it
        # If the video is found, it will be downloaded as MP3
        # If an error occurs, it will be caught and the error message will be returned
        try:
            url = buscar_video(cancion)
            if not url:
                raise Exception("No se encontró video")
            # Download the MP3 file from the video URL
            descargar_mp3(url)
            resultados.append({"nombre": cancion, "url": url, "estado": "descargado"})
        except Exception as e:
            resultados.append({"nombre": cancion, "url": None, "estado": f"error: {e}"})
    return {"resultados": resultados}
"""
This endpoint allows users to download a specific MP3 file by its name.
It checks if the file exists in the download directory and returns it if found, otherwise returns an error message.

 @Param nombre_archivo: The name of the MP3 file to download

  @Return: The MP3 file if it exists, or an error message if it does not
"""
@app.get("/descargas/{nombre_archivo}")
def obtener_mp3(nombre_archivo: str):
    ruta = os.path.join(DOWNLOAD_DIR, nombre_archivo)
    if os.path.exists(ruta):
        return FileResponse(path=ruta, filename=nombre_archivo, media_type='audio/mpeg')
    return {"error": "Archivo no encontrado"}

'''
    This endpoint lists all downloaded MP3 files in the download directory. 

    @Return: A list of MP3 files in the download directory, or an error message if there is an issue
'''
@app.get("/descargas")
def listar_descargas():
    try:
        # List all MP3 files in the download directory
        archivos = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".mp3")]
        return {"archivos": archivos}
    except Exception as e:
        return {"error": str(e)}

"""
    This endpoint allows users to delete a specific MP3 file by its name.
    
    @Param nombre_archivo: The name of the MP3 file to delete

    @Return: A success message if the file was deleted, or an error message if it does not exist
"""
@app.delete("/descargas/{nombre_archivo}")
def borrar_archivo(nombre_archivo: str):
    ruta = os.path.join(DOWNLOAD_DIR, nombre_archivo)
    if os.path.exists(ruta):
        os.remove(ruta)
        # Return a success message if the file was deleted
        return {"mensaje": f"'{nombre_archivo}' fue eliminado correctamente."}
    # If the file does not exist, raise an HTTP exception with a 404 status code
    raise HTTPException(status_code=404, detail="Archivo no encontrado")

"""
    This endpoint allows users to delete all downloaded MP3 files.
    It iterates through the download directory and removes all files with the .mp3 extension.

    @Return: A success message with a list of deleted files, or an error message if there are no files to delete
"""
@app.delete("/descargas")
def borrar_todos_los_archivos():
    
    archivos_eliminados = []
    for archivo in os.listdir(DOWNLOAD_DIR):
        if archivo.endswith(".mp3"):
            # Remove the file and add it to the list of deleted files
            os.remove(os.path.join(DOWNLOAD_DIR, archivo))
            archivos_eliminados.append(archivo)
    return {"mensaje": "Se eliminaron los archivos", "archivos": archivos_eliminados}