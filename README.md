
YT Music Downloader API 🎵
===========================

Una API REST creada con FastAPI que permite buscar canciones en YouTube, descargar sus audios en formato MP3 y acceder a ellos desde un navegador o aplicación. Ideal para automatizar conversiones de video a audio.

---

📦 Requisitos
-------------

- Python 3.8 o superior
- yt-dlp (descarga de YouTube)
- FastAPI (API framework)
- ffmpeg (para convertir a mp3)
- Uvicorn (servidor ASGI)

---

🔧 Instalación de dependencias
------------------------------

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/yt-music-api.git
cd yt-music-api
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

🎧 Instalación de FFMPEG
------------------------

yt-dlp usa ffmpeg para convertir audio a formato `.mp3`. Asegúrate de instalarlo antes de usar la API.

### ▶️ Windows

1. Descargar desde: https://ffmpeg.org/download.html  
2. Elegir una versión precompilada (por ejemplo: gyan.dev)
3. Extraer en `C:\ffmpeg`
4. Agrega `C:\ffmpeg\bin` al PATH del sistema

### 🍎 macOS

```bash
brew install ffmpeg
```

### 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg
```

Verifica la instalación con:

```bash
ffmpeg -version
```

---

🧱 Arquitectura del sistema
---------------------------

- **FastAPI**: Framework para construir APIs modernas con documentación automática.
- **yt-dlp**: Herramienta para buscar videos en YouTube.
- **ffmpeg**: Conversión de video a audio (`.mp3`).
- **app/**: Lógica de negocio organizada por módulos.
- **downloads/**: Carpeta donde se guardan los archivos descargados.

---

📄 Documentación de la API
--------------------------

La API expone endpoints documentados automáticamente con Swagger en:

➡️ [http://localhost:8000/docs](http://localhost:8000/docs)

### Ejemplo JSON de entrada:

```json
POST /descargar
{
  "canciones": ["Adele - Hello", "Coldplay - Yellow"]
}
```

---

📡 Endpoints disponibles
------------------------

| Método  | Ruta                              | Descripción                                              |
|---------|-----------------------------------|----------------------------------------------------------|
| POST    | `/descargar`                      | Recibe una lista de canciones y descarga los MP3         |
| GET     | `/descargas`                      | Devuelve una lista de canciones descargadas              |
| GET     | `/descargas/{nombre_archivo}`     | Descarga un archivo MP3 específico por nombre            |
| DELETE  | `/descargas/{nombre_archivo}`     | Elimina un archivo MP3 por nombre                        |
| DELETE  | `/descargas`                      | Elimina **todos** los archivos MP3 descargados           |

---

📂 Estructura del proyecto
---------------------------

```
yt_music_api/
├── app/
│   ├── main.py            ← Endpoints principales
│   ├── downloader.py      ← Lógica de búsqueda y descarga
│   ├── models.py          ← Esquemas de entrada (Pydantic)
│   ├── config.py          ← Configuración del sistema
│   └── utils.py           ← Funciones auxiliares
├── downloads/             ← Carpeta con archivos .mp3 descargados
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

🛡 Recomendaciones para producción
----------------------------------

- Añadir autenticación (token, API key)
- Establecer límites de tamaño y frecuencia de descargas
- Crear tareas asíncronas para descargas grandes (con Celery o BackgroundTasks)
- Programar eliminación automática de archivos viejos

---

📄 Licencia
-----------
MIT
