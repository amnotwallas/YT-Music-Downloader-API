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

@app.post("/descargar")
def descargar_canciones(request: CancionesRequest):
    resultados = []
    for cancion in request.canciones:
        try:
            url = buscar_video(cancion)
            if not url:
                raise Exception("No se encontró video")
            descargar_mp3(url)
            resultados.append({"nombre": cancion, "url": url, "estado": "descargado"})
        except Exception as e:
            resultados.append({"nombre": cancion, "url": None, "estado": f"error: {e}"})
    return {"resultados": resultados}

@app.get("/descargas/{nombre_archivo}")
def obtener_mp3(nombre_archivo: str):
    ruta = os.path.join(DOWNLOAD_DIR, nombre_archivo)
    if os.path.exists(ruta):
        return FileResponse(path=ruta, filename=nombre_archivo, media_type='audio/mpeg')
    return {"error": "Archivo no encontrado"}

@app.get("/descargas")
def listar_descargas():
    try:
        archivos = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".mp3")]
        return {"archivos": archivos}
    except Exception as e:
        return {"error": str(e)}

@app.delete("/descargas/{nombre_archivo}")
def borrar_archivo(nombre_archivo: str):
    ruta = os.path.join(DOWNLOAD_DIR, nombre_archivo)
    if os.path.exists(ruta):
        os.remove(ruta)
        return {"mensaje": f"'{nombre_archivo}' fue eliminado correctamente."}
    raise HTTPException(status_code=404, detail="Archivo no encontrado")

@app.delete("/descargas")
def borrar_todos_los_archivos():
    archivos_eliminados = []
    for archivo in os.listdir(DOWNLOAD_DIR):
        if archivo.endswith(".mp3"):
            os.remove(os.path.join(DOWNLOAD_DIR, archivo))
            archivos_eliminados.append(archivo)
    return {"mensaje": "Se eliminaron los archivos", "archivos": archivos_eliminados}