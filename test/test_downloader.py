from app.downloader import buscar_video

def test_buscar_video():
    url = buscar_video("Adele - Hello")
    assert url is None or url.startswith("https://www.youtube.com/watch")
