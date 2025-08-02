import os
from dotenv import load_dotenv

load_dotenv()
# Configuration for the application
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "./downloads")
QUALITY = os.getenv("YT_QUALITY", "192")
