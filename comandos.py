from os import getlogin, system
from subprocess import call
from pathlib import Path

usuario = getlogin()
path = Path().absolute()

def descargar(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f 140 {url}")
    call(["python", f"C:/Users/{usuario}/Desktop/Codigos/python/Proyecto descargar musica/conversor.pyw"])
