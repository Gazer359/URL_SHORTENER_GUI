from tkinter import * 
from tkinter import messagebox
import requests
import random

windo = Tk()
windo.configure(background="black")
windo.title("URL SHORTENER ")
windo.configure(relief="flat")
windo.resizable(True,False)
icon = PhotoImage(file=r"img\icon.png")
windo.iconphoto(True,icon)



def shorter():
  sitios_web=["www.google.com","https://www.youtube.com/watch?v=3GymExBkKjE","https://www.facebook.com/61550512050663/videos/1839298683285879/?__so__=discover&__rv__=video_home_www_loe_popular_videos","https://www.instagram.com/video/reels/?hl=es","www.x.com","www.amazon.com"]
 
  try:
        
        url_original = mi_entry.get()
        if  url_original.startswith(("http://", "https://","www.")):
            api_url = f"https://tinyurl.com/api-create.php?url={url_original}"
            respuesta = requests.get(api_url)   

            if respuesta.status_code == 200:
                url_acortada = respuesta.text
                mi_area.insert(1.0,f"\nURL acortado: \n{url_acortada}\n\nURL Engañosa:\n{url_acortada}?{random.choice(sitios_web)}")
                mi_area.configure(state="disabled")
                mi_clear.configure(state="active")
                mi_copiar.configure(state="active")
            else:
                print("Error al acortar la URL")
                messagebox.showerror(message=f"ERROR AL HACER LA PETICION:{respuesta.status_code} O URL NO VALIDA")
        else:
            messagebox.showerror(message="URL NO VALIDA")
  except (requests.ConnectionError,requests.Timeout):
      messagebox.showinfo(title="NO HAY INTERNET...?", message="Conectarse al internet para su funcionamiento correcto")
  
def limpiar_campo():
    mi_area.configure(state="normal")
    mi_area.delete(1.0,END)
    mi_entry.delete(0,END)
    mi_entry.insert(0,"Ingresar una URL Valida ")
    mi_clear.configure(state="disabled")
    mi_copiar.configure(state="disabled")

def copiar_paplera():
    mi_copiar.configure(state="normal")
    windo.clipboard_clear()
    windo.clipboard_append(mi_area.get(1.0,END))
    messagebox.showinfo(message="SE A COPIADO AL PORTA PAPELES ",title="Copiado_portapales")
    mi_copiar.configure(state="disabled")
      
mi_area = Text(windo,foreground="white",background="black",font=("Arial",13),state="normal",width=60,height=10)
mi_area.pack(fill="x")

mi_entry = Entry(windo,font=("Arial",15),foreground="white",background="black")
mi_entry.insert(0,"Ingresar una URL Valida")
mi_entry.pack(fill="x")

mi_button = Button(windo,font=("Arial",20),text="Acortar URL",foreground="White",background="black",command=shorter).pack(fill="x")
mi_clear = Button(windo,font=("Arial",20),text="Clear",foreground="White",background="black",command=limpiar_campo,state="disabled")
mi_clear.pack(fill="x")
mi_copiar = Button(windo,font=("Arial",20),text="Copiar",foreground="White",background="black",command=copiar_paplera,state="disabled")
mi_copiar.pack(fill="x")



    
windo.mainloop()

