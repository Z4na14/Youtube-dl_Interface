from moviepy.editor import AudioFileClip
from shutil import move
from glob import glob
from os import getlogin, remove

obj = []
usuario = getlogin()

for a in glob('./*.m4a'):
    obj.append(a)

def convertir(x):
    x = x[::-1]
    x = x[16:]
    x = x[::-1]
    return (f'./{x}.mp3')

for a in obj:

    audioClip = AudioFileClip(a)
    convertedFile = convertir(a)
    audioClip.write_audiofile(convertedFile)
    audioClip.close()

    move(convertir(a), f'C:/Users/{usuario}/Desktop')
    remove(a)
