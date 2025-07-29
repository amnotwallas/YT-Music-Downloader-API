
# 🎵 YT Music Downloader API

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Licencia](https://img.shields.io/badge/licencia-MIT-green)

API REST construida con **FastAPI** que permite buscar canciones por nombre en YouTube, descargar su audio en formato `.mp3` con ayuda de `yt-dlp` y `ffmpeg`, y servir los archivos mediante endpoints web.

---

## 📦 Requisitos

- Python 3.8 o superior
- FastAPI
- yt-dlp
- ffmpeg (requerido para conversión a MP3)
- Uvicorn

---

## ⚙️ Instalación de dependencias

1. Clona este repositorio:

```bash
git clone https://github.com/amnotwallas/YT-Music-Downloader-API.git
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

## 🎧 Instalación de FFMPEG

### Windows

1. Descargar desde: <https://ffmpeg.org/download.html>  
2. Extraer en `C:\ffmpeg`
3. Agrega `C:\ffmpeg\bin` al `PATH` del sistema

### macOS

```bash
brew install ffmpeg
```

### Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

Verifica con:

```bash
ffmpeg -version
```

---

## ⚙️ Variables de entorno

Crea un archivo `.env` en la raíz:

```env
YT_QUALITY=192
DOWNLOAD_DIR=./downloads
```

---

## 🚀 Ejecutar la API

```bash
uvicorn app.main:app --reload
```

Accede a la documentación Swagger:  
➡️ [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 Endpoints disponibles

| Método  | Ruta                              | Descripción                                              |
|---------|-----------------------------------|----------------------------------------------------------|
| POST    | `/descargar`                      | Recibe lista de canciones, busca en YouTube y descarga   |
| GET     | `/descargas`                      | Lista todos los archivos MP3 disponibles                 |
| GET     | `/descargas/{nombre_archivo}`     | Devuelve un archivo específico por nombre                |
| DELETE  | `/descargas/{nombre_archivo}`     | Elimina un archivo específico                            |
| DELETE  | `/descargas`                      | Elimina todos los archivos descargados                   |

---

## 🧪 Pruebas

### 📬 Usando curl

```bash
curl -X POST http://localhost:8000/descargar \
     -H "Content-Type: application/json" \
     -d '{"canciones": ["Adele - Hello", "Imagine Dragons - Believer"]}'
```

### 🌐 Usando HTML (interfaz visual)

Este repositorio incluye un archivo `index.html` ubicado en la carpeta `/frontend`, que sirve como interfaz web para probar la API fácilmente desde el navegador.

Para usarlo:

1. Abre `frontend/index.html` con doble clic
2. Escribe nombres de canciones
3. Haz clic en "Descargar" y gestiona la lista desde ahí

![Frontend](screenshots\frontend-view.jpeg)

---

## 🧱 Arquitectura del sistema

- **FastAPI**: para definir y documentar endpoints
- **yt-dlp**: para búsqueda y descarga de videos
- **ffmpeg**: para convertir el audio a mp3
- **app/**: módulo principal con toda la lógica
- **downloads/**: almacena los MP3 generados
- **.env**: variables de configuración

---

## 📂 Estructura del proyecto

```
yt_music_api/
├── app/
│   ├── main.py
│   ├── downloader.py
│   ├── models.py
│   ├── config.py
│   └── utils.py
├── downloads/
├── frontend/
│   └── index.html
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ✅ Por hacer

- [x] Descargar canciones desde nombre
- [x] Servir archivos mp3 desde endpoint
- [x] Eliminar archivos individuales o todos
- [ ] Añadir autenticación con API key o JWT
- [ ] Modo asíncrono con colas (Celery/Redis)
- [ ] Frontend integrado vía Docker/Nginx
- [ ] Subida a Docker Hub o Render

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Sigue estos pasos:

1. Haz fork del proyecto
2. Crea una rama (`git checkout -b nueva-funcionalidad`)
3. Haz tus cambios y commit (`git commit -am 'Agrega nueva funcionalidad'`)
4. Sube tu rama (`git push origin nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.
