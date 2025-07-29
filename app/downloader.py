import yt_dlp
import subprocess
from app.config import DOWNLOAD_DIR, QUALITY
from app.utils import crear_directorio_si_no_existe

def buscar_video(cancion: str) -> str | None:
    resultado = subprocess.run(
        ["yt-dlp", f"ytsearch1:{cancion}", "--get-id"],
        capture_output=True, text=True
    )
    video_id = resultado.stdout.strip()
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return None

def descargar_mp3(url: str) -> None:
    crear_directorio_si_no_existe(DOWNLOAD_DIR)

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': QUALITY,
        }],
        'quiet': True,
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])
        print(f"Descargando: {url}")
        print("Descarga completada.")