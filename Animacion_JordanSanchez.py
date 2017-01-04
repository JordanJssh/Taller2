from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
my_image=PhotoImage(file="Python-Logo.png")
canvas.create_image(0,0,ancho=NW, image=my_image)
def moverimagen(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Up>', moverimagen)
canvas.bind_all('<KeyPress-Down>', moverimagen)
canvas.bind_all('<KeyPress-Left>', moverimagen)
canvas.bind_all('<KeyPress-Right>', moverimagen)
tk.mainloop()


