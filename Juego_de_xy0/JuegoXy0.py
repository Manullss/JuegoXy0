import tkinter as tk
from PIL import Image, ImageTk  #Importamos Image para que trabaje con formate JPG

class JuegoXy0:
    def __init__ (self):
        self.contador = 0  #Cuenta los click, solo llega a 3 clicks por cada casilla
        self.casilla = None  #Determina en que casilla hacemos click asi reinicia el conteo en tal casilla
        self.eleX0=[1,2,3,4,5,6,7,8,9]  #Casillas vasias para luego ser reemplazadas por x o 0

        self.ventana1=tk.Tk()
        self.ventana1.title("Juego X y 0")

        self.canvas1=tk.Canvas(self.ventana1,width=300,height=300)  
        self.canvas1.grid(column=0,row=0)
        img=Image.open("cuadricula.jpg")
        img=img.resize((300,300))  #Tamaño de la imagen de fondo
        fondo=ImageTk.PhotoImage(img)
        self.canvas1.create_image(0,0,image=fondo,anchor="nw")
         
        self.simbolos=[
                tk.PhotoImage(file="x.png"),
                tk.PhotoImage(file="0.png")
                ]
        self.canvas1.bind("<Button-1>",self.presion_mouse)  #Detecta cuando presionamos el mouse
        self.ventana1.mainloop()

    def presion_mouse(self,evento):  #Verificamos en que casilla presiona el mouse

        if evento.x > 0 and evento.x < 100:
            if evento.y > 0 and evento.y < 100:         #casilla 1
                self.eleX0[0]=self.eleccion(0,0,"1")
                self.casilla = "1"
            elif evento.y > 100 and evento.y < 200:        #casilla 2                        
                self.eleX0[1]=self.eleccion(0,100,"2")
                self.casilla = "2" 
            elif evento.y > 200 and evento.y < 300:         #casilla 3
                self.eleX0[2]=self.eleccion(0,200,"3")
                self.casilla = "3"

        if evento.x > 100 and evento.x < 200:
            if evento.y > 0 and evento.y < 100:             #casilla 4                         
                self.eleX0[3]=self.eleccion(100,0,"4")
                self.casilla = "4"  
            elif evento.y > 100 and evento.y < 200:         #casilla 5           
                self.eleX0[4]=self.eleccion(100,100,"5")
                self.casilla = "5"  
            elif evento.y > 200 and evento.y < 300:           #casilla 6
                self.eleX0[5]=self.eleccion(100,200,"6")
                self.casilla = "6"

        if evento.x > 200 and evento.x < 300:
            if evento.y > 0 and evento.y < 100:             #casilla 7                         
                self.eleX0[6]=self.eleccion(200,0,"7")
                self.casilla = "7"  
            elif evento.y > 100 and evento.y < 200:         #casilla 8        
                self.eleX0[7]=self.eleccion(200,100,"8")
                self.casilla = "8"  
            elif evento.y > 200 and evento.y < 300:         #casilla 9
                self.eleX0[8]=self.eleccion(200,200,"9")
                self.casilla = "9"
        self.busca_linea()

    def eleccion(self,x,y,cas):  #Busca la opcion entre x y 0 
        if cas != self.casilla:   #Verifica si hemos cambiado de casilla, asi si lo hemos echo reinicia el contador en zero empezando siempre con x en cada casilla
            self.contador = 0
        self.contador += 1 

        if self.canvas1.find_withtag(f"casilla{cas}-x") or self.canvas1.find_withtag(f"casilla{cas}-0"):   #Busca si tenemos figuras ya establecidas en la casilla seleccionada 
            self.canvas1.delete(f"casilla{cas}-0" , f"casilla{cas}-x")                                                #Si hay alguna la borra para empezar desde x

        if self.contador==1:
            self.canvas1.create_image(x,y,image=self.simbolos[0],anchor="nw",tag=f"casilla{cas}-x") #Inserta imagen x
            return "x"
        elif self.contador==2:
            self.canvas1.delete(f"casilla{cas}-x")  #borra imagen anteriror x
            self.canvas1.create_image(x,y,image=self.simbolos[1],anchor="nw",tag=f"casilla{cas}-0") #Inserta imagen 0
            return "0"
        elif self.contador==3: 
            self.canvas1.delete(f"casilla{cas}-0")  #borra a imagen 0 

        if self.contador  == 3:
            self.contador = 0
    
    def busca_linea(self):   #Busca la linea que cumpla con las 3 en linea
        cor=[[50,50],[50,150],[50,250],[150,50],[150,150],[150,250],[250,50],[250,150],[250,250]] #coordenadas de la Linea
        #usamos la lista eleX0[] para comparar 

        for i in range(3):   #Busca el 3 en linea de manera Horizontal
            if self.eleX0[i] == self.eleX0[i+3] == self.eleX0[i+6]:
                self.canvas1.create_line(cor[i][0],cor[i][1],cor[i+6][0],cor[i+6][1],fill="Red",width=5,tag=f"Horizontal{i}")
            else:
                self.canvas1.delete(f"Horizontal{i}")  #Borra la linea si hay alguna cuando cambiamos de ficha
        
        for i in range(0,9,3):  #Busca el 3 en linea de manera Vertical
            if self.eleX0[i] == self.eleX0[i+1] == self.eleX0[i+2]:
                self.canvas1.create_line(cor[i][0],cor[i][1],cor[i+2][0],cor[i+2][1],width=5,fill="Red",tag=f"Vertical{i}")
            else:
                self.canvas1.delete(f"Vertical{i}")

        if self.eleX0[0] == self.eleX0[4] == self.eleX0[8]:   #Busca el 3 en linea de manera Diagonal Derecha
            self.canvas1.create_line(cor[0][0],cor[0][1],cor[8][0],cor[8][1],width=5,fill="Red",tag="DiagonalDer")
        else:
            self.canvas1.delete("DiagonalDer")

        if self.eleX0[6] == self.eleX0[4] == self.eleX0[2]:   #Busca el 3 en linea de manera Diagonal Izquierda
            self.canvas1.create_line(cor[6][0],cor[6][1],cor[2][0],cor[2][1],width=5,fill="red",tag="DiagonalIzq")
        else:
            self.canvas1.delete("DiagonalIzq")

juegoXy0=JuegoXy0()
