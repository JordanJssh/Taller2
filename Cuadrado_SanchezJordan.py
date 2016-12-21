import turtle

print("Ejercicio Cuadrado")
print("Jordan Sanchez")

t=turtle.Pen()

def micuadrado(size):
    for i in range(1,5):
        t.forward(size)
        t.left(90)
x=int(input("Ingrese el tamaño del cuadrado: "))
micuadrado(x)
