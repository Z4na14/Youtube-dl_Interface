import tkinter
import comandos

ventana = tkinter.Tk()
ventana.geometry("500x600")

texto_youtube_dl = tkinter.Label(ventana, text="YOUTUBE-DL", fg="black")
texto_youtube_dl.pack(side = tkinter.TOP)


caja_url = tkinter.Entry(ventana)
caja_url.pack(side = "top")

boton_descargar = tkinter.Button(ventana, text="Descargar", padx = 40, pady = 15, command = lambda: comandos.descargar(caja_url.get()))
boton_descargar.pack(side = "bottom")

ventana.mainloop()