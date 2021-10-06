import tkinter
from moviepy.audio.io.AudioFileClip import AudioFileClip
from shutil import move
from glob import glob
from os import getlogin, system, remove
from pathlib import Path


usuario = getlogin()
path = Path().absolute()

def descargar_mp3(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f 140 {url}")
    mp3()

def descargar_mp4(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f bestvideo {url}")
    system(f"start /min cmd /C cd {path} && youtube-dl -f bestaudio {url}")
    mp4()

def mp3():
    m4a = []
    def renombrar_mp3(url):
        url = url[::-1]
        url = url[16:]
        url = url[::-1]
        return (f'{url}.mp3')

    for a in glob('.\*.m4a'):
        m4a.append(str(path)+a[1:])

    for a in m4a:
        print(a)
        audioClip = AudioFileClip(a)
        convertedFile = renombrar_mp3(a)
        audioClip.write_audiofile(convertedFile)
        audioClip.close()
        move(renombrar_mp3(a), f'C:/Users/{usuario}/Desktop')
        remove(a)


def mp4():
    mkv = []
    def renombrar_mp4(url):
        url = url[::-1]
        url = url[16:]
        url = url[::-1]
        return (f'./{url}.mp4')

    for a in glob('./*.mkv'):
        mkv.append(a)

        # Aqui iria lo de convertir a MP4

        move(renombrar_mp4(a), f'C:/Users/{usuario}/Desktop')
        remove(a)

ventana = tkinter.Tk()
ventana.geometry("500x600")

texto_youtube_dl = tkinter.Label(ventana, text="YOUTUBE-DL", fg="black")
texto_youtube_dl.pack(side = tkinter.TOP)


caja_url = tkinter.Entry(ventana)
caja_url.pack(side = "top")

boton_descargar = tkinter.Button(ventana, text="Descargar MP3", padx = 40, pady = 15, command = lambda: descargar_mp3(caja_url.get()))
boton_descargar.pack(side = "bottom")

boton_descargar = tkinter.Button(ventana, text="Descargar MP4", padx = 40, pady = 15, command = lambda: descargar_mp4(caja_url.get()))
boton_descargar.pack(side = "bottom")

ventana.mainloop()