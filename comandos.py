from os import getlogin, system
from pathlib import Path
import conversor

usuario = getlogin()
path = Path().absolute()

def descargar_mp3(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f 140 {url}")
    conversor.mp3()

def descargar_mp4(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f bestvideo {url}")
    system(f"start /min cmd /C cd {path} && youtube-dl -f bestaudio {url}")
    conversor.mp4()
