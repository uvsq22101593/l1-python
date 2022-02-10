import tkinter as tk

colors = ["blue", "green", "black", "yellow", "magenta", "red"]

size = int (input("Taille de l'image :"))
nb = int (input( "Nombre de cercles:"))

CANVAS_WIDTH, CANVAS_HEIGHT = size, size
racine= tk.Tk()
racine.title("Une cible")

canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")

space = ((size -20)/2)//nb

x0 = 10
y0 = size - 10
x1 = size - 10
y1 = 10


for i in range (nb):
    canvas.create_oval(x0, y0, x1, y1, outline = colors[i%6], fill = colors[i%6])
    x0 += space
    x1 -= space
    y0 -= space
    y1 += space


canvas.pack()
racine.mainloop()

def get_color(r, g, b):
    

def draw_pixel (i, j, color = "white") :
    canvas.create_line(i, j, i+1, j, fill= color)