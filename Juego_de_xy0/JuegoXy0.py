import tkinter as tk

class JuegoXy0:
    def __init__ (self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Juego X y 0")

        self.canvas1=tk.Canvas(self.ventana1,width=300,height=300,background="Black")
        self.canvas1.grid(column=0,row=0)
        self.canvas1.bind("<Button-1>",self.presion_mouse)
    
        self.ventana1.mainloop()
    def presion_mouse(self,evento):
        if evento.x > 0 and evento.x < 100:
            if evento.y > 0 and evento.y < 100: 
                self.canvas1.create_oval(20,20,90,90,outline="white")
            if evento.y > 100 and evento.y < 200:
                self.canvas1.create_oval(20,120,90,190,outline="white")
            if evento.y > 200 and evento.y < 300:
                self.canvas1.create_oval(20,220,90,290,outline="white")
        if evento.x > 100 and evento.x < 200:
            if evento.y > 0 and evento.y < 100: 
                self.canvas1.create_oval(120,20,190,90,outline="white")
            if evento.y > 100 and evento.y < 200:
                self.canvas1.create_oval(120,120,190,190,outline="white")
            if evento.y > 200 and evento.y < 300:
                self.canvas1.create_oval(120,220,190,290,outline="white")
juegoXy0=JuegoXy0()