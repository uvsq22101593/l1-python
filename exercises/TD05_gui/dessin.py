import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

racine =tk.Tk()
racine.title("Mon dessin")

fill_color = "default"

def Cercle():
    rand_x = random.randint(60, CANVAS_WIDTH -60)
    rand_y = random.randint (60, CANVAS_HEIGHT -60)

    x0= rand_x - 50
    y0 = rand_y + 50
    x1 = rand_x + 50
    y1 = rand_y - 50



    if fill_color == "default":
        canvas.create_line(x0, y0, x1, y1, width=3, fill="yellow")
        canvas.create_line(x1, y0, x0, y1, width=3, fill="yellow")
    else:
        canvas.create_line(x0, y0, x1, y1, width=3, fill=fill_color)
        canvas.create_line(x1, y0, x0, y1, width=3, fill= fill_color)

    canvas.create_oval(x0, y0, x1, y1, fill ="blue")


def croix ():
    rand_x = random.randint(60, CANVAS_WIDTH -60)
    rand_y = random.randint (60, CANVAS_HEIGHT -60)

    x0 = rand_x - 50
    y0 = rand_y + 50
    x1 = rand_x + 50
    y1 = rand_y - 50

    if fill_color == "default":
        canvas.create_line(x0, y0, x1, y1, width=3, fill="yellow")
        canvas.create_line(x1, y0, x0, y1, width=3, fill="yellow")
    else:
        canvas.create_line(x0, y0, x1, y1, width=3, fill=fill_color)
        canvas.create_line(x1, y0, x0, y1, width=3, fill= fill_color)

    canvas.create_oval(x0, y0, x1, y1, fill ="blue")


def color():
    global fill_color
    fill_color = input ("Choisis une couleur:")


#création des widgets
bouton_cercle = tk.Button(racine, text="Cercle", bg ="pink", fg="red", command = Cercle)
bouton_carre = tk.Button( racine, text ="Carré")
bouton_croix = tk.Button (racine, text="Croix")
bouton_couleur = tk.Button (racine, text=" Choisir une couleur")

canvas =tk.Canvas( racine, width=500, height=500, bg="black")

#placement des widgets
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
bouton_couleur.grid(column=1, row=0)

canvas.grid(column=1, row=1, rowspan=3)



canvas.pack()
racine.mainloop()


